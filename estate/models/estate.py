from odoo import fields, models
from datetime import timedelta

selection = [('new', 'New'), ('offer_received', 'Offer Received'), ('offer_accepted', 'Offer Accepted'),
             ('sold', 'Sold'), ('canceled', 'Canceled')]


class TestModel(models.Model):
    _name = "th.estate"
    _description = "Test Model"

    name = fields.Char(required=True, string="Name")
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(copy=False, default=lambda l: fields.Date.today() + timedelta(days=90))
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer(default=1000)
    facades = fields.Integer(default=1000)
    garage = fields.Boolean(default=True)
    garden = fields.Boolean(default=True)
    garden_area = fields.Integer(default=1000)
    garden_orientation = fields.Selection(selection=[('s', 'South'), ('n', 'North'), ('e', 'East'), ('w', 'West')])
    active = fields.Boolean(default=True)
    state = fields.Selection(selection=selection, defualt='new')
    property_type_id = fields.Many2one('estate.property.type')

