# -*- coding: utf-8 -*-

from openerp import http
from openerp import api
from datetime import  datetime
from openerp.osv import fields,orm
import json

class wish_init(http.Controller):
    # display current users wishlist
    @http.route('/chd_init/wishlist/' ,website=True)
    def wish(self):
         partner = self.get_current_partner()
         if partner == False:
             return  http.request.render('website_chd_product_configurator.no_partner',{
                        })
         wishlist_model = http.request.env['chd.wishlist']
         result_model = http.request.env['chd.product_configurator.result']
         partner = self.get_current_partner()
         if not partner:
             return  http.request.render('website_chd_product_configurator.no_partner',{
                        })
         wishlist = wishlist_model.search([('owner','=',partner.id)])
         try:
             results = result_model.search([('wishlist','=',wishlist.ids[0])])
             return  http.request.render('website_chd_wishlist.show_list',{
                       'user':partner,
                       'results':results,
                        })
         except:
             return  http.request.render('website_chd_wishlist.no_list',{
                       'user':partner,
                        })

    def get_current_partner(self):
         partner_model = http.request.env['res.partner']
         current_partner = partner_model.search([('user_account_id','=',http.request.uid)])
         if len(current_partner) == 0:
             return False
         else:
             return current_partner.ids[0]

