{
'name': "website_chd_wishlist",
'description': """
Wishlist for web front chindu product configurator
When the sales options appear, a button
add to wishlist" will be available
The user will have the possibility to view his wishlists and transform them in orders
(in other words create quotations in the product configurator"

""",
'depends': ['base',
            'website',
            'chd_product_configurator',
            'website_chd_product_configurator'
           ],
'data': [
        'templates/templates.xml',
        ],
}
