import base64
import io
from odoo import models
from datetime import datetime

class StatistiqueVeeam(models.AbstractModel):
    _name = 'report.sauvegarde_veeam.statistique_veeam'
    _inherit = 'report.report_xlsx.abstract'



    def generate_xlsx_report(self, workbook, data, partners):
        # form_data=data['form_date']
        data_payroll=data['line_data']
        data2 = data['data2']
        data3 = data['data3']
        data4 = data['data4']
        data5 = data['data5']
        data6 = data['data6']
        data7 = data['data7']
        data8 = data['data8']
        data9 = data['data9']
        data10 = data['data10']
        data11 = data['data11']
        data12 = data['data12']
        data13 = data['data13']
        data14 = data['data14']
        data15 = data['data15']

        data16 = data['data16']

        data17 = data['data17']
        data18 = data['data18']
        data19 = data['data19']
        data20 = data['data20']

        data21 = data['data21']
        data22 = data['data22']
        data23 = data['data23']
        data24 = data['data24']
        data25 = data['data25']

        data26 = data['data26']
        data27 = data['data27']
        data28 = data['data28']
        data29 = data['data29']
        data30 = data['data30']
        data31 = data['data31']

        sheet = workbook.add_worksheet('STATISTIQUE DES SAUVEGARDES')

        #styles de livre de paie
        header_format = workbook.add_format(
            {'align': 'center', 'valign': 'vcenter', 'bold': 'TRUE', 'size':10,'color':'black'})
        header_format_titre = workbook.add_format(
            {'border': 2, 'align': 'center', 'valign': 'vcenter', 'bold': 'TRUE', 'size': 7})
        header_format11 = workbook.add_format(
            {'border': 1,'color':'blue', 'align': 'center', 'valign': 'vcenter', 'bold': 'TRUE', 'size': 13})
        header_taux = workbook.add_format(
            {'border': 2, 'bg_color': 'orange', 'color': 'black', 'align': 'center', 'valign': 'vcenter',
             'bold': 'TRUE', 'size': 10})
        header_numero_dossier = workbook.add_format(
            {'border':1, 'color': 'black', 'align': 'center', 'valign': 'vcenter',
              'size': 12})
        header_autres = workbook.add_format(
            {'border': 1, 'color': 'black', 'align': 'center', 'valign': 'vcenter',
              'size': 12})




        sheet.merge_range('J3:X3', "STATISTIQUE DES SAUVEGARDES", header_format)
        sheet.set_column('B:B', 30)
        sheet.set_column('C:C', 5)
        sheet.set_column('D:D', 5)
        sheet.set_column('E:E', 5)
        sheet.set_column('F:F', 5)
        sheet.set_column('G:G', 5)
        sheet.set_column('H:H', 5)
        sheet.set_column('I:I', 5)
        sheet.set_column('J:J', 5)
        sheet.set_column('K:K', 5)
        sheet.set_column('L:L', 5)
        sheet.set_column('M:M', 5)
        sheet.set_column('N:N', 5)
        sheet.set_column('O:O', 5)
        sheet.set_column('P:P', 5)
        sheet.set_column('Q:Q', 5)
        sheet.set_column('R:R', 5)
        sheet.set_column('S:S', 5)
        sheet.set_column('T:T', 5)
        sheet.set_column('U:U', 5)
        sheet.set_column('V:V', 5)
        sheet.set_column('W:W', 5)

        sheet.set_column('X:X', 5)
        sheet.set_column('Y:Y', 5)
        sheet.set_column('Z:Z', 5)
        sheet.set_column('AA:AA', 5)
        sheet.set_column('AB:AB', 5)
        sheet.set_column('AC:AC', 5)

        sheet.set_column('AD:AD', 5)
        sheet.set_column('AE:AE', 5)
        sheet.set_column('AF:AF', 5)
        sheet.set_column('AG:AG', 5)
        row=5
        col=1

        # sheet.write(row, col, 'CENTRALES', header_format11)
        # sheet.write(row, col + 1, '01', header_format11)
        # sheet.write(row, col + 2, '02', header_format11)
        # sheet.write(row, col + 3, '03', header_format11)
        # sheet.write(row, col + 4, '04', header_format11)
        # sheet.write(row, col + 5, '05', header_format11)
        # sheet.write(row, col + 6, "06", header_format11)
        # sheet.write(row, col + 7, "07", header_format11)
        # sheet.write(row, col + 8, "08", header_format11)
        # sheet.write(row, col + 9, "09", header_format11)
        # sheet.write(row, col + 10, '10', header_format11)
        # sheet.write(row, col + 11, '11', header_format11)
        # sheet.write(row, col + 12, '12', header_format11)
        # sheet.write(row, col + 13, '13', header_format11)
        # sheet.write(row, col + 14, "14", header_format11)
        # sheet.write(row, col + 15, "15", header_format11)
        # sheet.write(row, col + 16, '16', header_format11)
        # sheet.write(row, col + 17, '17', header_format11)
        # sheet.write(row, col + 18, '18', header_format11)
        # sheet.write(row, col + 19, '19', header_format11)
        # sheet.write(row, col + 20, '20', header_format11)
        # sheet.write(row, col + 21, '21', header_format11)
        # sheet.write(row, col + 22, "22", header_format11)
        # sheet.write(row, col + 23, '23', header_format11)
        # sheet.write(row, col + 24, '24', header_format11)
        # sheet.write(row, col + 25, '25', header_format11)
        # sheet.write(row, col + 26, '26', header_format11)
        # sheet.write(row, col + 27, '27', header_format11)
        # sheet.write(row, col + 28, '28', header_format11)
        # sheet.write(row, col + 29, '29', header_format11)
        # sheet.write(row, col + 30, '30', header_format11)
        # sheet.write(row, col + 31, '31', header_format11)
        # sheet.write(row, col + 32, 'TAUX', header_format11)
        row+=1

        # Combiner les deux boucles sur une même ligne
        for i in range(max(len(data_payroll), len(data2), len(data3), len(data4), len(data5), len(data6), len(data7), len(data8), len(data9), len(data10), len(data12), len(data13), len(data14), len(data15),len(data16),len(data17),len(data18),len(data19),len(data20),len(data21),len(data22),len(data23),len(data24),len(data25),len(data26),len(data27),len(data28),len(data29),len(data30),len(data31))):
            col = 1  # Réinitialiser la colonne au début de chaque ligne

            if i < len(data_payroll):  # Ajouter les données de data_payroll
                sheet.write(row, col, data_payroll[i]['name'],header_format)
                sheet.write(row, col + 1, data_payroll[i]['valeur'],header_format)

            if i < len(data2):
                sheet.write(row, col + 2, data2[i]['valeur'],header_format)

            if i < len(data3):
                sheet.write(row, col + 3, data3[i]['valeur'],header_format)

            if i < len(data4):
                sheet.write(row, col + 4, data4[i]['valeur'],header_format)

            if i < len(data5):
                sheet.write(row, col + 5, data5[i]['valeur'],header_format)

            if i < len(data6):
                sheet.write(row, col + 6, data6[i]['valeur'],header_format)

            if i < len(data7):
                sheet.write(row, col + 7, data7[i]['valeur'],header_format)

            if i < len(data8):
                sheet.write(row, col + 8, data8[i]['valeur'],header_format)


            if i < len(data9):  # Ajouter les données de data2

                sheet.write(row, col + 9, data9[i]['valeur'],header_format)

            if i < len(data10):  # Ajouter les données de data2

                sheet.write(row, col + 10, data10[i]['valeur'] ,header_format)

            if i < len(data11):  # Ajouter les données de data2

                 sheet.write(row, col + 11, data11[i]['valeur'],header_format )

            if i < len(data12):  # Ajouter les données de data2

                sheet.write(row, col + 12, data12[i]['valeur'],header_format )

            if i < len(data13):  # Ajouter les données de data2

                 sheet.write(row, col + 13, data13[i]['valeur'],header_format )


            if i < len(data14):  # Ajouter les données de data2

                sheet.write(row, col + 14, data14[i]['valeur'],header_format )

            if i < len(data15):  # Ajouter les données de data2

                sheet.write(row, col + 15, data15[i]['valeur'], header_format)

            if i < len(data16):  # Ajouter les données de data2

                sheet.write(row, col + 16, data16[i]['valeur'],header_format )

            if i < len(data17):  # Ajouter les données de data2

                 sheet.write(row, col + 17, data17[i]['valeur'],header_format)

            if i < len(data18):  # Ajouter les données de data2

                sheet.write(row, col + 18, data18[i]['valeur'],header_format )

            if i < len(data19):  # Ajouter les données de data2

                sheet.write(row, col + 19, data19[i]['valeur'],header_format )

            if i < len(data20):  # Ajouter les données de data2

                sheet.write(row, col + 20, data20[i]['valeur'],header_format )


            if i < len(data21):  # Ajouter les données de data2

                sheet.write(row, col + 21, data21[i]['valeur'] ,header_format)


            if i < len(data22):  # Ajouter les données de data2

                sheet.write(row, col + 22, data22[i]['valeur'],header_format)


            if i < len(data23):  # Ajouter les données de data2

                sheet.write(row, col + 23, data23[i]['valeur'],header_format)

            if i < len(data24):  # Ajouter les données de data2

                sheet.write(row, col + 24, data24[i]['valeur'],header_format)

            if i < len(data25):  # Ajouter les données de data2

                sheet.write(row, col + 25, data25[i]['valeur'],header_format)

            if i < len(data26):  # Ajouter les données de data2

                sheet.write(row, col + 26, data26[i]['valeur'],header_format )

            if i < len(data27):  # Ajouter les données de data2

                sheet.write(row, col + 27, data27[i]['valeur'],header_format)

            if i < len(data28):  # Ajouter les données de data2

                 sheet.write(row, col + 28, data28[i]['valeur'],header_format )

            if i < len(data29):  # Ajouter les données de data2

                    sheet.write(row, col + 29, data29[i]['valeur'],header_format)

            if i < len(data30):  # Ajouter les données de data2

                 sheet.write(row, col + 30, data30[i]['valeur1'],header_format)

            if i < len(data31):  # Ajouter les données de data2

                 sheet.write(row, col + 31, data31[i]['valeur1'],header_format)


            row += 1






