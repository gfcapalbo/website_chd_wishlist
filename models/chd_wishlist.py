# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2014 Therp BV (<http://therp.nl>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import orm, fields


class ChdWishlist(orm.Model):
    _name = 'chd.wishlist'
    _columns = {
        'owner': fields.many2one('res.partner', string="owner"),
        'element': fields.one2many(
            'chd.product_configurator.result',
            'wishlist',
            string='elements'),
        }


class chd_product_configurator_result(orm.Model):
    _inherit = 'chd.product_configurator.result'
    _columns = {
        'wishlist': fields.many2one('chd.wishlist', string="Parent wishlist"),
        'summary': fields.char(string='summary'),
        'favorites': fields.boolean(string='favorites'),
    }
