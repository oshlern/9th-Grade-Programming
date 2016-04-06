--main=putStrLn "Yellow!"
sumcb 0 = 0
sumcb n = n^3 + sumcb (n-1)

sumpwr 0 p = 0
sumpwr n p = n^p + sumpwr (n-1) p

len [] = 0
len (x:xs) = 1 + len xs

bigger a b
  | a<b b
  | a=b b
  | a>b a

smallest (x:y:xs) = if len x:y:xs == 1
  then x
  else if len x:y:xs==2
    then biggest x y
    else smallest ((biggest x y):xs)
