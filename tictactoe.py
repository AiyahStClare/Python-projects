# -----------------------------------------------------------------------------
# Name:       tictac
# Purpose:    Implement a game of Tic Tac Toe
#
# Author:       Christine Pham
# -----------------------------------------------------------------------------
'''
This program simulates a tic-tac-toe game between a user and the CPU using
different colors to designate each player. The bottom of the program decalres
who is the winner or if there is a tie.
'''
import tkinter
import random

class Game(object):
    '''
    A simple tic-tac-toe game using color.

    Arguments:
        parent = the tkinter.TK
        canvas = a method that allows you to draw shapes and objects onto GUI
        sq1, sq2, sq3, sq4, sq5, sq6, sq7, sq8, sq9 = rectangle objects drawn
            onto the canvas
        restart_button = button that allows users to restart the game
        comment = text that announces winners or if there is a tie
        win_combos = list of winning combinations
    Attributes:
        pack() = displays the object onto the GUI
        bind() = connects a button to an event
    '''

    def __init__(self, parent):
        parent.title('Tic Tac Toe')
        self.parent = parent
        restart_button = tkinter.Button(self.parent, text='Restart', width =10,
                                        command=self.restart)
        restart_button.pack()
        self.canvas = tkinter.Canvas(parent, width=300, height=300)

        self.sq1 = self.canvas.create_rectangle(0, 0, 99, 99)
        self.sq2 = self.canvas.create_rectangle(100, 0, 199, 99)
        self.sq3 = self.canvas.create_rectangle(200, 0, 300, 99)
        self.sq4 = self.canvas.create_rectangle(0, 100, 99, 199)
        self.sq5 = self.canvas.create_rectangle(100, 100, 199, 199)
        self.sq6 = self.canvas.create_rectangle(200, 100, 300, 199)
        self.sq7 = self.canvas.create_rectangle(0, 200, 99, 300)
        self.sq8 = self.canvas.create_rectangle(100, 200, 199, 300)
        self.sq9 = self.canvas.create_rectangle(200, 200, 300, 300)

        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.play)

        self.comment = tkinter.Label(parent, text=' ')
        self.comment.pack()

        self.restart()

        self.win_combos = [ [self.sq1, self.sq2, self.sq3],
                            [self.sq4, self.sq5, self.sq6],
                            [self.sq7, self.sq8, self.sq9],
                            [self.sq1, self.sq4, self.sq7],
                            [self.sq2, self.sq5, self.sq8],
                            [self.sq3, self.sq6, self.sq9],
                            [self.sq1, self.sq5, self.sq9],
                            [self.sq3, self.sq5, self.sq7] ]


    def restart(self):
        '''
        This method is invoked when the user clicks on the RESTART button. All
        objects are filled with 'white' and the comment text is cleared when
        this button is pressed.

        Attributes:
            find_all() = finds all objects on (in this case) the canvas
            itemconfigure() = changes an item's value
            configure() = changes a label's text value
        '''

        for shape in self.canvas.find_all():
            self.canvas.itemconfigure(shape, fill='white')
        self.comment.configure(self.comment, text=' ')

    def play(self, event):
        '''
        This method is invoked when the user clicks on a square.

        Arguments:
            user_square = determines position of where the user clicked mouse
            color = determines the color of the square the user clicked
            not_white = boolean value to see if the cpu's move is allowed.
            cpu_move = randomly picks a square to color. if the square is
                'white' and a winner isn't determined yet, a square will be
                colored. If both of these conditions aren't met another square
                is chosen randomly.
            combo = each individual combo is checked to determine if there is
                a winner.
        Attributes:
            itemconfigure() = changes an item's value
            configure() = changes a label's text value
            find_closest() = finds the closest pixel to the given value
            cget() = gets the value of a label's text
            randrange() = selects a random number from a range of values
        '''

        user_square = self.canvas.find_closest(event.x, event.y)
        color = self.canvas.itemcget(user_square, "fill")
        if color == 'white' and self.comment.cget("text") == ' ':
            self.canvas.itemconfigure(user_square, fill='green')

            not_white = True
            while not_white:
                cpu_move = self.canvas.find_closest(
                    random.randrange(0, 301, 25),
                    random.randrange(0, 301, 25))
                if (self.canvas.itemcget(cpu_move, "fill") == 'white' and
                                self.comment.cget("text") == ' '):
                    self.canvas.itemconfigure(cpu_move, fill='pink')
                    not_white = False
                else:
                    not_white = True

        for combo in self.win_combos:
            if (self.canvas.itemcget(combo[0], "fill") == 'green' and
                self.canvas.itemcget(combo[1], "fill") == 'green' and
                self.canvas.itemcget(combo[2], "fill") == 'green'):
                self.comment.configure(self.comment, text='You Win!')

        if ([self.canvas.itemcget(self.sq1,"fill"), # counts how many 'white'
            self.canvas.itemcget(self.sq2,"fill"),  # squares are left
            self.canvas.itemcget(self.sq3,"fill"),
            self.canvas.itemcget(self.sq4, "fill"),
            self.canvas.itemcget(self.sq5, "fill"),
            self.canvas.itemcget(self.sq6, "fill"),
            self.canvas.itemcget(self.sq7,"fill"),
            self.canvas.itemcget(self.sq8,"fill"),
            self.canvas.itemcget(self.sq9,"fill")].count('white') == 1 and
            self.comment.cget("text") != 'You Win!' and
            self.comment.cget("text") != 'CPU Wins!'):
            self.comment.configure(self.comment, text='It\'s A Tie!')

        for combo in self.win_combos:
            if (self.canvas.itemcget(combo[0], "fill") == 'pink' and
                self.canvas.itemcget(combo[1], "fill") == 'pink' and
                self.canvas.itemcget(combo[2], "fill") == 'pink'):
                self.comment.configure(self.comment, text='CPU Wins!')


def main():

    root = tkinter.Tk()
    my_game = Game(root)
    root.mainloop()


if __name__ == '__main__':
    main()