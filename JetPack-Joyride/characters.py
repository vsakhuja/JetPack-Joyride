import numpy as np
import colorama
from colorama import Fore,Back,Style
import os
from background import *
colorama.init()
class Obstacles:
	def __init__(self,size,temp):
		self._size=int(size)
		self._temp=temp
	def Straight(self):
		for i in range(self.Size()):
			self.Temp()[i][0]='|'
			self.Temp()[i][1]='|'
		return self.Temp()
	def Horizontal(self):
		for i in range(self.Size()):
			self.Temp()[0][i]='-'
			self.Temp()[1][i]='-'
		return self.Temp()
	def Cleaner (self):
		for i in range(self.Size()-1):
			for j in range(self.Size()-1):
				self.Temp()[i][j]=" "
	def Printarr (self):
		for i in range(self.Size()):
			for j in range(self.Size()):
				print(self.Temp()[i][j],end="")
			print()
	def Size(self):
		return self._size
	def Temp(self):
		return self._temp
#here I have used polymorphism
class Slant(Obstacles):
	def __init__(self,size,temp,direction):
		#super().__init__(size,temp)
		self._size=size
		self._temp=temp
		self.direction=direction
	def make_slant(self):
		if self.direction=="left":
			for i in range(self._size):
				for j in range(self._size-1):
					if i==j:
						self._temp[i][j]="\\"
						self._temp[i][j+1]="\\"
		elif self.direction=="right":
			for i in range(self._size):
				for j in range(self._size-1):
					if i==self._size-1-j:
						self._temp[i][j]="/"
						self._temp[i][j+1]="/"
		return self._temp
	def Cleaner (self):
		for i in range(self._size):
			for j in range(self._size):
				self._temp[i][j]=" "

class coins():
	def __init__(self,size,char):
		self._size=size
		self._char=char

	def Size(self):
		return self._size

	def Char(self):
		return self._char
	def make_coin(self,inp_row,inp_col):
		for i in range(self.Size()):
			for j in range(self.Size()):
				if inp[inp_row+i][inp_col+j]==" ":
					inp[inp_row+i][inp_col+j]='$'
				else:
					continue

class bullet():
	jump=4
	life_flag=0
	def __init__(self,xcordinate,ycordinate,symbol):
		self._xcordinate=xcordinate
		self._ycordinate=ycordinate
		self._symbol=symbol

	def Gety(self):
		return self._ycordinate
	def Sety(self,val):
		self._ycordinate = val

	def make_bullet(self):
		inp[self.Xcordinate()+1][self.Ycordinate()+1]=self.Symbol()
	def Xcordinate(self):
		return self._xcordinate
	def Ycordinate(self):
		return self._ycordinate
	def Symbol(self):
		return self._symbol
	def clear_bullet(self):
		if inp[self.Xcordinate()][self.Ycordinate()]=='$':
			inp[self.Xcordinate()][self.Ycordinate()]=='$'
		else:
			inp[self.Xcordinate()][self.Ycordinate()]=" "

	def move_bullet(self):
		if inp[self.Xcordinate()][self.Ycordinate()+self.jump]=='$':
			inp[self.Xcordinate()][self.Ycordinate()+self.jump]="$"
		else:
			inp[self.Xcordinate()][self.Ycordinate()+self.jump]=self.Symbol()

	def destroy(self):

		tempo=min(row-self.Xcordinate(),10)

		for i in range(tempo):
			for j in range(10):
				if inp[self.Xcordinate()+i][self.Ycordinate()+j]=='/' or inp[self.Xcordinate()+i][self.Ycordinate()+j]=='\\' or inp[self.Xcordinate()+i][self.Ycordinate()+j] =='|' or inp[self.Xcordinate()+i][self.Ycordinate()+j] == '-':
					inp[self.Xcordinate()+i][self.Ycordinate()+j]=' '
					self.life_flag=1

		tempo2=min(self.Xcordinate()-5,10)

		for i in range(tempo2):
				for j in range(10):
					if inp[self.Xcordinate()+i-10][self.Ycordinate()+j]=='/' or inp[self.Xcordinate()+i-10][self.Ycordinate()+j]=='\\' or inp[self.Xcordinate()+i-10][self.Ycordinate()+j] =='|' or inp[self.Xcordinate()+i-10][self.Ycordinate()+j] == '-':
						inp[self.Xcordinate()+i-10][self.Ycordinate()+j]=' '
						self.life_flag=1

		for i in range(tempo):
			for j in range(10):
				if inp[self.Xcordinate()+i][self.Ycordinate()+j-10]=='/' or inp[self.Xcordinate()+i][self.Ycordinate()+j-10]=='\\' or inp[self.Xcordinate()+i][self.Ycordinate()+j-10] =='|' or inp[self.Xcordinate()+i][self.Ycordinate()+j-10] == '-':
					inp[self.Xcordinate()+i][self.Ycordinate()+j-10]=" "
					self.life_flag=1

		for i in range(tempo2):
				for j in range(10):
					if inp[self.Xcordinate()+i-10][self.Ycordinate()+j+10]=='/' or inp[self.Xcordinate()+i-10][self.Ycordinate()+j+10]=='\\' or inp[self.Xcordinate()+i-10][self.Ycordinate()+j+10] =='|' or inp[self.Xcordinate()+i-10][self.Ycordinate()+j+10] == '-':
						inp[self.Xcordinate()+i-10][self.Ycordinate()+j+10]=' '
						self.life_flag=1

		for i in range(tempo):
			for j in range(10):
				if inp[self.Xcordinate()+i][self.Ycordinate()+j+10]=='/' or inp[self.Xcordinate()+i][self.Ycordinate()+j+10]=='\\' or inp[self.Xcordinate()+i][self.Ycordinate()+j+10] =='|' or inp[self.Xcordinate()+i][self.Ycordinate()+j+10] == '-':
					inp[self.Xcordinate()+i][self.Ycordinate()+j+10]=" "
					self.life_flag=1

		for i in range(tempo2):
				for j in range(10):
					if inp[self.Xcordinate()+i-10][self.Ycordinate()+j-10]=='/' or inp[self.Xcordinate()+i-10][self.Ycordinate()+j-10]=='\\' or inp[self.Xcordinate()+i-10][self.Ycordinate()+j-10] =='|' or inp[self.Xcordinate()+i-10][self.Ycordinate()+j-10] == '-':
						inp[self.Xcordinate()+i-10][self.Ycordinate()+j-10]=' '
						self.life_flag=1


	def destroy_inpath(self):
		for i in range(self.jump):
			if inp[self.Xcordinate()][self.Ycordinate()+i]=='\\' or inp[self.Xcordinate()][self.Ycordinate()+i]=='/' or inp[self.Xcordinate()][self.Ycordinate()+i]=='|' or inp[self.Xcordinate()][self.Ycordinate()+i]=='-':
				self.destroy()













