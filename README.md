# Week 5 — Midnight Mail Train

## Summary
This assignment implements a doubly linked list to manage train cars and uses recursion for solving string and list problems. The program allows adding and removing train cars, validating ticket codes, counting priority labels recursively, and cleaning radio messages by removing spaces. It demonstrates both data structure manipulation and recursive problem-solving.

## Approach  
- **Problem 1:** Implemented a doubly linked list with head and tail pointers. Added cars using `append_car`, removed the last car using `detach_last_car`, and traversed backward using `to_reverse_list`.
- **Problem 2:** Checked if a ticket code starts with "MM-" and ends with exactly 4 digits using string slicing and validation methods.
- **Problem 3:** Used recursion to count occurrences of a target label in a list by checking the first element and calling the function on the rest.
- **Problem 4:** Used recursion to remove spaces from a string by processing one character at a time.

## Complexity

### Problem 1 (DLL operations)
- **Time:** O(1) for append and detach, O(n) for reverse traversal  
- **Space:** O(1)  
- **Why:** Direct pointer updates are constant time, but traversal requires visiting all nodes.

### Problem 2 (Ticket validation)
- **Time:** O(1)  
- **Space:** O(1)  
- **Why:** Fixed-length string checks and simple operations.

### Problem 3 (Recursive label count)
- **Time:** O(n)  
- **Space:** O(n)  
- **Why:** Each recursive call processes one element, and recursion uses stack space.

### Problem 4 (Recursive string cleaning)
- **Time:** O(n)  
- **Space:** O(n)  
- **Why:** Each character is processed once, and recursion builds a new string.

## Edge-case checklist
- [x] empty train  
- [x] one train car  
- [x] invalid ticket code  
- [x] empty label list  
- [x] empty message  
- [x] one-character or all-space message  

## Assistance & Sources
- **AI used?** Y  
- **What it helped with:** Understanding recursion, debugging linked list logic, and writing test cases.  
- **Other sources used:** Python official documentation  