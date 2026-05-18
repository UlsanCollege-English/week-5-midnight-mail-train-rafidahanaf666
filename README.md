# Week 5 — Midnight Mail Train

## Summary

This assignment implements four tools for a late-night rail delivery company. It includes a doubly linked list (DLL) to manage train cars, a ticket code validator using string operations, and two recursive functions — one for counting labelled packages and one for cleaning up radio messages. The focus is on data structure manipulation, recursion, and writing clear, tested Python code.

---

## Approach

### Problem 1 — Train Cars in Reverse (DLL)

Built a doubly linked list with `head` and `tail` pointers. Each `TrainCarNode` holds a `car_id` and links to both the previous and next node.

- `append_car`: creates a new node, links it to `tail`, and updates `tail`. O(1).
- `detach_last_car`: reads the tail's ID, relinks `tail` to `tail.prev`, and severs the old connection. Handles empty and single-node cases. O(1).
- `to_reverse_list`: walks backward from `tail` to `head`, collecting IDs into a list. O(n).

### Problem 2 — Ticket Code Check

Splits the work into two checks:
1. Does the string start with `"MM-"`?
2. Is everything after the prefix exactly 4 characters, all digits?

Uses `str.startswith`, slicing, `len`, and `str.isdigit`. No regex needed.

### Problem 3 — Count Priority Packages (Recursion)

Base case: empty list → return 0.  
Recursive step: check if the first element matches the target (1 or 0), then add the result of calling the function on the remaining list.

### Problem 4 — Clean the Radio Message (Recursion)

Base case: empty string → return `""`.  
Recursive step: skip the character if it is a space; otherwise prepend it to the result of calling the function on the rest of the string.

---

## Complexity

| Problem | Time | Space | Reason |
|---------|------|-------|--------|
| `append_car` | O(1) | O(1) | Direct pointer update at tail |
| `detach_last_car` | O(1) | O(1) | Direct pointer update at tail |
| `to_reverse_list` | O(n) | O(n) | Must visit every node; result list grows with n |
| `is_valid_ticket_code` | O(1) | O(1) | Fixed-length string checks only |
| `count_priority_labels` | O(n) | O(n) | One call per element; n frames on the call stack |
| `clean_radio_message` | O(n) | O(n) | One call per character; n frames on the call stack |

---

## Edge-case checklist

- [x] Empty train — `detach_last_car` and `to_reverse_list` both handle an empty DLL
- [x] One train car — detaching the only car leaves `head` and `tail` both `None`
- [x] Several train cars — sequential detach tested until list is empty
- [x] Valid ticket code — `"MM-1234"` → `True`
- [x] Invalid prefix — `"XX-1234"` → `False`
- [x] Too few digits — `"MM-12"` → `False`
- [x] Too many digits — `"MM-12345"` → `False`
- [x] Non-digit suffix — `"MM-12AB"` → `False`
- [x] Empty string ticket — `""` → `False`
- [x] Empty label list — `count_priority_labels([], ...)` → `0`
- [x] No matches in label list — returns `0` without error
- [x] All-space radio message — returns `""`
- [x] Leading/trailing spaces in message — stripped correctly
- [x] Empty radio message — returns `""`

---

## Stretch — Iterative vs Recursive Comparison

Both `count_priority_labels` and `clean_radio_message` have iterative versions included in `src/challenges.py`.

| | Recursive | Iterative |
|-|-----------|-----------|
| **Readability** | Mirrors the problem definition closely — base case + one step. Feels natural for list/string problems. | Slightly more code but familiar to most readers; easy to trace with print statements. |
| **Call stack space** | O(n) stack frames — each call waits for the next. Long inputs can hit Python's recursion limit (~1000 by default). | O(1) stack space — only one frame, no risk of `RecursionError`. |
| **Performance** | Slightly slower due to function call overhead and repeated slicing (`labels[1:]` copies the list each time). | Faster in practice; no copy overhead. |
| **Which feels clearer** | Recursive — especially for `clean_radio_message`, where "skip or keep one character, then handle the rest" is exactly what the code says. | Iterative — for production code where inputs can be large or where hitting the recursion limit is a real concern. |

For this assignment the inputs are small, so both are fine. For real systems, the iterative version is safer.

---

## Assistance & Sources

- **AI used?** Yes
- **What it helped with:** Understanding how to structure the DLL with both `head` and `tail` pointers, thinking through recursion base cases, and reviewing test coverage.
- **Other sources:** [Python official documentation](https://docs.python.org/3/) — `str` methods (`startswith`, `isdigit`), list slicing, type hints.
