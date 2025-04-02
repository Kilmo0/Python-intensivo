cidades = {
    'Timbó': {
        'população': '50000',
        'Colonização': 'Germanica',
        'Pib': '2,5B'
        },
    'Indaial': {
         'população': '72000',
        'Colonização': 'Germanica-italica',
        'Pib': '3,8B'
    },
    'Rio dos Cedros': {
        'população': '10865',
        'Colonização': 'Italiana',
        'Pib': '437M'
    }
}

for cidade in cidades:
    print(f'a cidade de {cidade}\ntem a população de {cidades[cidade]["população"]}')
    print(f'com o pib de: {cidades[cidade]["Pib"]}')