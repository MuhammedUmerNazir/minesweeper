from tkinter import *
from cell import Cell
import settings
import utils
import random

root = Tk()
# Override the settings of the window
root.configure(bg="black")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Minesweeper")
root.resizable(False, False) # False passed twice, once for the width and once for the height

top_frame = Frame(
    root,
    bg="black",
    width=settings.WIDTH,
    height=utils.height_percent(25),
)
top_frame.place(x=0,y=0)

left_frame = Frame(
    root,
    bg="black",
    width = utils.width_percent(25),
    height = utils.height_percent(75),
)
left_frame.place(x=0,y=utils.height_percent(25))

center_frame = Frame(
    root,
    bg="black",
    width = utils.width_percent(75),
    height = utils.height_percent(75),
)

center_frame.place(
    x=utils.width_percent(25),
    y=utils.height_percent(25),
)

# # Example Button
# btn1 = Button(
#     center_frame,
#     bg="blue",
#     text="first_button",
# )
# btn1.place(x=0,y=0)


# c1 = Cell()
# c1.create_btn_object(center_frame)
# c1.cell_btn_object.grid(
#     column=0, row= 0
#     )

# c2 = Cell()
# c2.create_btn_object(center_frame)
# c2.cell_btn_object.grid(
#     column=1, row=0
# )

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x, row=y
        )
Cell.randomize_mines()

# Run the window
root.mainloop()