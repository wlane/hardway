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
			current_scene = self.scene_map.next_scene(next_scene_name)

class Death(Scene):
	quips = ["You died. You kinda suck at this.","Your mom would be proud...if she were smarter.",
			"Such a luser.","I have a small puppy that's better at this."]

	def enter(self):
		print Death.quips[randint(0, len(self.quips)-1)]
		exit(1)

class CentralCorridor(Scene):
	def enter(self):
		print "The Gothons of Planet Percal #25 have invaded your ship and destroyed."
		print "\n"
		print "Armory and about to pull a weapon to blast you."

		action = raw_input('> ')
		if action == "shoot!":
			print "Quick on the draw you yank out your blaster and fire it at the Gothan."
			return 'death'
		elif action == "dodge!":
			print "Like a world class boxer you dodge, weave, slip and slide right."
			return 'death'
		elif action == "tell a joke":
			print "Lucky for you they made you learn Gothan insults in the academy."
			return 'laser_weapon_armory'
		else:
			print "DOES NOT COMPUTE."
			return 'central_corridor'

class LaserWeaponArmory(Scene):
	def enter(self):
		print "You do a dive roll into the Weapon Armory, crouch and scan the room."
		code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
		guess = raw_input("[keypad]> ")
		guesses = 0

		while guess != code and guesses < 10:
			print "BZZZZEDDDD"
			guesses += 1
			guess = raw_input("[keypad]> ")

		if guess == code:
			print "The container clicks open and the seal breaks,letting gas out."
		else:
			print "The local buzzes one last tine and then you hear a sickening."
			return 'death'

class TheBridge(Scene):
	def enter(self):
		print "You burst onto the Bridge with the netron destruct bomb."
		action = raw_input("> ")
		if action == "throw the bomb":
			print "In a panic you throw the bomb at the group of Gothons."
			return 'death'
		elif action == "slowly place the bomb":
			print "You point your blaster at the bomb under your arm"
			return 'eacape_pod'
		else:
			print "DOES NOT COMPUTE."
			return 'the_bridge'

class EscapePod(Scene):
	def enter(self):
		print "You rush through the ship desperately trying to make it to..."
		good_pod = randint(1,5)
		guess = raw_input("[pod #]> ")

		if int(guess) != good_pod:
			print "You ump into pod %s and hit the eject button." % guess
			return 'death'
		else:
			print "You jump into pod %s and hit the eject button"
			return 'finished.'

class Map(object):
	scenes = {'central_corridor':CentralCorridor(),'laser_weapon_armory':LaserWeaponArmory(),'the_bridge':TheBridge(),'escape_pod':EscapePod(),'death':Death()}
	def __init__(self,start_scene):
		self.start_scene = start_scene
	def next_scene(self,scene_name):
		return Map.scenes.get(scene_name)
	def opening_scene(self):
 		return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
