{
    'name': 'Ecuadorian Localization Payment in POS Order',
    'version': '18.01',
    'summary': 'Customization module for Ecuadorian localization make Payment details in POS Order',
    'description': """
    Este módulo permite guardar datos de las diferentes formas de pago
    """,
    'icon': '/account/static/description/l10n.png',
    'countries': ['ec'],
    'author': 'Elmer Salazar Arias',
    'category': 'Point of Sale/Localizations/',
    'maintainer': 'Elmer Salazar Arias',
    'website': 'http://www.galapagos.tech',
    'email': 'esalazargps@gmail.com',
    'license': 'LGPL-3',
    'depends': [
        'l10n_ec_base',
        'sale',
        'purchase',
        'point_of_sale',
        'l10n_ec_edi_pos',
        'l10n_ec_payment',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/pos_payment_method_views.xml',
        'views/pos_payment_views.xml',
        'views/res_bank_view.xml',
        'views/account_credit_card_brand_view.xml',
        'views/account_credit_card_deadline_view.xml',
        
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'l10n_ec_payment_pos/static/src/**/*',
        ],
    },
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
