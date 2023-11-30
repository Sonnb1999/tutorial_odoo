from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    th_estate_id = fields.Many2one(relation='th.estate')
