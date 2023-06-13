import csv

# Função para verificar se a linha contém os dados relevantes
def is_data_line(line):
    return line.startswith('VEICULO:')

# Função para extrair os campos da linha de dados
def extract_fields(line):
    fields = line.split()
    return {
        'Veiculo': fields[1],
        'Data': fields[0],
        'N.Ordem': fields[2],
        'Material': ' '.join(fields[3:-3]),
        'Quantidade': fields[-3].replace(',', '.'),
        'Unidade': fields[-2],
        'Valor': fields[-1].replace('.', '').replace(',', '.')
    }

# Lista para armazenar os dados extraídos
data = []

# Leitura do arquivo de texto e extração dos dados relevantes
with open('arquivo.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        if is_data_line(line):
            data.append(extract_fields(line))

# Escrita dos dados no arquivo CSV
csv_file = 'dados.csv'
csv_columns = ['Veiculo', 'Data', 'N.Ordem', 'Material', 'Quantidade', 'Unidade', 'Valor']

with open(csv_file, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=csv_columns)
    writer.writeheader()
    writer.writerows(data)

print("Conversão concluída com sucesso. Os dados foram salvos em 'dados.csv'.")
