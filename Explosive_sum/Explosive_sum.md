 Esplosive sum

How many ways can you make the sum of a number?
In number theory and combinatorics, a partition of a positive integer n,
also called integer partition, is a way of writing n as a sum of positive integers.
Two sums that differ only in the *order ot their summands* are considered the same 
partition. If order matters, the sum becomes the **composition**. For examle, 4 can be 
partitioned in five distinct ways:
 
```
4 
3 + 1
2 + 2
2 + 1 + 1
1 + 1 + 1 + 1
```

## Algorithm:
1. Recursively calculate partion of an integer **n** as: <br>
```
partions(n - 1)
```
2. Eliminate all repeat
