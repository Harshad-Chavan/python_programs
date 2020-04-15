import random

three_by_three = ["-" for x in range(0, 9)]
marks = ['X', 'O']
places = [x for x in range(0, 9)]


def win_condition(mark, place):
    return False


def print_box():
    print(three_by_three[0], three_by_three[1], three_by_three[2], )
    print(three_by_three[3], three_by_three[4], three_by_three[5], )
    print(three_by_three[6], three_by_three[7], three_by_three[8], )


print_box()


def put_mark(place, mark):
    if three_by_three[place - 1] == '-':
        three_by_three[place - 1] = mark
        return True
    else:
        return False


while True:
    player_one = input("Enter x/o to start the game(Enter exit to quit)::")
    if player_one == 'X':
        player_one_mark = 'X'
        player_two_mark = 'O'
        break
    elif player_one == 'O':
        player_one_mark = 'O'
        player_two_mark = 'X'
        break
    else:
        print("Exited or wrong mark")
        break

turn = 1
count = 0
while True:
    if turn == 1:
        if count != 9:
            place = input("player one enter your place::")
            if put_mark(int(place), player_one_mark):
                count += 1
                if win_condition(player_one_mark, int(place) - 1):
                    print("player one wins")
                    print_box()
                    break
                turn = 2
                print_box()
            else:
                print("already filled")
        else:
            break

    if turn == 2:
        if count != 9:
            place = input("player two enter your place::")
            if put_mark(int(place), player_two_mark):
                count += 1
            if win_condition(player_two_mark, int(place) - 1):
                print("player Two wins")
                print_box()
                break
            turn = 1
            print_box()
        else:
            break
