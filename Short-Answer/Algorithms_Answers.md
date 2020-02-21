#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)Time Complexity O(n):
The number of operations increases linearly with the input size (n) due to the While loop.


b)Time Complexity O(n log(n))
The outer loop is (n) and the nested loop is (log n) since j *= 2 is processing chunks of elements at a time, making the entire algorithm O(n log(n))


c)Time Complexity O(n) 
It is a recursive function. Each time you make a recursive call has the runtime complexity of n. The base case is O(1) and the recursive case is O(n) since it makes one recursive call, which can all be simplified to O(n)

## Exercise II

                                ============> My approach would be to use Binary search <============

-find the middle floor in the building and drop an egg from there. 

-if the egg breaks then we determine that the bottom half contains floor f and we could go ahead and find the middle floor of the bottom half of the building.

-We continue in the same manner until we find the floor that is one floor lower than floor f at which point the egg doesn't break.

-If the egg doesn't break at the first half of the building, the we do the same with the floors on the higher half until we find floor f.

So since binary search has a runtime complexity of O(log n), i assume this algorithm would have a runtime complexity of O(log n)
