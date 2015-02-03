# -*- coding: utf-8 -*-

from openerp import http
import openerp.addons.website_chd_product_configurator.controllers.controllers as pc


class wish_init(http.Controller):
    # display current users wishlist
    @http.route('/chd_init/wishlist/', website=True)
    def wish(self):
        partner = get_current_partner()
        if partner is False:
            return http.request.render(
                'website_chd_product_configurator.no_partner', {})
        wishlist_model = http.request.env['chd.wishlist']
        result_model = http.request.env['chd.product_configurator.result']
        wishlist = wishlist_model.search([('owner', '=', partner.id)])
        try:
            results = result_model.search([('wishlist', '=', wishlist.ids[0])])
            return http.request.render('website_chd_wishlist.show_list', {
                'user': partner,
                'results': results,
                })
        except:
            return http.request.render('website_chd_wishlist.no_list', {
                'user': partner,
                })


# inheriting and extending the controller in the website_chd_module
class Chd_website_ext(pc.Chd_website):
    @http.route()
    def chosen_option(self, **form_data):
        partner = get_current_partner()
        if partner is False:
            return http.request.render(
                'website_chd_product_configurator.no_partner', {})
        result_model = http.request.env['chd.product_configurator.result']
        result = result_model.search([('id', '=', form_data['id'])])
        http.request.context['active_id'] = result.id
        wishlist_model = http.request.env['chd.wishlist']
        # check if the user already has a wishlist if not create
        wishlist = wishlist_model.search([('owner', '=', partner.id)])
        if form_data['action'] == 'wish':
            if len(wishlist) == 0:
                wishlist = wishlist_model.create({'owner': partner.id})
            # better to write wishlist.ids[0] ala 8.0 instead of wishlist[0].id
            result.write({
                'wishlist': wishlist.ids[0],
                'summary': form_data['summary'],
                'favorites': False,
                })
            results = result_model.search([('wishlist', '=', wishlist.ids[0])])
            return http.request.render('website_chd_wishlist.show_list', {
                'summary': result.summary,
                'user': result.create_uid,
                'results': results,
                })
        elif form_data['action'] == 'erase':
            #do not want to erase the configurator result.
            #wishlist[0].write({'element':[(2,result.ids[0],0)]})
            #will make all "erased" results point to wishlist 0.
            result.write({
                'wishlist': 0,
                })
            results = result_model.search([('wishlist', '=', wishlist.ids[0])])
            return http.request.render('website_chd_wishlist.show_list', {
                'summary': form_data['summary'],
                'user': result.create_uid,
                'results': results,
                })
        return super(Chd_website_ext, self).chosen_option(**form_data)


def get_current_partner():
        partner_model = http.request.env['res.partner']
        current_partner = partner_model.search([
            ('user_account_id', '=', http.request.uid)
            ])
        if len(current_partner) == 0:
            return False
        else:
            return current_partner[0]
