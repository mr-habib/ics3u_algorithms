# ICS3U Algorithms

Your job is going to be to implement the "Selection sort" algorithm.
I am going to list out the instructions, and it will be your job to code it.
You may use online sources, put please put the sources you utilized in your comments.

Note, just like the functions assignment, I want you to write a function calld ```selection_sort``` that takes in an array as an argument.
The function should first copy the array (```a_copy = arr.copy()```) and return that list in the end.

No user input is required, just testing the functions.

## Selection Sort Algorithm
1. Loop through the array using the enumerate method... we will need the index too
2. Create a second loop that finds index of the the minimum value of the array from the current loop index to the end of the array
3. Swap those two value

Here is the pseudo code
```
function selection_sort <- arr 
  for i1 goes from 0 to end of arr:
    find min value of arr from i1 to end of list (requires another for loop)
    arr[i1], arr[min] = arr[min], arr[i1]

```

If you have any questions, please let me know.
