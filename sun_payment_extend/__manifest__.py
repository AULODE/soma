{
    'name': 'Payment Extend',
    'category': 'Accounting',
    'author': 'Kiran Kantesariya',
    'version': '11.0.1',
    'description':
        """
Odoo-11.0 Payment Extend Module.
===================================
        """,
    'depends': ['account'],
    'data': [
             'views/account_payment_view.xml',
    ],
    'auto_install': True,
    'installable': True,
}
