#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

from graphics import *

diagonal = 1.4


class node():
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.G = None #Distancia al origen
		self.H = None #Distancia al destino
		self.children = []
		self.dad = []
		self.interns = False #Interiores. Todos los nodos por los que ya pase
		self.front = False #Fronteras. Todos los nodos que ya vi
		self.route = False #Ruta. Resultado final
		self.free = True #Libres. Los que nunca vi y nunca pase por ellos
		self.wall = False #Bloques.
	
	def set_dad(self, dad):
		self.dad.append(dad)
		
	def get_f(self):
		return self.G + self.H
		
	def get_h(self):
		return self.H
	
	def get_g(self):
		return self.H
		
	def set_g(self, start):
		self.G = abs(self.x - start.x) + abs(self.y - start.y) - min(abs(self.x - start.x), abs(self.y - start.y))*( 2 - diagonal)
				
	def set_h(self, goal):
		self.H = abs(self.x - goal.x) + abs(self.y - goal.y) - min(abs(self.x - goal.x), abs(self.y - goal.y))*( 2 - diagonal)
				
	def set_route(self, value):
		self.route = value
	
	def set_interns(self, value):
		self.interns = value
	
	def set_front(self, value):
		self.front = value
	
	def set_free(self):
		self.free = False
	
	def add_children(self, children):
		self.children.append(children)
		
	def get_children(self):
		return self.children.pop()


def a_star(start, goal, mapa):
	n = len(mapa)
	m = len(mapa[0])
	
	#Mapeamos el modo inicial
	mapa[start.x][start.y].set_route(True)
	mapa[start.x][start.y].set_interns(True)
	mapa[start.x][start.y].set_front(True)
	mapa[start.x][start.y].set_h(goal)
	
	#Hacemos Setters a H y a G
	for i in range(len(mapa)):
		for j in range(len(mapa[0])):
			mapa[i][j].set_g(start)
			mapa[i][j].set_h(goal)
	
	current = mapa[start.x][start.y]
	fronts = []	
	def around(cur):
		for i in range(3):
			for j in range(3):
				#validamos que esté dentro del rango del mapa
				if (n - 1 >= cur.x + i - 1) and (cur.x + i - 1 >= 0) and (m - 1 >= cur.y + j - 1) and (cur.y + j - 1 >= 0):
				#El pixel deja de ser libre
					mapa[cur.x + i - 1][cur.y + j - 1].set_free()
					#Validamos que no hayamos pasado antes por el
					if not(mapa[cur.x + i - 1][cur.y - 1 + j].interns):
						#Validamos que no sea un muro
						if not(mapa[cur.x + i - 1][cur.y - 1 + j].wall):
							#Validamos que no lo haya visto el nodo anterior
							if not(mapa[cur.x + i - 1][cur.y - 1 + j].front):
								mapa[cur.x + i - 1][cur.y - 1 + j].set_front(True) #Lo añadimos a la lista de vistos
								mapa[cur.x + i - 1][cur.y - 1 + j].set_dad(current) #Seteamos su padre
								mapa[cur.x][cur.y].add_children(mapa[cur.x + i - 1][cur.y - 1 + j]) #Al padre le asignamos el hijo
								fronts.append(mapa[cur.x + i - 1][cur.y - 1 + j])
								
		
		
	
	def next_node():		
		if fronts:
			n_cur = min(fronts, key=lambda x: x.get_f())
			fronts.remove(n_cur)
			return n_cur
		else:
			return None
		
	print("X Y  F")
	while (True):
		mapa[current.x][current.y].set_interns(True)
		print(current.x, current.y, current.get_f())
		around(current)
		current = next_node()
		
		
		if current is None:
			print("No hay solucion")
			break
		elif current.x == goal.x and current.y == goal.y:
			break
	
	def map_route(n_cur):
		mapa[n_cur.x][n_cur.y].set_route(True)
		if mapa[n_cur.x][n_cur.y].dad:
			map_route(mapa[n_cur.x][n_cur.y].dad[0])
		else:
			return 0
	
	map_route(mapa[goal.x][goal.y])
	
	
	return mapa





def paint(win, color, x, y):
	colorDeLinea = "yellow"
	square = Rectangle(Point(x,y), Point(x+1,y+1))
	square.draw(win)
	square.setOutline(colorDeLinea)
	square.setFill(color)
	#square.draw(win)
        
def ui_astar():
	n = int(input('Escriba el tamano en x del mapa: '))
	m = int(input("Escriba el tamano en y del mapa: "))
	matriz = [[node(i, j) for j in range(n)] for i in range(m)]
    
	win = GraphWin('A-Star', 500, 500)
	win.setCoords(0.0, 0.0, len(matriz), len(matriz[0]))
	win.setBackground("white")
	for x in range(len(matriz)):
		for y in range(len(matriz[0])): 
			paint(win,"black", x, y)
    
	print("Seleccione el nodo inicial")
	xy=win.getMouse()
	start = node(int(xy.x), int(xy.y))
	paint(win,"white", start.x, start.y)
    
	print("Seleccione el nodo final")
	xy=win.getMouse()
	goal = node(int(xy.x), int(xy.y))
	paint(win,"blue", goal.x, goal.y)
	win.checkKey()
    
	bloques=int(input("Cantidad de bloques que desea: "))
	for h in range(bloques):
		xy=win.getMouse()
		matriz[int(xy.x)][int(xy.y)].wall = True
		matriz[int(xy.x)][int(xy.y)].free = False
		paint(win,"green", int(xy.x), int(xy.y))
	

	matriz = a_star(start, goal, matriz)
    
	for x in range(n):
		for y in range(m):
				if(matriz[x][y].route):
					paint(win, "orange", x, y)
				elif(matriz[x][y].interns):
					paint(win, "purple", x, y)
				elif matriz[x][y].front:
					paint(win, "red", x, y)
	
	paint(win,"white", start.x, start.y)			
	paint(win,"blue", goal.x, goal.y)
	print("Muros: Verdes \nRuta: Naranja \nInternos: Morados \nFronteras: Rojos")
	print(int(win.getMouse().x))
    
    
ui_astar()



