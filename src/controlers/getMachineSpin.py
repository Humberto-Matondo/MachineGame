from src.models import symbols
import random

def get_slot_machine_Spin(rows, cols, symbols): #Essa e a funcao que vai gerar os itens. 
    all_symbols = [] 
    #PARTE PARA PEGAR OS SIMBOLOS DO DICIONARIO E ADD NA LISTA: 
    for symbol, symbol_count in symbols.items(): #Ex: se o Symbol for A ele vai girar 2 vezes(essa inf. está no dicionario Symbols)
        for _ in range(symbol_count):#Contador anonimo, Usa-se para quando tu n vais precisar de interagir com o contador.
            all_symbols.append(symbol) #qualquer que seja o simbolo add na lista dos all_symbols para depois usar o random.
    
    columns = []# vai ser uma lista tripla ou seja 3 colunas [1-[A,A,A], 2-[A,A,A], 3-[A,A,A]]
    #PARTE PARA PEGAR OS SIMBOLOS E ADD EM CADA COLUNA:
    for _ in range (cols):
        column = [] #vai preencher uma coluna de cada vez [A,A,A] 
        current_symbols = all_symbols[ : ] #[:] e para permitir que a copiar dos symbols aconteca, nao se usou assim: "current_symbols = all_symbols "
                                           #para n mover os symbols, copia-se apenas paraos symbols repetirem-se e enxer a coluna com eles para o jogador ganhar
        for _ in range(rows):            
            value = random.choice(current_symbols)
            current_symbols.remove(value) #tem que se remover o valor que acalhou para que n aconteca qe tdas colunas saiam apenas uma unica letra
            column.append(value)
        
        columns.append(column)  
    return columns

