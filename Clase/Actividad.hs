myButLast x = x !! (length x - 2)

elementAt l i = l !! (i-1)

isPalindrome l = l == (reverse l)

dupli [] = []
dupli (x:xs) = x:x:dupli xs

split l x = (take x l, drop x l)

rotate l x 
	| x < 0 = drop (length l + x) l ++ take (length l + x) l
	| otherwise = drop x l ++ take x l

range x y = [x..y]

isPrime k = null [ x | x <- [2..k - 1], k `mod`x  == 0]

coprime k y = null [ x | x <- [2..min k y], k `mod`x == 0, y `mod`x == 0]

primesR i j = [x | x <- [min i j..max i j], isPrime x]
