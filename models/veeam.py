# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

from odoo import models, fields, api

class AtmVeeam(models.Model):
    _name = 'atm.veeam'
    _description = "Gestion des automatisations des machines virtuelles"


    # Définition des champs du modèle
    name = fields.Char("Machine virtuelle")
    dat_imp = fields.Datetime("Date")
    nbre_machine = fields.Char("Nombre de machines")
    statut = fields.Selection(
        [
            ("Success", "Success"),
            ("Failed", "Failed"),
        ],
        string="Statut"
    )
    ref = fields.Selection([
        (f"j{i}", f"J{i}") for i in range(1, 32)
    ], string="Référence")

    mois = fields.Char(string="Mois")
    annee = fields.Char(string="Année")

    @api.model
    def create(self, vals):
        jour =""
        """ Surcharge de la méthode create pour extraire mois et année depuis dat_imp """
        if 'dat_imp' in vals and vals['dat_imp']:
            date_obj = fields.Datetime.from_string(vals['dat_imp'])
            vals['mois'] = date_obj.strftime('%m')
            vals['annee'] = date_obj.strftime('%Y')
            jour = date_obj.strftime('%d')

        res = super(AtmVeeam, self).create(vals)

        #Verification des statuts des machines
        if 'of' not in str(res.nbre_machine) and '0' not in str(res.nbre_machine):
            res.update({"statut": "Success"})
        else:
            res.update({"statut": "Failed"})

        # ajoute de la reference en fonction de la date
        if jour:
            if jour == '01':
                res.update({"ref": "j1"})
            if jour == '02':
                res.update({"ref": "j2"})
            if jour == '03':
                res.update({"ref": "j3"})
            if jour == '04':
                res.update({"ref": "j4"})
            if jour == '05':
                res.update({"ref": "j5"})
            if jour == '06':
                res.update({"ref": "j6"})
            if jour == '07':
                res.update({"ref": "j7"})
            if jour == '08':
                res.update({"ref": "j8"})
            if jour == '09':
                res.update({"ref": "j9"})
            if jour == '10':
                res.update({"ref": "j10"})
            if jour == '11':
                res.update({"ref": "j11"})
            if jour == '12':
                res.update({"ref": "j12"})
            if jour == '13':
                res.update({"ref": "j13"})
            if jour == '14':
                res.update({"ref": "j14"})
            if jour == '15':
                res.update({"ref": "j15"})
            if jour == '16':
                res.update({"ref": "j16"})
            if jour == '17':
                res.update({"ref": "j17"})
            if jour == '18':
                res.update({"ref": "j18"})
            if jour == '19':
                res.update({"ref": "j19"})
            if jour == '20':
                res.update({"ref": "j20"})
            if jour == '21':
                res.update({"ref": "j21"})
            if jour == '22':
                res.update({"ref": "j22"})
            if jour == '23':
                res.update({"ref": "j23"})
            if jour == '24':
                res.update({"ref": "j24"})
            if jour == '25':
                res.update({"ref": "j25"})
            if jour == '26':
                res.update({"ref": "j26"})
            if jour == '27':
                res.update({"ref": "j27"})
            if jour == '28':
                res.update({"ref": "j28"})
            if jour == '29':
                res.update({"ref": "j29"})
            if jour == '30':
                res.update({"ref": "j30"})
            if jour == '31':
                res.update({"ref": "j31"})

        return res


