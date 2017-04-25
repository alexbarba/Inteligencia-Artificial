from pystockfish import *  
deep = Engine(depth=20)
deep.setposition(['e2e4'])
print(deep.bestmove())
