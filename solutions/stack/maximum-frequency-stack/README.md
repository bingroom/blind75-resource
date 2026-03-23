# Maximum Frequency Stack

## Problem Description
Design a stack-like data structure where `push` adds an element and `pop` removes the most frequent element. If there is a tie in frequency, the element closest to the top (most recently pushed) is removed.

## Approach
Maintain two mappings: `freq` maps each value to its current frequency, and `group` maps each frequency level to a stack of values pushed at that frequency. Track `max_freq`. On `push`, increment the value's frequency and append it to `group[new_freq]`. On `pop`, pop from `group[max_freq]`, decrement the value's frequency, and if that group becomes empty, decrement `max_freq`. This works because a value with frequency f appears in groups 1 through f, so decrementing preserves consistency.

## Complexity
- **Time:** O(1) for both push and pop
- **Space:** O(n)
