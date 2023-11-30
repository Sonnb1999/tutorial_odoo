from odoo import models, fields


class ResUser(models.Model):
    _inherit = 'res.users'

    estate_id = fields.Many2one(relation='th.estate')
