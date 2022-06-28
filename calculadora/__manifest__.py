# -*- coding: utf-8 -*-
{
    'name': 'Calculadora Final',
    'version': '1',
    'summary': 'Ejercicios',
    'sequence': -100,
    'description': """Calculadora Fernando""",
    'author': 'Fernando Alberico',
    'maintainer': 'Fernando',
    'license': 'AGPL-3',
    'depends': [
        'sale',
        'mail',
            ],
    'data': [
        'views/calculadora.xml',
        'report/calculadora_report.xml',
        'report/report.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}