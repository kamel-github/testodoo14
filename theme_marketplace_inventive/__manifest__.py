# -*- coding: utf-8 -*-
#################################################################################
# Author      : Webkul Software Pvt. Ltd. (<https://webkul.com/>)
# Copyright(c): 2015-Present Webkul Software Pvt. Ltd.
# All Rights Reserved.
#
#
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#
# You should have received a copy of the License along with this program.
# If not, see <https://store.webkul.com/license.html/>
#################################################################################
{
  "name"                 :  "Odoo Marketplace Theme Inventive",
  "summary"              :  """Your Odoo Marketplace needs to be perfect! So, here is Odoo Marketplace Theme Inventive that fits your Odoo Marketplace perfectly.""",
  "category"             :  "Theme/Ecommerce",
  "version"              :  "1.0.1",
  "sequence"             :  1,
  "author"               :  "Webkul Software Pvt. Ltd.",
  "license"              :  "Other proprietary",
  "website"              :  "https://store.webkul.com",
  "description"          :  """Webkul Odoo theme. This Theme is depenedent on theme xtremo and odoo multivendor marketplace,
                                Inventive theme
                                Webkul Odoo theme
                                Odoo theme
                                Website Theme
                                themes in Odoo
                                Odoo Website Theme: Inventive
                                Theme Inventive in Odoo Website
                                Odoo Website Theme Inventive
                                Website Theme: Inventive
                                Odoo Responsive theme
                                Responsive theme
                                theme
                                themes
                                Enhanced Theme
                                website theme
                                Best theme
                                website outlook
                                theme clarico
                                Theme xtremo
                                Inventive
                                Theme Inventive
                                Odoo
                                Odoo Multi Vendor Marketplace
                                Marketplace in Odoo
                                Odoo Marketplace website
                                E-commerce marketplace
                                Multi-Seller Marketplace
                                Turn your Odoo website in Marketplace
                                start marketplace in Odoo""",
  "live_test_url"        :  "https://marketplace_inventive_13.odoothemes.webkul.com/seller",
  "depends"              :  [
                             'odoo_marketplace',
                             'theme_inventive',
                            ],
  "data"                 :  [
                             'views/theme_templates.xml',
                             'views/mp_templates.xml',
                             'views/seller_landing_page_templates.xml',
                            ],
  "images"               :  [
                             'static/description/Banner.png',
                             'static/description/inventive_screenshot.gif',
                            ],
  "application"          :  False,
  "installable"          :  True,
  "auto_install"         :  False,
  "price"                :  51,
  "currency"             :  "USD",
  "pre_init_hook"        :  "pre_init_check",
}