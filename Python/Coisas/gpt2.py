import codecs

def remove_blank_lines(file_path):
    # Lê o conteúdo do arquivo
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Remove as linhas em branco
    non_blank_lines = [line for line in lines if line.strip()]

    # Escreve o conteúdo processado em um novo arquivo
    with open('arquivo_sem_linhas_em_branco.txt', 'w') as file:
        file.writelines(non_blank_lines)

def process_file(file_path):
    # Especifique a codificação correta do arquivo
    encoding = 'UTF-8'  # Ou outra codificação adequada

    # Abra o arquivo para leitura usando a codificação correta
    with codecs.open(file_path, 'r', encoding) as file:
        lines = file.readlines()

    processed_lines = []

    # Adiciona o cabeçalho
    header =  " MÓDULO CONTROLE DE ESTOQUE                                  ORDENS DE SERVICO DE VEICULOS                           PÁGINA :          1\n"
    header += " 000-TODAS AS EMPRESAS                                       Emissão: 01/03/2023 A 31/05/2023                        DATA   : 07/06/2023\n"
    header += " ---------------------------------------------------------------------------------------------------------------------------------------\n"
    header += " MOTORISTA:                                                                                                                             \n"
    header += " VEICULO: N. -                                                                        GRUPO:                                            \n"
    header += " SETOR:                                                                               SUBGRUPO:                                         \n"
    header += " TIPO OS:                                                      STATUS: TODOS          MATERIAL:                                          \n"
    header += " ---------------------------------------------------------------------------------------------------------------------------------------\n"
    header += " Data       N.Ordem    Material                                                                       Quantidade Unidade           Valor\n"
    header += " ---------------------------------------------------------------------------------------------------------------------------------------\n"

    processed_lines.append(header)
    
    foi=0;
    templine=''
    total=0
    for line in lines:
        if "VEICULO: " in line and any(c.isdigit() for c in line.split("VEICULO: ")[1].split(" ")[0].strip()) and foi!=1:
            if templine==line:
                foi+=1
            elif templine!=line:
                if total > 0:
                    templine = templine.rstrip()
                    total_line = ' TOTAL DO ' + templine + f': R$ {total:.2f}\n'
                    processed_lines.append(total_line)
                total = 0
                templine=line
                processed_lines.append(templine)
            print(line)
            continue
        if  not line.strip() or not line.strip()[0].isdigit() or "   OLEO" in line or "   ARLA" in line or "000" in line:
            continue
        processed_lines.append(line)

        # Extrai o valor da linha
        value_str = line.strip().split()[-1].replace('.', '').replace(',', '.')
        value = float(value_str)
        total += value

    processed_text = ''.join(processed_lines)

    # Escreve o texto processado em um novo arquivo
    with open('arquivo_processado.txt', 'w') as file:
        file.write(processed_text)

    # Remove as linhas em branco do arquivo processado
    remove_blank_lines('arquivo_processado.txt')

# Chame a função passando o caminho do arquivo como argumento
process_file('arquivo.txt')
