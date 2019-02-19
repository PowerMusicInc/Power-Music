from odoo import models, fields,api


class Magentoproducturl(models.Model):
    _name = "magento.product.url"
    _description = "Magento Product Url"
    
    
    magento_product_id = fields.Many2one('magento.product.product', string = 'Product')
    website_id = fields.Many2one('magento.website', string = 'Website')
    storeview_id = fields.Many2one('magento.storeview', string = 'Store')
    product_url = fields.Char(string = 'Product Url')  