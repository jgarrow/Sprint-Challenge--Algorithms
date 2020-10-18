#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) `O(n^3)` because even though it's a loop, it will keep looping while `a < n^3`. That means that as `n` increases, the number of operations that will be performed will be `n^3`.

b) `O(n^2)` because there are nested loops that keep looping based on a incrementation of 1.

c) `O(n)` because the number of recursive calls has a linear relationship with how many `bunnies` there are. For every bunny, one recursive call is made until we reach 0 `bunnies`

## Exercise II

-   Make a list of integers up to `n` (`floors = [*range(n)]`). This will be our array of floors in the building
-   Recursive binary search
-   Find the middle floor in our list and drop the egg
    -   If it broke, then find the middle floor between the lowest one and the floor we just dropped from
    -   If it didn't break, then find the middle floor between the one we just dropped from and the highest
-   Keep doing that process ^ until we find the two adjacent floors where the higher one breaks the egg and the lower one doesn't

-   Since this is a binary search, the runtime complexity is `O(log n)` because we are cutting the number of possible floors in half each time. We don't need to sort an arry first, so it's not `O(n log n)`

```python
def binary_search(floors, start, end):
    lowest = start
    highest = end
    middle = lowest + ((highest - lowest) // 2)

    # if list is empty, return -1
    if end < 0 or start < 0:
        return -1

    # if we've gotten down to the last 2 possible floors
    if len(floors) == 2:
        if floors[lowest] doesn't break egg and floors[highest] breaks egg:
            return lowest

    elif floors[middle] broke egg:
        highest = middle

    elif floors[middle] didn't break egg:
        lower = middle
```
