len :: [a] -> Int
len [] = 0
len (x:xs) = 1 + len xs

merge :: (Ord a) => [a] -> [a] -> [a]
merge [] [] = []
merge (x:xs) [] = [x] ++ merge xs []
merge [] (y:ys) = [y] ++ merge [] ys
merge (x:xs) (y:ys) = if x<y then [x] ++ merge xs (y:ys)
                      else [y] ++ merge (x:xs) ys

mergesort :: (Ord a) => [a] -> [a]
mergesort [] = []
mergesort [x] = [x]
mergesort ls = let length = len ls
                   half = length `div` 2
                   left = [ ls!!x | x <- [0..half-1] ]
                   right = [ ls!!x | x <- [half..length-1] ]
               in merge (mergesort left) (mergesort right)
