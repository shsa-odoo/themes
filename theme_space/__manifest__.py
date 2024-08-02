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
        # 'views/footer.xml',
        # 'views/header.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'theme_space/static/fonts/*',
            'theme_space/static/src/scss/font.scss',
        ],
    },
    'license': 'LGPL-3',
}
