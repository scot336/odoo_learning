# noinspection PyStatementEffect
{
    'name': "hr_hospital",
    'summary': """Hospital management""",
    'license': 'LGPL-3',
    'author': "Shevchenko Igor",
    'website': "https://github.com/scot336",
    'category': 'Administration',
    'version': '15.0.1.0.0',
    'depends': ['base', 'contacts'],
    'data': [
        'security/ir.model.access.csv',
        'data/disease_data.xml',
        'data/doctor_demo.xml',
        'data/patient_demo.xml',
        'views/hr_hospital_menus.xml',
        'views/hr_hospital_doctor_views.xml',
        'views/hr_hospital_patient_views.xml',
        'views/hr_hospital_patient_visit_views.xml',
        'views/hr_hospital_disease_views.xml',
    ],
    'application': False,
    'installable': True,
    'auto_install': False,
}
