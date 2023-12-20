
class Tictactoe:

    def __init__(self):
        self.p1 = ""
        self.p2 = ""
        self.r1 = {"A1": "A1", "2": "|", "A2": "A2", "4": "|", "A3": "A3"}
        self.r2 = {"B1": "B1", "2": "|", "B2": "B2", "4": "|", "B3": "B3"}
        self.r3 = {"C1": "C1", "2": "|", "C2": "C2", "4": "|", "C3": "C3"}
        self.p1_win = False
        self.p2_win = False
        self.turn = 0


    def o_or_x(self):
        self.p1 = input("Player 1 choose your symbol - O or X").upper()
        if self.p1 == "X":
            self.p2 = "O"
        else:
            self.p2 = "X"

    def show_board(self):
        print(f"{self.r1['A1']}{self.r1['2']}{self.r1['A2']}{self.r1['4']}{self.r1['A3']}")
        print("-----------")
        print(f"{self.r2['B1']}{self.r2['2']}{self.r2['B2']}{self.r2['4']}{self.r2['B3']}")
        print("-----------")
        print(f"{self.r3['C1']}{self.r3['2']}{self.r3['C2']}{self.r3['4']}{self.r3['C3']}")

    def reset(self):
        self.p1 = ""
        self.p2 = ""
        self.r1 = {"A1": "A1", "2": "|", "A2": "A2", "4": "|", "A3": "A3"}
        self.r2 = {"B1": "B1", "2": "|", "B2": "B2", "4": "|", "B3": "B3"}
        self.r3 = {"C1": "C1", "2": "|", "C2": "C2", "4": "|", "C3": "C3"}
        self.p1_win = False
        self.p2_win = False

    def p1_add(self):
        self.turn += 1
        self.show_board()
        choice = input("Player 1, place your mark on one of the coordinates above").upper()
        if choice in self.r1:
            self.r1[choice] = f" {self.p1} "
        elif choice in self.r2:
            self.r2[choice] = f" {self.p1} "
        elif choice in self.r3:
            self.r3[choice] = f" {self.p1} "
        else:
            print("COORDINATE ERROR!! Please try again")
            self.p1_add()

    def p2_add(self):
        self.turn += 1
        self.show_board()
        choice = input("Player 2, place your mark on one of the coordinates above").upper()
        if choice in self.r1:
            self.r1[choice] = f" {self.p2} "
        elif choice in self.r2:
            self.r2[choice] = f" {self.p2} "
        elif choice in self.r3:
            self.r3[choice] = f" {self.p2} "
        else:
            print("COORDINATE ERROR!! Please try again")
            self.p2_add()

    def eval_board_x(self):
        if self.r1["A1"]+self.r1["A2"]+self.r1["A3"] == " X  X  X ":
            return True
        elif self.r2["B1"]+self.r2["B2"]+self.r2["B3"] == " X  X  X ":
            return True
        elif self.r3["C1"]+self.r3["C2"]+self.r3["C3"] == " X  X  X ":
            return True
        elif self.r1["A1"]+self.r2["B1"]+self.r3["C1"] == " X  X  X ":
            return True
        elif self.r1["A2"]+self.r2["B2"]+self.r3["C2"] == " X  X  X ":
            return True
        elif self.r1["A3"]+self.r2["B3"]+self.r3["C3"] == " X  X  X ":
            return True
        elif self.r1["A1"]+self.r2["B2"]+self.r3["C3"] == " X  X  X ":
            return True
        elif self.r3["C1"]+self.r2["B2"]+self.r1["A3"] == " X  X  X ":
            return False

    def eval_board_o(self):
        if self.r1["A1"]+self.r1["A2"]+self.r1["A3"] == " O  O  O ":
            return True
        elif self.r2["B1"]+self.r2["B2"]+self.r2["B3"] == " O  O  O ":
            return True
        elif self.r3["C1"]+self.r3["C2"]+self.r3["C3"] == " O  O  O ":
            return True
        elif self.r1["A1"]+self.r2["B1"]+self.r3["C1"] == " O  O  O ":
            return True
        elif self.r1["A2"]+self.r2["B2"]+self.r3["C2"] == " O  O  O ":
            return True
        elif self.r1["A3"]+self.r2["B3"]+self.r3["C3"] == " O  O  O ":
            return True
        elif self.r1["A1"]+self.r2["B2"]+self.r3["C3"] == " O  O  O ":
            return True
        elif self.r3["C1"]+self.r2["B2"]+self.r1["A3"] == " O  O  O ":
            return True
        else:
            return False

    def game_loop(self):
        self.o_or_x()
        while not self.p1_win or not self.p2_win:
            self.p1_add()
            if self.p1 == "X":
                if self.eval_board_x():
                    self.p1_win = True
                    self.show_board()
                    print("Player 1 wins!!")
                    break
                elif self.turn == 9:
                    self.show_board()
                    print("It's a draw!!")
                    break
            else:
                if self.eval_board_o():
                    self.p1_win = True
                    self.show_board()
                    print("Player 1 wins!!")
                    break
                elif self.turn == 9:
                    self.show_board()
                    print("It's a draw!!")
                    break
            self.p2_add()
            if self.p2 == "X":
                if self.eval_board_x():
                    self.p2_win = True
                    self.show_board()
                    print("Player 1 wins!!")
                    break
                elif self.turn == 9:
                    self.show_board()
                    print("It's a draw!!")
                    break
            else:
                if self.eval_board_o():
                    self.p2_win = True
                    self.show_board()
                    print("Player 1 wins!!")
                    break
                elif self.turn == 9:
                    self.show_board()
                    print("It's a draw!!")
                    break
