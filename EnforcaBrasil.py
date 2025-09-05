import random
forca= [
    """
    _______
   |/
   |
   |
   |
   |
___|___
    """,
    """
    _______
   |/      |
   | \033[32m     (o_o)   \033[m
   |
   |
   |
___|___
    """,
    """
    _______
   |/      |
   | \033[32m     (o_o)   \033[m
   | \033[32m       |     \033[m
   | \033[32m       |     \033[m
   |
   |
___|___
    """,
    """
    _______
   |/      |
   | \033[32m     (o_o)   \033[m
   | \033[32m      /|     \033[m
   | \033[32m       |     \033[m
   |
   | 
___|___
    """,
    """
    _______
   |/      |
   | \033[33m     (o_o)     \033[m
   | \033[33m      /|\\     \033[m
   | \033[33m       |       \033[m
   |
   |
___|___
    """,
    """
    _______
   |/      |
   | \033[33m     (o_o)   \033[m
   | \033[33m      /|\\   \033[m
   | \033[33m       |     \033[m
   | \033[33m      /      \033[m
   |
___|___
    """,
    """
    _______
   |/      |
   | \033[31m     (X_X)   \033[m
   | \033[31m      /|\\   \033[m
   | \033[31m       |     \033[m
   | \033[31m      / \\   \033[m
   |
___|___
    """
]
atleta=['HUGO CALDERANO','REBECA ANDRADE','RAYSSA LEAL','MARTA','RONALDINHO']
cantor=['MATUÊ','MARÍLIA MENDONÇA','THIAGUINHO','SEU JORGE','DJAVAN']
cidade=['RIO DE JANEIRO','SÃO PAULO','FORTALEZA','RECIFE','BRASÍLIA']
animal=['MICO-LEÃO-DOURADO','ARARA AZUL','TATaU-BOLA','PEIXE BOI','LOBO GUARÁ']
prato=['FEIJOADA','ACARAJÉ','PÃO DE QUEIJO','ARROZ CARRETEIRO','BAIÃO DE DOIS']
dat=['1º Dica - É atualmente o 3º lugar no ranking mundial no seu esporte.','2º Dica - Campeão mundial de tênis de mesa 2025.','1º Dica - Seu esporte é ginástica artística.','2º Dica - Bicampeã olímpica e a maior medalhista da história do Brasil nos Jogos Olímpicos.','1º Dica - Mais jovem medalhista olímpica brasileira.','2º Dica - Atualmente tem 17 anos e seu esporte é skate.','1º Dica - Maior artilheira de todos os tempos na copa do mundo.','2º Dica - Considerada a Rainha do futebol.','1º Dica - Campeão da copa do mundo de 2002.','2º Dica - Um dos maiores dribladores da história do futebol.']
dca=['1º Dica - Estilo musical: Trap.','2º Dica - Cantor da música "Vampiro".','1º Dica - Estilo musical: Sertanejo.','2º Dica - Cantor da música "Bem pior que eu".','1º Dica - Estilo musical: Samba.','2º Dica - Cantor da música "Falta Você".','1º Dica - Estilo musical: R&B.','2º Dica - Cantor da música "Amiga da Minha Mulher".','1º Dica - Estilo musical: MPB.','2º Dica - Cantor da música "Oceano".']
dci=['1º Dica - Sede dos jogos olímpicos 2016.','2º Dica - Conhecida mundialmente pelo Cristo Redentor e o Pão de Açúcar.','1º Dica - Possui a avenida mais famosa do Brasil.','2º Dica - Maior cidade do Brasil, capital financeira do país.','1º Dica - Possui a famosa praia do Futuro.','2º Dica - Capital do Ceará, muito procurada por turistas no Nordeste.','1º Dica - Cidade litorânea do Nordeste.','2º Dica - Tem muitos rios e pontes, sendo conhecida como a Veneza brasileira.','1º Dica - Tem o formato de um avião se vista por cima.','2º Dica - Capital federal.']
dan=['1º Dica - Nativo da mata atlântica.','2º Dica - Estampado nas notas de 20 reais.','1º Dica - É um animal voador.','2º Dica - Está em ameaça de extinção.','1º Dica - Vive na caatinga e cerrado.','2º Dica - Mascote da copa do mundo em 2014.','1º Dica - Mamífero aquático.','2º Dica - Localizado na floresta amazônica.','1º Dica - Típico do cerrado.','2º Dica - Está na nota de 200 reais.']
dp=['1º Dica - Um dos pilares da gastronomia do nosso país.','2º Dica - Prato típico do Rio de Janeiro.','1º Dica - Seu principal ingrediente é o feijão-fradinho.','2º Dica - Prato típico da Bahia.','1º Dica - Seus principais ingredientes são polvilho azedo e queijo.','2º Dica - Pão típico de Minas Gerais.','1º Dica - Um dos seus ingredientes é a carne seca.','2º Dica - Prato típico do Rio Grande do Sul.','1º Dica - Seu nome faz referência a uma dança típica do nordeste.','2º Dica - Prato típico do Ceará.']
x=0
jn=1
while jn==1:
    print('\033[1;7mEnforca Brasil\033[m\n')
    if x==0:
        print('''Bem-vindos ao \033[1mEnforca Brasil\033[m, um jogo de forca sobre esse Brasilzão, aqui vão algumas instruções:
- Temos um total de 25 palavras, 5 em cada categoria;
- Caracteres que não sejam letras não serão aceitos;
- É possível dar um palpite da palavra a qualquer momento;
- Não se esqueça dos espaços, hifens e acentos na hora do palpite;
- Ao jogar novamente, é possível que uma palavra seja repita, uma vez que são sorteadas aleatoriamente.
- Se divirta e boa sorte ;)\n''')
        x=1
    print('''\033[1mCategorias\033[m
1 - Animais Nativos
2 - Atletas
3 - Cantores
4 - Cidades Famosas
5 - Pratos Típicos''')
    cat=input("Categoria: ")
    while cat<'1' or cat>'5':
        print('Categoria não identificada, escolha novamente.')
        cat = input("Categoria: ")

    if cat=='1':
        palavra=random.choice(animal)
        print('\n\033[1mAnimais Nativos\033[m')
        d1=0
        while palavra!=animal[d1]:
            d1+=1
        d2=dan[d1*2+1]
        d1=dan[d1*2]
    elif cat=='2':
        palavra=random.choice(atleta)
        print('\n\033[1mAtletas\033[m')
        d1 = 0
        while palavra != atleta[d1]:
            d1 += 1
        d2 = dat[d1 * 2 + 1]
        d1 = dat[d1 * 2]
    elif cat=='3':
        palavra = random.choice(cantor)
        print('\n\033[1mCantores\033[m')
        d1 = 0
        while palavra != cantor[d1]:
            d1 += 1
        d2 = dca[d1 * 2 + 1]
        d1 = dca[d1 * 2]
    elif cat=='4':
        palavra = random.choice(cidade)
        print('\n\033[1mCidades Famosas\033[m')
        d1 = 0
        while palavra != cidade[d1]:
            d1 += 1
        d2 = dci[d1 * 2 + 1]
        d1 = dci[d1 * 2]
    else:
        palavra = random.choice(prato)
        print('\n\033[1mPratos Típicos\033[m')
        d1 = 0
        while palavra != prato[d1]:
            d1 += 1
        d2 = dp[d1 * 2 + 1]
        d1 = dp[d1 * 2]

    vp=[]
    for i in range(len(palavra)):
        if palavra[i]==' ':
            vp.append(' ')
        elif palavra[i]=='-':
            vp.append('-')
        else:
            vp.append('_')
    pos_f=0
    letra_usada=[]
    d=1
    x=0
    while pos_f<6 and '_' in vp:
        if x==1:
            print('\033[1mLetras Usadas:\033[m', end=' ')
            for i in range(len(letra_usada)-1):
                print(letra_usada[i], end=' - ')
            print(letra_usada[-1])

        if pos_f==3 and d==1:
            print('\033[32m'+d1+'\033[m')
            d+=1
        elif pos_f==5 and d==2:
            print('\033[32m'+d2+'\033[m')
            d+=1
        print(forca[pos_f])

        for i in range(len(vp)):
            print(vp[i], end=' ')
        print('\n')

        letra = input('Letra: ').upper()
        if letra==palavra:
            for i in range(len(palavra)):
                vp[i]=palavra[i]
        else:
            while letra<'A' or letra>'Z':
               letra=input('Por favor, digite uma letra: ')[0].upper()
            while letra in letra_usada:
                letra=input('Letra já usada, tente novamente: ')[0].upper()
                while letra < 'A' or letra > 'Z':
                    letra = input('Por favor, digite uma letra: ')[0].upper()

            aux=0
            if len(letra)==1 and letra in palavra or letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U' or letra=='C':
                if letra == 'A':
                    for i in range(len(palavra)):
                        if palavra[i] == letra:
                            vp[i] = letra
                            aux=1
                        elif palavra[i] == 'Á':
                            vp[i] = 'Á'
                            aux = 1
                        elif palavra[i] == 'À':
                            vp[i] = 'À'
                            aux = 1
                        elif palavra[i] == 'Ã':
                            vp[i] = 'Ã'
                            aux = 1
                        elif palavra[i] == 'Â':
                            vp[i] = 'Â'
                            aux = 1
                    if aux==0:
                        pos_f+=1
                elif letra == 'E':
                    for i in range(len(palavra)):
                        if palavra[i] == letra:
                            vp[i] = letra
                            aux = 1
                        elif palavra[i] == 'É':
                            vp[i] = 'É'
                            aux = 1
                        elif palavra[i] == 'È':
                            vp[i] = 'È'
                            aux = 1
                        elif palavra[i] == 'Ê':
                            vp[i] = 'Ê'
                            aux = 1
                    if aux==0:
                        pos_f+=1
                elif letra == 'I':
                    for i in range(len(palavra)):
                        if palavra[i] == letra:
                            vp[i] = letra
                            aux = 1
                        elif palavra[i] == 'Í':
                            vp[i] = 'Í'
                            aux = 1
                        elif palavra[i] == 'Ì':
                            vp[i] = 'Ì'
                            aux = 1
                        elif palavra[i] == 'Î':
                            vp[i] = 'Î'
                            aux = 1
                    if aux==0:
                        pos_f+=1
                elif letra == 'O':
                    for i in range(len(palavra)):
                        if palavra[i] == letra:
                            vp[i] = letra
                            aux = 1
                        elif palavra[i] == 'Ó':
                            vp[i] = 'Ó'
                            aux = 1
                        elif palavra[i] == 'Ò':
                            vp[i] = 'Ò'
                            aux = 1
                        elif palavra[i] == 'Õ':
                            vp[i] = 'Õ'
                            aux = 1
                        elif palavra[i] == 'Ô':
                            vp[i] = 'Ô'
                            aux = 1
                    if aux==0:
                        pos_f+=1
                elif letra == 'U':
                    for i in range(len(palavra)):
                        if palavra[i] == letra:
                            vp[i] = letra
                            aux = 1
                        elif palavra[i] == 'Ú':
                            vp[i] = 'Ú'
                            aux = 1
                        elif palavra[i] == 'Ù':
                            vp[i] = 'Ù'
                            aux = 1
                        elif palavra[i] == 'Û':
                            vp[i] = 'Û'
                            aux = 1
                    if aux==0:
                        pos_f+=1
                elif letra=='C':
                    for i in range(len(palavra)):
                        if palavra[i] == letra:
                            vp[i] = letra
                            aux = 1
                        elif palavra[i] == 'Ç':
                            vp[i] = 'Ç'
                            aux = 1
                    if aux==0:
                        pos_f+=1
                else:
                    for i in range(len(palavra)):
                        if palavra[i] == letra:
                            vp[i] = letra
            else:
                pos_f+=1
            if len(letra)==1:
                letra_usada.append(letra)
                x=1
            else:
                print('\033[31mPalpite errado =(\033[m')
            print('\n')

    if pos_f==6:
        print(forca[pos_f])
        for i in range(len(vp)):
            print(palavra[i], end=' ')
        print('\n')
        print("\033[33mNão foi dessa vez\033[m, vamos tentar de novo?\n\033[32m1-Sim\033[m\n\033[31m2-Não\033[m")
        jn=int(input('Jogar novamente: '))
        print('\n')
    else:
        print(forca[pos_f])
        for i in range(len(vp)):
            print(vp[i], end=' ')
        print('\n')
        print("\033[32mParabéns\033[m, parece que temos um brasileiro nato.\nQue tal tentar mais uma vez em outra categoria?\n\033[32m1-Sim\033[m\n\033[31m2-Não\033[m")
        jn=int(input('Jogar novamente: '))
        print('\n')
    if jn==1:
        x=1
print('Obrigado por jogar, espero que tenha se divertido.')