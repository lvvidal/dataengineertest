# importa as libs que serão utilizadas
import argparse
import datetime
import credentials_contabilizei
import util

# define os argumentos que serão passados para o script
parser = argparse.ArgumentParser(    
	description=''' Como executar o programa ''',
    epilog="""Não faz drama. Vem pra Contabilizei""")
parser.add_argument('--product', default=None, help='Inform the name of the product. Ex: water')
parser.add_argument('--company_state', default=None, help='Inform a company state or a list of company states separated by comma. Ex = PR or SP,PR')


def download_products(product):
	
	if customers is not None:
		print("*********** Começando aqui a sua busca ***********")
		totalemp=0
		list = []

		for item in customers:

			productlist = item['Products_list']

			for p in productlist:
#				print(p['product'][0])
				if p['product'][0] == product:

					dict = {'company_Id': '', 'product': '', 'product_price': '', 'company_state': ''}
					dict['company_Id'] = item['company_Id']
					dict['product'] = p['product'][0]
					dict['product_price'] = p['product_price']
					dict['company_state'] = ', '.join(item['company_state'])
					list.append(dict)
					totalemp+=1
					
					print(dict['company_Id'],'|', dict['product'],'|',dict['product_price'],'|',dict['company_state'])
		
		# download do relatório
		now = datetime.datetime.now()
		util.download_csv(list, 'D:\\Python\\testeContabilizei\\tmp\\' + now.strftime("%d-%m-%Y") + '_Busca_por_Produto_' + product + '_' + str(totalemp) + '.csv', 'utf-8')

		print('Quantidade total de empresas encontradas: '+str(totalemp))
	else:
		print('[!] Request Falhou')

def download_products_companystate(product,companystate):
	
	if customers is not None:
		print("*********** Começando aqui a sua busca ***********")
		totalemp=0
		list = []

		for item in customers:

			productlist = item['Products_list']
			#tamanho = len(item['company_state'])

			for p in productlist:
#				print(p['product'][0])
				if p['product'][0] == product and companystate in item['company_state']:

					dict = {'company_Id': '', 'product': '', 'product_price': '', 'company_state': ''}
					dict['company_Id'] = item['company_Id']
					dict['product'] = p['product'][0]
					dict['product_price'] = p['product_price']
					dict['company_state'] = ', '.join(item['company_state'])
					list.append(dict)
					totalemp+=1
					
					print(dict['company_Id'],'|', dict['product'],'|',dict['product_price'],'|',dict['company_state'])
		
		# download do relatório
		now = datetime.datetime.now()
		util.download_csv(list, 'D:\\Python\\testeContabilizei\\tmp\\' + now.strftime("%d-%m-%Y") + '_Busca_por_Produto_' + product + '_em_' + companystate + '_' + str(totalemp) + '.csv', 'utf-8')

		print('Quantidade total de empresas encontradas: '+str(totalemp))
	else:
		print('[!] Request Falhou')

# inicio do script
if __name__ == '__main__':
	args = parser.parse_args()
	
	# inicializa o client
	customers = credentials_contabilizei.get_data_json()
	
	#product = input("Qual produto você está buscando?  \n")

	# verifica se foi passado o nome do produto e os estados(company_state) para chamar a função que realiza o download
	if args.company_state is not None and args.product is not None:
		download_products_companystate(args.product, args.company_state)
	elif args.company_state is None and args.product is not None:
		download_products(args.product)
	else:
		print('Favor informar ao menos o nome do produto a ser pesquisado')