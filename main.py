from tic_tac_toe import Tictactoe

on = True
t = Tictactoe()


while on:
    t.game_loop()
    start = input("Would you like to play again?").title()
    if start == "Yes":
        t.reset()
        t.game_loop()
    else:
        print("See you soon")
        on = False
