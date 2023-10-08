from odoo import fields, models


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Test Model"

    name = fields.Char(required=True, string="Name")
    description = fields.Text()
