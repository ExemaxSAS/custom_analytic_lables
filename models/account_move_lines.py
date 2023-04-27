from odoo import _, api, fields, models
from odoo.exceptions import UserError

class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    analytic_tag_ids = fields.Many2many('account.analytic.tag', string='Analytic Tags', store=True)

    @api.depends('analytic_tag_ids')
    def _compute_legajo(self):
        for employee in self:
            employee.employee_complete = str(
                employee.employee_id.short_number) + '-' + employee.employee_id.name + '- CUIL: ' + str(
                employee.employee_id.ssnid)

