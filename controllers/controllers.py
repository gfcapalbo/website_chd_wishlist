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




    @http.route('/chd_init/wishadd/<id>/',website=True)
    def wishadd(self,**form_data):

        http.request.env['chd.wishlist'].create({'wishlist_id': (0,0,[int(form_data['id'])]),'favorites': False})



        """result = http.request.env['chd.product_configurator.result'].search([('id','=',form_data['id'])])
        configurator = http.request.env['chd.product_configurator'].search([('id','=',result.configurator_id.id)])
        http.request.context['active_id'] = result.id
        fields = ['order_id','return_to_order','display_order_id','result_id']
        doorder_model = http.request.env['chd.product_configurator.do_order']
        # again, access 7.0 with ._model property
        doorder_model._model.default_get(http.request.cr,http.request.uid,fields_list=fields,context=http.request.context)
        return http.request.render('website_chd_product_configurator.buy_option',{
               'summary':form_data['summary'],
                })"""
