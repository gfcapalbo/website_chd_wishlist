# -*- coding: utf-8 -*-

from openerp import http
from openerp import api
from datetime import  datetime
from openerp.osv import fields,orm
import json

class Chd_init(http.Controller):
    # display current users wishlist
    @http.route('/chd_init/<id>/wishlist/' ,website=True)
    def wish(self,id):
        return True


    @http.route('/chd_init/wishadd/' ,type='json',website=True)
    def wishadd(self,**form_data):
        # check if the user already has a wishlist
        wishlist_model = http.request.env['chd.wishlist']
        result_model = http.request.env['chd.product_configurator.result']
        wish_ids = wishlist_model.search([('owner','=',1)])
        if len(wish_ids) == 0:
            wish_ids = wishlist_model.create({'owner':1,'favorites': False})
        # better to write wish_ids.ids[0] ala 8.0 instead of writing wish_ids[0].ids
        wish_ids.write({
                    'chd_results':[(1,0,{'chd_results': toadd_id })]
                     })

        data = json.dumps(http.request.registry['chd.wishlist'].search_read(
        http.request.cr,
        http.request.uid,
        fields=['id','chd_results'],
        limit=30,
        domain=[('owner','in',[int(1)])],
        context=http.request.context
        ))
        return data

