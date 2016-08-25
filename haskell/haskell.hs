import System.Random
import Data.List
 
main = do
    seed  <- newStdGen
    let rs = randomlist 1000000 seed
    writeFile "haskell.txt" ( show (rs) )
 
randomlist :: Int -> StdGen -> [Double]
randomlist n = take n . unfoldr (Just . random)
