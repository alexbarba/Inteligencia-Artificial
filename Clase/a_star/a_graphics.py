from graphics import *
from a_star import *


def paint(matriz, inicio, final,bloques):
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
#	
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
	for y in range(len(bloques)):
			square = Rectangle(Point(bloques[y].x, bloques[y].y),Point(bloques[y].x+1, bloques[y].y+1))
			#square = Rectangle(Point(matriz[x][y].x, matriz[x][y].y), Point(matriz[x][y].x + 1, matriz[x][y].y + 1))
			square.draw(win)
			square.setOutline("yellow")
			square.setFill("green")
	print(int(win.getMouse().x)) 
	win.close()
        
def enter(matriz):
    
    win = GraphWin('Floor', 500, 500)
    win.setCoords(0.0, 0.0, len(matriz), len(matriz[0]))
    win.setBackground("white")
    for x in range(len(matriz)):
            for y in range(len(matriz[0])): 
                    square = Rectangle(Point(x,y), Point(x+1,y+1))
                    square = Rectangle(Point(matriz[x][y].x, matriz[x][y].y), Point(matriz[x][y].x + 1, matriz[x][y].y + 1))
                    square.draw(win)
                    square.setOutline("yellow")
                    square.setFill("black")
    print("inicial")
    xy=win.getMouse()
    x=int(xy.x)
    y=int(xy.y)
    square = Rectangle(Point(x,y), Point(x+1,y+1))
    square.draw(win)
    square.setFill("red")
    print("final")
    xy2=win.getMouse()
    x2=int(xy2.x)
    y2=int(xy2.y)
    square = Rectangle(Point(x2,y2), Point(x2+1,y2+1))
    square.draw(win)
    square.setFill("blue")
    win.checkKey()
    
    
    print("cuantos bloques?")
    bloques=int(input())
    block=[]
    for h in range (bloques):
        xyb=win.getMouse()
        xb=int(xyb.x)
        yb=int(xyb.y)
        matriz[xb][yb].wall = True
        matriz[xb][yb].free = False
        square = Rectangle(Point(xb,yb), Point(xb+1,yb+1))
        square.draw(win)
        square.setFill("green")
        block.append(matriz[xb][yb])
    win.getMouse()
    
    return xy, xy2, matriz
    
enter(mapa = [[node(i, j) for j in range(10)] for i in range(10)])
    

