import os

print("""Sabor Express
      """)

print('1. Cadastrar restaurante')
print('2. Listar restaurante')
print('3. Ativar restaurante')
print('4. Sair')
#https://fsymbols.com/pt/letras/

opcao_escolhida = int(input('Escolha uma opção: '))
#print('Você escolheu a opção', opcao_escolhida)
#print(f'Você escolheu a opção {opcao_escolhida}')

def finaliza_app():
    os.system('cls') #os.system('clear')
    print('Encerrando o programa\n')

if opcao_escolhida == 1:
    print('Cadastrar restaurante')
elif opcao_escolhida == 2:
    print('Listar restaurantes')
elif opcao_escolhida == 3:
    print('Ativar restaurantes')
else:
     finaliza_app()