# OS---Memory-Allocation-Algorithms
Contains Best Fit, Worst Fit and Worst Fit Memory Allocation Algorithms

BEST FIT

The best fit deals with allocating the smallest free partition which meets the requirement of the requesting process. This algorithm first searches the entire list of free partitions and considers the smallest hole that is adequate. It then tries to find a hole which is close to actual process size needed.

WORST FIT

Worst Fit allocates a process to the partition which is largest sufficient among the freely available partitions available in the main memory. If a large process comes at a later stage, then memory will not have space to accommodate it.

FIRST FIT

First Fit Algorithm is the simplest technique of allocating the memory block to the processes amongst all. In this algorithm, the pointer keeps track of all the free blocks in the memory and accepts the request of allocating a memory block to the coming process. After that pointer start searching for the largest first free block for the process and allocate that memory block to the coming process.
