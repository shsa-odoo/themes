from odoo import models

class ThemeSpace(models.AbstractModel):
    """
    ThemeSpace is an abstract model that inherits from 'theme.utils'. This class is responsible for configuring
    the theme settings for the 'theme_space' module in Odoo. Specifically, it enables certain header and footer
    templates to be used in the website.

    Methods:
        _theme_space_post_copy(mod):
            This method is called after the theme is copied. It enables specific header and footer views
            to be used in the website. The available header and footer templates are listed in the comments
            for reference.

            - Headers:
                - website.template_header_default
                - website.template_header_default_align_right
                - website.template_header_hamburger_align_right
                - website.template_header_sales_one
                - website.template_header_sales_three
                - website.template_header_search

            - Footers:
                - website.template_footer_headline
                - website.template_footer_contact
                - website.template_footer_descriptive
                - website.template_footer_links
                - website.template_footer_minimalist
                - website.template_footer_slideout

            In this implementation, the following views are enabled:
                - Header: website.template_header_sales_one
                - Footer: website.template_footer_descriptive
    """

    _inherit = 'theme.utils'

    # def _theme_space_post_copy(self, mod):
    #     # these are available views for headers and footer:
    #     ##
    #     # Other examples::
    #     # website.template_header_default
    #     # website.template_header_default_align_right
    #     # website.template_header_hamburger_align_right
    #     # website.template_header_sales_one
    #     # website.template_header_sales_three
    #     # website.template_header_search
    #     ##
    #     self.enable_view('website.template_header_sales_one')

    #     ##
    #     # website.template_footer_headline
    #     # website.template_footer_contact
    #     # website.template_footer_descriptive
    #     # website.template_footer_links
    #     # website.template_footer_minimalist
    #     #website.template_footer_slideout
    #     # #

    #     self.enable_view('website.template_footer_descriptive')

    # example of how to override the header and footer templates

    @property
    def _header_template(self):
        return ['theme_space.custom_header'] + super()._header_template

    @property
    def _footer_template(self):
        return ['theme_space.custom_footer'] + super()._footer_template

    def _theme_space_post_copy(self, mod):
        self.enable_view('theme_space.custom_header')
        self.enable_view('theme_space.custom_footer')
