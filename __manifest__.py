# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
# Copyright (c) 2011 CCI Connect asbl (http://www.cciconnect.be) All Rights Reserved.
#                       Philmer <philmer@cciconnect.be>
{
    'name': 'SAUVEGARDE VEEAM',
    'version': '1.0',
    'category': '',
    'description': """
              Gestion des sauvegardes veeam
    """,
    'depends': ['base',"report_xlsx"],
    'data': [
            'security/ir.model.access.csv',
             "views/veeam.xml",
             "wizard/wizard_veeam_views.xml",
             "views/menu.xml"
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
