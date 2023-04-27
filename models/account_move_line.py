
from odoo import _, api, fields, models
from odoo.exceptions import UserError

class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    #tomo una sola etiqueta para reportes pivot y agrupado
    analytic_tag_id= fields.Many2one('account.analytic.tag', string='Etiqueta Analitica',compute="_take_one_analytic_tag", store=True)

    def _take_one_analytic_tag(self):
        for record in self:
            if record.analytic_tag_ids:
                record.analytic_tag_id=record.analytic_tag_ids[0]

