import time
from Node import Node

cond_s, cond_e = True, True
canvas = None
canvas_map = None
width, height = 0, 0

#use for zoom
check = 0
scale_point_x, scale_point_y = 0.0, 0.0
text_check = False

def draw_boardline(pass_canvas, distance, pass_width, pass_height, pass_canvas_map):
	global canvas, width, height, canvas_map
	canvas = pass_canvas
	canvas_map = pass_canvas_map
	width, height = pass_width, pass_height
	for x in range(distance, width, distance):
		canvas.create_line(x, 0, x, height, fill = 'white', tags = 'xline')
	for y in range(distance, height, distance):
		canvas.create_line(0, y, width, y, fill = 'white', tags = 'yline')

def get_xy(event, start_end_position, who):
	if check == 0:
		block_x = event.x // 30
		block_y = event.y // 30
		if who == "Button-1":
			draw_start(block_x, block_y, start_end_position)
		elif who == "Button-3":
			draw_end(block_x, block_y, start_end_position)
		elif who == "Block":
			draw_block(block_x, block_y)
		else:
			draw_clear(block_x, block_y)

def draw_block(block_x, block_y):
	global canvas_map
	if canvas_map[block_x + 1][block_y + 1].status == 0:
		canvas_map[block_x + 1][block_y + 1].status = 1
		canvas_x = block_x * 30 + 1
		canvas_y = block_y * 30 + 1
		canvas.create_rectangle(canvas_x, canvas_y, canvas_x + 28, canvas_y + 28, fill = 'black', tags = 'drawed')

def draw_start(block_x, block_y, start_end_position):
	global cond_s, canvas_map
	if canvas_map[block_x + 1][block_y + 1].status == 0 and cond_s == True:
		cond_s = False
		canvas_map[block_x + 1][block_y + 1].status = 2
		canvas_x = block_x * 30 + 1
		canvas_y = block_y * 30 + 1
		canvas.create_rectangle(canvas_x, canvas_y, canvas_x + 28, canvas_y + 28, fill = 'blue', tags = 'drawed')
		start_end_position[0] = block_x + 1
		start_end_position[1] = block_y + 1				

def draw_end(block_x, block_y, start_end_position):
	global cond_e, canvas_map
	if canvas_map[block_x + 1][block_y + 1].status == 0 and cond_e == True:
		cond_e = False
		canvas_map[block_x + 1][block_y + 1].status = 3
		canvas_x = block_x * 30 + 1
		canvas_y = block_y * 30 + 1
		canvas.create_rectangle(canvas_x, canvas_y, canvas_x + 28, canvas_y + 28, fill = 'red', tags = 'drawed')
		start_end_position[2] = block_x + 1
		start_end_position[3] = block_y + 1

def draw_clear(block_x, block_y):
	global cond_s, cond_e, canvas_map
	if canvas_map[block_x + 1][block_y + 1].status != 0:
		if canvas_map[block_x + 1][block_y + 1].status == 2:
			cond_s = True
		if canvas_map[block_x + 1][block_y + 1].status == 3:
			cond_e = True
		canvas_map[block_x + 1][block_y + 1].status = 0
		canvas_x = block_x * 30 + 1
		canvas_y = block_y * 30 + 1
		canvas.create_rectangle(canvas_x, canvas_y, canvas_x + 29, canvas_y + 29, fill = 'gray', outline = '', tags = 'drawed')

def draw_origin():
	global cond_s, cond_e
	cond_s, cond_e = True, True
	canvas.delete('drawed', 'text')

def zoom(event, canvas):
	global check, text_check
	zoom_delta = 0.75
	scale = 1.0

	def zoom_function():
		global scale_point_x, scale_point_y, width, height
		if check == 0:
			scale_x = canvas.canvasx(event.x)
			scale_y = canvas.canvasy(event.y)
			scale_point_x = scale_x
			scale_point_y = scale_y
		else:
			scale_x = scale_point_x
			scale_y = scale_point_y
		canvas.scale('all', scale_x, scale_y, scale, scale)
		canvas.config(scrollregion = canvas.bbox('all'))

	if scale >= 1.0:
		if event.delta == -120 and check > 0:
			scale *= zoom_delta
			zoom_function()
			check -= 1
		if event.delta == 120:
			scale /= zoom_delta
			zoom_function()
			check += 1
	if check >= 4 and not text_check:
		canvas.itemconfig('text', state = 'normal')
		text_check = True
	if check < 4 and text_check:
		canvas.itemconfig('text', state = 'hidden')
		text_check = False

def draw_text(canvas):
	for x in range(42):
		for y in range(35):
			if canvas_map[x][y].text_status:
				canvas.create_text((canvas_map[x][y].x - 1) * 30 + 7, (canvas_map[x][y].y - 1) * 30 + 5,\
								   font = ('Helvetica', 15), text = canvas_map[x][y].F, state = 'hidden', tags = 'text')
				canvas.create_text((canvas_map[x][y].x - 1) * 30 + 7, (canvas_map[x][y].y - 1) * 30 + 25,\
								   font = 15, text = canvas_map[x][y].G, state = 'hidden', tags = 'text')
				canvas.create_text((canvas_map[x][y].x - 1) * 30 + 24, (canvas_map[x][y].y - 1) * 30 + 25,\
								   font = 15, text = canvas_map[x][y].H, state = 'hidden', tags = 'text')

def draw_open(x, y):
	canvas.create_rectangle(x, y, x + 28, y + 28, fill = 'lightgreen', tags = 'drawed')
	time.sleep(0.01)
	canvas.update()

def draw_close(x, y):
	canvas.create_rectangle(x, y, x + 28, y + 28, fill = 'pink', tags = 'drawed')
	time.sleep(0.01)
	canvas.update()

def draw_path(x, y):
	canvas.create_rectangle(x, y, x + 28, y + 28, fill = 'lightblue', tags = 'drawed')
	draw_text(canvas)

def last_draw(x, y, who):
	canvas_map[x][y].text_status = True
	x = (x - 1) * 30 + 1
	y = (y - 1) * 30 + 1
	if who == "open":
		draw_open(x, y)
	elif who == "close":
		draw_close(x, y)
	else:
		draw_path(x, y)