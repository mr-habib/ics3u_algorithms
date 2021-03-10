# ICS3U Algorithms

Your job is going to be to implement the "Selection sort" algorithm.
I am going to list out the instructions, and it will be your job to code it.
You may use online sources, put please put the sources you utilized in your comments.

## You may NOT use the ```sorted()``` function or the ```arr.sort()``` method!!
## You may NOT use the ```min()``` function.

Note, just like the functions assignment, I want you to write a function calld ```selection_sort``` that takes in an array as an argument.
The function should first copy the array (```a_copy = arr.copy()```) and return that list in the end.

No user input is required, just testing the functions.

## Selection Sort Algorithm
1. Loop through the entire array. We only need the index from this loop.
2. Create a second loop that finds index of the the minimum value of the array from the current loop index to the end of the array (hint: use the range() function to go from 1 to the len(arr)
3. Swap the values of the current position in the outer loop with the position of the min value

Here is the pseudo code
```
function selection_sort <- arr
  arr_copy <- arr.copy()
  for i goes from 0 to end of arr_copy:
    find the index of the min value of arr_copy from i to end of list (requires another for loop)
    arr_copy[i], arr_copy[min_index] = arr_copy[min_index], arr_copy[i]

  return arr_copy
```

If you have any questions, please let me know.
