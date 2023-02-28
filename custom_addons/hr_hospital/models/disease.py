from odoo import models, fields


class HospitalDoctor(models.Model):
    _name = 'hr.hospital.disease'
    _description = 'Disease of Hospital Patient'

    name = fields.Char(required=True)
