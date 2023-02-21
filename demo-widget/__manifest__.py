# -*- encoding: utf-8 -*- 
{
    "name" : 'Prueba de snippet odoo',
    "version" : '15.0',
    "author" : 'exdoo.mx/imeza',
    "category" : 'website',
    "website" : "exdoo.mx",
    "license" : "AGPL-3",
    "description" : """
        Este módulo agrega con copia a la plantilla de correo sin crearlo como contacto.
        
        Si tiene dudas, quiere reportar algún error o mejora póngase en contacto con nosotros: info@exdoo.mx
        """,
    "depends" : ['base','website'],
    "data" : [
        "views/snippets.xml",
        ],
    "installable" : True,
    "auto_install" : False,
    'price': 0.0,
    'currency': 'MXN',
}
