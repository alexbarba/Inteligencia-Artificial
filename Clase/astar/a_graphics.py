from graphics import *

def paint(matriz, inicio, final):
	win = GraphWin('Floor', 500, 500)

	win.setCoords(0.0, 0.0, len(matriz), len(matriz))
	win.setBackground("white")
    

    
    
    #pinta un grid inicial
	for x in range(len(matriz)):
		for y in range(len(matriz[0])):
			square = Rectangle(Point(x,y), Point(x+1,y+1))
			square = Rectangle(Point(matriz[x][y].x, matriz[x][y].y), Point(matriz[x][y].x + 1, matriz[x][y].y + 1))
			square.draw(win)
			square.setOutline("yellow")
			square.setFill("black")
						
			if (matriz[x][y].wall):
				square.setFill("green")
			elif(matriz[x][y].route):
				square.setFill("orange")
			elif(matriz[x][y].interns):
				square.setFill("purple")
			elif matriz[x][y].front:
				square.setFill("red")
	
	#pinta el punto inicial
	square = Rectangle(Point(inicio.x,inicio.y), Point(inicio.x+1,inicio.y+1))
	square.draw(win)
	square.setOutline("yellow")
	square.setFill("white")
    #pinta el punto final
	square = Rectangle(Point(final.x,final.y), Point(final.x+1,final.y+1))
	square.draw(win)
	square.setOutline("yellow")
	square.setFill("blue")
    #pinta los bloques
    
	win.getMouse()
	win.close()

