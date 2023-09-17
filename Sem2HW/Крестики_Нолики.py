
import random

b_list = list(range(1, 10))

wins = [(1, 2, 3,), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]


def board():
    print('_____________')
    for i in range(3):
        print('|', b_list[0 + i * 3], '|', b_list[1 + i * 3], '|', b_list[2 + i * 3], '|')
    print('_____________')


def user_in(userX):
    while True:
        value = input('Куда ставим  ?' + userX)
        if not (value in '123456789'):
            print('Что то не так')
            continue
        value = int(value)
        if str(b_list[value - 1]) in 'XO':
            print('Занято уже')
            continue
        b_list[value - 1] = userX
        break
def bot(tx):
    while True:
        value =random.randint(1, 9)
        if str(b_list[value - 1]) in 'XO':
            value = random.randint(1, 9)
        b_list[value - 1] = tx
        break


def check_win():
    for each in wins:
        if (b_list[each[0] - 1]) == (b_list[each[1] - 1]) == (b_list[each[2] - 1]):
            return b_list[each[1] - 1]
    else:
        return False


def play():
    count = 0
    while True:
        board()
        if count % 2 == 0:
            user_in('X')
        else:
            bot('O')
        if count > 3:
            wins = check_win()
            if wins:
                board()
                print(wins, 'Победа')
                break
        count += 1
        if count > 8:
            board()
            print('Ничья')
            break


play()
