from Node import Node
from draw_event import last_draw

def compute_H(end, point):
	return (abs(point.x - end.x) + abs(point.y - end.y)) * 10

def compute_G(current, point):
	return current.G + int((((point.x - current.x) ** 2 + (point.y - current.y) ** 2) ** 0.5) * 10)

def A_finding(start, end, canvas_map):
	open_set = []
	close_set = set()

	current = start
	close_set.add(current)

	while end not in close_set:
		for block_x in range(-1, 2):
			for block_y in range(-1, 2):
				now_node = canvas_map[current.x + block_x][current.y + block_y]
				if block_x != 0 and block_y != 0:
					if canvas_map[current.x + block_x][current.y].status == 1 or canvas_map[current.x][current.y + block_y].status == 1:
						continue
				if now_node.status != 1 and now_node.status != 2 and now_node not in close_set:
					if now_node in open_set:
						buffer_G = compute_G(current, now_node)
						if buffer_G <= now_node.G:
							now_node.G = buffer_G
							now_node.compute_F()
							now_node.parent = current
					else:		
						open_set.append(now_node)
						now_node.G = compute_G(current, now_node)
						now_node.H = compute_H(end, now_node)
						now_node.compute_F()
						now_node.parent = current
					if now_node != end:
						last_draw(now_node.x, now_node.y, "open")

		next_node = open_set[len(open_set) - 1 - open_set[::-1].index(min(open_set, key = lambda point : point.F))]

		current = next_node
		open_set.remove(current)
		close_set.add(current)
		if current != end:
			last_draw(current.x, current.y, "close")

	path_node = end
	while path_node.parent != start:
		print (path_node.parent.x, path_node.parent.y)
		last_draw(path_node.parent.x, path_node.parent.y, "path")
		path_node = path_node.parent

def A_path(canvas_map, start_end_position):
	A_finding(canvas_map[start_end_position[0]][start_end_position[1]], canvas_map[start_end_position[2]][start_end_position[3]], canvas_map)