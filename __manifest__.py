{
    'name': 'NTFoods module',
    'version': '1.0',
    'description': 'NTFoods description',
    'author': 'NTFoods dev',
    'depends': ['base', 'product', ],
    'application': True,
    'installable': True,
    'data': [
        'security/ntf_security.xml',
        'security/ir.model.access.csv',
        'views/ntf_menu.xml',
        'views/product_template_views.xml',
        'views/ntf_category_view.xml',
        'views/ntf_cuisine_view.xml',
        'views/ntf_brand_view.xml',
        'views/ntf_department_view.xml',

    ],
}