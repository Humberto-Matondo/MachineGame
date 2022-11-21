from src.controlers.deposit import theDepositFuncion
from src.controlers.repit import game


print('x'*32)
print('xxx|WELCOLL TO MY FIRST GAME|xxx')
print('x'*32)

balance = theDepositFuncion() #assim, posso repeti quantas vezes quiser essa operacao basta chamar-la
while True:
    print(f'Current balance is kz{balance}')
    gameStart = input('Press enter to play (q to quit): ')
    if gameStart == 'q':
        break
    balance += game(balance)
print(f'You left with kz{balance}.')
