from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class Ntf_Category(models.Model):
    _name = 'ntf.category'
    _description = 'Product Template Category Ntf-food'
    _parent_store = True
    _rec_name = 'complete_name'

    
    name = fields.Char(translate=True, required=True)

    complete_name = fields.Char(
        'Complete Name', compute='_compute_complete_name',
        store=True)

    parent_id = fields.Many2one(
        'ntf.category',
        string='Parent Category',
        ondelete='restrict',)

    sequence = fields.Char(string="Sequence", required=False, )

    parent_path = fields.Char(index=True)

    child_ids = fields.One2many(
        'ntf.category',
        'parent_id',
        string='Subcategories',)

    descr = fields.Text(string="Description", required=False, )

    image = fields.Binary(string="",  )

    @api.depends('name', 'parent_id.complete_name')
    def _compute_complete_name(self):
        for category in self:
            if category.parent_id:
                category.complete_name = '%s / %s' % (category.parent_id.complete_name, category.name)
            else:
                category.complete_name = category.name

    @api.constrains('parent_id')
    def _check_category_recursion(self):
        if not self._check_recursion():
            raise ValidationError(_('You cannot create recursive categories.'))
        return True