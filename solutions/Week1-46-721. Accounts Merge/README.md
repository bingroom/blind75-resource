# Accounts Merge

**Topic:** Graph
- **LeetCode 連結:** [721. Accounts Merge](https://leetcode.com/problems/accounts-merge/)
- **難度:** Medium

## 題目描述

給定一組帳戶列表，每個帳戶包含一個名稱和若干電子郵件。若兩個帳戶有相同的電子郵件，則它們屬於同一人。將屬於同一人的帳戶合併，回傳合併後的帳戶列表，每個帳戶的郵件需排序。

## 解題思路

1. 使用並查集（Union-Find），為每個電子郵件建立節點。
2. 將同一帳戶中的所有郵件互相合併（union）。
3. 若某郵件出現在不同帳戶中，也將它們合併。
4. 遍歷所有郵件，依其根代表分組。
5. 每組郵件排序後，配上對應的帳戶名稱加入結果。

## 程式碼

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

## 複雜度分析

- **時間複雜度:** O(n * k * alpha(n * k)) where n is the number of accounts and k is the max emails per account. alpha is the inverse Ackermann function (nearly constant).
- **空間複雜度:** O(n * k) -- for the Union-Find structure and email mappings.
