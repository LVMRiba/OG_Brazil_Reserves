import pandas as pd

M3_TO_BARRIL = 6.28981

def alt_name(database):
    database['Estado'] = database['Estado'].replace({
        'Bacia do Amazonas': 'Amazonas',
        'Bacia de Espírito Santo': 'Espirito Santo',
        'Bacia do Espírito Santo': 'Espirito Santo',
        'Bacia de Camamu-Almada': 'Bacia de Camamu',
        'Bacia de Tucano Sul': 'Bacia do Tucano Sul',
        'Bacia de Solimões': 'Bacia do Solimões',
        'Espírito Santo': 'Espirito Santo'
    })

    return database

def gerar_tabela_barril(database):

    database['RPO Barrel'] = round(database['Reservas Provadas O'] * M3_TO_BARRIL, 3)
    database['RTO Barrel'] = round(database['Reservas Totais O'] * M3_TO_BARRIL, 3)
    database['RPG Barrel'] = round(database['Reservas Provadas G'] * M3_TO_BARRIL, 3)
    database['RTG Barrel'] = round(database['Reservas Totais G'] * M3_TO_BARRIL, 3)

    return database

# SET_OPTION
pd.set_option('display.max_columns', 15)
pd.set_option('display.min_rows', 50)
pd.set_option('display.max_rows', 50)
pd.set_option('display.width', 500)

# VISUALIZAR OS RESULTADOS DE LEITURA DAS TABELAS

path_data = f"Dados Excel/Dados O&G.xlsx"

database = pd.read_excel(path_data)
database = alt_name(database)
database = gerar_tabela_barril(database)
print(database)
list_bacias = sorted(database['Estado'].drop_duplicates())
for bacia in list_bacias:
    print(bacia)
