assignments = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9',
             'A10', 'A11', 'A12', 'A13', 'A14', 'A15', 'A16', 'A17',
             'A18', 'A19', 'A20', 'A21', 'A22', 'A23', 'A24', 'A25', 
             'A26', 'A27', 'A28', 'A29', 'A30', 'A31', 'A32', 'A33',
             'A34', 'A35', 'A36', 'A37', 'A38', 'A39', 'A40', 'A41', 
             'A42', 'A43', 'A44', 'A45', 'A46', 'A47', 'A48', 'A49', 
             'A50', 'A51', 'A52', 'A53', 'A54', 'A55', 'A56', 'A57', 
             'A58', 'A59', 'A60', 'A61', 'A62', 'A63', 'A64', 'A65', 
             'A66', 'A67', 'A68', 'A69', 'A70', 'A71', 'A72', 'A73', 
             'A74', 'A75', 'A76', 'A77', 'A78', 'A79', 'A80', 'A81', 
             'A82', 'A83', 'A84', 'A85', 'A86', 'A87', 'A88']

times = {'A1': 15, 'A2': 5, 'A3': 8, 'A4': 11, 'A5': 9, 'A6': 8, 'A7': 10,
         'A8': 12, 'A9': 9, 'A10': 13, 'A11': 6, 'A12': 12, 'A13': 3, 'A14': 9,
         'A15': 13, 'A16': 12, 'A17': 10, 'A18': 6, 'A19': 11, 'A20': 4, 'A21': 11,
         'A22': 10, 'A23': 9, 'A24': 10, 'A25': 8, 'A26': 6, 'A27': 8, 'A28': 6,
         'A29': 9, 'A30': 11, 'A31': 14, 'A32': 6, 'A33': 3, 'A34': 13, 'A35': 12,
         'A36': 5, 'A37': 12, 'A38': 12, 'A39': 10, 'A40': 14, 'A41': 7, 'A42': 13,
         'A43': 14, 'A44': 15, 'A45': 5, 'A46': 15, 'A47': 14, 'A48': 5, 'A49': 4,
         'A50': 11, 'A51': 13, 'A52': 11, 'A53': 5, 'A54': 5, 'A55': 9, 'A56': 5,
         'A57': 9, 'A58': 8, 'A59': 7, 'A60': 3, 'A61': 4, 'A62': 12, 'A63': 9,
         'A64': 6, 'A65': 9, 'A66': 15, 'A67': 14, 'A68': 8, 'A69': 4, 'A70': 6,
         'A71': 3, 'A72': 11, 'A73': 11, 'A74': 13, 'A75': 4, 'A76': 15, 'A77': 9,
         'A78': 13, 'A79': 9, 'A80': 9, 'A81': 5, 'A82': 9, 'A83': 13, 'A84': 9,
         'A85': 6, 'A86': 11, 'A87': 9, 'A88': 4}

values = {'A1': 12, 'A2': 9, 'A3': 9, 'A4': 13, 'A5': 9, 'A6': 9, 'A7': 10,
'A8': 14, 'A9': 9, 'A10': 13, 'A11': 9, 'A12': 14, 'A13': 9, 'A14': 15,
'A15': 14, 'A16': 15, 'A17': 10, 'A18': 9, 'A19': 13, 'A20': 9, 'A21': 10,
'A22': 11, 'A23': 9, 'A24': 13, 'A25': 9, 'A26': 9, 'A27': 9, 'A28': 9,
'A29': 13, 'A30': 11, 'A31': 12, 'A32': 9, 'A33': 9, 'A34': 12, 'A35': 15,
'A36': 14, 'A37': 15, 'A38': 9, 'A39': 13, 'A40': 9, 'A41': 14, 'A42': 9,
'A43': 15, 'A44': 13, 'A45': 9, 'A46': 15, 'A47': 9, 'A48': 9, 'A49': 10,
'A50': 12, 'A51': 9, 'A52': 13, 'A53': 9, 'A54': 9, 'A55': 9, 'A56': 9,
'A57': 13, 'A58': 11, 'A59': 12, 'A60': 9, 'A61': 9, 'A62': 15, 'A63': 13,
'A64': 9, 'A65': 9, 'A66': 12, 'A67': 9, 'A68': 15, 'A69': 13, 'A70': 9,
'A71': 15, 'A72': 9, 'A73': 10, 'A74': 12, 'A75': 9, 'A76': 9, 'A77': 9,
'A78': 13, 'A79': 9, 'A80': 9, 'A81': 13, 'A82': 9, 'A83': 9, 'A84': 9,
'A85': 15, 'A86': 13, 'A87': 9, 'A88': 15}

#

dependencies = {'A3':['A52'],'A5':['A11'],
                'A6':['A77'],'A8':['A4'],'A10':['A54'],
                'A15':['A75'],'A16':['A59'],'A17':['A2'],'A22':['A4'],'A24':['A53'],
                'A26':['A27'],'A30':['A19'],'A34':['A30'],'A39':['A1'],'A42':['A85'],
                'A46':['A35'],'A48':['A62'],'A51':['A84'],'A53':['A69'],'A57':['A29'],
                'A58':['A48'],'A59':['A62'],'A60':['A74'],'A64':['A85'],'A66':['A48'],
                'A70':['A10'],'A71':['A63'],'A72':['A64'],'A76':['A36'],'A77':['A23'],
                'A81':['A8'],'A82':['A60'],'A83':['A67'], 'A86':['A29'],
                'A88':['A18']}

#required = ['A2','A3','A4','A8','A9','A19','A20','A23','A28','A30','A34','A39','A40','A43','A48','A52','A56','A61','A68','A70','A76','A79','A83','A85','A87','A88']

kmin = 88
kmax = 100