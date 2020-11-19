pontos_jogador1 = 0
pontos_jogador2 = 0
rodada=0
opcao1=''
opcao2=''
print ('#############################')
print ('####      JO KEN PO      ####')
print ('#############################')
nome1 = str(input('Player1 insira o seu nickname: '))
nome2 = str(input('Player2 insira o seu nickname: '))
while (rodada <= 2):
    rodada = rodada + 1 
    print ('#############################')
    print ('####    R O D A D A ',rodada,'  ####')
    print ('#############################')
    print(nome1,' escolha uma opção:')
    jogador1 = int(input('''    [1] Pedra
    [2] Papel
    [3] Tesoura
    >_'''))
    print(nome2,' escolha uma opção:')
    jogador2 = int(input('''    [1] Pedra
    [2] Papel
    [3] Tesoura
    >_'''))
    print('O player ',nome1,' escolheu a opção ',jogador1) 
    print('O player ',nome2,' escolheu a opção ',jogador2)     
    if jogador1 == 1:
        if jogador2 == 3:
          pontos_jogador1 = pontos_jogador1 + 1  
          print(nome1,' VENCEU!')
        elif jogador2 == 2:
          pontos_jogador2 = pontos_jogador2 + 1 
          print(nome2,' VENCEU!')
        elif jogador2 == 1:
          pontos_jogador1 = pontos_jogador1 + 1 
          pontos_jogador2 = pontos_jogador2 + 1 
          print('EMPATE')
    if jogador1 == 2:
        if jogador2 == 1:
           pontos_jogador1 = pontos_jogador1 + 1 
           print(nome1,' VENCEU!')
        elif jogador2 == 3:
           pontos_jogador2 = pontos_jogador2 + 1 
           pontos_jogador1 = pontos_jogador1 + 1 
           pontos_jogador2 = pontos_jogador2 + 1 
           print(nome2,' VENCEU!')
        elif jogador2 == 2:
           print('EMPATE')
    if (jogador1 == 3):
        if jogador2 == 2:
           pontos_jogador1 = pontos_jogador1 + 1
           print(nome1,' VENCEU!')
        elif jogador2 == 1:
           pontos_jogador2 = pontos_jogador2 + 1
           print(nome2,' VENCEU!')
        elif jogador2 == 3:
           pontos_jogador1 = pontos_jogador1 + 1 
           pontos_jogador2 = pontos_jogador2 + 1 
           print('EMPATE')
    if pontos_jogador1 == 2 and pontos_jogador2 == 0:
      print('-------------------------------------------------')
      print(nome1.upper(),' WINS | CONQUISTA:MESTRE DO JO KEN PO')
      print('PLACAR: ',nome1.upper(),' 2 pontos x ',nome2.upper(), '0 pontos')
      print('QUANTIDADE DE RODADAS:',rodada,'               ')
      print('-------------------------------------------------')
      break
else:
   if(pontos_jogador1 > pontos_jogador2):
      print('-------------------------------------------------')
      print(nome1.upper(),' WINS| CONQUISTA:EXPERT EM JO KEN PO')
      print('PLACAR: ',nome1.upper(),' ',pontos_jogador1,' x ',nome2.upper(), ' ',pontos_jogador2,' pontos')
      print('QUANTIDADE DE RODADAS:',rodada,'               ')
      print('-------------------------------------------------')
   if (pontos_jogador1 < pontos_jogador2):  
      print('-------------------------------------------------')
      print(nome2.upper(),' WINS| CONQUISTA:EXPERT EM JO KEN PO')
      print('PLACAR: ',nome1.upper(),' ',pontos_jogador1,' x ',nome2.upper(), ' ',pontos_jogador2,' pontos')
      print('QUANTIDADE DE RODADAS:',rodada,'               ')
      print('-------------------------------------------------') 


    