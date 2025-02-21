from odoo import models, fields
from datetime import datetime

class WizardPointeuse(models.TransientModel):
    _name = 'wizard.veeam'

    # Champs par défaut
    mois = fields.Char(string="Mois", default=lambda self: datetime.now().strftime('%m'))
    annee = fields.Char(string="Année", default=lambda self: str(datetime.now().year))

    def action_extraction_veeam(self):
        lines = []
        lines2= []
        lines3 = []
        lines4 = []
        lines5 = []
        lines6 = []
        lines7 = []
        lines8 = []
        lines9 = []
        lines10= []
        lines11 = []
        lines12 = []
        lines13 = []
        lines14 = []
        lines15 = []
        lines16 = []
        lines17 = []
        lines18 = []
        lines19 = []
        lines20 = []
        lines21 = []
        lines22 = []
        lines23 = []
        lines24 = []
        lines25 = []
        lines26 = []
        lines27 = []
        lines28 = []
        lines29 = []
        lines30 = []
        lines31 = []

        pointeuse = self.env["atm.veeam"].search([("ref","=",'j1'),("mois", "=", self.mois), ("annee", "=", self.annee)])
        pointeuse2 = self.env["atm.veeam"].search([('ref', '=','j2'),("mois", "=", self.mois), ("annee", "=", self.annee)])
        pointeuse3 = self.env["atm.veeam"].search(  [('ref', '=', 'j3'), ("mois", "=", self.mois), ("annee", "=", self.annee)])
        pointeuse4 = self.env["atm.veeam"].search([('ref', '=', 'j4'), ("mois", "=", self.mois), ("annee", "=", self.annee)])
        pointeuse5 = self.env["atm.veeam"].search([('ref', '=', 'j5'), ("mois", "=", self.mois), ("annee", "=", self.annee)])

        pointeuse6= self.env["atm.veeam"].search([("ref", "=", 'j6'), ("mois", "=", self.mois), ("annee", "=", self.annee)])
        pointeuse7 = self.env["atm.veeam"].search([('ref', '=', 'j7'), ("mois", "=", self.mois), ("annee", "=", self.annee)])
        pointeuse8 = self.env["atm.veeam"].search([('ref', '=', 'j8'), ("mois", "=", self.mois), ("annee", "=", self.annee)])
        pointeuse9 = self.env["atm.veeam"].search([('ref', '=', 'j9'), ("mois", "=", self.mois), ("annee", "=", self.annee)])
        pointeuse10 = self.env["atm.veeam"].search([('ref', '=', 'j10'), ("mois", "=", self.mois), ("annee", "=", self.annee)])

        pointeuse11= self.env["atm.veeam"].search([("ref", "=", 'j11'), ("mois", "=", self.mois), ("annee", "=", self.annee)])
        pointeuse12= self.env["atm.veeam"].search([('ref', '=', 'j12'), ("mois", "=", self.mois), ("annee", "=", self.annee)])
        pointeuse13= self.env["atm.veeam"].search([('ref', '=', 'j13'), ("mois", "=", self.mois), ("annee", "=", self.annee)])
        pointeuse14= self.env["atm.veeam"].search([('ref', '=', 'j14'), ("mois", "=", self.mois), ("annee", "=", self.annee)])
        pointeuse15= self.env["atm.veeam"].search([('ref', '=', 'j15'), ("mois", "=", self.mois), ("annee", "=", self.annee)])

        pointeuse16 = self.env["atm.veeam"].search([("ref", "=", 'j16'), ("mois", "=", self.mois), ("annee", "=", self.annee)])

        pointeuse17 = self.env["atm.veeam"].search([('ref', '=', 'j17'), ("mois", "=", self.mois), ("annee", "=", self.annee)])
        pointeuse18 = self.env["atm.veeam"].search([('ref', '=', 'j18'), ("mois", "=", self.mois), ("annee", "=", self.annee)])
        pointeuse19 = self.env["atm.veeam"].search([('ref', '=', 'j19'), ("mois", "=", self.mois), ("annee", "=", self.annee)])
        pointeuse20= self.env["atm.veeam"].search([('ref', '=', 'j20'), ("mois", "=", self.mois), ("annee", "=", self.annee)])

        pointeuse21 = self.env["atm.veeam"].search([("ref", "=", 'j21'), ("mois", "=", self.mois), ("annee", "=", self.annee)])
        pointeuse22 = self.env["atm.veeam"].search( [('ref', '=', 'j22'), ("mois", "=", self.mois), ("annee", "=", self.annee)])
        pointeuse23 = self.env["atm.veeam"].search( [('ref', '=', 'j23'), ("mois", "=", self.mois), ("annee", "=", self.annee)])
        pointeuse24 = self.env["atm.veeam"].search([('ref', '=', 'j24'), ("mois", "=", self.mois), ("annee", "=", self.annee)])
        pointeuse25= self.env["atm.veeam"].search([('ref', '=', 'j25'), ("mois", "=", self.mois), ("annee", "=", self.annee)])

        pointeuse26 = self.env["atm.veeam"].search([("ref", "=", 'j26'), ("mois", "=", self.mois), ("annee", "=", self.annee)])
        pointeuse27 = self.env["atm.veeam"].search([('ref', '=', 'j27'), ("mois", "=", self.mois), ("annee", "=", self.annee)])
        pointeuse28 = self.env["atm.veeam"].search([('ref', '=', 'j28'), ("mois", "=", self.mois), ("annee", "=", self.annee)])
        pointeuse29 = self.env["atm.veeam"].search([('ref', '=', 'j29'), ("mois", "=", self.mois), ("annee", "=", self.annee)])
        pointeuse30 = self.env["atm.veeam"].search([('ref', '=', 'j30'), ("mois", "=", self.mois), ("annee", "=", self.annee)])

        pointeuse31 = self.env["atm.veeam"].search([('ref', '=', 'j31'), ("mois", "=", self.mois), ("annee", "=", self.annee)])

        for line in pointeuse:
            valeur_process = line.nbre_machine.strip()
            val1, val2 = 0, 0

            if 'of' in valeur_process:
                parts = valeur_process.split('of')  # Séparation autour de "of"
                val1 = parts[0].strip()  # Extraction du premier chiffre
                val2 = parts[1].strip()  # Extraction du deuxième chiffre

                #Faisons le calcule
                if val1 == 0:
                    valeur_p =0
                else:
                    valeur_p= int(val1)/int(val2) * 100

                vals = {
                    'name': line.name,
                    'valeur': valeur_p
                }

            else:
                val1 = valeur_process[:1]  # Si pas "of", récupérer le premier chiffre seulement

                # faisons le calcul
                valeur_p = int(val1) * 100
                vals = {
                    'name': line.name,
                    'valeur':valeur_p
                }

            lines.append(vals)

        for line in pointeuse2:
            valeur_process = line.nbre_machine.strip()
            val1, val2 = 0, 0

            if 'of' in valeur_process:
                parts = valeur_process.split('of')  # Séparation autour de "of"
                val1 = parts[0].strip()  # Extraction du premier chiffre
                val2 = parts[1].strip()  # Extraction du deuxième chiffre

                # Faisons le calcule
                if val1 == 0:
                    valeur_p = 0
                else:
                    valeur_p = int(val1) / int(val2) * 100

                vals = {
                    'valeur': valeur_p
                }

            else:
                val1 = valeur_process[:1]  # Si pas "of", récupérer le premier chiffre seulement

                # faisons le calcul
                valeur_p = int(val1) * 100
                vals = {
                    'valeur': valeur_p
                }
            lines2.append(vals)

        for line in pointeuse3:
            valeur_process = line.nbre_machine.strip()
            val1, val2 = 0, 0

            if 'of' in valeur_process:
                parts = valeur_process.split('of')  # Séparation autour de "of"
                val1 = parts[0].strip()  # Extraction du premier chiffre
                val2 = parts[1].strip()  # Extraction du deuxième chiffre

                # Faisons le calcule
                if val1 == 0:
                    valeur_p = 0
                else:
                    valeur_p = int(val1) / int(val2) * 100

                vals = {
                    'valeur': valeur_p
                }

            else:
                val1 = valeur_process[:1]  # Si pas "of", récupérer le premier chiffre seulement

                # faisons le calcul
                valeur_p = int(val1) * 100
                vals = {
                    'valeur': valeur_p
                }
            lines3.append(vals)

        for line in pointeuse4:
            valeur_process = line.nbre_machine.strip()
            val1, val2 = 0, 0

            if 'of' in valeur_process:
                parts = valeur_process.split('of')  # Séparation autour de "of"
                val1 = parts[0].strip()  # Extraction du premier chiffre
                val2 = parts[1].strip()  # Extraction du deuxième chiffre

                # Faisons le calcule
                if val1 == 0:
                    valeur_p = 0
                else:
                    valeur_p = int(val1) / int(val2) * 100

                vals = {
                    'valeur': valeur_p
                }

            else:
                val1 = valeur_process[:1]  # Si pas "of", récupérer le premier chiffre seulement

                # faisons le calcul
                valeur_p = int(val1) * 100
                vals = {
                    'valeur': valeur_p
                }
            lines4.append(vals)

        for line in pointeuse5:
            valeur_process = line.nbre_machine.strip()
            val1, val2 = 0, 0

            if 'of' in valeur_process:
                parts = valeur_process.split('of')  # Séparation autour de "of"
                val1 = parts[0].strip()  # Extraction du premier chiffre
                val2 = parts[1].strip()  # Extraction du deuxième chiffre

                # Faisons le calcule
                if val1 == 0:
                    valeur_p = 0
                else:
                    valeur_p = int(val1) / int(val2) * 100

                vals = {
                    'valeur': valeur_p
                }

            else:
                val1 = valeur_process[:1]  # Si pas "of", récupérer le premier chiffre seulement

                # faisons le calcul
                valeur_p = int(val1) * 100
                vals = {
                    'valeur': valeur_p
                }
            lines5.append(vals)

        for line in pointeuse6:
            valeur_process = line.nbre_machine.strip()
            val1, val2 = 0, 0

            if 'of' in valeur_process:
                parts = valeur_process.split('of')  # Séparation autour de "of"
                val1 = parts[0].strip()  # Extraction du premier chiffre
                val2 = parts[1].strip()  # Extraction du deuxième chiffre

                # Faisons le calcule
                if val1 == 0:
                    valeur_p = 0
                else:
                    valeur_p = int(val1) / int(val2) * 100

                vals = {
                    'valeur': valeur_p
                }

            else:
                val1 = valeur_process[:1]  # Si pas "of", récupérer le premier chiffre seulement

                # faisons le calcul
                valeur_p = int(val1) * 100
                vals = {
                    'valeur': valeur_p
                }
            lines6.append(vals)

        for line in pointeuse7:
            valeur_process = line.nbre_machine.strip()
            val1, val2 = 0, 0

            if 'of' in valeur_process:
                parts = valeur_process.split('of')  # Séparation autour de "of"
                val1 = parts[0].strip()  # Extraction du premier chiffre
                val2 = parts[1].strip()  # Extraction du deuxième chiffre

                # Faisons le calcule
                if val1 == 0:
                    valeur_p = 0
                else:
                    valeur_p = int(val1) / int(val2) * 100

                vals = {
                    'valeur': valeur_p
                }

            else:
                val1 = valeur_process[:1]  # Si pas "of", récupérer le premier chiffre seulement

                # faisons le calcul
                valeur_p = int(val1) * 100
                vals = {
                    'valeur': valeur_p
                }
            lines7.append(vals)

        for line in pointeuse8:
            valeur_process = line.nbre_machine.strip()
            val1, val2 = 0, 0

            if 'of' in valeur_process:
                parts = valeur_process.split('of')  # Séparation autour de "of"
                val1 = parts[0].strip()  # Extraction du premier chiffre
                val2 = parts[1].strip()  # Extraction du deuxième chiffre

                # Faisons le calcule
                if val1 == 0:
                    valeur_p = 0
                else:
                    valeur_p = int(val1) / int(val2) * 100

                vals = {
                    'valeur': valeur_p
                }

            else:
                val1 = valeur_process[:1]  # Si pas "of", récupérer le premier chiffre seulement

                # faisons le calcul
                valeur_p = int(val1) * 100
                vals = {
                    'valeur': valeur_p
                }
            lines8.append(vals)

        for line in pointeuse9:
            valeur_process = line.nbre_machine.strip()
            val1, val2 = 0, 0

            if 'of' in valeur_process:
                parts = valeur_process.split('of')  # Séparation autour de "of"
                val1 = parts[0].strip()  # Extraction du premier chiffre
                val2 = parts[1].strip()  # Extraction du deuxième chiffre

                # Faisons le calcule
                if val1 == 0:
                    valeur_p = 0
                else:
                    valeur_p = int(val1) / int(val2) * 100

                vals = {
                    'valeur': valeur_p
                }

            else:
                val1 = valeur_process[:1]  # Si pas "of", récupérer le premier chiffre seulement

                # faisons le calcul
                valeur_p = int(val1) * 100
                vals = {
                    'valeur': valeur_p
                }

            lines9.append(vals)

        for line in pointeuse10:
            valeur_process = line.nbre_machine.strip()
            val1, val2 = 0, 0

            if 'of' in valeur_process:
                parts = valeur_process.split('of')  # Séparation autour de "of"
                val1 = parts[0].strip()  # Extraction du premier chiffre
                val2 = parts[1].strip()  # Extraction du deuxième chiffre

                # Faisons le calcule
                if val1 == 0:
                    valeur_p = 0
                else:
                    valeur_p = int(val1) / int(val2) * 100

                vals = {
                    'valeur': valeur_p
                }

            else:
                val1 = valeur_process[:1]  # Si pas "of", récupérer le premier chiffre seulement

                # faisons le calcul
                valeur_p = int(val1) * 100
                vals = {
                    'valeur': valeur_p
                }
            lines10.append(vals)

        for line in pointeuse11:
            valeur_process = line.nbre_machine.strip()
            val1, val2 = 0, 0

            if 'of' in valeur_process:
                parts = valeur_process.split('of')  # Séparation autour de "of"
                val1 = parts[0].strip()  # Extraction du premier chiffre
                val2 = parts[1].strip()  # Extraction du deuxième chiffre

                # Faisons le calcule
                if val1 == 0:
                    valeur_p = 0
                else:
                    valeur_p = int(val1) / int(val2) * 100

                vals = {
                    'valeur': valeur_p
                }

            else:
                val1 = valeur_process[:1]  # Si pas "of", récupérer le premier chiffre seulement

                # faisons le calcul
                valeur_p = int(val1) * 100
                vals = {
                    'valeur': valeur_p
                }
            lines11.append(vals)

        for line in pointeuse12:
            valeur_process = line.nbre_machine.strip()
            val1, val2 = 0, 0

            if 'of' in valeur_process:
                parts = valeur_process.split('of')  # Séparation autour de "of"
                val1 = parts[0].strip()  # Extraction du premier chiffre
                val2 = parts[1].strip()  # Extraction du deuxième chiffre

                # Faisons le calcule
                if val1 == 0:
                    valeur_p = 0
                else:
                    valeur_p = int(val1) / int(val2) * 100

                vals = {
                    'valeur': valeur_p
                }

            else:
                val1 = valeur_process[:1]  # Si pas "of", récupérer le premier chiffre seulement

                # faisons le calcul
                valeur_p = int(val1) * 100
                vals = {
                    'valeur': valeur_p
                }
            lines12.append(vals)

        for line in pointeuse13:
            valeur_process = line.nbre_machine.strip()
            val1, val2 = 0, 0

            if 'of' in valeur_process:
                parts = valeur_process.split('of')  # Séparation autour de "of"
                val1 = parts[0].strip()  # Extraction du premier chiffre
                val2 = parts[1].strip()  # Extraction du deuxième chiffre

                # Faisons le calcule
                if val1 == 0:
                    valeur_p = 0
                else:
                    valeur_p = int(val1) / int(val2) * 100

                vals = {
                    'valeur': valeur_p
                }

            else:
                val1 = valeur_process[:1]  # Si pas "of", récupérer le premier chiffre seulement

                # faisons le calcul
                valeur_p = int(val1) * 100
                vals = {
                    'valeur': valeur_p
                }
            lines13.append(vals)

        for line in pointeuse14:
            valeur_process = line.nbre_machine.strip()
            val1, val2 = 0, 0

            if 'of' in valeur_process:
                parts = valeur_process.split('of')  # Séparation autour de "of"
                val1 = parts[0].strip()  # Extraction du premier chiffre
                val2 = parts[1].strip()  # Extraction du deuxième chiffre

                # Faisons le calcule
                if val1 == 0:
                    valeur_p = 0
                else:
                    valeur_p = int(val1) / int(val2) * 100

                vals = {
                    'valeur': valeur_p
                }

            else:
                val1 = valeur_process[:1]  # Si pas "of", récupérer le premier chiffre seulement

                # faisons le calcul
                valeur_p = int(val1) * 100
                vals = {
                    'valeur': valeur_p
                }
            lines14.append(vals)

        for line in pointeuse15:
            valeur_process = line.nbre_machine.strip()
            val1, val2 = 0, 0

            if 'of' in valeur_process:
                parts = valeur_process.split('of')  # Séparation autour de "of"
                val1 = parts[0].strip()  # Extraction du premier chiffre
                val2 = parts[1].strip()  # Extraction du deuxième chiffre

                # Faisons le calcule
                if val1 == 0:
                    valeur_p = 0
                else:
                    valeur_p = int(val1) / int(val2) * 100

                vals = {
                    'valeur': valeur_p
                }


            else:
                val1 = valeur_process[:1]  # Si pas "of", récupérer le premier chiffre seulement

                # faisons le calcul
                valeur_p = int(val1) * 100
                vals = {
                    'valeur': valeur_p
                }

            lines15.append(vals)

        for line in pointeuse16:
            valeur_process = line.nbre_machine.strip()
            val1, val2 = 0, 0

            if 'of' in valeur_process:
                parts = valeur_process.split('of')  # Séparation autour de "of"
                val1 = parts[0].strip()  # Extraction du premier chiffre
                val2 = parts[1].strip()  # Extraction du deuxième chiffre

                # Faisons le calcule
                if val1 == 0:
                    valeur_p = 0
                else:
                    valeur_p = int(val1) / int(val2) * 100

                vals = {
                    'valeur': valeur_p
                }

            else:
                val1 = valeur_process[:1]  # Si pas "of", récupérer le premier chiffre seulement

                # faisons le calcul
                valeur_p = int(val1) * 100
                vals = {
                    'valeur': valeur_p
                }
            lines16.append(vals)

        for line in pointeuse17:
            valeur_process = line.nbre_machine.strip()
            val1, val2 = 0, 0

            if 'of' in valeur_process:
                parts = valeur_process.split('of')  # Séparation autour de "of"
                val1 = parts[0].strip()  # Extraction du premier chiffre
                val2 = parts[1].strip()  # Extraction du deuxième chiffre

                # Faisons le calcule
                if val1 == 0:
                    valeur_p = 0
                else:
                    valeur_p = int(val1) / int(val2) * 100

                vals = {
                    'valeur': valeur_p
                }

            else:
                val1 = valeur_process[:1]  # Si pas "of", récupérer le premier chiffre seulement

                # faisons le calcul
                valeur_p = int(val1) * 100
                vals = {
                    'valeur': valeur_p
                }
            lines17.append(vals)

        for line in pointeuse18:
            valeur_process = line.nbre_machine.strip()
            val1, val2 = 0, 0

            if 'of' in valeur_process:
                parts = valeur_process.split('of')  # Séparation autour de "of"
                val1 = parts[0].strip()  # Extraction du premier chiffre
                val2 = parts[1].strip()  # Extraction du deuxième chiffre

                # Faisons le calcule
                if val1 == 0:
                    valeur_p = 0
                else:
                    valeur_p = int(val1) / int(val2) * 100

                vals = {
                    'valeur': valeur_p
                }

            else:
                val1 = valeur_process[:1]  # Si pas "of", récupérer le premier chiffre seulement

                # faisons le calcul
                valeur_p = int(val1) * 100
                vals = {
                    'valeur': valeur_p
                }
            lines18.append(vals)

        for line in pointeuse19:
            valeur_process = line.nbre_machine.strip()
            val1, val2 = 0, 0

            if 'of' in valeur_process:
                parts = valeur_process.split('of')  # Séparation autour de "of"
                val1 = parts[0].strip()  # Extraction du premier chiffre
                val2 = parts[1].strip()  # Extraction du deuxième chiffre

                # Faisons le calcule
                if val1 == 0:
                    valeur_p = 0
                else:
                    valeur_p = int(val1) / int(val2) * 100

                vals = {
                    'valeur': valeur_p
                }

            else:
                val1 = valeur_process[:1]  # Si pas "of", récupérer le premier chiffre seulement

                # faisons le calcul
                valeur_p = int(val1) * 100
                vals = {
                    'valeur': valeur_p
                }
            lines19.append(vals)

        for line in pointeuse20:
            valeur_process = line.nbre_machine.strip()
            val1, val2 = 0, 0

            if 'of' in valeur_process:
                parts = valeur_process.split('of')  # Séparation autour de "of"
                val1 = parts[0].strip()  # Extraction du premier chiffre
                val2 = parts[1].strip()  # Extraction du deuxième chiffre

                # Faisons le calcule
                if val1 == 0:
                    valeur_p = 0
                else:
                    valeur_p = int(val1) / int(val2) * 100

                vals = {
                    'valeur': valeur_p
                }

            else:
                val1 = valeur_process[:1]  # Si pas "of", récupérer le premier chiffre seulement

                # faisons le calcul
                valeur_p = int(val1) * 100
                vals = {
                    'valeur': valeur_p
                }
            lines20.append(vals)

        for line in pointeuse21:
            valeur_process = line.nbre_machine.strip()
            val1, val2 = 0, 0

            if 'of' in valeur_process:
                parts = valeur_process.split('of')  # Séparation autour de "of"
                val1 = parts[0].strip()  # Extraction du premier chiffre
                val2 = parts[1].strip()  # Extraction du deuxième chiffre

                # Faisons le calcule
                if val1 == 0:
                    valeur_p = 0
                else:
                    valeur_p = int(val1) / int(val2) * 100

                vals = {
                    'valeur': valeur_p
                }

            else:
                val1 = valeur_process[:1]  # Si pas "of", récupérer le premier chiffre seulement

                # faisons le calcul
                valeur_p = int(val1) * 100
                vals = {
                    'valeur': valeur_p
                }
            lines21.append(vals)

        for line in pointeuse22:
            valeur_process = line.nbre_machine.strip()
            val1, val2 = 0, 0

            if 'of' in valeur_process:
                parts = valeur_process.split('of')  # Séparation autour de "of"
                val1 = parts[0].strip()  # Extraction du premier chiffre
                val2 = parts[1].strip()  # Extraction du deuxième chiffre

                # Faisons le calcule
                if val1 == 0:
                    valeur_p = 0
                else:
                    valeur_p = int(val1) / int(val2) * 100

                vals = {
                    'valeur': valeur_p
                }

            else:
                val1 = valeur_process[:1]  # Si pas "of", récupérer le premier chiffre seulement

                # faisons le calcul
                valeur_p = int(val1) * 100
                vals = {
                    'valeur': valeur_p
                }
            lines22.append(vals)

        for line in pointeuse23:
            valeur_process = line.nbre_machine.strip()
            val1, val2 = 0, 0

            if 'of' in valeur_process:
                parts = valeur_process.split('of')  # Séparation autour de "of"
                val1 = parts[0].strip()  # Extraction du premier chiffre
                val2 = parts[1].strip()  # Extraction du deuxième chiffre

                # Faisons le calcule
                if val1 == 0:
                    valeur_p = 0
                else:
                    valeur_p = int(val1) / int(val2) * 100

                vals = {
                    'valeur': valeur_p
                }

            else:
                val1 = valeur_process[:1]  # Si pas "of", récupérer le premier chiffre seulement

                # faisons le calcul
                valeur_p = int(val1) * 100
                vals = {
                    'valeur': valeur_p
                }
            lines23.append(vals)

        for line in pointeuse24:
            valeur_process = line.nbre_machine.strip()
            val1, val2 = 0, 0

            if 'of' in valeur_process:
                parts = valeur_process.split('of')  # Séparation autour de "of"
                val1 = parts[0].strip()  # Extraction du premier chiffre
                val2 = parts[1].strip()  # Extraction du deuxième chiffre

                # Faisons le calcule
                if val1 == 0:
                    valeur_p = 0
                else:
                    valeur_p = int(val1) / int(val2) * 100

                vals = {
                    'valeur': valeur_p
                }

            else:
                val1 = valeur_process[:1]  # Si pas "of", récupérer le premier chiffre seulement

                # faisons le calcul
                valeur_p = int(val1) * 100
                vals = {
                    'valeur': valeur_p
                }
            lines24.append(vals)

        for line in pointeuse25:
            valeur_process = line.nbre_machine.strip()
            val1, val2 = 0, 0

            if 'of' in valeur_process:
                parts = valeur_process.split('of')  # Séparation autour de "of"
                val1 = parts[0].strip()  # Extraction du premier chiffre
                val2 = parts[1].strip()  # Extraction du deuxième chiffre

                # Faisons le calcule
                if val1 == 0:
                    valeur_p = 0
                else:
                    valeur_p = int(val1) / int(val2) * 100

                vals = {
                    'valeur': valeur_p
                }

            else:
                val1 = valeur_process[:1]  # Si pas "of", récupérer le premier chiffre seulement

                # faisons le calcul
                valeur_p = int(val1) * 100
                vals = {
                    'valeur': valeur_p
                }
            lines25.append(vals)

        for line in pointeuse26:
            valeur_process = line.nbre_machine.strip()
            val1, val2 = 0, 0

            if 'of' in valeur_process:
                parts = valeur_process.split('of')  # Séparation autour de "of"
                val1 = parts[0].strip()  # Extraction du premier chiffre
                val2 = parts[1].strip()  # Extraction du deuxième chiffre

                # Faisons le calcule
                if val1 == 0:
                    valeur_p = 0
                else:
                    valeur_p = int(val1) / int(val2) * 100

                vals = {
                    'valeur': valeur_p
                }

            else:
                val1 = valeur_process[:1]  # Si pas "of", récupérer le premier chiffre seulement

                # faisons le calcul
                valeur_p = int(val1) * 100
                vals = {
                    'valeur': valeur_p
                }
            lines26.append(vals)

        for line in pointeuse27:
            valeur_process = line.nbre_machine.strip()
            val1, val2 = 0, 0

            if 'of' in valeur_process:
                parts = valeur_process.split('of')  # Séparation autour de "of"
                val1 = parts[0].strip()  # Extraction du premier chiffre
                val2 = parts[1].strip()  # Extraction du deuxième chiffre

                # Faisons le calcule
                if val1 == 0:
                    valeur_p = 0
                else:
                    valeur_p = int(val1) / int(val2) * 100

                vals = {
                    'valeur': valeur_p
                }

            else:
                val1 = valeur_process[:1]  # Si pas "of", récupérer le premier chiffre seulement

                # faisons le calcul
                valeur_p = int(val1) * 100
                vals = {
                    'valeur': valeur_p
                }
            lines27.append(vals)

        for line in pointeuse28:
            valeur_process = line.nbre_machine.strip()
            val1, val2 = 0, 0

            if 'of' in valeur_process:
                parts = valeur_process.split('of')  # Séparation autour de "of"
                val1 = parts[0].strip()  # Extraction du premier chiffre
                val2 = parts[1].strip()  # Extraction du deuxième chiffre

                # Faisons le calcule
                if val1 == 0:
                    valeur_p = 0
                else:
                    valeur_p = int(val1) / int(val2) * 100

                vals = {
                    'valeur': valeur_p
                }

            else:
                val1 = valeur_process[:1]  # Si pas "of", récupérer le premier chiffre seulement

                # faisons le calcul
                valeur_p = int(val1) * 100
                vals = {
                    'valeur': valeur_p
                }
            lines28.append(vals)

        for line in pointeuse29:
            valeur_process = line.nbre_machine.strip()
            val1, val2 = 0, 0

            if 'of' in valeur_process:
                parts = valeur_process.split('of')  # Séparation autour de "of"
                val1 = parts[0].strip()  # Extraction du premier chiffre
                val2 = parts[1].strip()  # Extraction du deuxième chiffre

                # Faisons le calcule
                if val1 == 0:
                    valeur_p = 0
                else:
                    valeur_p = int(val1) / int(val2) * 100

                vals = {
                    'valeur': valeur_p
                }

            else:
                val1 = valeur_process[:1]  # Si pas "of", récupérer le premier chiffre seulement

                # faisons le calcul
                valeur_p = int(val1) * 100
                vals = {
                    'valeur': valeur_p
                }
            lines29.append(vals)

        for line in pointeuse30:
            valeur_process = line.nbre_machine.strip()
            val1, val2 = 0, 0

            if 'of' in valeur_process:
                parts = valeur_process.split('of')  # Séparation autour de "of"
                val1 = parts[0].strip()  # Extraction du premier chiffre
                val2 = parts[1].strip()  # Extraction du deuxième chiffre

                # Faisons le calcule
                if val1 == 0:
                    valeur_p = 0
                else:
                    valeur_p = int(val1) / int(val2) * 100

                vals = {
                    'valeur': valeur_p
                }

            else:
                val1 = valeur_process[:1]  # Si pas "of", récupérer le premier chiffre seulement

                # faisons le calcul
                valeur_p = int(val1) * 100
                vals = {
                    'valeur': valeur_p
                }
            lines30.append(vals)

        for line in pointeuse31:
            valeur_process = line.nbre_machine.strip()
            val1, val2 = 0, 0

            if 'of' in valeur_process:
                parts = valeur_process.split('of')  # Séparation autour de "of"
                val1 = parts[0].strip()  # Extraction du premier chiffre
                val2 = parts[1].strip()  # Extraction du deuxième chiffre

                # Faisons le calcule
                if val1 == 0:
                    valeur_p = 0
                else:
                    valeur_p = int(val1) / int(val2) * 100

                vals = {
                    'valeur': valeur_p
                }

            else:
                val1 = valeur_process[:1]  # Si pas "of", récupérer le premier chiffre seulement

                # faisons le calcul
                valeur_p = int(val1) * 100
                vals = {
                    'valeur': valeur_p
                }
            lines31.append(vals)





        # Inclure les champs mois et annee dans les données envoyées au rapport
        data = {
            'form_date': self.read()[0],
            'line_data': lines,
            'data2': lines2,
            'data3': lines3,
            'data4': lines4,
            'data5': lines5,
            'data6': lines6,
            'data7': lines7,
            'data8': lines8,
            'data9': lines9,
            'data10': lines10,
            'data11': lines11,
            'data12': lines12,
            'data13': lines13,
            'data14': lines14,
            'data15': lines15,
            'data16': lines16,
            'data17': lines17,
            'data18': lines18,
            'data19': lines19,
            'data20': lines20,
            'data21': lines21,
            'data22': lines22,
            'data23': lines23,
            'data24': lines24,
            'data25': lines25,
            'data26': lines26,
            'data27': lines27,
            'data28': lines28,
            'data29': lines29,
            'data30': lines30,
            'data31': lines31,
            'mois': self.mois,  # Mois par défaut
            'annee': self.annee  # Année par défaut
        }

        return self.env.ref('sauvegarde_veeam.action_veeam_xlsx').report_action(self, data=data)
