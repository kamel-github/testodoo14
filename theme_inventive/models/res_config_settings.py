# -*- coding: utf-8 -*-
#################################################################################
#
# Copyright (c) 2019-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>:wink:
# See LICENSE file for full copyright and licensing details.
#################################################################################
from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    slider_min_price = fields.Integer(
        "Slider Min Price", config_parameter='theme_inventive.slider_min_price', default=0, required="True")
    slider_max_price = fields.Integer(
        "Slider Max Price", config_parameter='theme_inventive.slider_max_price', default=100000, required="True")
    price_range_step = fields.Integer(
        "Price Range Step",  config_parameter='theme_inventive.price_range_step', default=100, required="True")
    show_price_filter = fields.Boolean(
        "Show Price Filter", config_parameter='theme_inventive.show_price_filter')

    enable_lazy_loading = fields.Boolean('Enable Lazy Loading', default = False, config_parameter='theme_inventive.enable_lazy_loading')
    lazy_loading_options = fields.Selection([('button','Button Click'),('scroll',"On Scroll")], config_parameter = 'theme_inventive.lazy_loading_options', default = 'button')


    products_rating = fields.Selection(
        [('show', 'Show all the Ratings'),
            ('hide', 'Show Only that have value greater then 0'),
            ('hidden', 'Do not show Ratings at all.'),
         ],
        "Show/Hide Product Ratings", config_parameter='theme_inventive.products_rating', default="show")
    product_filter_views = fields.Selection([ ('default', 'Default'),('side_bar', 'Left Side bar'), ('dropdown', 'Dropdown')],
                                            "Product Filters Views", config_parameter='theme_inventive.product_filter_views', default="dropdown")

    product_quick_view = fields.Boolean(
        "Product Quick View", config_parameter='theme_inventive.product_quick_view')
    product_alternatives_view = fields.Boolean(
        "Product Alternates View", config_parameter='theme_inventive.product_alternatives_view')
    product_accessories_view = fields.Boolean(
        "Product Accessories View", config_parameter='theme_inventive.product_accessories_view')

    def set_values(self):
        super(ResConfigSettings, self).set_values()
