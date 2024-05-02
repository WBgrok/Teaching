

sum2 x y = x + y

-- Fizzbuzz
fb n
  | mod n 15 == 0 = "FizzBuzz"
  | mod n 3 == 0 = "Fizz"
  | mod n 5 == 0 = "Buzz"
  | otherwise = show n

l = [1..30]

-- sumList :: [Integral a] => a
sumList hs = foldr (+) 0 hs

sayMe :: (Integral a) => a -> String

sayMe 1 = "One!"
sayMe 2 = "Two!"
sayMe 3 = "Three!"
sayMe 4 = "Four!"
sayMe 5 = "Five!"
sayMe x = "Not between 1 and 5"
