from sys import exit
from random import randint

class Scene(object):
	def enter(self):
		print "This scene is not yet configured. Subclass it and implement enter()."
			exit(1)

class Engine(object):
	def __init__(self,scene_map):
		self.scene_map = scene_map
	def play(self):
		current_scene = self.scene_map.opening_scene()

		while True:
			print "\n------"
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_map)

class Death(Scene):
	quips = ["You died. You kinda suck at this.","Your mom would be proud...if she were smarter.",
			"Such a luser.","I have a small puppy that's better at this."]

	def enter(self):
		print Death.quips[randint(0, len(self.quips)-1)]
		exit(1)

class CentralCorridor(Scene):
	print "The Gothons of Planet Percal #25 have invaded your ship and destroyed."
	print "\n"
	print "Armory and about to pull a weapon to blast you."

	action = raw_input('> ')
	if action == "shoot!":
		print "Quick on the draw you yank out your blaster and fire it at the Gothan."
		return 'death.'
	elif action == "dodge!":
		print "Like a world class boxer you dodge, weave, slip and slide right."
		return 'death.'
	elif action == "tell a joke":
		print "Lucky for you they made you learn Gothan insults in the academy."
		return 'laser_weapon_armory'
	else:
		print "DOES NOT COMPUTE."
		return 'central_corridor'



