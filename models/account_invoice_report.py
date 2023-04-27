
from odoo import _, api, fields, models
from odoo.exceptions import UserError

class AccountInvoiceReport(models.Model):
    _inherit = "account.invoice.report"

    analytic_tag_id = fields.Many2one('account.analytic.tag', string='Etiqueta Analitica',  store=True, readonly=True)
    _depends = {
        'account.move': [
            'name', 'state', 'move_type', 'partner_id', 'invoice_user_id', 'fiscal_position_id',
            'invoice_date', 'invoice_date_due', 'invoice_payment_term_id', 'partner_bank_id',
        ],
        'account.move.line': [
            'quantity', 'price_subtotal', 'amount_residual', 'balance', 'amount_currency',
            'move_id', 'product_id', 'product_uom_id', 'account_id', 'analytic_account_id',
            'journal_id', 'company_id', 'currency_id', 'partner_id','analytic_tag_id',
        ],
        'product.product': ['product_tmpl_id'],
        'product.template': ['categ_id'],
        'uom.uom': ['category_id', 'factor', 'name', 'uom_type'],
        'res.currency.rate': ['currency_id', 'name'],
        'res.partner': ['country_id'],
    }


    def _select(self):
        return super()._select() + ",analytic_tag_id"

    def _group_by(self):
        return super()._group_by() + ",analytic_tag_id"