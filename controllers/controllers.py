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
         wishlist_model = http.request.env['chd.wishlist']
         wishlist_element_model = http.request.env['chd.wishlist.element']
         partner = self.get_current_partner()
         wishlist = wishlist_model.search([('owner','=',partner.id)])
         results = wishlist_element_model.search([('wishlist','=',wishlist.ids[0])])

         if results:
             return  http.request.render('website_chd_wishlist.show_list',{
                       'user':partner,
                       'results':results,
                        })
         else:
             return  http.request.render('website_chd_wishlist.no_list',{
                       'user':partner,
                        })


    def get_current_partner(self):
         partner_model = http.request.env['res.partner']
         current_partner = partner_model.search([('user_account_id','=',http.request.uid)])
         return current_partner[0]

