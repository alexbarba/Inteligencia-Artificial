#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from a_graphics import paint

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
		#dad = node(-1, -1)
	
	def set_dad(self, dad):
		self.dad.append(dad)
		
	def get_f(self):
		return self.G + self.H
		
	def get_h(self):
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


def a_star(start, goal, n_blocks, n, m):
	#Creamos todos los nodos del mapa
	mapa = [[node(i, j) for j in range(n)] for i in range(m)]
	
	#Mapeamos el modo inicial
	mapa[start.x][start.y].set_route(True)
	mapa[start.x][start.y].set_interns(True)
	mapa[start.x][start.y].set_front(True)
	mapa[start.x][start.y].set_h(goal)
	
	#Mapeamos todos los bloques
	for i in n_blocks:
			mapa[i.x][i.y].wall = True
			mapa[i.x][i.y].set_free()
	
	#Hacemos Setters a H y a G
	for i in range(len(mapa)):
		for j in range(len(mapa[0])):
			mapa[i][j].set_g(start)
			mapa[i][j].set_h(goal)
	
	current = mapa[start.x][start.y]
	
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
								
								
									
		#Se ordenan por prioridad de acuerdo al valor de f
		mapa[cur.x][cur.y].children.sort(key=lambda x: x.get_f(), reverse=True)
		
		
		
	def next_node(n_cur):
		#Validamos que tenga hijo
		if mapa[n_cur.x][n_cur.y].children:
			n_cur = mapa[n_cur.x][n_cur.y].get_children()
			
		#Si no tiene hijo, vemos que tenga padre
		elif mapa[n_cur.x][n_cur.y].dad:
			n_cur = next_node(mapa[n_cur.x][n_cur.y].dad[0])
			
		#Si no le quedan hijos y no tiene padre, no hay solución
		elif mapa[n_cur.x][n_cur.y].dad and mapa[n_cur.x][n_cur.y].dad[0].children:
			n_cur = mapa[n_cur.x][n_cur.y].dad[0].get_children()
			
		else:
			return None
			
		return n_cur
		
	while (True):
		mapa[current.x][current.y].set_interns(True)
		around(current)
		current = next_node(current)
		
		if current is None:
			print("No hay solucion")
			break
		elif current.x == goal.x and current.y == goal.y:
			break
	
	def map_route(n_cur):
		mapa[n_cur.x][n_cur.y].set_route(True)
		
		if mapa[n_cur.x][n_cur.y].dad:
			#print("Mi papa es:", mapa[n_cur.x][n_cur.y].dad[0].x, mapa[n_cur.x][n_cur.y].dad[0].y)
			map_route(mapa[n_cur.x][n_cur.y].dad[0])
		else:
			return 0
	
	map_route(mapa[goal.x][goal.y])
	
	
	return mapa




inicial = node(2,2)
meta = node(8,8)
bloques = []
bloques.append(node(5,0))
#bloques.append(node(5,1))
bloques.append(node(5,2))
bloques.append(node(5,3))
bloques.append(node(5,4))
bloques.append(node(5,5))
bloques.append(node(5,6))
bloques.append(node(5,7))
bloques.append(node(5,8))
bloques.append(node(5,9))


mapa = a_star(inicial, meta, bloques, 10, 10)

paint(mapa, inicial, meta)
