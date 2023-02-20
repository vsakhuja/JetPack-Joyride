import numpy as np
import colorama
from colorama import Fore,Back,Style
import os
import random
from background import *
from characters import *
from player import *

class detect_things():
	def __init__(self,position_x,position_y):
		self._position_y=position_y
		self._position_x=position_x
	def detect_coins(self, obj):
		for i in range(3):
			for j in range(3):
				if inp[self.Position_x()+i][self.Position_y()+j]=='$':
					obj.increase_coin()

	def Position_x(self):
		return self._position_x
	def Position_y(self):
		return self._position_y
	def detect_nitros(self,obj):
		for i in range(3):
			for j in range(3):
				pass
			#	if inp[self.Position_x()+i][self.Position_y()+j]=='N':

	def detect_obstacles(self,obj):
		ft=0
		if ft==0:
			for i in range(5):
				for j in range(5):
					if inp[self.Position_x()+i][self.Position_y()+j]=='/' or inp[self.Position_x()+i][self.Position_y()+j]=='\\' or inp[self.Position_x()+i][self.Position_y()+j] =='|' or inp[self.Position_x()+i][self.Position_y()+j] == '-':
						if obj.shield_flag==0 and ft==0 :
							obj.xcordi=10
							obj.ycordi+=10
							ft=1
		if ft==1:
			tempo=min(row-self.Position_x(),10)
			for i in range(tempo):
				for j in range(10):
					if inp[self.Position_x()+i][self.Position_y()+j]=='/' or inp[self.Position_x()+i][self.Position_y()+j]=='\\' or inp[self.Position_x()+i][self.Position_y()+j] =='|' or inp[self.Position_x()+i][self.Position_y()+j] == '-':
						inp[self.Position_x()+i][self.Position_y()+j]=' '

			tempo2=min(self.Position_x(),10)
			for i in range(tempo2):
					for j in range(10):
						if inp[self.Position_x()+i-10][self.Position_y()+j]=='/' or inp[self.Position_x()+i-10][self.Position_y()+j]=='\\' or inp[self.Position_x()+i-10][self.Position_y()+j] =='|' or inp[self.Position_x()+i-10][self.Position_y()+j] == '-':
							inp[self.Position_x()+i-10][self.Position_y()+j]=' '

			for i in range(tempo):
				for j in range(10):
					if inp[self.Position_x()+i][self.Position_y()+j-10]=='/' or inp[self.Position_x()+i][self.Position_y()+j-10]=='\\' or inp[self.Position_x()+i][self.Position_y()+j-10] =='|' or inp[self.Position_x()+i][self.Position_y()+j-10] == '-':
						inp[self.Position_x()+i][self.Position_y()+j-10]=" "

			for i in range(tempo2):
					for j in range(10):
						if inp[self.Position_x()+i-10][self.Position_y()+j+10]=='/' or inp[self.Position_x()+i-10][self.Position_y()+j+10]=='\\' or inp[self.Position_x()+i-10][self.Position_y()+j+10] =='|' or inp[self.Position_x()+i-10][self.Position_y()+j+10] == '-':
							inp[self.Position_x()+i-10][self.Position_y()+j+10]=' '

			for i in range(tempo):
				for j in range(10):
					if inp[self.Position_x()+i][self.Position_y()+j+10]=='/' or inp[self.Position_x()+i][self.Position_y()+j+10]=='\\' or inp[self.Position_x()+i][self.Position_y()+j+10] =='|' or inp[self.Position_x()+i][self.Position_y()+j+10] == '-':
						inp[self.Position_x()+i][self.Position_y()+j+10]=" "
			for i in range(tempo2):
					for j in range(10):
						if inp[self.Position_x()+i-10][self.Position_y()+j-10]=='/' or inp[self.Position_x()+i-10][self.Position_y()+j-10]=='\\' or inp[self.Position_x()+i-10][self.Position_y()+j-10] =='|' or inp[self.Position_x()+i-10][self.Position_y()+j-10] == '-':
							inp[self.Position_x()+i-10][self.Position_y()+j-10]=' '

			obj.decrease_life()

	def break_obstacles(self,obj):
		l_flag=0
		for i in range(5):
			for j in range(5):
				if inp[self.Position_x()+i][self.Position_y()+j]=='/' or inp[self.Position_x()+i][self.Position_y()+j]=='\\' or inp[self.Position_x()+i][self.Position_y()+j] =='|' or inp[self.Position_x()+i][self.Position_y()+j] == '-':
					if obj.shield_flag==1:
						l_flag=1
		if l_flag==1:
			tempo=min(row-self.Position_x(),10)
			for i in range(tempo):
				for j in range(10):
					if inp[self.Position_x()+i][self.Position_y()+j]=='/' or inp[self.Position_x()+i][self.Position_y()+j]=='\\' or inp[self.Position_x()+i][self.Position_y()+j] =='|' or inp[self.Position_x()+i][self.Position_y()+j] == '-':
						inp[self.Position_x()+i][self.Position_y()+j]=' '

			tempo2=min(self.Position_x(),10)
			for i in range(tempo2):
					for j in range(10):
						if inp[self.Position_x()+i-10][self.Position_y()+j]=='/' or inp[self.Position_x()+i-10][self.Position_y()+j]=='\\' or inp[self.Position_x()+i-10][self.Position_y()+j] =='|' or inp[self.Position_x()+i-10][self.Position_y()+j] == '-':
							inp[self.Position_x()+i-10][self.Position_y()+j]=' '

			for i in range(tempo):
				for j in range(10):
					if inp[self.Position_x()+i][self.Position_y()+j-10]=='/' or inp[self.Position_x()+i][self.Position_y()+j-10]=='\\' or inp[self.Position_x()+i][self.Position_y()+j-10] =='|' or inp[self.Position_x()+i][self.Position_y()+j-10] == '-':
						inp[self.Position_x()+i][self.Position_y()+j-10]=" "

			for i in range(tempo2):
					for j in range(10):
						if inp[self.Position_x()+i-10][self.Position_y()+j+10]=='/' or inp[self.Position_x()+i-10][self.Position_y()+j+10]=='\\' or inp[self.Position_x()+i-10][self.Position_y()+j+10] =='|' or inp[self.Position_x()+i-10][self.Position_y()+j+10] == '-':
							inp[self.Position_x()+i-10][self.Position_y()+j+10]=' '

			for i in range(tempo):
				for j in range(10):
					if inp[self.Position_x()+i][self.Position_y()+j+10]=='/' or inp[self.Position_x()+i][self.Position_y()+j+10]=='\\' or inp[self.Position_x()+i][self.Position_y()+j+10] =='|' or inp[self.Position_x()+i][self.Position_y()+j+10] == '-':
						inp[self.Position_x()+i][self.Position_y()+j+10]=" "
			for i in range(tempo2):
					for j in range(10):
						if inp[self.Position_x()+i-10][self.Position_y()+j-10]=='/' or inp[self.Position_x()+i-10][self.Position_y()+j-10]=='\\' or inp[self.Position_x()+i-10][self.Position_y()+j-10] =='|' or inp[self.Position_x()+i-10][self.Position_y()+j-10] == '-':
							inp[self.Position_x()+i-10][self.Position_y()+j-10]=' '



				
	







