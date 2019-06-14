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

The runtime complexity for the code in 'names.py' is O(n^2) (quadratic time) because there are 2 'for' loops, one nested inside of the other. So, in this case, n = the number of names in the .txt files. As n (the number of names) increases, the number of operations that our 'for' loops are going to run will also increase every time 'names.py' is executed.

6. What is the space complexity of the provided code in `names.py`?

7. What is the runtime complexity of your optimized code in `names.py`?

8. What is the space complexity of your optimized code in `names.py`?
