#crie um programa que gerencia o aproveitamento de um jogar de futebol.
# o programa vai ler o nomedojogador ###
# quantas partidas ele jogou.###
# depois vai ler a quantidadedegols feitos em cada partida.
# no final tudo isso sera guardado em um dicionario,incluindo o total de gols feitos durante o campeonato


###########
#jogador:dict = dict()
#partidas:list = list()

#jogador['nome']= str(input("Insira seu nome:"))
#tot = int(input(f"insira a quantidade de partidas que o {jogador["nome"]} jogou: "))

#for p in range(0,tot):
#    partidas.append(int(input(f"quantos gols o {jogador["nome"]} fez na partida {p}:")))
#jogador_gols = partidas[:]
#print(f"o jogador {jogador['nome']} fez um total de {jogador_gols}gols em {tot} partidas")
#print(f"dando uma média de {media_p_jogo} gols por partida")

#for p, g in enumerate(jogador_gols):
#    print(f"o jogador {jogador['nome']} fez {g} gols na partida {p}")



#############
#faca um programa que leia nome e media de um aluno.
#guardando tambem a situaçaõ em um dicionario
#no final mostre o conteudo da estrutura na tela

#aluno = dict()
#aluno['nome'] = str(input("insira seu nome:"))
#aluno['media'] = float(input(f"digite a media do {aluno['nome']}:"))

#if aluno["media"] <= 5:
#    aluno['situação'] = 'reprovado'
#elif aluno["media"] >5 and aluno["media"] <=7:
#    aluno['situação'] = 'média'
#else :
#    aluno["media"] >7
#    aluno['situação'] = 'aprovado'
    
#for k, v in aluno.items():
#    print(k , v)

###############

#crie um programa que leia o 
# nome ano de nascimento
#  carteira de trabalho 
# e cadastre-os(com idade) em um dicionario
#  se por acaso a ctps for diferente de zero o dicionario recebera tambem o ano de contrataçao e o salario
# calculo e acrescente alem da idade com quantos anos a pessoa vai se aposentar

#nome = dict()
#nome['usuario'] = str(input("Digite seu nome:"))
#nome['nascimento'] = input("qual sua data de nascimento: ")
#nome['carteira'] = int(input("qual numero da sua carteira de trabalho:"))

#if nome["carteira"] <= 0:
#    nome['ano de contratação'] = str(input("qual seu ano de contratação: "))
#    nome['salario'] = int(input("qual seu salario: "))
#else:
#    print("ctps ativa")
    
#for k, v in nome.items():
 #   print(k, v)

#CRIE UM PROGRAMA QUE LEIA NOME,SEXO E IDADE DE VARIOS PESSOAS
#GUARDANDO OS DADOS DE CADA PESSOA EM UM DICIONARIO
#E TODOS OS DICIONARIOS EM UMA LISTA
#NO FINAL MOESTRE
#QUANTAS PESSOAS FORAM CADASTRADAS
#A MEDIA DE IDADE DO GRUPO
#UMA LISTA COM TODAS AS MULHEREA
#UMA LISTA COM TODOS AS PESSOAS COM IDADE ACIMA DE MEDIA
#python desafio.py
galera = list()
pessoa = dict()
soma = média = 0
while True:
    pessoa.clear()
    pessoa['pessoa'] = str(input("nome: "))  
    while True:
        pessoa['sexo'] = str(input("sexo: [M/F]")).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print("ERRO!Por favor,digite apenas M ou F")
    pessoa['idade'] = int(input("idade: "))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input("quer continuar? [S/N]")).upper() [0]
        if resp in 'SN':
            break
        print("ERRO!, Responda apenas S ou N.")
    if resp =='N':
        break
print(f"a quantidade de pessoas cadastradas foi {len(galera)}")
média = soma / len(galera)
print(f'a média é {média}')
print(f'as mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p['pessoa']} ', end='')
print()
print('lista das pessoas acima da média: ')
for p in galera:
    if p['idade'] >= média:
        print('    ')
        for k, v in p.items():
            print(f'{k} = {v}')