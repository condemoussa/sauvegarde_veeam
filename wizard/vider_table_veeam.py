from odoo import models, fields
from datetime import datetime

class ViderVeeam(models.TransientModel):
    _name = 'vider.veeam'


    def vider_veeam(self):

        veeam = self.env["atm.veeam"].search([])
        veeam.unlink()




