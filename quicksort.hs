-- We could get rid of the middle filter statement by making one of the outer filter statements <= or >= respectively,
-- but it's clearer this way, albeit very slightly slower.
quicksort :: (Ord a) => [a] -> [a]
quicksort [] = []
quicksort [x] = [x]
quicksort (x:xs) = (quicksort $ filter (<x) xs) ++ [x] ++ (filter (==x) xs) ++ (quicksort $ filter (>x) xs)
