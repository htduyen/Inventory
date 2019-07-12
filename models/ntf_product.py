from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class NTFProduct(models.Model):

    _inherit = 'product.template'

    status_id = fields.Selection(string="Status",
                                selection=[('active', 'Active'),
                                    ('inactive', 'Inactive'),
                                    ('discontinue', 'Discontinue')],
                                default = 'active')
    season = fields.Selection(string="Season",
                                selection=[('spring', 'Spring'),
                                    ('summer', 'Summer'),
                                    ('fall', 'Fall'),
                                    ('winter', 'Winter')],
                                default = 'spring')
    alcoholic = fields.Boolean(string="Alcoholic",default = True)

    country_of_origin = fields.Many2one('res.country', string="Country of Origin", required=False, )

    cuisine = fields.Many2one('ntf.cuisine', string="Cuisine", required=False, )

    brand = fields.Many2one('ntf.brand', string="Brand", required=False, )

    department = fields.Many2one('ntf.department', string="Department", required=False, )

    ntf_category_id = fields.Many2one('ntf.category', string="Category", required=False, )


    @api.model
    def create(self, vals):
        name = vals.get('cuisine')
        new_name = name.title()
        vals['cuisine'] = new_name
        return super().create(vals)