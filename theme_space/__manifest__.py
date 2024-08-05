{
    'name': 'Space Theme',
    'description': 'A custom theme for Odoo',
    'version': '1.0',
    'author': 'Sanjay Sharma',
    'category': 'Theme/Creative',
    'depends': ['website'],
    'data': [
        'data/ir_asset.xml',
        'data/generate_primary_templates.xml',
        'views/image_library.xml',

        'views/snippets/s_cover.xml',
        'views/snippets/s_text_image.xml',
        'views/snippets/s_title.xml',
        'views/snippets/s_features.xml',
        'views/snippets/s_image_text.xml',
        'views/snippets/s_product_catalog.xml',
        # 'views/footer.xml',
        # 'views/header.xml',
    ],
    'images': [
        'static/description/space_description.jpg',
        'static/description/space_screenshot.jpg',
    ],
    'images_preview_theme': {
        'website.s_banner_default_image': '/theme_space/static/src/img/background/img1.jpg',
        'website.s_cover_default_image': '/theme_space/static/src/img/background/img5.jpg',
        'website.s_text_image_default_image': '/theme_space/static/src/img/background/img6.jpg',
        'website.s_picture_default_image': '/theme_space/static/src/img/background/img8.jpg',
    },
    'assets': {
        'web.assets_frontend': [
            'theme_space/static/fonts/*',
            'theme_space/static/src/scss/font.scss',
        ],
    },
    'license': 'LGPL-3',
}
