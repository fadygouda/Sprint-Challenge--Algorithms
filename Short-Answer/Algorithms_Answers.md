#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) This should be O(n) operation as there is only one while loop which indicates that the number of operations are linear compared to the input size.


b) This is an O(n^2) operation, you have a nested while loop in a for loop which makes the operations grow exponentially as the input size increases


c) This is O(2^n), i initially thought it was log(n) but after noticing that this functions will grow based on the input size (number of bunnies), so the functions has to be based on input size which makes it 2^n

## Exercise II


this could be solved O(n) but i think if you use the midpoint, you can split the function into two to give you a better start. if you start at the midpoint and the egg breaks, i would then start on the midpoint of the floor i was on and the bottom floor to see if it will break. if it doesn't, then i would use the midpoint from where i was initially and the top floor and check to see if it breaks and loop until i find the floor less than f. this would make it O(log(n))


