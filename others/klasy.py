import pathlib
import os, stat
import shutil
from tkinter import *
from datetime import datetime

class Hero:
    def __init__(self, nick, type, level, stat, weapon):
        self.nick = nick
        self.type = type
        self.level = level
        self.stat = stat
        self.weapon = weapon
        print(f"{nick}")
        print(f"{type} {level}, {stat}, {weapon}")

p1 = Hero("Hagar", "Warrior", 2, "Strength", "Sword")
p2 = Hero("Dib", "Rogue", 5, "Agility", "Dagger")
p3 = Hero("Tanis", "Mage", 3, "Intellect", "Staff")

class NewLine:
    def __init__(self):
        self.log_file.write