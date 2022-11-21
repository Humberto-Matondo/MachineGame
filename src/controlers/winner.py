
def check_winnings(columns, lines, bet, value):
    winnings = 0
    winning_lines = []
    for line in range(lines): #desta vez estamos a girar nas linhas. 
        symbol = columns[0][line] #para fixar a coluna e ir verificando os simbolos das linas
        for column in columns: # vai girar na coluna em busca do simbolo escolhido.
            symbol_to_check = column[line]
            if symbol != symbol_to_check: #se o simbolo gerado for diferente ao digitado entao...
                break
        else: 
            winnings += value[symbol] * bet #Se todos simbols forem igual ao digitado entao...
            winning_lines.append(line + 1)
            
    return winnings, winning_lines
