from tkinter import *
import draw_event, A_star, Init
from Node import Node

window = Tk()
window.title("A_path finding")
window.geometry("1200x720")

canvas_width = 1200
canvas_height = 660
canvas = Canvas(window, width = canvas_width, height = canvas_height, bg = "gray")
canvas.grid()

canvas_map = [[0 for i in range(35)] for j in range(42)]
start_end_position = [0 for i in range(4)]

draw_event.draw_boardline(canvas, 30, canvas_width, canvas_height, canvas_map)

Init.init_map(canvas_map)

#draw block
canvas.bind('<Control-B1-Motion>', lambda event, canvas_map = canvas_map, start_end_position = start_end_position, who = "Block" :
	draw_event.get_xy(event, start_end_position, who))

#clear block
canvas.bind('<Control-B3-Motion>', lambda event, start_end_position = start_end_position, who = "Clear" : 
	draw_event.get_xy(event, start_end_position, who))

#draw start
canvas.bind('<Button-1>', lambda event, start_end_position = start_end_position, who = "Button-1" : 
	draw_event.get_xy(event, start_end_position, who))

#draw end
canvas.bind('<Button-3>', lambda event, start_end_position = start_end_position, who = "Button-3" : 
	draw_event.get_xy(event, start_end_position, who))

#zoom
canvas.bind('<MouseWheel>', lambda event, canvas = canvas : draw_event.zoom(event, canvas))

start_button = Button(window, text = "Start", width = 10, command = lambda canvas_map = canvas_map, start_end_position = start_end_position : 
	A_star.A_path(canvas_map, start_end_position))
start_button.grid(sticky = W)

clear_button = Button(window, text = "Clear", width = 10, command = lambda canvas_map = canvas_map, start_end_position = start_end_position :
	Init.clear(canvas_map, start_end_position))
clear_button.grid(sticky = N+W)

window.mainloop()