# Accounts Merge

- **LeetCode:** [721. Accounts Merge](https://leetcode.com/problems/accounts-merge/)

## Problem Description

Given a list of accounts where each element `accounts[i]` is a list of strings (the first element is a name, the rest are emails), merge accounts that share at least one common email. Return the merged accounts with emails sorted.

## Approach

Union-Find (Disjoint Set Union):

1. For each account, union all its emails together.
2. If an email was seen in a previous account, also union it with that account's emails (linking the two accounts).
3. After processing all accounts, group emails by their root representative.
4. For each group, attach the account owner's name and sort the emails.

## Complexity

- **Time:** O(n * k * alpha(n * k)) where n is the number of accounts and k is the max emails per account. alpha is the inverse Ackermann function (nearly constant).
- **Space:** O(n * k) -- for the Union-Find structure and email mappings.
