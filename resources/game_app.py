import pygame
pygame.init()
width,height,d = 700,700,0
position = ["a","b","c","d","e","f","g","h"]
turn = ["b","w"]
count = [0 for i in range(8)]
board = [[False for x in range(8)] for y in range(8)]
board[3][3] = "w"
board[4][4] = "w"
board[4][3] = "b"
board[3][4] = "b"
#Board definition	
class BoxesGame():
	#Images and graphics sources
	def initGraphics(self):
		self.normallinev=pygame.image.load("line3.png")
		self.normallineh=pygame.transform.rotate(pygame.image.load("line3.png"), -90)
		self.white = pygame.image.load("w.png")
		self.black = pygame.image.load("b.png")
		self.green = pygame.image.load("green.png")		
	#Class initialization	
	def __init__(self):
		self.screen = pygame.display.set_mode((width,height))
		pygame.display.set_caption("reversi")
		self.clock = pygame.time.Clock()
		self.boardh = [[False for x in range(9)] for y in range(9)]
		self.boardv = [[False for x in range(9)] for y in range(9)]
		self.initGraphics()	
	#Construct Board	
	def drawBoard(self):
		for x in range(9):
			for y in range(9):
				if not self.boardh[y][x]:
					self.screen.blit(self.normallineh, [(x)*59, (y)*66.3])
		for x in range(9):
			for y in range(9):
				if not self.boardv[y][x]:
					self.screen.blit(self.normallinev, [(x)*66.3, (y)*59])			
		#Initial black and white configuration
		self.screen.blit(self.white, [208.9,208.9])
		self.screen.blit(self.black, [275.2,208.9])
		self.screen.blit(self.white, [275.2,275.2])
		self.screen.blit(self.black, [208.9,275.2])
		myfont = pygame.font.SysFont(None, 32)	
		label = myfont.render( "Black's "+"Turn",1,(0,0,0))
		self.screen.blit(label,(0,550))
		#self.screen.fill((51,102,0),(64*(a)+11,64*(i)+11,64*(a)+20,64*(i)+20))
	def surround_check(self,a,b):
		global board,d,count
		t = 0
		count = [0 for i in range(8)]
		self.screen.fill((51,102,0),(0,550,400,700))
		if b<8 and a<8:
			p = 1		
			if board[b][a] == False:
				#Up
				w = b-1
				if w>0:
					while w>=0:
						if w>7 or w<0:
							break
						if board[w][a] == turn[1-d] and w!=0:
							count[0] += 1
							w -= 1
						elif board[w][a] == turn[d] and count[0]!=0:
							t = 1		
							break
						else:
							count[0] = 0
							break
				if t!=1:
					count[0] = 0						
				#Down
				t = 0
				w = b+1
				if w<7:			
					while w<8:
						if w>7 or w<0:
							break
						if board[w][a] == turn[1-d] and w!=7:
							count[1] += 1
							w += 1
						elif board[w][a] == turn[d] and count[1]!=0:
							t = 1
							break
						else:
							count[1] = 0
							break
				if t!=1:
					count[1] = 0					
				#Left
				t = 0
				w = a-1
				if w>0:			
					while w>=0:
						if w>7 or w<0:
							break
						if board[b][w] == turn[1-d] and w!=0:
							count[2] += 1
							w -= 1
						elif board[b][w] == turn[d] and count[2]!=0:
							t = 1
							break
						else:
							count[2] = 0
							break
				if t!=1:
					count[2] = 0					
				#Right
				t = 0
				w = a+1
				if w<7:			
					while w<8:
						if w>7 or w<0:
							break
						if board[b][w] == turn[1-d] and w!=7:
							count[3] += 1
							w += 1
						elif board[b][w] == turn[d] and count[3]!=0:
							t = 1 
							break
						else:
							count[3] = 0
							break
				if t!=1:
					count[3] = 0						
				#Left-Upper Diagonal
				w,x,t = a-1,b-1,0
				if w>0 and x>0:
					while w*x >=0:
						if w>7 or w<0 or x>7 or x<0:
							break
						if board[x][w] == turn[1-d] and (x!=0 or w!=0):
							count[4] += 1
							w -= 1
							x -= 1
						elif board[x][w] == turn[d] and count[4]!=0:
							t = 1
							break
						else:
							count[4] = 0
							break
				if t!=1:
					count[4] = 0			
				#Right-Lower Diagonal
				w,x,t = a+1,b+1,0
				if w<7 and x<7:
					while w*x <=49:
						if w>7 or w<0 or x>7 or x<0:
							break
						if board[x][w] == turn[1-d] and (x!=7 or w!=7):
							count[5] += 1
							w += 1
							x += 1
						elif board[x][w] == turn[d] and count[5]!=0:
							t = 1							
							break
						else:
							count[5] = 0
							break
				if t!=1:
					count[5] = 0				
				#Left Lower Diagonal
				w,x,t = a-1,b+1,0
				if w>0 and x<7:
					while w*x >=0:
						if w>7 or w<0 or x>7 or x<0:
							break
						if board[x][w] == turn[1-d] and (w!=0 or x!=7):
							count[6] += 1
							w -= 1
							x += 1
						elif board[x][w] == turn[d] and count[6]!=0:
							t = 1
							break
						else:
							count[6] = 0
							break
				if t!=1:
					count[6] = 0				
				#Right Upper Diagonal
				w,x,t = a+1,b-1,0
				if w<7 and x>0:
					while w*x >=0:
						if w>7 or w<0 or x>7 or x<0:
							break
						if board[x][w] == turn[1-d] and (w!=7 or x!=0):
							count[7] += 1
							w += 1
							x -= 1
						elif board[x][w] == turn[d] and count[7]!=0:
							t = 1
							break
						else:
							count[7] = 0
							break
				if t!=1:
					count[7] = 0			
		return sum(count)	
	def change_color(self,a,b):
		global count,d,turn
		#UP
		if count[0] >0:
			for i in range(b-count[0],b+1):
				board[i][a] = turn[d]
				self.screen.blit(pygame.image.load("green.png"),[66.3*(a)+10,66.3*(i)+10])
				self.screen.blit(pygame.image.load(turn[d]+".png"),[66.3*(a)+10,66.3*(i)+10])
				pygame.display.flip()
		#DOWN
		if count[1]>0:
			for i in range(b,b+1+count[1]):
				board[i][a] = turn[d]
				self.screen.blit(pygame.image.load("green.png"),[66.3*(a)+10,66.3*(i)+10])
				self.screen.blit(pygame.image.load(turn[d]+".png"),[66.3*(a)+10,66.3*(i)+10])
				pygame.display.flip()
		#LEFT
		if count[2]>0:
			for i in range(a-count[2],a+1):
				board[b][i] = turn[d]
				self.screen.blit(pygame.image.load("green.png"),[66.3*(i)+10,66.3*(b)+10])
				self.screen.blit(pygame.image.load(turn[d]+".png"),[66.3*(i)+10,66.3*(b)+10])
				pygame.display.flip()
		#RIGHT
		if count[3]>0:
			for i in range(a,a+1+count[3]):
				board[b][i] = turn[d]
				self.screen.blit(pygame.image.load("green.png"),[66.3*(i)+10,66.3*(b)+10])
				self.screen.blit(pygame.image.load(turn[d]+".png"),[66.3*(i)+10,66.3*(b)+10])
				pygame.display.flip()
		#LUD
		if count[4]>0:
			i,j,k = a-count[4],b-count[4],0
			while k<=count[4]:
				board[j][i] = turn[d]
				self.screen.blit(pygame.image.load("green.png"),[66.3*(i)+10,66.3*(j)+10])
				self.screen.blit(pygame.image.load(turn[d]+".png"),[66.3*(i)+10,66.3*(j)+10])
				pygame.display.flip()
				i +=1 
				j += 1
				k += 1
		#RLD
		if count[5]>0:
			i,j,k = a,b,0
			while k<=count[5]:
				board[j][i] = turn[d]
				self.screen.blit(pygame.image.load("green.png"),[66.3*(i)+10,66.3*(j)+10])
				self.screen.blit(pygame.image.load(turn[d]+".png"),[66.3*(i)+10,66.3*(j)+10])
				pygame.display.flip()
				i +=1 
				j += 1
				k += 1
		#LLD
		if count[6]>0:
			i,j,k = a-count[6],b+count[6],0
			while k<=count[6]:
				board[j][i] = turn[d]
				self.screen.blit(pygame.image.load("green.png"),[66.3*(i)+10,66.3*(j)+10])
				self.screen.blit(pygame.image.load(turn[d]+".png"),[66.3*(i)+10,66.3*(j)+10])
				pygame.display.flip()
				i +=1 
				j -= 1
				k += 1
		#RUD
		if count[7]>0:
			i,j,k = a+count[7],b-count[7],0
			while k<=count[7]:
				board[j][i] = turn[d]
				self.screen.blit(pygame.image.load("green.png"),[66.3*(i)+10,66.3*(j)+10])
				self.screen.blit(pygame.image.load(turn[d]+".png"),[66.3*(i)+10,66.3*(j)+10])
				pygame.display.flip()
				i -=1 
				j += 1
				k += 1
		d = 1-d
		count = [0 for i in range(8)]		 		
	def check_zero_moves(self):
		global initial,board,d,count
		a = d
		c = 0
		initial = board
		for i in range(8):
			for j in range(8):
				board = initial
				d = a
				count = [0 for k in range(8)]						 		
				if board[j][i] == False:
					if self.surround_check(i,j) != 0:
						c += 1
						break
		if c == 0:
			return 0
		else:
			return 1
		board = initial
		d = a
		count = [0 for i in range(8)]
	def game_finish(self):
		global d
		c = 0
		if self.check_zero_moves() == 0:
			d = 1-d
			if self.check_zero_moves() == 0:
				d = 1-d
				return True
			else:
				return False
		else:
			return False	
	
	def winner(self):
		global board
		count_w,count_b = 0,0
		for item in board:
			count_w += item.count("w")
			count_b += item.count("b")	
		if count_w>count_b:
			print "White Wins" + str(count_w)+" : "+str(count_b)
		elif count_b>count_w:
			print "Black Wins" + str(count_b)+" : "+str(count_w)	
		else:
			print "Draw" + str(count_w)+" : "+str(count_b)
	
	def game_history(self,a,b):
		global position
		print turn[1-d]+" "+position[a]+str(b+1)																																																																						
	def gameBoard(self):
		#sleep to make the game 60 fps
		self.clock.tick(60) 
		#clear the screen
		self.screen.fill((51,102,0))
		self.drawBoard()																																										
	def label_print(self):
		self.screen.fill((51,102,0),(0,550,400,700))
		myfont = pygame.font.SysFont(None, 32)
		if d == 1:				
			label = myfont.render( "White's "+"Turn",1,(255,255,255))
			self.screen.blit(label,(0,550))
		else:
			label = myfont.render( "Black's "+"Turn",1,(0,0,0))
			self.screen.blit(label,(0,550))	
	def update(self):
		global d
		clock = pygame.time.Clock()			
		for event in pygame.event.get():
			#quit if the quit button was pressed
			if event.type == pygame.QUIT:	
				exit()
			#elif self.game_finish() == True:
			#	self.winner()
			else:		
				if pygame.mouse.get_pressed()[0]:
					self.x = int(pygame.mouse.get_pos()[0]/67)
					self.y = int(pygame.mouse.get_pos()[1]/68.3)
					if self.x<8 and self.y<8 and self.surround_check(self.x,self.y) > 0 and self.check_zero_moves()>0:
						self.surround_check(self.x,self.y)					
						self.change_color(self.x,self.y)
						self.game_history(self.x,self.y)
						if not self.check_zero_moves():
							d = 1-d
							if not self.check_zero_moves():
								self.winner()
						self.label_print()			
						pygame.display.update()
						clock.tick(30)
						break
					elif self.x<8 and self.y<8 and self.surround_check(self.x,self.y) == 0 and self.check_zero_moves()>0:
						self.label_print()			
						pygame.display.update()
						clock.tick(30)
						break				
			pygame.display.flip()
bg=BoxesGame()
bg.gameBoard()
while 1:
	bg.update()
