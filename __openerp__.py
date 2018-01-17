# -*- coding: utf-8 -*-

{
    'name': 'ARO HR',
    'version': '0.1',
    'author': 'Rakotomalala Haritiana <haryoran04@gmail.com>',
    'category': 'Tools',
    'complexity': 'normal',
    'data': [
        # 'data/templates.xml', # un comment to enable js, css code
        # 'security/security.xml',
        'security/ir.model.access.csv',
        # 'views/view.xml',
        # 'actions/act_window.xml',
        # 'menu.xml',
        # 'data/data.xml',
        'views/hr_employee_sanction_view.xml',
        'views/sanction_type_view.xml',
        'views/medical_type_view.xml',
        'views/hr_employee_medical_ticket_view.xml',

        'views/hr_holidays_view.xml',
        'views/hr_employee_view.xml',
        'views/children_view.xml',
        'views/hr_holidays_status_view.xml',
        'views/hr_holidays_status_type_view.xml',
        'views/hr_job_view.xml',
        'views/hr_holiday_job_view.xml',
        'views/hr_qualification_view.xml',
        'views/hr_applicant_view.xml',

        'views/hr_employee_formation_view.xml',
        'views/hr_employee_aptitude_view.xml',
    ],
    'depends': [
        'base', 'hr',
        'hr_holidays',
        'hr_contract',
        'hr_recruitment',
    ],
    'qweb': [
        # 'static/src/xml/*.xml',
    ],
    'test': [
    ],
    'installable': True,
    'auto_install': False,
}
