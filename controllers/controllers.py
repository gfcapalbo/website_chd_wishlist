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





