isVowel x = x `elem` ['a','e','i','o','u','A','E','I','O','U']
eliminavocales l = [ r | r <- l,not(isVowel r) ]

perfecto e = e == sum [ x | x <- [1..e-1], e `mod`x == 0] 

serie 0 = 0
serie 1 = 1
serie 2 = 1
serie n = serie (n-1) + 3*serie (n-2)




ultimo l = [if e < ultimo then maximo else e | e <- l, let ultimo = last l, let maximo = maximum l]



