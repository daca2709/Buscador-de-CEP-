

"" 'BUSCADOR de CEP


"""

#!pip install requests #instalando a biblioteca através do PIP.
import requests #https://pypi.org/project/pipa/ INSTALAR O PIP NO MEU PC.
#instalar o setup, dps rodar no CMD como 'py setup.py', e vai instalar as bibliotecas
#Logo, para instalar uma biblioteca 'pip install ....'
def funcao():
  print('CEPython')

  cep = input('Digite o CEP para realizar sua consulta: ')
   
   # == igual / != diferente / >= maior ou igual / <= menor ou igual

  while len(cep) != 8:            # Variavel LEN é utilizada para contar a quantidade de caracteres
    print('Insira uma quantidade de caracteres válida')
    cep = input('Digite o CEP para realizar sua consulta: ')

  bau = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
  endereco = bau.json()      #Pesquisar sobre json() "Protocolo de comunicação ou padrão."


  if 'erro' not in endereco:
    print('===> CEP encontrado <===')
    print('CEP: {}'.format(endereco['cep']))     #FORMAT serve para colocar a informçãop dentro das CHAVES. Funciona apenas com {}
    print('Cidade: {}'.format(endereco['localidade'])) #Diferentes formas de utilizar a variavel format na parte do code ao lado
    print(f"Estado: {endereco['uf']}")
    print(f"Logradouro: {endereco['logradouro']}")
    print(f"Bairro: {endereco['bairro']}")
  else:
    print('Este CEP não existe...')

  print('=================================')


  def validacao():
    opcao01 = input('Gostaria de gerar outra pesquisa?')  #/n pode pular a linha dentro dos apóstrofos laranja, não precisa utilizar mais '''
    if opcao01 == ' 1' or opcao01 == ' 2':
      if int(opcao01) == 1:
        funcao()
      else:
        print('Até a próxima.')
    else:
      print('Não entendi')
      validacao()
  validacao()


funcao()
