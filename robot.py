# -----------------------------------------------------------------------------
# Name:       robot
# Author:     Christine Pham
# Date:       November 12, 2017
# -----------------------------------------------------------------------------

"""
Robots can navigate the maze as long as there are no obstacles in their way and
until their battery runs out; they need to be recharged at that point. One
robot is capable of moving forward, back, left, and right, while the other
robot is able to dive and go up and down as well.
recharged with
"""
import tkinter


class Robot(object):
    """
    A rechargeable robot that's lost in a maze.

    Arguments:
    name (str): robot's name.
    color(str): color of the robot.
    row (int, optional): row index position in maze, defaults to 0.
    column (int, optional): column index position in maze, defaults to 0.

    Attributes:
    name (str): robot's name.
    color(str): color of the robot.
    row (int): row index position in maze.
    column (int): column index position in maze.
    """

    # class variable used by the show method
    unit_size = 60

    # Class variable describing the maze
    # False represents an obstacle, True represents open space
    maze = [[True, True, False, True, True, True, False, True, True, True],
            [True, True, False, True, True, True, False, True, True, True],
            [True, False, True, True, True, True, False, True, True, True],
            [True, True, True, True, True, True, True, True, False, True],
            [True, True, True, True, True, True, True, True, False, True],
            [True, True, True, True, True, True, True, True, True, True],
            [True, False, False, False, False, True, True, True, True, True],
            [True, True, False, True, True, True, True, True, False, True],
            [True, False, True, True, True, True, True, True, False, True],
            [True, True, True, True, True, True, True, True, False, True]]

    maze_size = len(maze)
    # class variable to represent a full charge
    # A robot with a fully charged battery can take up to 20 steps
    battery = 20

    def __init__(self,  name, color, row=0, column=0):
        self.name = name
        self.color = color
        self.row = row
        self.column = column

    def __str__(self):
        return self.name + ' is a ' + self.color + ' robot lost in the maze.'

    def __gt__(self, other):
        return self.battery > other.battery

    def recharge(self):
        """
        Recharges the robot's battery.
        Parameter:
            battery (int): fully charged battery
        Return:
            The updated robot object (Robot)
        """
        self.battery = Robot.battery
        return self.battery

    def one_step_forward(self):
        """
        Moves the robot one step forward, if possible.
        Returns None
        """
        if self.row+1 < len(Robot.maze):
            if Robot.maze[self.row+1][self.column]== True and self.battery > 0:
                self.row += 1
                self.battery -= 1

    def one_step_back(self):
        """
        Moves the robot one step back, if possible.
        Returns None
        """
        if self.row-1 >= 0:
            if Robot.maze[self.row-1][self.column]== True and self.battery > 0:
                self.row -= 1
                self.battery -= 1

    def one_step_right(self):
        """
        Moves robot one step to the right, if possible.
        Returns None
        """
        if self.column+1 < len(Robot.maze[0]):
            if Robot.maze[self.row][self.column+1]== True and self.battery > 0:
                self.column += 1
                self.battery -= 1

    def one_step_left(self):
        """
        Moves robot one step to the left, if possible.
        Returns None
        """
        if self.column-1 >= 0:
            if Robot.maze[self.row][self.column-1]== True and self.battery > 0:
                self.column -= 1
                self.battery -= 1

    def forward(self, steps):
        """
        Calls the method one_step_forward() for number of steps inputted.
        Parameter:
        steps(int): the number of steps robot is asked to move.
        Returns None
        """
        for i in range(steps):
            self.one_step_forward()

    def backward(self, steps):
        """
        Calls the method one_step_back() for number of steps inputted.
        Parameter:
        steps(int): the number of steps robot is asked to move.
        Returns None
        """
        for i in range(steps):
            self.one_step_back()

    def right(self, steps):
        """
        Calls the method one_step_right() for number of steps inputted.
        Parameter:
        steps(int): the number of steps robot is asked to move.
        Returns None
        """
        for i in range(steps):
            self.one_step_right()

    def left(self, steps):
        """
        Calls the method one_step_left() for number of steps inputted.
        Parameter:
        steps(int): the number of steps robot is asked to move.
        Returns None
        """
        for i in range(steps):
            self.one_step_left()

    def show(self):
        """
        A graphical representation of the robot in the maze.

        The robot's position and color are shown.
        The color is assumed to be one of the colors recognized by tkinter
        (https://www.tcl.tk/man/tcl8.4/TkCmd/colors.htm)
        If the robot's battery is empty, the robot is shown in a
        horizontal position. Otherwise the robot is shown in an upright
        position.
        The obstacles in the maze are shown in red.

        Parameter: None
        Return: None
        """
        root = tkinter.Tk()
        root.title(self.name + ' in the Maze')
        canvas = tkinter.Canvas(root, background='light green',
                                width=self.unit_size * self.maze_size,
                                height=self.unit_size * self.maze_size)
        canvas.grid()

        # a representation of the robot in the maze
        if self.battery:
            upper_x = self.column * self.unit_size + self.unit_size / 4
            upper_y = self.row * self.unit_size
            lower_x = upper_x + self.unit_size / 2
            lower_y = upper_y + self.unit_size
            eye_x = lower_x - 3 * self.unit_size / 20
            eye_y = upper_y + self.unit_size / 10

        else: # the robot ran out of battery
            upper_x = self.column * self.unit_size
            upper_y = self.row * self.unit_size + self.unit_size / 2
            lower_x = upper_x + self.unit_size
            lower_y = upper_y + self.unit_size / 2
            eye_x = lower_x - 9 * self.unit_size / 10
            eye_y = lower_y - 3 * self.unit_size / 20

        rectangle = canvas.create_rectangle(upper_x,
                                            upper_y,
                                            lower_x,
                                            lower_y,
                                            fill=self.color)
        # the robot's eyes
        canvas.create_oval(upper_x + self.unit_size / 10,
                           upper_y + self.unit_size / 10,
                           upper_x + 3 * self.unit_size / 20,
                           upper_y + 3 * self.unit_size / 20,
                           fill='black')
        canvas.create_oval(eye_x,
                           eye_y,
                           eye_x + self.unit_size / 20,
                           eye_y + self.unit_size / 20,
                           fill='black')
        # draw the obstacles in the maze
        for row in range(self.maze_size):
            for col in range(self.maze_size):
                if not self.maze[row][col]:
                    canvas.create_rectangle(col * self.unit_size,
                                            row * self.unit_size,
                                            (col + 1) * self.unit_size,
                                            (row + 1) * self.unit_size,
                                            fill='red')
        for row in range(self.maze_size):
            canvas.create_line(0,
                               row * self.unit_size,
                               self.maze_size * self.unit_size,
                               row * self.unit_size)
        for col in range(self.maze_size):
            canvas.create_line(col * self.unit_size,
                               0,
                               col * self.unit_size,
                               self.maze_size * self.unit_size)
        root.mainloop()


class UnderwaterRobot(Robot):
    """
    A rechargeable underwater robot with diving capability.

    Arguments:
    name (str): robot's name.
    color(str): color of the robot.
    row (int, optional): row index position in maze, defaults to 0.
    column (int, optional): column index position in maze, defaults to 0.
    depth (int, optional): how deep underwater the robot is, defaults to 0.

    Attributes:
    name (str): robot's name.
    color(str): color of the robot.
    row (int): row index position in maze.
    column (int): column index position in maze.
    depth (int): how deep underwater the robot is.
    """
    def __init__(self, name, color, row=0, column=0, depth=0):
        self.depth = depth
        super().__init__(name,color, row, column)

    def __str__(self):
        return self.name + ' is a ' + self.color + ' robot diving under water.'

    def dive(self, distance):
        """
        Updates the depth that the underwater robot is diving at.
        Parameter:
        distance(int): the number of feet the robot is asked to dive.
        Returns None
        """
        if self.depth + distance >= 0:
            self.depth += distance