# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2013,14 Therp BV (<http://therp.nl>).
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

{
'name': "website_chd_wishlist",
'description': """
Wishlist for web front chindu product configurator
When the sales options appear, a button
add to wishlist" will be available
The user will have the possibility to view his wishlists
and transform them in orders
(in other words create quotations in the product configurator"

""",
'author' : 'Therp B.V.',
'depends': ['base',
            'website',
            'chd_product_configurator',
            'website_chd_product_configurator'
           ],
'data': [
        'templates/templates.xml',
        'views/chd_wishlist.xml',
        ],
}
