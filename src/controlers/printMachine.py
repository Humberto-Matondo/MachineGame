def print_slot_machine(columns): #att tem muitas outras formas de fazer isso, essa e uma delas
    for row in range(len(columns[0])):#para saber o tamanho da coluna e rodar usando aquele tamaanho 
        for i, column in enumerate(columns):
            if i != len(columns) - 1: # se o item n for ultimo da coluna print(idem|) para dividir  as colunas
                print(column[row], end= ' | ')
            else:
                print(column[row], end=' ')
        print()
          

      