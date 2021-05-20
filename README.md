# ICS3U Algorithms

Your job is going to be to implement the "Selection sort" algorithm.
I am going to list out the instructions, and it will be your job to code it.
You may use online sources, put please put the sources you utilized in your comments.

* You may NOT use the `sorted()` function or the `arr.sort()` method!!
* You may NOT use the `min()` function.

No user input is required, just testing the functions.

## To test your function
1. Go to Console
2. `pip install pytest`
3. `pytest`

## Selection Sort Algorithm
1. Loop through the entire array. We only need the index from this loop.
2. Create a second loop that finds index of the the minimum value of the array from the current loop index to the end of the array (hint: use the range() function to go from 1 to the len(arr)
3. Swap the values of the current position in the outer loop with the position of the min value

Here is the pseudo code
```
FUNCTION selection_sort(array)
    FOR i = 0 To end of array
        smallest = i
        FOR index = i + 1 TO end of array
            IF array item @ index < array item @ smallest
                smallest = index
            END IF
        END FOR
        swap array item @ index with array item @ smallest
    END FOR
RETURN array
```
Code taken from [Intro to Algorithms: Crash Course Computer Science #13](https://youtu.be/rL8X2mlNHPM?t=187)

If you have any questions, please let me know.

