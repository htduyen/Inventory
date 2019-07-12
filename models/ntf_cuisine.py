from odoo import api, fields, models, _


class Ntf_Cuisine(models.Model):
    _name = 'ntf.cuisine'
    _description = 'Cuisine Ntf-food'


    name = fields.Char(translate=True, required=True)

    descr = fields.Text(string="Description", required=False, )

    image = fields.Binary()