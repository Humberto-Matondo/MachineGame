from src.controlers.getNumberOfLine import get_number_of_line
from src.controlers.getBet import get_bet
from src.controlers.getMachineSpin import get_slot_machine_Spin
from src.controlers.printMachine import print_slot_machine
from src.controlers.winner import check_winnings
from src.models.symbols import symbol_count
from src.models.symbol_value import symbol_value

ROWS = 3
COLS = 3

def game(balance):
    lines = get_number_of_line() #assim, posso repitir quantas vezes quiser, basta chamar a funcao
    while True:
        bet = get_bet()
        total_bet = bet*lines
        if total_bet > balance:
            print(f'\nYour current balance is: {balance}\nSorry, You dont have enough to bet that amount.')
        else:
            break

    print(f'\nyou are betting Kz{bet} on {lines} lines. Total bet is equal to: Kz{total_bet}')
    slots = get_slot_machine_Spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots) 
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f'\nYou won kz{winnings}.')
    print(f'You won on lines:', *winning_lines)
    print()
    return winnings - total_bet
