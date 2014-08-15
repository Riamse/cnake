class Snake:

	def __init__(self, width, height):
		this.pos = (width / 2, height / 2)
		this.alive = True
		this.size = 3
		this.body = []
		this.body.append(pos)
		this.body.append((pos[0], pos[1] + 1))
		this.body.append((pos[0], pos[1] + 2))
		this.direction = 'up'

	def move(self):
		#if the snake size is too big, delete its tail, otherwise let it grow to however many units
		if this.size < len(this.body):
			del this.body[len(this.body) - 1] #check if im doing this right please lol, deleting its tail
		if this.direction == 'up':
			this.pos = (this.pos[0] - 1, this.pos[1])
		elif this.direction == 'down':
			this.pos = (this.pos[0] + 1, this.pos[1])
		elif this.direcition == 'left':
			this.pos = (this.pos[0], this.pos[1] - 1)
		elif this.direction == 'right':
			this.pos = (this.pos[0], this.pos[1] + 1)
		else:
			print('You made a typo')