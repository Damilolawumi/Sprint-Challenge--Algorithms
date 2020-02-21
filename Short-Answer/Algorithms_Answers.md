#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)

a = 0 assignment of a value to a, so we denote a notation of 1.... 0(1)

while(a<n*n*n>) => while loop that will only stop if a exceeds n**3
O(n)

a=a + n*n => assignment of a value to a so we denote a notation of 1

runtime is O(n)

b)


c)

## Exercise II

My approach would be to use Binary search

-find the middle floor in the building and drop an egg from there. 
-if the egg breaks then we determine that the bottom half contains floor f and we could go ahead and find the middle floor of the bottom half of the building. -We continue in the same manner until we find the floor that is one floor lower than floor f at which point the egg doesn't break.
-If the egg doesn't break at the first half of the building, the we do the same with the floors on the higher half until we find floor f.

So since binary search has a runtime complexity of O(log n), i assume this algorithm would have a runtime complexity of O(log n)
