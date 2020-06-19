#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

```python
a)  a = 0                   O(c)
    while (a < n * n * n):  O(n)
      a = a + n * n         O(n) 
```

Despite there being a couple instances of multiplication occuring, this is a simple while loop that increments a variable an undefined amount. 

If n = 1, then the Big O for this is O(c) or constant time since `a` immediately become `= n` and stop the loop. 

If n > 1 then Big O for this will be O(log) or logarithmic time since `a` will increment exponentially until it's `>= n`

```
b)  sum = 0                 O(c)
    for i in range(n):      O(n)
      j = 1                 O(c)
      while j < n:          O(n)
        j *= 2              makes this loop O(log n)
        sum += 1            O(n)
```

`range(n)` is an O(n) or linear runtime, but due to `j *= 2`, the `while` loop will slowly increase as `n` increases resulting in O(n log n) or Log-Linear

```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```
This is O(n) since it's just a linear subtraction problem. 

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

------------ANSWER-------------------------

Abstractly, there are two ways to approach this problem. If we assume gravity, we can probably start at the first floor and increment up from there since an egg probably won't survive past the 2nd or 3rd floor, making this basically an O(c) or constant time problem. But given what is probably being asked of us, this is the same problem as finding a name in a phone book, regardless of how big the phone book is. So, we'll use a BST to find the answer. 

Given that you know how many n-stories the building is, you can start at the halfway mark. `n // 2`

If the egg breaks, you ignore the floors above and make your search space the floors below. So `top_floor = n // 2` and you check `n // 2` again until you find a floor that the egg doesn't break from. 

If the egg doesn't break, you do the same process, but now ignore the bottom half of the floors so `bottom_floor = n // 2 + 1` continuing your search until found. 