'''class Player1:
	def __init__(self, game):
		self.Game = game
		self.Gridposvert1 = Node(playerdraw((self.Game.width / 3) + ((self.Game.width / 3) / 6), 
								 (self.Game.height / 1.05), (self.Game.width * 0.025)), 
					  Node(playerdraw((self.Game.width / 3) + ((self.Game.width / 3) / 6), 
					   (self.Game.height / 1.14), (self.Game.width * 0.025)), empty))
		l = self.Gridposvert1
		self.Gridposhor1 = Node(playerdraw((self.Game.width / 3) + ((self.Game.width / 3) / 6), 
								 (self.Game.height / 1.05), (self.Game.width * 0.025)), 
					  Node(playerdraw((self.Game.width / 3) + ((self.Game.width / 3) / 3), 
					   (self.Game.height / 1.05), (self.Game.width * 0.025)), empty))
		l_2 = self.Gridposhor1
		while (not l_2.Tail.IsEmpty):
			l_2 = l_2.Tail
		l_2.Tail = self.Gridposhor1

		while (not l.Tail.IsEmpty):
			l = l.Tail
		l.Tail = self.Gridposvert1

		self.delete_pos = False
	
	def key_event(self, event):
		if event.key == pygame.K_w:
			l = self.Gridposvert1
			while(l.Tail.Value != self.Gridposvert1.Value):
				l = l.Tail
			self.Gridposvert1 = l
		if event.key == pygame.K_s:
			self.Gridposvert1 = self.Gridposvert1.Tail
		if event.key == pygame.K_a:
			self.Gridposhor1 = self.Gridposhor1.Tail
		if event.key == pygame.K_d:
			l_2 = self.Gridposhor1
			self.delete_pos = True
			while(l_2.Tail.Value != self.Gridposhor1.Value):
				l_2 = l_2.Tail
			self.Gridposhor1 = l_2

	def update(self):
		"""
		keys = pygame.key.get_pressed()

		if keys[pygame.K_w] and not self.IsWDown:
			self.IsWDown = True
			l = self.Gridposvert1
			while(l.Tail.Value != self.Gridposvert1.Value):
				l = l.Tail
			self.Gridposvert1 = l
		else:
			if not keys[pygame.K_w]:
				self.IsWDown = False



		if keys[pygame.K_s] and not self.IsSDown:
			self.Gridposvert1 = self.Gridposvert1.Tail
			self.IsSDown = True

		else:
			if not keys[pygame.K_s]:
				self.IsSDown = False
	
		if keys[pygame.K_d] and not self.IsDDown:
			self.IsDDown = True
			l_2 = self.Gridposhor1
			self.delete_pos = True
			while(l_2.Tail.Value != self.Gridposhor1.Value):
				l_2 = l_2.Tail
			self.Gridposhor1 = l_2
		else:
			if not keys[pygame.K_d]:
				self.IsDDown = False

		if keys[pygame.K_a] and not self.IsADown:
			self.Gridposhor1 = self.Gridposhor1.Tail
			self.IsADown = True
			if self.Gridposhor1.Value == playerdraw((self.Game.width / 3) + ((self.Game.width / 3) / 6), 
								 (self.Game.height / 1.05), (self.Game.width * 0.025)):
				self.delete_pos - False
			else:
				if not keys[pygame.K_d]:
					self.IsADown = False
"""
		pass

	def draw(self, screen):
		if not self.delete_pos:
			self.Gridposvert1.Value.draw(screen, (self.Gridposvert1.Value), (self.Gridposvert1.Value), (self.Gridposvert1.Value))
		else:
			self.Gridposhor1.Value.draw(screen, (self.Gridposhor1.Value), (self.Gridposhor1.Value), (self.Gridposhor1.Value))

class playerdraw:
	def __init__(self, positionx, positiony, radius):
		self.Positionx = positionx
		self.Positiony = positiony
		self.Radius = radius
	def draw(self, screen, positionx, positiony, radius):
		pygame.draw.circle(screen, black, (int(self.Positionx), int(self.Positiony)), int(self.Radius))
'''