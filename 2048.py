from tkinter import Frame, Label, CENTER

import Logics
import constants as c

class Game2048(Frame):
    def __init__(self):
        Frame.__init__(self)
        # visualizing Frame in grid form
        self.grid()
        self.master.title('2048')
        # binding the control, i.e., if any key is pressed go to key_pressed function
        self.master.bind("<Key>", self.key_pressed)
        self.commands = {
            c.KEY_UP : Logics.move_up,
            c.KEY_DOWN : Logics.move_down,
            c.KEY_LEFT : Logics.move_left,
            c.KEY_RIGHT : Logics.move_right
        }
        self.grid_cells = []
        self.init_grid()
        self.init_matrix()
        # update UI (set cell bg color and cell text color)
        self.update_grid_cells()
        # gameplay loop
        self.mainloop()

    def init_grid(self):
        # making the background
        background = Frame(self, bg = c.BG_COLOR_GAME, width = c.SIZE, height = c.SIZE)
        # visualizing background in grid form
        background.grid()

        for i in range(c.GRID_LEN):
            grid_row = []
            for j in range(c.GRID_LEN):
                # making cells inside background
                cell = Frame(background, bg = c.BG_COLOR_EMP_CELL,
                width = c.SIZE/c.GRID_LEN, height = c.SIZE/c.GRID_LEN)

                # placing cells in the correct position with padding
                cell.grid(row = i, column = j, padx = c.GRID_PAD, pady = c.GRID_PAD)

                # making the textbox(Label) inside cell which will contain the numbers
                t = Label(master = cell, text = "", bg = c.BG_COLOR_EMP_CELL,
                justify = CENTER, font = c.FONT, width = 5, height = 2)

                t.grid()
                grid_row.append(t)

            self.grid_cells.append(grid_row)

    def init_matrix(self):
        self.matrix = Logics.start_game()
        Logics.add_new_2(self.matrix)
        Logics.add_new_2(self.matrix)

    def update_grid_cells(self):
        # UI update
        for i in range(c.GRID_LEN):
            for j in range(c.GRID_LEN):
                new_num = self.matrix[i][j]
                if new_num == 0:
                    self.grid_cells[i][j].configure(text = "", bg = c.BG_COLOR_EMP_CELL)
                else:
                    self.grid_cells[i][j].configure(text = str(new_num),
                    bg = c.CELL_BG_COLOR_DICT[new_num], fg = c.CELL_TXT_COLOR_DICT[new_num])
        # waits until all UI changes are done
        self.update_idletasks()
    
    def key_pressed(self, event):
        # string representation of the event
        key = repr(event.char)
        if key in self.commands:
            changed = self.commands[key](self.matrix)
            if changed:
                Logics.add_new_2(self.matrix)
                self.update_grid_cells()
                changed = False
                if Logics.get_curr_state(self.matrix) == 1:
                    self.grid_cells[1][1].configure(text = 'YOU', bg = c.BG_COLOR_EMP_CELL)
                    self.grid_cells[1][2].configure(text = 'WIN!', bg = c.BG_COLOR_EMP_CELL)
                if Logics.get_curr_state(self.matrix) == -1:
                    self.grid_cells[1][1].configure(text = 'YOU', bg = c.BG_COLOR_EMP_CELL)
                    self.grid_cells[1][2].configure(text = 'LOSE!', bg = c.BG_COLOR_EMP_CELL)

gamegrid = Game2048()
