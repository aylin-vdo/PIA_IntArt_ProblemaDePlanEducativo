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

times = {'A1': 5, 'A2': 10, 'A3': 15, 'A4': 8, 'A5': 3, 'A6': 9, 'A7': 7,
          'A8': 15, 'A9': 6, 'A10': 9, 'A11': 9, 'A12': 9, 'A13': 12, 'A14': 7,
         'A15': 14, 'A16': 13, 'A17': 11, 'A18': 15, 'A19': 8, 'A20':3, 'A21': 11,
         'A22': 10, 'A23': 7, 'A24': 7, 'A25': 9, 'A26': 15, 'A27': 9, 'A28': 10,
         'A29': 10, 'A30': 11, 'A31': 11, 'A32': 11, 'A33': 8, 'A34': 9, 'A35': 3,
         'A36': 9, 'A37': 7, 'A38': 8, 'A39': 12, 'A40': 6, 'A41': 6, 'A42': 9,
         'A43': 8, 'A44': 9, 'A45': 9, 'A46': 5, 'A47': 14, 'A48': 7, 'A49': 10,
         'A50': 14, 'A51': 9, 'A52': 11, 'A53': 13, 'A54': 8, 'A55': 4, 'A56': 7,
         'A57': 9, 'A58': 8, 'A59': 10, 'A60': 5, 'A61': 10, 'A62': 13, 'A63': 12,
         'A64': 8, 'A65': 15, 'A66': 9, 'A67': 11, 'A68': 9, 'A69': 10, 'A70': 6,
         'A71': 11, 'A72': 15, 'A73': 10, 'A74': 5, 'A75': 9, 'A76': 4, 'A77': 14,
         'A78': 6, 'A79': 13, 'A80': 6, 'A81': 8, 'A82': 13, 'A83': 4, 'A84': 3,
         'A85': 14, 'A86': 9, 'A87': 10, 'A88': 12}

values = {'A1': 9, 'A2': 13, 'A3': 14, 'A4': 9, 'A5': 9, 'A6': 9, 'A7': 9,
        'A8': 10, 'A9': 9, 'A10': 9, 'A11': 9, 'A12': 9, 'A13': 12, 'A14': 9,
        'A15': 9, 'A16': 9, 'A17': 12, 'A18': 11, 'A19': 9, 'A20': 9, 'A21': 13,
        'A22': 11, 'A23': 9, 'A24': 9, 'A25': 12, 'A26': 12, 'A27': 9, 'A28': 12,
        'A29': 12, 'A30': 9, 'A31': 15, 'A32': 15, 'A33': 9, 'A34': 12, 'A35': 9,
        'A36': 9, 'A37': 9, 'A38': 9, 'A39': 9, 'A40': 9, 'A41': 9, 'A42': 10,
        'A43': 9, 'A44': 9, 'A45': 9, 'A46': 9, 'A47': 13, 'A48': 9, 'A49': 9,
        'A50': 13, 'A51': 15, 'A52': 13, 'A53': 15, 'A54': 9, 'A55': 9, 'A56': 9,
        'A57': 9, 'A58': 9, 'A59': 11, 'A60': 9, 'A61': 13, 'A62': 9, 'A63': 12,
        'A64': 9, 'A65': 11, 'A66': 9, 'A67': 14, 'A68': 14, 'A69': 15, 'A70': 9,
        'A71': 9, 'A72': 13, 'A73': 15, 'A74': 9, 'A75': 9, 'A76': 9, 'A77': 11,
        'A78': 9, 'A79': 14, 'A80': 9, 'A81': 9, 'A82': 10, 'A83': 9, 'A84': 9,
        'A85': 13, 'A86': 9, 'A87': 11, 'A88': 9}

dependencies = {}

required = ['A7', 'A16', 'A22', 'A25', 'A27', 'A33', 'A34', 'A35', 'A40', 'A46',
            'A47', 'A53', 'A58', 'A62', 'A64', 'A66', 'A67', 'A68', 'A70', 'A74',
            'A76', 'A78', 'A79', 'A82', 'A86', 'A87']

kmin = 88
kmax = 100