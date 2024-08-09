{
    'name': 'Purple Theme',
    'description': 'A custom theme for Odoo',
    'version': '1.0',
    'author': 'Sanjay Sharma',
    'category': 'Theme/Creative',
    'depends': ['website'],
    'data': [
        'data/ir_asset.xml',
        # i dont think we actually need this
        # 'data/generate_primary_templates.xml',
        'views/image_library.xml',

        'views/snippets/s_cover.xml',
        'views/snippets/s_text_image.xml',
        'views/snippets/s_title.xml',
        'views/snippets/s_features.xml',
        'views/snippets/s_image_text.xml',
        'views/snippets/s_product_catalog.xml',
        'views/snippets/s_banner.xml',
        'views/footer.xml',
        'views/header.xml',
    ],
    'images': [
        'static/description/theme_description.jpg',
        'static/description/theme_purple.jpg',
    ],
    'images_preview_theme': {
        'website.s_banner_default_image': '/theme_purple/static/src/img/background/img1.jpg',
        'website.s_cover_default_image': '/theme_purple/static/src/img/background/img5.jpg',
        'website.s_text_image_default_image': '/theme_purple/static/src/img/background/img6.jpg',
        'website.s_picture_default_image': '/theme_purple/static/src/img/background/img8.jpg',
    },
    'configurator_snippets': {
        'homepage': ['s_cover', 's_text_image', 's_title', 's_features', 's_image_text', 's_product_catalog', 's_banner'],
    },
    'assets': {
        'web.assets_frontend': [
            'theme_purple/static/fonts/*',
            'theme_purple/static/src/scss/font.scss',
        ],
    },
    'license': 'LGPL-3',
}
