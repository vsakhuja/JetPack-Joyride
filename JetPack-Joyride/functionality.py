import numpy as np
import colorama
from colorama import Fore,Back,Style
import os
import random
from characters import *
from background import *

class render():
	def __init__(self,idx_r,idx_c,size,inp,out):
		self.idx_r=idx_r
		self.idx_c=idx_c
		self.size=size
		self.inp=inp
		self.out=out
	def placement(self):
		for i in range(self.size):
			for j in range(self.size):
				self.out[self.idx_r+i][self.idx_c+j]=self.inp[i][j]





