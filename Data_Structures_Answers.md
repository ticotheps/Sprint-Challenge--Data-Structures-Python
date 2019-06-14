Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?

The runtime complexity for 'append()' is O(1) (constant time) because (while n = the value of the single 'item' that we're adding to the buffer) as n increases, we will only ever perform the same number of operations to add that 'item' each time the append() function is called.

2. What is the space complexity of your ring buffer's `append` function?

The space complexity for 'append()' is also O(1) (constant space)because (while n = the value of the single 'item' that we're adding to the buffer) as n increases, we will only ever have the same amount of space/memory that was originally allocated to the ring buffer when the buffer was instantiated with the 'capacity' parameter.

3. What is the runtime complexity of your ring buffer's `get` method?

The runtime complexity for 'get()' is O(n) (linear time) because (while n = the number of items in the ring buffer) as n increases, our for loop will also increase the number of operations it performs when the get() function is called.

4. What is the space complexity of your ring buffer's `get` method?

The space complexity for 'get()' is O(n) (linear space) because (while n = the number of items in the ring buffer) as n increases, the space/memory required to store the items from our operations must also increase every time the get() function is called.

5. What is the runtime complexity of the provided code in `names.py`?

The runtime complexity for the code in 'names.py' is O(n^2) (quadratic time) because there are 2 'for' loops, one nested inside of the other. In this case, n = the total number of names in the .txt files. So, as n (the number of names) increases, the number of operations that our 2 'for' loops are going to run will also increase every time 'names.py' is executed.

6. What is the space complexity of the provided code in `names.py`?

The space complexity for the code in 'names.py' is also O(n^2) (quadratic space) because there are 2 'for' loops, one nested inside of the other and as n (the number of names) increases, the space/memory required to store those names from our operations must also increase exponentially (to the power of 2) every time 'names.py' is executed.

7. What is the runtime complexity of your optimized code in `names.py`?

I was able to get the runtime complexity for my first iteration to the solution in 'names.py' down to O(n) (linear time) because I decreased the number of 'for' loops to only one.

The runtime complexity of my second iteration to the solution is O(min(len(s),len(t)) (which is similar to O(1) on average) because there was only one 'for' loop used in the built-in .intersection() method and only required the creation/use of ONE set (basically a hash table), without any arrays (compared to the use of two sets and an array in my first iteration).

8. What is the space complexity of your optimized code in `names.py`?

The space complexity for my first iteration to the solution in 'names.py' is O(n) (linear time) because 'for' loops in Python create and destroy objects during each iteration, but my 'for' loop is adding those items into a list that persists through each iteration of the 'for' loop.

The space complexity of my second iteration to the solution is O(n) (on average) because of the hash table data structure behind the set that was created in that solution.
