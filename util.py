# script com funções uteis que podem ser utilizadas por qualquer metódo

# importa as libs que serão utilizadas
import csv
import os.path

def download_csv(list, file_path, encode=None):
	# busca o cabeçalho do relatório
	header = list[0].keys()
	
	# cria o arquivo .csv do relatório
	with open(caminho_csv(file_path), 'w', newline='', encoding=encode) as output_file:
		dict_writer = csv.DictWriter(output_file, header, delimiter='|')
		dict_writer.writeheader()
		dict_writer.writerows(list)

	# informa onde o arquivo .csv foi gravado
	print ("O relatório está disponível em : " + file_path)

def caminho_csv(file_path):
	# Verificar se caminho existe, caso contrário diretório é criado
	if not os.path.exists(os.path.dirname(file_path)):
		os.makedirs(os.path.dirname(file_path))

	return file_path