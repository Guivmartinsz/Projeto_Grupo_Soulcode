"""

print('-'*30, ' \n \033[1;35;107m  Bem Vindos ao Codeback \033[0m \n' ,'-'*30)
#DEFININDO VARIÁVEIS
total=total1=0
# Listas que recebem as opções
comidas=[]
bebidas=[]
petiscos=[]
sobremesas=[]
#Variáveis que recebem as quantidades em string 
quant1='0'
quant3='0'
#Variáveis que  transformam string em número inteiro
quant2=quant4=0
#Listas que recebem os ítens solicitados 
itens_comida=[]
itens_bebida=[]
itens_sobremesa=[]
itens_petisco=[]
#Listas que guardam as quantidades parciais cada vez que o loop roda (essas são zeradas toda vez após o pagamento)
lista_qcom1=[]
lista_qcom2=[]
lista_qbeb1=[]
lista_qbeb2=[]
lista_qpet1=[]
lista_qpet2=[]
lista_qsob1=[]
lista_qsob2=[]
#Listas que recebem as quantidades para exibir no final
lista_qcomf1=[]
lista_qcomf2=[]
lista_qbebf1=[]
lista_qbebf2=[]
lista_qpetf1=[]
lista_qpetf2=[]
lista_qsobf1=[]
lista_qsobf2=[]
#Variáveis para contar ítens cancelados/eliminar pedidos cancelados, guardar total de pedidos e somar os totais
cancela1=cancela2=cancela3=cancela4=cancela5=cancela6=cancela7=cancela8=0

a=b=c=d=e=f=g=h=0

cont1=cont2=cont3=cont4=cont5=cont6=cont7=0

total2=[]

total3=0
#Variáveis que somam os valores dos ítens em cada setor 

valor_noalc=valor_chic=valor_cost=valor_lemon=valor_maca=valor_mousse=valor_noalc=valor_onion=valor_torta=0

#Variáveis que somam os subtotais (são zerados sempre que o cliente efetua o pagamento)

sum_sobremesas=sum_petiscos=sum_comidas=sum_bebidas=0

#Variáveis calculam os subtotais apresentados ao encerrar a compra

sum_sobremesas1=sum_petiscos1=sum_comidas1=sum_bebidas1=0
################## Menu ###########################
while True:
  menu = str(input(' Digite [A] para ter acesso ao nosso cardápio:  \n Caso precise finalizar o programa digite  [F]: \n [A/F]  ')).upper().strip()[0].rsplit('.')[0].rsplit(',')[0].rsplit(' ')[0]
  if menu == 'A':
    #zerando os dados para caso o usuário queira comprar de novo antes de finalizar
    sum_sobremesas=sum_petiscos=sum_comidas=sum_bebidas=0
    total1=total=0
    comidas=[] 
    bebidas=[]
    petiscos=[]
    sobremesas=[]
    lista_qcom1.clear()
    lista_qcom2.clear()
    lista_qbeb1.clear()
    lista_qbeb2.clear()
    lista_qpet1.clear()
    lista_qpet2.clear()
    lista_qsob1.clear()
    lista_qsob2.clear()
    contp=contp1=contp2=contp3=contp4=contp5=contp6=contp7=0
################ Cardápio ###################
    cardapio='100'
    while cardapio !='0':
      print('-'*30, ''' \n \033[1;35;107m
Você está no Cardápio Codeback.

Digite o número indicado ao lado do produto desejado: \033[0m \n
_____________________________________

[1]-Comidas
[2]-Bebida
[3]-Petiscos
[4]-Sobremesas
[0]-Pagar
_____________________________________\n''')
      cardapio=str(input(' ')).rsplit('.')[0].rsplit(',')[0].rsplit(' ')[0].strip()[0] # essas são funções para permitir qu o cliente insira . ou , ou (' ') sem dar erro.
      print('-'*30)
      comida='14'
      if cardapio=='0':
        break
#Essa seção é para validar o sub-menu
      if cardapio not in '1234':
        print('\033[1;31;107m Infelizmente não consegui entender o que você deseja, tente novamente. \033[0m ') 

        comida=bebida=petisco=sobremesa='14'
      else:
        comida=bebida=petisco=sobremesa='11'

############### Seção 1- Comidas ######################

      comida='1'
      while cardapio== '1' and comida!='14':
        print('-'*30, '''\n \033[0;35;107m
Hello, you! Bem-vindo à \033[4;35;107m Seção de Comidas \033[0;35;107m escolha um dos nossos pratos.

Digite o número indicado ao lado da opção desejada \033[0m \n
____________________________________________
Código    Opção         Quantidade    Valor
____________________________________________
[011]- Costela na brasa    (700g)     R$70,00 
[012]- Nhoc de camarão     (500g)     R$50,00
[014]- Voltar ao cardápio
[015]- Finalizar pedido \n
____________________________________________ ''')
        comida=str(input(' ')).replace('0', '').rsplit('.')[0].rsplit(',')[0].rsplit(' ')[0].strip()[0:2]
        if comida =='15':
          print(f'\nVocê selecionou: {comida}.\nRetornamos ao menu principal.\n Você tem certeza que quer finalizar?\n [A/F]','-'*30)
        elif comida=='11'or comida=='12':
          print(f'\nVocê selecionou: {comida}\n','-'*30)
        elif comida=='14':
          print(f'\nVocê selecionou {comida}, voltaremos ao cardápio para que possa desfrutar da nossa variedade de opções:\n','-'*30)
        if comida=='11':
          quant1=str(input('Selecione a quantidade de Costela na brasa desejada: ')).rsplit('.')[0].rsplit(',')[0].rsplit(' ')[0]
          if quant1.isnumeric()==True:
            quant2=float(quant1)
            valor_cost= quant2*70
            if quant2>0:
              lista_qcom1.append(quant2)
              lista_qcomf1.append(quant2)
              itens_comida.append(comida)
            print(f'{valor_cost:.2f} reais' )
            comidas.append(valor_cost)
          else:
            print('\n \033[1;35;107m Ínvalido.\033[m')
          
        elif comida =='12':
          quant3=str(input('Quantas porções de Nhoc de camarão branco desejada: ')).rsplit('.')[0].rsplit(',')[0].rsplit(' ')[0]
          if quant3.isnumeric()==True:
            quant4=int(quant3)
            if quant4>0:
              itens_comida.append(comida)
              lista_qcom2.append(quant4)
              lista_qcomf2.append(quant4)
            valor_maca= quant4*50
            print(f'{valor_maca} reais' ) 
            comidas.append(valor_maca) 
        elif comida=='14':
          break
        elif comida=='15':
          break
        else:
          print('\033[1;31;107m Selecione novamente. Não temos essa opção. \033[0m')
        sum_comidas=sum(comidas)
        sum_comidas1=sum(comidas)
        print(f'\nO subtotal em comidas é {sum_comidas}')
      if comida=='15':
        break

      
############### Seção 2- Bebidas######################
      bebida='2'
      while cardapio== '2' and bebida!='14':
        print('-'*30, '''\n \033[0;35;107m
Hello, you! Bem-vindo à \033[4;35;107m Seção de Bebidas \033[0;35;107m

Digite o número indicado ao lado da opção desejada \033[0m\n
______________________________________________
Código    Opção         Quantidade    Valor
______________________________________________
[041]- Caipiroska limão         (500mL)   R$25,00
[042]- Caipiroska.pop("álcool") (500mL)    R$20,00
[014]- Voltar ao cardápio
[015]- Finalizar pedido \n
____________________________________________ \n''')
        bebida=input(' ').replace('0', '').strip()[0:2]
        if bebida =='15':
          print(f'\nVocê selecionou: {bebida}.\nRetornamos ao menu principal.\n Você tem certeza que quer finalizar?\n [A/F]','-'*30)
        elif bebida=='41'or bebida=='42':
          print(f'\nVocê selecionou: {bebida}\n','-'*30)
        elif bebida=='14':
          print(f'\nVocê selecionou {bebida}, voltaremos ao cardápio para que possa desfrutar da nossa variedade de opções:\n','-'*30)

        if bebida=='41':
          quant1=str(input(' Selecione a quantidade de Caipiroska de limão desejada: ')).rsplit('.')[0].rsplit(',')[0].rsplit(' ')[0]
          if quant1.isnumeric()==True:
            quant2=float(quant1)
            if quant2>0:
              itens_bebida.append(bebida)
              lista_qbeb1.append(quant2)
              lista_qbebf1.append(quant2)              
            valor_lemon= quant2*25
            print(f'{valor_lemon:.2f} reais' )
            bebidas.insert(0,valor_lemon)
                
        elif bebida =='42':
          quant3=str(input('Caipiroska sem álcool? é suco, rsrs. Selecione a quantidade desejada: ')).rsplit('.')[0].rsplit(',')[0].rsplit(' ')[0]
          if quant3.isnumeric()==True:
            quant4=float(quant3)
            valor_noalc= quant4*20
            if quant4>0:
              itens_bebida.append(bebida)
              lista_qbeb2.append(quant4)
              lista_qbebf2.append(quant4)             
          print(f'{valor_noalc:.2f} reais' )
          bebidas.insert(0,valor_noalc)                
        elif bebida=='14':
          break
        elif bebida=='15':
          break
        else:
          print('\033[1;31;107m Não temos essa opção. \033[0m')
        sum_bebidas=sum(bebidas)
        sum_bebidas1=sum(bebidas)
        print(f'O subtotal em bebidas é {sum_bebidas}')
      if bebida=='15':
        break     



############### Seção 3- Petiscos ######################
      petisco='3'
      while cardapio== '3' and petisco!='14':
        print('-'*30, ''' \n \033[0;35;107m 
Hello, you! \033[4;35;107m Seção de petiscos \033[0;35;107m 

Digite o número indicado ao lado da opção desejada \033[0m \n

_____________________________________________
Código    Opção         Quantidade    Valor
_____________________________________________
[021]- Camarão empanado      10       R$35,00 
[022]- Bolinho de bacalhau   10       R$40,00
[014]- Voltar ao cardápio
[015]- Finalizar pedido \n
_____________________________________________''')
        petisco=input(' ').replace('0', '').strip()[0:2]
        if petisco =='15':
          print(f'Você selecionou: {petisco}.\nRetornamos ao menu principal.\n Você tem certeza que quer finalizar [A/F]?\n ','-'*30)
        elif petisco=='21'or petisco=='22':
          print(f'Você selecionou: {petisco}\n','-'*30)
        elif petisco=='14':
          print(f'Você selecionou {petisco}, voltaremos ao cardápio para que possa desfrutar da nossa variedade de opções:\n','-'*30) 
             
        if petisco=='21':
          quant1=str(input('Você importou Camarão empanado. Quantas porções: ')).rsplit('.')[0].rsplit(',')[0].rsplit(' ')[0]
          if quant1.isnumeric()==True:
            quant2=float(quant1)
            if quant2>0:
              itens_petisco.append(petisco)
              lista_qpet1.append(quant2)
              lista_qpetf1.append(quant2)
            valor_chic= quant2*35
            print(f'{valor_chic:.2f} reais' )
            petiscos.insert(0,valor_chic)

          
        elif petisco =='22':
          quant3=str(input('Você importou Bolinho de bacalhau. Quantas porções: ')).rsplit('.')[0].rsplit(',')[0].rsplit(' ')[0]
          if quant3.isnumeric()==True:
            quant4=float(quant3)
            valor_onion= quant4*40
            if quant4>0:
              itens_petisco.append(petisco)
              lista_qpet2.append(quant4)
              lista_qpetf2.append(quant4)
            print(f'{valor_onion:.2f} reais' )
            petiscos.insert(0,valor_onion)      
        elif petisco=='14':
          break
        elif petisco=='15':
          break
        else:
          print('\033[1;31;107m Não temos essa opção. \033[0m')
        sum_petiscos=sum(petiscos)
        sum_petiscos1=sum(petiscos)
        print(f'o subtotal em petiscos é {sum_petiscos}')
      if petisco=='15':
        break      

############### Seção 4- Sobremesas ######################     
      sobremesa='4'
      while cardapio== '4' and sobremesa!='14':
        print('-'*30, ''' \n \033[0;35;107m 
Hello, you! Bem-vindo à nossa \033[4;35;107m Lista Sobremesas \033[0;35;107m

Digite o número indicado ao lado da opção desejada \033[0m \n
________________________________________________
Código    Opção         Quantidade       Valor
________________________________________________
[031]- Torta de limão     (200g)        R$15,00 
[032]- Mousse maracujá    (200g)        R$10,00
[014]- Voltar ao cardápio
[015]- Finalizar pedido \n

________________________________________________\n''','-'*30)
        sobremesa=input(' ').strip()[0:2].rsplit('.')[0].rsplit(',')[0].rsplit(' ')[0].replace('0', '')
        if sobremesa =='15':
          print(f'\nVocê selecionou: {sobremesa}.\nRetornamos ao menu principal.\n Você tem certeza que quer finalizar?\n ','-'*30)
        elif sobremesa=='31'or sobremesa=='32':
          print(f'\nVocê selecionou: {sobremesa}\n','-'*30)
        elif sobremesa=='14':
          print(f'\nVocê selecionou {sobremesa}, voltaremos ao cardápio para que possa desfrutar da nossa variedade de opções:\n','-'*30)
        if sobremesa=='31':
          quant1=str(input('Selecione a quantidade de Torta de limão desejada: ')).rsplit('.')[0].rsplit(',')[0].rsplit(' ')[0]
          if quant1.isnumeric()==True:
            quant2=float(quant1)
            valor_torta= quant2*15
            if quant2>0:
              lista_qsob1.append(quant2)
              lista_qsobf1.append(quant2)
              itens_sobremesa.append(sobremesa)
            print(f'{valor_torta:.2f} reais' )
            sobremesas.insert(0,valor_torta)
          
        elif sobremesa =='32':
          quant3=str(input('Selecione a quantidade de Mousse de maracujá desejada: ')).rsplit('.')[0].rsplit(',')[0].rsplit(' ')[0]
          if quant3.isnumeric()==True:
            quant4=float(quant3)
            valor_mousse= quant4*10
            if quant4>0:
              itens_sobremesa.append(sobremesa)
              lista_qsob2.append(quant4)
              lista_qsobf2.append(quant4)              
            print(f'{valor_mousse:.2f} reais' )
            sobremesas.insert(0,valor_mousse)
        elif sobremesa=='14':
          break
        elif sobremesa=='15':
          break
        else:
          print('\033[1;31;107m Não temos essa opção. \033[0m ')
        sum_sobremesas=sum(sobremesas)
        sum_sobremesas1=sum(sobremesas)
        print(f'O subtotal em sobremesas é {sum_sobremesas}')
      if sobremesa=='15':
        break
    soma=[sum(comidas),sum(bebidas),sum(petiscos),sum(sobremesas)]
    total=sum(soma)
    total2.append(total)
####################### Seção de pagamentos###############################
    if total>0:
      total1=total
      print('_'*30,'\n \033[1;35;107m Você solicitou: \033[0m \n ')
      if sum_comidas>0:
        if '11' in itens_comida:
          cont=sum(lista_qcomf1)
          sub1=cont*70
          contp=sum(lista_qcom1)
          subp1=contp*70
          print(f'{contp}x Costela na brasa________________R$ {subp1}')
        if '12' in itens_comida:
          cont1=sum(lista_qcomf2)
          sub2=cont1*50          
          contp1=sum(lista_qcom2)
          subp2=contp1*50
          print(f'{contp1}x Nhoc de camarão________________R$ {subp2}')      
      if sum_bebidas>0:
        if '41' in itens_bebida:
          cont2=sum(lista_qbebf1)
          sub3=cont2*25
          contp2=sum(lista_qbeb1)
          subp3=contp2*25
          print(f'{contp2}x Caipiroska limão________________R$ {subp3}\n')
        if '42' in itens_bebida:
          cont3=sum(lista_qbebf2)
          sub4=cont3*20
          contp3=sum(lista_qbeb2)
          subp4=contp3*20
          print(f'{contp3}x Caipiroska.pop("álcool")________________R$  {subp4}\n')
      if sum_petiscos>0:
        if '21' in itens_petisco:
          cont4=sum(lista_qpetf1)
          sub5=cont4*35
          contp4=sum(lista_qpet1)
          subp5=contp4*35
          print(f'{contp4}x Camarão empanado________________R$ {subp5}\n')
        if '22' in itens_petisco:
          cont5=sum(lista_qpetf2)
          contp5=sum(lista_qpet2)
          sub6=contp5*40
          subp6=contp5*40
          print(f'{contp5}x Bolinho de bacalhau________________R$ {subp6}\n')
      if sum_sobremesas>0:
        if '31' in itens_sobremesa:
          cont6=sum(lista_qsobf1)
          sub7=cont6*15
          contp6=sum(lista_qsob1)
          subp7=contp6*15
          print(f'{contp6}x Torta de limão________________R$ {subp7}\n')
        if '32' in itens_sobremesa:
          cont7=sum(lista_qsobf2)
          sub8=cont7*10
          contp7=sum(lista_qsob2)
          subp8=contp7*10
          print(f'{contp7}x Mousse maracujá________________R$ {subp8}\n')
      print(f'\n\033[0;34;107m Totalizando \033[0;34;107m R$ {total1} \033[0m \n', '_'*30)
    else:
      print('')
    while total != 0:
      print('-'*30, '''\n \033[1;35;107m Você está acessando à sessão pagamentos. Qual a forma de pagamento? \033[0m
[1] Cartão
[2] Dinheiro
[3] Cancelar compra
    ''')
      pagamento=str(input(' ')).replace('0', '').rsplit('.')[0].rsplit(',')[0].rsplit(' ')[0].strip()[0]
      print('-'*30)

      if pagamento not in '123':
        print('\033[1;31;107m Incorreto.\033[0m')
      else:
        if pagamento=='1':
          print('''\033[1;32;107m
      
Você selecionou Cartão. Selecione a opção desejada \033[0m
___________________________________________________
[1] Cartão de crédito parcelado em 1x sem juros
[2] Cartão de crédito parcelado em 2x sem juros
[3] Cartão de crédito parcelado em 3x sem juros 
[4] Cartão de débito
[5] Escolher outro método de pagamento/cancelar a compra
___________________________________________________
    ''')
          total1=total  
          vezes=str(input(' ')).replace('0', '').rsplit('.')[0].rsplit(',')[0].rsplit(' ')[0].strip()[0]
          if vezes not in '12345':
            print('Incorreto.')
          elif vezes == '1':
            print(f'Pagamento aprovado! O valor cobrado foi R$ {total:.2f}\nA codeback agradece pela sua compra, volte sempre!')
            break
          elif vezes == '2':
            total_2=total/2
            print(f'Pagamento aprovado! Você pagará 2x R$ {total_2:.2f}, sem juros.\nA codeback agradece pela sua compra, volte sempre!')
            break
          elif vezes == '3':
            total_3=total/3
            print(f'Pagamento aprovado! Você pagará 3x R$ {total_3:.2f}, sem juros.\nA codeback agradece pela sua compra, volte sempre!')
            break
          elif vezes == '4':
            print(f'Pagamento aprovado! O valor cobrado foi R$ {total:.2f} no cartão de débito.\nA codeback agradece pela sua compra, volte sempre!')
            break
          elif vezes =='5':
            print('Retornando à sessão anterior')
            pagamento=4
    ############################## código cancelamento de compra ################################################
        elif pagamento=='3':
          print('_'*30,'\n \033[1;35;107m Você está desistindo de: \033[0m \n ')
          if sum_comidas>0:
            if '11' in itens_comida:
              print(f'{contp}x Costela na brasa________________R$ {subp1}')
            if '12' in itens_comida:
              print(f'{contp1}x Nhoc de camarão________________R$ {subp2}')      
          if sum_bebidas>0:
            if '41' in itens_bebida:
              print(f'{contp2}x Caipiroska limão________________R$ {subp3}\n')
            if '42' in itens_bebida:
              print(f'{contp3}x Caipiroska.pop("álcool")________________R$  {subp4}\n')
          if sum_petiscos>0:
            if '21' in itens_petisco:
              print(f'{contp4}x Camarão empanado________________R$ {subp5}\n')
            if '22' in itens_petisco:
              print(f'{contp5}x Bolinho de bacalhau________________R$ {subp6}\n')
          if sum_sobremesas>0:
            if '31' in itens_sobremesa:
              print(f'{contp6}x Torta de limão________________R$ {subp7}\n')
            if '32' in itens_sobremesa:
              print(f'{contp7}x Mousse maracujá________________R$ {subp8}\n')
          print(f'\n\033[0;34;107m Totalizando \033[0;34;107m R$ {total1} \033[0m \n', '_'*30)
          print('''\033[0;31;107m Você tem certeza que quer desistir da compra?
[1] Sim
[2] Não \033[0m\n''')
          certeza=str(input(' ')).rsplit('.')[0].rsplit(',')[0].rsplit(' ')[0].strip()[0]
          while certeza!='2':
            if certeza not in '12':
              print('\033[0;31;107m incorreto. Selecione 1 ou 2: \033[0m\n ')
              certeza=str(input(' ')).rsplit('.')[0].rsplit(',')[0].rsplit(' ')[0].strip()[0]
              if certeza=='12':
                break
            if certeza=='1':
              cancela1+=contp
              cancela2+=contp1
              cancela3+=contp2
              cancela4+=contp3
              cancela5+=contp4
              cancela6+=contp5
              cancela7+=contp6
              cancela8+=contp7
              total2.pop()
              nota=0
              total=0
              print('Sua compra foi cancelada')
              break
            print('Voltaremos à seção de pagamentos')



    ########## Pagamento em dinheiro ###########################
        elif pagamento=='2':
          print('''Você selecionou dinheiro.''')
          falta=total
          total1=total
          while total!=0:
            while total>0:
              nota=str(input(f'''
....................................................................
O total foi {total1}

Está faltando = > R$ {total}
Digite [c] retornar à sessão anterior\cancelar a compra

Não aceitamos moedas, se você adicionar moedas elas serão devolvidas:
.....................................................................
          ''')).rsplit('.')[0].rsplit(',')[0].rsplit(' ')[0]
              if nota.isnumeric()==True:
                notas=int(nota) 
                total-=notas       
              elif nota =='c':
                pagamento=4
                break      
            if nota=='c':
              pagamento=4
              break
              
    ############################ código do troco#################################
            if total<0:
              troco=total*(-1)
              while troco>0:
                trocon=0
                notas=100
                print(f'Seu troco será R$ {troco}.\n \033[4;31;107m \n Entregando: \033[0m \n ')
                while True:
                  if troco>=notas:
                    troco-=notas
                    trocon+=1
                  else:
                    if trocon>0:
                      print(f'{trocon} notas de  {notas} reais \n')
                    if notas==100:
                      notas=50

                    elif notas==50:
                      notas=20

                    elif notas==20:
                      notas=10

                    elif notas==10:
                      notas=5

                    elif notas==5:
                      notas=2

                    elif notas==2:
                      notas=1
                            
                    trocon=0

                    if troco==0:
                      total=0
                      break
    sum_sobremesas=sum_petiscos=sum_comidas=sum_bebidas=0
    total1=total=0
# Encerrando o pedido
  elif menu =='F': 
    break
  else:
    print(f'''Inválido''') 
#  soma=[sum(comidas),sum(bebidas),sum(petiscos),sum(sobremesas)]
#  total=sum(soma)
total3=sum(total2)
if total3>0:
  print('_'*30,'\n\033[1;35;107m Obrigada pela preferência! Você consumiu: \033[0m \n ')
  if sum_comidas1>0:
    if '11' in itens_comida:
      if cont>0:
        a=int(cont-cancela1)
        sub1=a*70
        print(f'{a}x Costela na brasa______________________R$ {sub1}\n')
    if '12' in itens_comida:
      if cont1>0:
        b=int(cont1-cancela2)
        sub2=b*50
        print(f'{b}x Nhoc de camarão______________________R$ {sub2}\n')      
  if sum_bebidas1>0:
    if '41' in itens_bebida:
      if cont2>0:
        c=int(cont2-cancela3)
        sub3=c*25
        print(f'{c}x Caipiroska limão______________________R$ {sub3}\n')
    if '42' in itens_bebida:
      if cont3>0:
        d=int(cont3-cancela4)
        sub4=d*20
        print(f'{d}x Caipiroska.pop("álcool")______________________R$  {sub4}\n')
  if sum_petiscos1>0:
    if '21' in itens_petisco:
      if cont4>0:
        e=int(cont4-cancela5)
        sub5=e*35
        print(f'{e}x Camarão empanado______________________ R$ {sub5}\n')
    if '22' in itens_petisco:
      if cont5>0:
        f=int(cont5-cancela6)
        sub6=f*40
        print(f'{f}x Bolinho de bacalhau______________________R$ {sub6}\n')
  if sum_sobremesas1>0:
    if '31' in itens_sobremesa:
      if cont6>0:
        g=int(cont6-cancela7)
        sub7=g*15
        print(f'{g}x Torta de limão______________________R$ {sub7}\n')
    if '32' in itens_sobremesa:
      if cont7>0:
        h=int(cont7-cancela8)
        sub8=h*10
        print(f'{h}x Mousse maracujá______________________R$ {sub8}\n')
  print(f'\n \033[0;34;107m E o total foi= \033[0;34;107m R$ {total3} \033[0m \n', '_'*30)

  
else:
  print('Vejo que não teve nenhum consumo. Obrigada pela visita!')
  
print( '\n \033[1;32;107m Operação finalizada \033[0m \n''','-'*30)
