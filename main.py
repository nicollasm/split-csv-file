import os
import csv

# Constante para o tamanho máximo do arquivo (em bytes)
TAMANHO_MAXIMO = 512 * 1024 * 1024

# Nome do arquivo CSV de entrada
arquivo_entrada = 'entrada.csv'

# Prefixo para os arquivos de saída
prefixo_arquivo_saida = 'saida'

# Inicializar contadores e dados do arquivo
contagem_arquivo = 0
arquivo_saida = None
escritor = None
tamanho_atual = 0

with open(arquivo_entrada, 'r') as entrada:
    leitor = csv.reader(entrada, delimiter=';')

    for linha in leitor:
        # Converta a linha em uma string e calcule seu tamanho em bytes
        linha_str = ';'.join(linha) + '\n'
        tamanho_linha = len(linha_str.encode('utf-8'))

        # Se a adição da linha atual excederá o tamanho máximo do arquivo
        if tamanho_atual + tamanho_linha > TAMANHO_MAXIMO:
            # Incrementar o contador do arquivo
            contagem_arquivo += 1

            # Abrir um novo arquivo de saída
            arquivo_saida = open(f'{prefixo_arquivo_saida}_{contagem_arquivo}.csv', 'w', newline='')
            escritor = csv.writer(arquivo_saida, delimiter=';')

            # Resetar o tamanho do arquivo atual
            tamanho_atual = 0

        # Se o escritor não está inicializado, inicialize-o (isto acontece na primeira linha)
        if escritor is None:
            arquivo_saida = open(f'{prefixo_arquivo_saida}_{contagem_arquivo}.csv', 'w', newline='')
            escritor = csv.writer(arquivo_saida, delimiter=';')

        # Escrever a linha no arquivo de saída
        escritor.writerow(linha)

        # Adicionar o tamanho da linha ao tamanho do arquivo atual
        tamanho_atual += tamanho_linha

# Fechar o último arquivo de saída
if arquivo_saida is not None:
    arquivo_saida.close()
