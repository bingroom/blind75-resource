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
