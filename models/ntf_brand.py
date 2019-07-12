from odoo import api, fields, models, _


class Ntf_Brand(models.Model):
    _name = 'ntf.brand'
    _description = 'Brand Ntf-food'


    name = fields.Char(translate=True, required=True, string = "Brand Name")

    descr = fields.Text(string="Description", required=False, )

    image = fields.Binary(string="Image",)

    create_date = fields.Datetime(string="Cteated date", required=False, default=lambda self: fields.Datetime.now(),)