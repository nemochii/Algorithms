from draw_event import draw_origin
from Node import Node

def init_map(canvas_map):
	for x in range(42):
		for y in range(35):
			canvas_map[x][y] = Node(x, y)

	set_board(canvas_map)

def set_board(canvas_map):
	for x in range(42):
		canvas_map[x][0].status = 1
		canvas_map[x][34].status = 1
	for y in range(35):
		canvas_map[0][y].status = 1
		canvas_map[41][y].status = 1

def clear(canvas_map, start_end_position):
	for y in range(35):
		for x in range(42):
			canvas_map[x][y].reset()

	for i in range(4):
		start_end_position[i] = 0

	set_board(canvas_map)
	draw_origin()