# Gas Station

## Problem Description
There are n gas stations along a circular route. `gas[i]` is the amount of gas at station i and `cost[i]` is the gas needed to travel from station i to station i+1. Return the starting station index if you can complete the circuit, or -1.

## Approach
First check feasibility: if total gas < total cost, return -1. Otherwise a solution is guaranteed to exist. Greedily track the tank balance. Whenever it drops below 0, the start must be after the current station. Reset the tank and start index.

## Complexity
- **Time:** O(n)
- **Space:** O(1)
