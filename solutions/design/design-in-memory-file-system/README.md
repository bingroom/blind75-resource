# Design In-Memory File System

## Problem Description
Design an in-memory file system supporting `ls`, `mkdir`, `addContentToFile`, and `readContentFromFile` operations with Unix-style paths.

## Approach
Use a trie where each node represents a directory or file. Each node has a `children` dict (subdirectories/files), a `content` string (for files), and an `is_file` flag. Path traversal splits by `/` and walks the trie. `defaultdict(TrieNode)` auto-creates intermediate directories.

## Complexity
- **Time:** O(m + k log k) for `ls` (m = path depth, k = entries to sort), O(m + n) for file operations (n = content length)
- **Space:** O(total stored content + total path nodes)
