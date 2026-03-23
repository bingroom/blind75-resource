# Reverse Integer

## Problem Description
Given a signed 32-bit integer `x`, return `x` with its digits reversed. If reversing causes overflow outside the 32-bit signed integer range `[-2^31, 2^31 - 1]`, return 0.

## Approach
Extract digits from the end using modulo, build the reversed number by multiplying by 10 and adding each digit. Handle the sign separately and check for 32-bit overflow at the end.

## Complexity
- **Time:** O(log x) -- number of digits
- **Space:** O(1)
