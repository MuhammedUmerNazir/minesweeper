
from tkinter import Button, Label
import random
import settings

class Cell:
    all = []
    cell_count = settings.CELL_COUNT
    cell_count_label_object = None

    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.is_opened = False
        self.is_mine_candidate = False
        self.cell_btn_object = None
        self.x = x
        self.y = y

        # Append the cell to Cell.all
        Cell.all.append(self)

    def create_btn_object(self, location):
        btn = Button(
            location,
            width= 12,
            height= 4,
        )
        btn.bind("<Button-1>", self.left_click_actions)
        btn.bind("<Button-3>", self.right_click_actions)
        self.cell_btn_object = btn
        self.orig_color = self.cell_btn_object.cget("background")

    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            bg='black',
            fg="white",
            text=f"Cells Left:{Cell.cell_count}",
            width=12,
            height=4,
            font=("", 30)
        )

        Cell.cell_count_label_object = lbl
    
    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()

        else:
            if self.surrounded_cells_mine_length == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()

    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x-1, self.y-1),
            self.get_cell_by_axis(self.x-1, self.y),
            self.get_cell_by_axis(self.x-1, self.y+1),
            self.get_cell_by_axis(self.x, self.y-1),
            self.get_cell_by_axis(self.x, self.y+1),
            self.get_cell_by_axis(self.x + 1, self.y-1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y+1),
        ]
        cells = [cell for cell in cells if cell is not None]
        return cells 
    
    @property
    def surrounded_cells_mine_length(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1
                
        return counter
                
    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -= 1
            
            self.cell_btn_object.configure(
                text= self.surrounded_cells_mine_length
            )

            # Replace the text of the cell count with the newer count
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                    text = f"Cells Left:{Cell.cell_count}"
                )

        # Mark the cell as opened
        self.is_opened = True

    def get_cell_by_axis(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell
            else:
                pass
    
    def show_mine(self):
        # A logic to interupt game and display that the player has lost.
        self.cell_btn_object.configure(bg="red")

    def right_click_actions(self, event):

        # is_green = False
        # if not is_green:
        #     self.cell_btn_object.configure(bg="green")
        #     is_green = True
        # else:
        #     self.cell_btn_object.configure(bg="white")

        if not self.is_mine_candidate:
            self.cell_btn_object.configure(
                bg="orange"
            )
            self.is_mine_candidate = True
        
        else:
            self.cell_btn_object.configure(
                bg=self.orig_color
            )
            self.is_mine_candidate = False
        
    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(
            Cell.all, settings.MINES_COUNT
        )

        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"