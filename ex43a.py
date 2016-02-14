from sys import exit
from random import randint

class Scene(object):

    def enter(self):
        print "There is paul in this room"
        print "This is our characters: \nPaul \nKevin \nBrighton "
        player_name = raw_input("What Character do you want to choose? ")
        pass


class Engine(object):

    def __init__(self, scene_map):
        pass

    def play(self):
        print ("Now you have entered the room "+player_name )
        choice = raw_input ("Do you want to coninue or retreat? \n")

        if choice == "continue":
            print ("Yah you have made the right choice")
            Death()

        elif choice == "retreat":
            print ("You loser go home and cry because you didn't
            are u talking about the prints ??
        pass

class Death(Scene):

    def enter(self):
        print """You have proceed to the next level in the game
        You are in the middle of a room filled with traps and so watch carefully
        You can either turn back or keep moving.
        You can either walk fast or slow.
        """
        choice = raw_input("What is your choice? "):
            if choice == "fast"
                print "Sorry "+player_name+" you just died a horrible death with no explanation"

            else:
                print ("Now you are at the door")


        pass

class CentralCorridor(Scene):
    print ("You have opened the door and proceeded to the next level"

    def enter(self):
        pass

class LaserWeaponArmory(Scene):

    def enter(self):
        pass

class TheBridge(Scene):

    def enter(self):
        pass

class EscapePod(Scene):

    def enter(self):
        pass


class Map(object):

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
