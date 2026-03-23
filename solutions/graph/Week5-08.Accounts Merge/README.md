# Accounts Merge

- **LeetCode:** [721. Accounts Merge](https://leetcode.com/problems/accounts-merge/)

## Problem Description

Given a list of accounts where each element `accounts[i]` is a list of strings (the first element is a name, the rest are emails), merge accounts that share at least one common email. Return the merged accounts with emails sorted.


## Solution

```python
# LeetCode 721. Accounts Merge
# Time: O(n * k * alpha(n*k))  Space: O(n * k)
# Union-Find approach

from typing import List
from collections import defaultdict


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        rank = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if rank[ra] < rank[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            if rank[ra] == rank[rb]:
                rank[ra] += 1

        # Map each email to the account index where it first appears
        email_to_id = {}
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email not in parent:
                    parent[email] = email
                    rank[email] = 0
                if email in email_to_id:
                    # Union with the first occurrence
                    union(email, accounts[email_to_id[email]][1])
                else:
                    email_to_id[email] = i
                # Union all emails in the same account
                union(email, account[1])

        # Group emails by their root representative
        groups = defaultdict(list)
        for email in parent:
            groups[find(email)].append(email)

        # Build result: attach the owner name from the first account that had the root email
        result = []
        for root, emails in groups.items():
            name = accounts[email_to_id[root]][0]
            result.append([name] + sorted(emails))

        return result
```

## Approach

Union-Find (Disjoint Set Union):

1. For each account, union all its emails together.
2. If an email was seen in a previous account, also union it with that account's emails (linking the two accounts).
3. After processing all accounts, group emails by their root representative.
4. For each group, attach the account owner's name and sort the emails.

## Complexity

- **Time:** O(n * k * alpha(n * k)) where n is the number of accounts and k is the max emails per account. alpha is the inverse Ackermann function (nearly constant).
- **Space:** O(n * k) -- for the Union-Find structure and email mappings.
