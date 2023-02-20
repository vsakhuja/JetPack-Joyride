class enemy():

	def _init_(self,x_cordinate,y_cordinate):
			
			self.b = [row.rstrip('\n') for row in self.b]
			self.bsx = x_cordinate
			self.life = 20
			self.life+=1
				
		def create_boss(self,boss1,boss2):
			
			for i in range(len(self.x_cordinate)):    	
				for j in range(self.y_cordinate):
					obj_board.matrix[bosx + i][j] = self.b[i][j-row_matrice]
			self.boss1 = boss1
			self.boss2=boss2

		def clear_boss(self,bosx):
		
			for i in range(len(self.b)):    	
				for j in range():
					obj_board.matrix[bosx + i][j] = ' '
		def move_boss(self,posx):
			self.clear_boss(self.bsx)
			self.create_boss(posx)
		# if bull.move_bullet(obj_player.k,0):
			# self.life -= 1