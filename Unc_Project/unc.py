
import pygame
from global_variables import gravity

class Unc():
	def __init__(self, screen, position, size):
		# public variables
		self.screen = screen
		self.position = position
		self.size = size

		# private variables
		self.velocity = 0
		self.distance_from_ground = 0
		self.bounciness = 0.6

	def draw(self):

		#draw the shadow of the ball
		if (self.distance_from_ground != 0):
			shadowsize = (80 - (self.distance_from_ground/4))
		else:
			shadowsize = 80
		#shadowsize = 10.0
		pygame.draw.ellipse(self.screen, 
				"#D59D24", 
				pygame.Rect(self.position.x - (shadowsize/2), 425 - (shadowsize/4) + self.size/2, shadowsize, shadowsize/2), 
				self.size) 

		# draw the ball
		pygame.draw.circle(self.screen, "#574344", (self.position.x, self.position.y), self.size)

	def update(self, deltatime):
		self.velocity -= gravity
		self.position.y = self.position.y - self.velocity
		if self.position.y >= 400:
			self.position.y = 400.0
			self.velocity = -self.velocity * self.bounciness
		self.distance_from_ground = 400-self.position.y

	def SetPosition(self, x, y):
		self.velocity = 0
		self.position.x = x
		self.position.y = y