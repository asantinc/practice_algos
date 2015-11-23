'''
Question from: http://codegolf.stackexchange.com/questions/19188/partition-a-map-of-water-flows
Partition of a map of waterflows
''''

import pdb
from collections import defaultdict, deque, namedtuple

Point = namedtuple('Point', ['x', 'y'])

CURRENT = Point(0, 0)
LEFT = Point(-1, 0)
RIGHT = Point(1, 0)
TOP = Point(0, -1)
BOT = Point(0, 1)

all_directions = (CURRENT, TOP, BOT,
					LEFT, RIGHT)

def print_2D(self, array):
	for row in array:
		print '{}'.format(row)


def direction_legal(array, x, y, dir):
	'''
	Check if direction falls on or off map of elevations
	'''
	return (y+dir.y>=0 and y+dir.y< len(array) 
		and x+dir.x>=0 and x+dir.x<len(array))


def connected(directions, origin, dest_dir):
	'''
	Return true if the origin points to dest
	and dest points towards position
	@param: directions (list(list))
	@param: origin (Point(int, int))
	@param: dest_dir (Point(int, int))
	'''
	if direction_legal(directions, origin.x, origin.y, dest_dir):
		dest_x, dest_y = origin.x+dest_dir.x, origin.y+dest_dir.y
		dest_diff = directions[dest_y][dest_x]

		if (origin.x - dest_x == dest_diff.x 
			and origin.y - dest_y == dest_diff.y):
				return True
		else:
			return False
	else:
		return False



def find_basins(sinks, directions, elevations):
	'''
	Run BFS starting at each sink.
	Count size of connected components
	'''
	def sort_elevation(pos):
		return elevations[pos.y][pos.x]

	basins = defaultdict(list)
	available_pos = [[True]*len(elevations) for l in elevations]

	sorted_sinks = sorted(sinks, key=sort_elevation, reverse=False)

	for sink in sinks:
		available_pos[sink.y][sink.x] = False
		q = deque()

		for curr_dir in all_directions:
			#visit all four neighbors of a sink
			if (direction_legal(directions, sink.x, sink.y, curr_dir)
				and curr_dir != CURRENT 
					and available_pos[sink.y+curr_dir.y][sink.x+curr_dir.x]):
				new_pos = Point(sink.x+curr_dir.x, sink.y+curr_dir.y)
				q.append(new_pos)
				basins[sink].append(new_pos)
				available_pos[new_pos.y][new_pos.x] = False

		while q:
			#visit any other connected point
			curr_pos = q.pop()
			for curr_dir in all_directions:

				if (curr_dir != CURRENT and
					connected(directions, curr_pos, curr_dir)
						and available_pos[curr_pos.y+curr_dir.y][curr_pos.x+curr_dir.x]):
					new_pos = Point(curr_pos.x+curr_dir.x, curr_pos.y+curr_dir.y)
					basins[sink].append(new_pos)
					q.appendleft(new_pos)
					available_pos[new_pos.y][new_pos.x] = False
				else:
					pass
				#pdb.set_trace()
	return basins



def get_min_direction(elevations, y, x):
	'''
	Return the min direction 
	'''
	min_dir_val = (float('inf'), float('inf'))
	min_dir = None

	for curr_dir in all_directions:
		if direction_legal(elevations, x, y, curr_dir):
			curr_val = elevations[y+curr_dir[1]][x+curr_dir[0]]
			if curr_val < min_dir_val:
				min_dir_val = curr_val
				min_dir = curr_dir
	return min_dir

def preprocess_basins(elevations):
	'''
	Find the sinks and return an array with min direction
	for each non-sink
	'''
	directions = [[None]*len(elevations) for l in elevations]

	sinks = list()
	for y, row  in enumerate(elevations):
		for x, item in enumerate(row):
			directions[y][x] = get_min_direction(elevations, y, x)
			if directions[y][x] == CURRENT:
				sinks.append(Point(x, y))
	return sinks, directions

def process_input(string):
	split_str = string.split('\n')
	split_str = [x.strip(' ') for x in split_str]
	# = ['3', '4 5 6', '7 8 9', '5 6 7']

	size = int(float(split_str[0]))
	elevations = list()

	for i in range(1, size+1): 
		x = split_str[i]
		elevations.append(list())

		for j, y in enumerate(x.split(' ')):
			try:
				elevations[i-1].append(int(float(y)))
			except ValueError:
				print 'Could not append {}'.format(y)
	return size, elevations


def main(input):
	size, elevations = process_input(input)
	if size == 1: return '1'
	if size == 0: return '0'

	assert len(elevations) == size and len(elevations[0]) == size

	sinks, directions = preprocess_basins(elevations)
	basins = find_basins(sinks, directions, elevations)
	return ' '.join([str(x) for x in sorted([len(positions)+1 for sink, positions in basins.iteritems()], reverse=True)])


if __name__ == '__main__':
	inputs = list()
	inputs.append(('7 2','3 \n 1 5 2 \n 2 4 7 \n 3 6 9 \n'))
	inputs.append(('11 7 7', '5 \n 1 0 2 5 8 \n 2 3 4 7 9 \n 3 5 7 8 9 \n1 2 5 4 2 \n3 3 5 2 1'))
	inputs.append(('1','1 \n 10'))
	inputs.append(('7 5 4','4\n 0 2 1 3\n 2 1 0 4\n 3 3 3 3\n 5 5 2 1 '))
	inputs.append(('0', '0\n'))

	for truth, input in inputs:
		basin_sizes = main(input)
		assert truth == basin_sizes

