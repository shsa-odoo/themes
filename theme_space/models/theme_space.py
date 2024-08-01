from odoo import models


class ThemeSpace(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_space_post_copy(self, mod):
        # there are various other ways to way we can display header and footer
        self.enable_view('website.template_header_hamburger')

        self.enable_view('website.template_footer_centered')
