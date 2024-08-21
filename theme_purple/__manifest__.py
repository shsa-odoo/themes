{
    'name': 'Purple Theme',
    'description': 'A custom theme for Odoo',
    'version': '1.0',
    'author': 'Sanjay Sharma',
    'category': 'Theme/Creative',
    'depends': ['website'],
    'data': [
        'views/image_library.xml',
        'views/snippets/s_banner.xml',
        # 'views/footer.xml',
        # 'views/header.xml',
    ],

    'images': [
        'static/description/theme_description.jpg',
        'static/description/theme_purple.jpg',
    ],
    'images_preview_theme': {
        'website.s_banner_default_image': '/theme_purple/static/src/img/background/img1.jpg',
    },
    'configurator_snippets': {
        'homepage': ['s_banner'],
    },
    'assets': {
        'web._assets_primary_variables': [
            'theme_purple/static/src/scss/primary_variables.scss',
        ],
        'web.assets_frontend': [
            'theme_purple/static/fonts/*',
            'theme_purple/static/src/scss/font.scss',
        ],
    },
    'license': 'LGPL-3',
}
