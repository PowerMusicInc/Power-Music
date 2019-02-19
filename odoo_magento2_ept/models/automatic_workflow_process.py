from odoo import models, fields, api, _
from odoo.api import Environment
import time
from datetime import datetime

class auto_workflow_process(models.Model):
    _inherit = "sale.workflow.process.ept"
    _description = "sale workflow process"
        
    @api.multi
    @api.depends('payment_method_ids')
    def set_payment_methods_count(self):
        for record in self :
            record.payment_methods_count = len(record.payment_method_ids)
            
    payment_method_ids = fields.One2many('magento.payment.method.ept','magento_workflow_process_id','Payment Methods')
    payment_methods_count = fields.Integer(string="Payment Methods count",compute="set_payment_methods_count",store=True)
    team_id = fields.Many2one(comodel_name='crm.team',oldname='section_id',
                                 string='Sales Team')
    
    @api.multi
    def view_payment_methods(self):
        payment_method_ids = self.mapped('payment_method_ids')
        xmlid=('odoo_magento2_ept','act_payment_method_form')
        action = self.env['ir.actions.act_window'].for_xml_id(*xmlid)
        action['domain']= "[('id','in',%s)]" % payment_method_ids.ids
        if not payment_method_ids : 
            return {'type': 'ir.actions.act_window_close'}
        if len(payment_method_ids) == 1 :
            ref = self.env.ref('odoo_magento2_ept.payment_method_view_form')
            action['views'] = [(ref.id, 'form')]
            action['res_id'] = payment_method_ids[0].id if payment_method_ids else False
            return action
        return action
