# Grind 169 — Python 解題資源

> 題單來源：[Tech Interview Handbook — Grind 75](https://www.techinterviewhandbook.org/grind75?hours=40&weeks=4)（hours=40, weeks=4）

本資源包含 Grind 169 全部 169 題的 **Python 解法（可提交 AC）**、**解題思路**、**逐步說明**與**時間/空間複雜度分析**，README 全程以**正體中文**撰寫。

---

## 週次分配

依照 Grind 75 網站的排程（40h/週、4 週），共分為 4 週：

| 週次 | 題數 | 難度分布 |
|------|------|----------|
| Week 1 | 58 | Easy 為主，部分 Medium |
| Week 2 | 42 | 全部 Medium |
| Week 3 | 44 | Medium 為主，1 題 Hard |
| Week 4 | 25 | 全部 Hard |

---

## 資料夾結構

```
solutions/
├── Week1-01-1. Two Sum/
│   ├── solution.py       # LeetCode 可直接提交的 Python 程式碼
│   ├── README.md         # 題目描述、解題思路、複雜度（正體中文）
│   └── AC_result.json    # 提交結果（runtime / memory percentile）
├── Week1-02-20. Valid Parentheses/
│   └── ...
├── ...
├── Week4-25-632. Smallest Range Covering Elements from K Lists/
└── Extra.*/              # 5 題原 Blind 75 額外題
```

資料夾命名格式：`Week{週}-{週內序號}-{LeetCode題號}. {題目名稱}`

---

## 題目清單

### Week 1（58 題）

| # | 題目 | 難度 | Topic |
|---|------|------|-------|
| 1 | [Two Sum](solutions/Week1-01-1.%20Two%20Sum/README.md) | Easy | Array |
| 2 | [Valid Parentheses](solutions/Week1-02-20.%20Valid%20Parentheses/README.md) | Easy | Stack |
| 3 | [Merge Two Sorted Lists](solutions/Week1-03-21.%20Merge%20Two%20Sorted%20Lists/README.md) | Easy | Linked List |
| 4 | [Best Time to Buy and Sell Stock](solutions/Week1-04-121.%20Best%20Time%20to%20Buy%20and%20Sell%20Stock/README.md) | Easy | Array |
| 5 | [Valid Palindrome](solutions/Week1-05-125.%20Valid%20Palindrome/README.md) | Easy | String |
| 6 | [Invert Binary Tree](solutions/Week1-06-226.%20Invert%20Binary%20Tree/README.md) | Easy | Binary Tree |
| 7 | [Valid Anagram](solutions/Week1-07-242.%20Valid%20Anagram/README.md) | Easy | String |
| 8 | [Binary Search](solutions/Week1-08-704.%20Binary%20Search/README.md) | Easy | Binary Search |
| 9 | [Flood Fill](solutions/Week1-09-733.%20Flood%20Fill/README.md) | Easy | Graph |
| 10 | [Lowest Common Ancestor of a Binary Search Tree](solutions/Week1-10-235.%20Lowest%20Common%20Ancestor%20of%20a%20Binary%20Search%20Tree/README.md) | Easy | Binary Search Tree |
| 11 | [Balanced Binary Tree](solutions/Week1-11-110.%20Balanced%20Binary%20Tree/README.md) | Easy | Binary Tree |
| 12 | [Linked List Cycle](solutions/Week1-12-141.%20Linked%20List%20Cycle/README.md) | Easy | Linked List |
| 13 | [Implement Queue using Stacks](solutions/Week1-13-232.%20Implement%20Queue%20using%20Stacks/README.md) | Easy | Stack |
| 14 | [First Bad Version](solutions/Week1-14-278.%20First%20Bad%20Version/README.md) | Easy | Binary Search |
| 15 | [Ransom Note](solutions/Week1-15-383.%20Ransom%20Note/README.md) | Easy | Hash Table |
| 16 | [Climbing Stairs](solutions/Week1-16-70.%20Climbing%20Stairs/README.md) | Easy | Dynamic Programming |
| 17 | [Longest Palindrome](solutions/Week1-17-409.%20Longest%20Palindrome/README.md) | Easy | String |
| 18 | [Reverse Linked List](solutions/Week1-18-206.%20Reverse%20Linked%20List/README.md) | Easy | Linked List |
| 19 | [Majority Element](solutions/Week1-19-169.%20Majority%20Element/README.md) | Easy | Array |
| 20 | [Add Binary](solutions/Week1-20-67.%20Add%20Binary/README.md) | Easy | Binary |
| 21 | [Diameter of Binary Tree](solutions/Week1-21-543.%20Diameter%20of%20Binary%20Tree/README.md) | Easy | Binary Tree |
| 22 | [Middle of the Linked List](solutions/Week1-22-876.%20Middle%20of%20the%20Linked%20List/README.md) | Easy | Linked List |
| 23 | [Maximum Depth of Binary Tree](solutions/Week1-23-104.%20Maximum%20Depth%20of%20Binary%20Tree/README.md) | Easy | Binary Tree |
| 24 | [Contains Duplicate](solutions/Week1-24-217.%20Contains%20Duplicate/README.md) | Easy | Array |
| 25 | [Meeting Rooms](solutions/Week1-25-252.%20Meeting%20Rooms/README.md) | Easy | Array |
| 26 | [Roman to Integer](solutions/Week1-26-13.%20Roman%20to%20Integer/README.md) | Easy | Math |
| 27 | [Backspace String Compare](solutions/Week1-27-844.%20Backspace%20String%20Compare/README.md) | Easy | Stack |
| 28 | [Counting Bits](solutions/Week1-28-338.%20Counting%20Bits/README.md) | Easy | Binary |
| 29 | [Same Tree](solutions/Week1-29-100.%20Same%20Tree/README.md) | Easy | Binary Tree |
| 30 | [Number of 1 Bits](solutions/Week1-30-191.%20Number%20of%201%20Bits/README.md) | Easy | Binary |
| 31 | [Longest Common Prefix](solutions/Week1-31-14.%20Longest%20Common%20Prefix/README.md) | Easy | String |
| 32 | [Single Number](solutions/Week1-32-136.%20Single%20Number/README.md) | Easy | Binary |
| 33 | [Palindrome Linked List](solutions/Week1-33-234.%20Palindrome%20Linked%20List/README.md) | Easy | Linked List |
| 34 | [Move Zeroes](solutions/Week1-34-283.%20Move%20Zeroes/README.md) | Easy | Array |
| 35 | [Symmetric Tree](solutions/Week1-35-101.%20Symmetric%20Tree/README.md) | Easy | Binary Tree |
| 36 | [Missing Number](solutions/Week1-36-268.%20Missing%20Number/README.md) | Easy | Binary |
| 37 | [Palindrome Number](solutions/Week1-37-9.%20Palindrome%20Number/README.md) | Easy | Math |
| 38 | [Convert Sorted Array to Binary Search Tree](solutions/Week1-38-108.%20Convert%20Sorted%20Array%20to%20Binary%20Search%20Tree/README.md) | Easy | Binary Search Tree |
| 39 | [Reverse Bits](solutions/Week1-39-190.%20Reverse%20Bits/README.md) | Easy | Binary |
| 40 | [Subtree of Another Tree](solutions/Week1-40-572.%20Subtree%20of%20Another%20Tree/README.md) | Easy | Binary Tree |
| 41 | [Squares of a Sorted Array](solutions/Week1-41-977.%20Squares%20of%20a%20Sorted%20Array/README.md) | Easy | Array |
| 42 | [Maximum Subarray](solutions/Week1-42-53.%20Maximum%20Subarray/README.md) | Medium | Dynamic Programming |
| 43 | [Insert Interval](solutions/Week1-43-57.%20Insert%20Interval/README.md) | Medium | Array |
| 44 | [01 Matrix](solutions/Week1-44-542.%2001%20Matrix/README.md) | Medium | Graph |
| 45 | [K Closest Points to Origin](solutions/Week1-45-973.%20K%20Closest%20Points%20to%20Origin/README.md) | Medium | Heap |
| 46 | [Longest Substring Without Repeating Characters](solutions/Week1-46-3.%20Longest%20Substring%20Without%20Repeating%20Characters/README.md) | Medium | String |
| 47 | [3Sum](solutions/Week1-47-15.%203Sum/README.md) | Medium | Array |
| 48 | [Binary Tree Level Order Traversal](solutions/Week1-48-102.%20Binary%20Tree%20Level%20Order%20Traversal/README.md) | Medium | Binary Tree |
| 49 | [Clone Graph](solutions/Week1-49-133.%20Clone%20Graph/README.md) | Medium | Graph |
| 50 | [Evaluate Reverse Polish Notation](solutions/Week1-50-150.%20Evaluate%20Reverse%20Polish%20Notation/README.md) | Medium | Stack |
| 51 | [Course Schedule](solutions/Week1-51-207.%20Course%20Schedule/README.md) | Medium | Graph |
| 52 | [Implement Trie (Prefix Tree)](solutions/Week1-52-208.%20Implement%20Trie%20(Prefix%20Tree)/README.md) | Medium | Trie |
| 53 | [Coin Change](solutions/Week1-53-322.%20Coin%20Change/README.md) | Medium | Dynamic Programming |
| 54 | [Product of Array Except Self](solutions/Week1-54-238.%20Product%20of%20Array%20Except%20Self/README.md) | Medium | Array |
| 55 | [Min Stack](solutions/Week1-55-155.%20Min%20Stack/README.md) | Medium | Stack |
| 56 | [Validate Binary Search Tree](solutions/Week1-56-98.%20Validate%20Binary%20Search%20Tree/README.md) | Medium | Binary Search Tree |
| 57 | [Number of Islands](solutions/Week1-57-200.%20Number%20of%20Islands/README.md) | Medium | Graph |
| 58 | [Rotting Oranges](solutions/Week1-58-994.%20Rotting%20Oranges/README.md) | Medium | Graph |

### Week 2（42 題）

| # | 題目 | 難度 | Topic |
|---|------|------|-------|
| 1 | [Search in Rotated Sorted Array](solutions/Week2-01-33.%20Search%20in%20Rotated%20Sorted%20Array/README.md) | Medium | Binary Search |
| 2 | [Combination Sum](solutions/Week2-02-39.%20Combination%20Sum/README.md) | Medium | Array |
| 3 | [Permutations](solutions/Week2-03-46.%20Permutations/README.md) | Medium | Recursion |
| 4 | [Merge Intervals](solutions/Week2-04-56.%20Merge%20Intervals/README.md) | Medium | Array |
| 5 | [Lowest Common Ancestor of a Binary Tree](solutions/Week2-05-236.%20Lowest%20Common%20Ancestor%20of%20a%20Binary%20Tree/README.md) | Medium | Binary Tree |
| 6 | [Time Based Key-Value Store](solutions/Week2-06-981.%20Time%20Based%20Key-Value%20Store/README.md) | Medium | Binary Search |
| 7 | [Accounts Merge](solutions/Week2-07-721.%20Accounts%20Merge/README.md) | Medium | Graph |
| 8 | [Sort Colors](solutions/Week2-08-75.%20Sort%20Colors/README.md) | Medium | Array |
| 9 | [Word Break](solutions/Week2-09-139.%20Word%20Break/README.md) | Medium | Trie |
| 10 | [Partition Equal Subset Sum](solutions/Week2-10-416.%20Partition%20Equal%20Subset%20Sum/README.md) | Medium | Dynamic Programming |
| 11 | [String to Integer (atoi)](solutions/Week2-11-8.%20String%20to%20Integer%20(atoi)/README.md) | Medium | String |
| 12 | [Spiral Matrix](solutions/Week2-12-54.%20Spiral%20Matrix/README.md) | Medium | Matrix |
| 13 | [Subsets](solutions/Week2-13-78.%20Subsets/README.md) | Medium | Recursion |
| 14 | [Binary Tree Right Side View](solutions/Week2-14-199.%20Binary%20Tree%20Right%20Side%20View/README.md) | Medium | Binary Tree |
| 15 | [Longest Palindromic Substring](solutions/Week2-15-5.%20Longest%20Palindromic%20Substring/README.md) | Medium | String |
| 16 | [Unique Paths](solutions/Week2-16-62.%20Unique%20Paths/README.md) | Medium | Dynamic Programming |
| 17 | [Construct Binary Tree from Preorder and Inorder Traversal](solutions/Week2-17-105.%20Construct%20Binary%20Tree%20from%20Preorder%20and%20Inorder%20Traversal/README.md) | Medium | Binary Tree |
| 18 | [Container With Most Water](solutions/Week2-18-11.%20Container%20With%20Most%20Water/README.md) | Medium | Array |
| 19 | [Letter Combinations of a Phone Number](solutions/Week2-19-17.%20Letter%20Combinations%20of%20a%20Phone%20Number/README.md) | Medium | Recursion |
| 20 | [Word Search](solutions/Week2-20-79.%20Word%20Search/README.md) | Medium | Graph |
| 21 | [Find All Anagrams in a String](solutions/Week2-21-438.%20Find%20All%20Anagrams%20in%20a%20String/README.md) | Medium | String |
| 22 | [Minimum Height Trees](solutions/Week2-22-310.%20Minimum%20Height%20Trees/README.md) | Medium | Graph |
| 23 | [Task Scheduler](solutions/Week2-23-621.%20Task%20Scheduler/README.md) | Medium | Heap |
| 24 | [LRU Cache](solutions/Week2-24-146.%20LRU%20Cache/README.md) | Medium | Linked List |
| 25 | [Kth Smallest Element in a BST](solutions/Week2-25-230.%20Kth%20Smallest%20Element%20in%20a%20BST/README.md) | Medium | Binary Search Tree |
| 26 | [Daily Temperatures](solutions/Week2-26-739.%20Daily%20Temperatures/README.md) | Medium | Stack |
| 27 | [House Robber](solutions/Week2-27-198.%20House%20Robber/README.md) | Medium | Dynamic Programming |
| 28 | [Gas Station](solutions/Week2-28-134.%20Gas%20Station/README.md) | Medium | Array |
| 29 | [Next Permutation](solutions/Week2-29-31.%20Next%20Permutation/README.md) | Medium | Recursion |
| 30 | [Valid Sudoku](solutions/Week2-30-36.%20Valid%20Sudoku/README.md) | Medium | Matrix |
| 31 | [Group Anagrams](solutions/Week2-31-49.%20Group%20Anagrams/README.md) | Medium | String |
| 32 | [Maximum Product Subarray](solutions/Week2-32-152.%20Maximum%20Product%20Subarray/README.md) | Medium | Dynamic Programming |
| 33 | [Design Add and Search Words Data Structure](solutions/Week2-33-211.%20Design%20Add%20and%20Search%20Words%20Data%20Structure/README.md) | Medium | Trie |
| 34 | [Pacific Atlantic Water Flow](solutions/Week2-34-417.%20Pacific%20Atlantic%20Water%20Flow/README.md) | Medium | Graph |
| 35 | [Remove Nth Node From End of List](solutions/Week2-35-19.%20Remove%20Nth%20Node%20From%20End%20of%20List/README.md) | Medium | Linked List |
| 36 | [Shortest Path to Get Food](solutions/Week2-36-1730.%20Shortest%20Path%20to%20Get%20Food/README.md) | Medium | Graph |
| 37 | [Find the Duplicate Number](solutions/Week2-37-287.%20Find%20the%20Duplicate%20Number/README.md) | Medium | Binary |
| 38 | [Top K Frequent Words](solutions/Week2-38-692.%20Top%20K%20Frequent%20Words/README.md) | Medium | Heap |
| 39 | [Longest Increasing Subsequence](solutions/Week2-39-300.%20Longest%20Increasing%20Subsequence/README.md) | Medium | Dynamic Programming |
| 40 | [Graph Valid Tree](solutions/Week2-40-261.%20Graph%20Valid%20Tree/README.md) | Medium | Graph |
| 41 | [Course Schedule II](solutions/Week2-41-210.%20Course%20Schedule%20II/README.md) | Medium | Graph |
| 42 | [Swap Nodes in Pairs](solutions/Week2-42-24.%20Swap%20Nodes%20in%20Pairs/README.md) | Medium | Linked List |

### Week 3（44 題）

| # | 題目 | 難度 | Topic |
|---|------|------|-------|
| 1 | [Path Sum II](solutions/Week3-01-113.%20Path%20Sum%20II/README.md) | Medium | Binary Tree |
| 2 | [Longest Consecutive Sequence](solutions/Week3-02-128.%20Longest%20Consecutive%20Sequence/README.md) | Medium | Array |
| 3 | [Rotate Array](solutions/Week3-03-189.%20Rotate%20Array/README.md) | Medium | Array |
| 4 | [Odd Even Linked List](solutions/Week3-04-328.%20Odd%20Even%20Linked%20List/README.md) | Medium | Linked List |
| 5 | [Decode String](solutions/Week3-05-394.%20Decode%20String/README.md) | Medium | Stack |
| 6 | [Contiguous Array](solutions/Week3-06-525.%20Contiguous%20Array/README.md) | Medium | Array |
| 7 | [Maximum Width of Binary Tree](solutions/Week3-07-662.%20Maximum%20Width%20of%20Binary%20Tree/README.md) | Medium | Binary Tree |
| 8 | [Find K Closest Elements](solutions/Week3-08-658.%20Find%20K%20Closest%20Elements/README.md) | Medium | Heap |
| 9 | [Longest Repeating Character Replacement](solutions/Week3-09-424.%20Longest%20Repeating%20Character%20Replacement/README.md) | Medium | String |
| 10 | [Inorder Successor in BST](solutions/Week3-10-285.%20Inorder%20Successor%20in%20BST/README.md) | Medium | Binary Search Tree |
| 11 | [Jump Game](solutions/Week3-11-55.%20Jump%20Game/README.md) | Medium | Dynamic Programming |
| 12 | [Add Two Numbers](solutions/Week3-12-2.%20Add%20Two%20Numbers/README.md) | Medium | Linked List |
| 13 | [Generate Parentheses](solutions/Week3-13-22.%20Generate%20Parentheses/README.md) | Medium | Recursion |
| 14 | [Sort List](solutions/Week3-14-148.%20Sort%20List/README.md) | Medium | Linked List |
| 15 | [Number of Connected Components in an Undirected Graph](solutions/Week3-15-323.%20Number%20of%20Connected%20Components%20in%20an%20Undirected%20Graph/README.md) | Medium | Graph |
| 16 | [Minimum Knight Moves](solutions/Week3-16-1197.%20Minimum%20Knight%20Moves/README.md) | Medium | Graph |
| 17 | [Subarray Sum Equals K](solutions/Week3-17-560.%20Subarray%20Sum%20Equals%20K/README.md) | Medium | Array |
| 18 | [Asteroid Collision](solutions/Week3-18-735.%20Asteroid%20Collision/README.md) | Medium | Stack |
| 19 | [Random Pick with Weight](solutions/Week3-19-528.%20Random%20Pick%20with%20Weight/README.md) | Medium | Math |
| 20 | [Kth Largest Element in an Array](solutions/Week3-20-215.%20Kth%20Largest%20Element%20in%20an%20Array/README.md) | Medium | Heap |
| 21 | [Maximal Square](solutions/Week3-21-221.%20Maximal%20Square/README.md) | Medium | Dynamic Programming |
| 22 | [Rotate Image](solutions/Week3-22-48.%20Rotate%20Image/README.md) | Medium | Matrix |
| 23 | [Binary Tree Zigzag Level Order Traversal](solutions/Week3-23-103.%20Binary%20Tree%20Zigzag%20Level%20Order%20Traversal/README.md) | Medium | Binary Tree |
| 24 | [Design Hit Counter](solutions/Week3-24-362.%20Design%20Hit%20Counter/README.md) | Medium | Queue |
| 25 | [Path Sum III](solutions/Week3-25-437.%20Path%20Sum%20III/README.md) | Medium | Binary Tree |
| 26 | [Pow(x, n)](solutions/Week3-26-50.%20Pow(x%2C%20n)/README.md) | Medium | Math |
| 27 | [Search a 2D Matrix](solutions/Week3-27-74.%20Search%20a%202D%20Matrix/README.md) | Medium | Binary Search |
| 28 | [Largest Number](solutions/Week3-28-179.%20Largest%20Number/README.md) | Medium | String |
| 29 | [Decode Ways](solutions/Week3-29-91.%20Decode%20Ways/README.md) | Medium | Dynamic Programming |
| 30 | [Meeting Rooms II](solutions/Week3-30-253.%20Meeting%20Rooms%20II/README.md) | Medium | Array |
| 31 | [Reverse Integer](solutions/Week3-31-7.%20Reverse%20Integer/README.md) | Medium | Math |
| 32 | [Set Matrix Zeroes](solutions/Week3-32-73.%20Set%20Matrix%20Zeroes/README.md) | Medium | Matrix |
| 33 | [Reorder List](solutions/Week3-33-143.%20Reorder%20List/README.md) | Medium | Linked List |
| 34 | [Encode and Decode Strings](solutions/Week3-34-271.%20Encode%20and%20Decode%20Strings/README.md) | Medium | String |
| 35 | [Cheapest Flights Within K Stops](solutions/Week3-35-787.%20Cheapest%20Flights%20Within%20K%20Stops/README.md) | Medium | Graph |
| 36 | [All Nodes Distance K in Binary Tree](solutions/Week3-36-863.%20All%20Nodes%20Distance%20K%20in%20Binary%20Tree/README.md) | Medium | Binary Tree |
| 37 | [3Sum Closest](solutions/Week3-37-16.%203Sum%20Closest/README.md) | Medium | Array |
| 38 | [Rotate List](solutions/Week3-38-61.%20Rotate%20List/README.md) | Medium | Linked List |
| 39 | [Find Minimum in Rotated Sorted Array](solutions/Week3-39-153.%20Find%20Minimum%20in%20Rotated%20Sorted%20Array/README.md) | Medium | Binary Search |
| 40 | [Basic Calculator II](solutions/Week3-40-227.%20Basic%20Calculator%20II/README.md) | Medium | Stack |
| 41 | [Combination Sum IV](solutions/Week3-41-377.%20Combination%20Sum%20IV/README.md) | Medium | Dynamic Programming |
| 42 | [Insert Delete GetRandom O(1)](solutions/Week3-42-380.%20Insert%20Delete%20GetRandom%20O(1)/README.md) | Medium | Hash Table |
| 43 | [Non-overlapping Intervals](solutions/Week3-43-435.%20Non-overlapping%20Intervals/README.md) | Medium | Array |
| 44 | [Minimum Window Substring](solutions/Week3-44-76.%20Minimum%20Window%20Substring/README.md) | Hard | String |

### Week 4（25 題）

| # | 題目 | 難度 | Topic |
|---|------|------|-------|
| 1 | [Serialize and Deserialize Binary Tree](solutions/Week4-01-297.%20Serialize%20and%20Deserialize%20Binary%20Tree/README.md) | Hard | Binary Tree |
| 2 | [Trapping Rain Water](solutions/Week4-02-42.%20Trapping%20Rain%20Water/README.md) | Hard | Stack |
| 3 | [Find Median from Data Stream](solutions/Week4-03-295.%20Find%20Median%20from%20Data%20Stream/README.md) | Hard | Heap |
| 4 | [Word Ladder](solutions/Week4-04-127.%20Word%20Ladder/README.md) | Hard | Graph |
| 5 | [Basic Calculator](solutions/Week4-05-224.%20Basic%20Calculator/README.md) | Hard | Stack |
| 6 | [Maximum Profit in Job Scheduling](solutions/Week4-06-1235.%20Maximum%20Profit%20in%20Job%20Scheduling/README.md) | Hard | Binary Search |
| 7 | [Merge k Sorted Lists](solutions/Week4-07-23.%20Merge%20k%20Sorted%20Lists/README.md) | Hard | Heap |
| 8 | [Largest Rectangle in Histogram](solutions/Week4-08-84.%20Largest%20Rectangle%20in%20Histogram/README.md) | Hard | Stack |
| 9 | [Binary Tree Maximum Path Sum](solutions/Week4-09-124.%20Binary%20Tree%20Maximum%20Path%20Sum/README.md) | Hard | Binary Tree |
| 10 | [Maximum Frequency Stack](solutions/Week4-10-895.%20Maximum%20Frequency%20Stack/README.md) | Hard | Stack |
| 11 | [Median of Two Sorted Arrays](solutions/Week4-11-4.%20Median%20of%20Two%20Sorted%20Arrays/README.md) | Hard | Binary Search |
| 12 | [Longest Increasing Path in a Matrix](solutions/Week4-12-329.%20Longest%20Increasing%20Path%20in%20a%20Matrix/README.md) | Hard | Graph |
| 13 | [Longest Valid Parentheses](solutions/Week4-13-32.%20Longest%20Valid%20Parentheses/README.md) | Hard | Stack |
| 14 | [Design In-Memory File System](solutions/Week4-14-588.%20Design%20In-Memory%20File%20System/README.md) | Hard | Trie |
| 15 | [Employee Free Time](solutions/Week4-15-759.%20Employee%20Free%20Time/README.md) | Hard | Array |
| 16 | [Word Search II](solutions/Week4-16-212.%20Word%20Search%20II/README.md) | Hard | Graph |
| 17 | [Alien Dictionary](solutions/Week4-17-269.%20Alien%20Dictionary/README.md) | Hard | Graph |
| 18 | [Bus Routes](solutions/Week4-18-815.%20Bus%20Routes/README.md) | Hard | Graph |
| 19 | [Sliding Window Maximum](solutions/Week4-19-239.%20Sliding%20Window%20Maximum/README.md) | Hard | Array |
| 20 | [Palindrome Pairs](solutions/Week4-20-336.%20Palindrome%20Pairs/README.md) | Hard | String |
| 21 | [Reverse Nodes in k-Group](solutions/Week4-21-25.%20Reverse%20Nodes%20in%20k-Group/README.md) | Hard | Linked List |
| 22 | [Sudoku Solver](solutions/Week4-22-37.%20Sudoku%20Solver/README.md) | Hard | Matrix |
| 23 | [First Missing Positive](solutions/Week4-23-41.%20First%20Missing%20Positive/README.md) | Hard | Hash Table |
| 24 | [N-Queens](solutions/Week4-24-51.%20N-Queens/README.md) | Hard | Recursion |
| 25 | [Smallest Range Covering Elements from K Lists](solutions/Week4-25-632.%20Smallest%20Range%20Covering%20Elements%20from%20K%20Lists/README.md) | Hard | Heap |

---

## 如何使用

1. **依週練習**：按 Week 1 → Week 4 順序，每週完成對應題目。
2. **查看解法**：打開題目資料夾的 `solution.py`，可直接複製貼上到 LeetCode 提交。
3. **複習思路**：閱讀 `README.md` 取得正體中文解題說明與複雜度分析。
4. **追蹤 AC**：`AC_result.json` 記錄每次提交的 runtime / memory percentile。

> **注意**：部分題目為 LeetCode Premium 專屬（Meeting Rooms 系列、Encode and Decode Strings、Graph Valid Tree 等），無法在免費帳號提交。

---

## Scripts

需先設定 LeetCode cookie 環境變數：

```bash
export LEETCODE_SESSION="..."
export LEETCODE_CSRF="..."
```

```bash
# 提交單題
python scripts/leetcode_submit.py "solutions/Week1-01-1. Two Sum/solution.py"

# 批次提交所有題目
python3 scripts/run_all_leetcode_checks.py

# 只提交尚未 AC 的題目
python3 scripts/run_all_leetcode_checks.py --resume
```

---

## 相關連結

- [Tech Interview Handbook — Grind 75](https://www.techinterviewhandbook.org/grind75?hours=40&weeks=4)
- [LeetCode](https://leetcode.com)
- [14 Patterns to Ace Any Coding Interview](https://hackernoon.com/14-patterns-to-ace-any-coding-interview-question-c5bb3357f6ed)
