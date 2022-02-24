# This program is a Fibonacci Nim game, played by two players
# Task: Assignment 1
# Data: February 22, 2022
# Author: Youssef Moataz

def fibonacci_nim():
    # the maximum number of coins, etc...
    pile_size = int(input("Enter pile size : "))

    # assign the players' initial values
    first = 0
    second = 0

    # input function 1
    def get_first_player_number(player):
        player = int(input("First player : "))
        return player

    # input function 2
    def get_second_player_number(player):
        player = int(input("Second player : "))
        return player

    # output winner statement
    def player_wins(number):
        print("Player", number, "wins !")

    # changed false after first move done
    is_first_move = True

    # changed false after a player wins
    no_winner = True

    # changed true if the input is valid, returns to false after the check
    available_choice = False

    # Game starts here
    while no_winner:

        # print(pile_size)

        # assign the first player value from input
        first = get_first_player_number(first)

        # check input validity
        while not available_choice:
            if first > pile_size or first == 0:
                first = get_first_player_number(first)
            else:
                available_choice = True
        available_choice = False

        # first move case
        if is_first_move:

            if first < pile_size:
                pile_size -= first

                # assign the second player value from input
                second = get_second_player_number(second)

                # check input validity
                while not available_choice:
                    if second > pile_size or second == 0:
                        second = get_second_player_number(second)
                    else:
                        available_choice = True
                available_choice = False

                # check input validity
                while not available_choice:
                    if second <= pile_size and second <= first * 2:
                        pile_size -= second

                        # winning condition
                        if pile_size == 0:
                            player_wins(2)
                            no_winner = False
                            break

                        is_first_move = False
                        available_choice = True
                    else:
                        second = get_second_player_number(second)
                available_choice = False
                continue
            else:
                continue
        # not first move case
        else:
            # check input validity
            if first <= pile_size and first <= second * 2:
                pile_size -= first

                # winning condition
                if pile_size == 0:
                    player_wins(1)
                    no_winner = False
                    break

                second = get_second_player_number(second)

                # check input validity
                while not available_choice:
                    if second > pile_size or second == 0:
                        second = get_second_player_number(second)
                    else:
                        available_choice = True
                available_choice = False

                # check input validity
                while not available_choice:
                    if second <= pile_size and second <= first * 2:
                        pile_size -= second

                        # winning condition
                        if pile_size == 0:
                            player_wins(2)
                            no_winner = False
                            break

                        available_choice = True
                        
                    else:
                        second = get_second_player_number(second)

                available_choice = False

                continue

            else:

                continue


if __name__ == '__main__':

    # runs the game
    fibonacci_nim()
