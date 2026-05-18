from __future__ import annotations


class TrainCarNode:
    """A single node in a doubly linked list representing one train car."""

    def __init__(self, car_id: str) -> None:
        self.car_id = car_id
        self.prev: TrainCarNode | None = None
        self.next: TrainCarNode | None = None


class MidnightMailDLL:
    """A doubly linked list that manages train cars."""

    def __init__(self) -> None:
        self.head: TrainCarNode | None = None
        self.tail: TrainCarNode | None = None

    def append_car(self, car_id: str) -> None:
        """Add a train car to the end of the list."""
        new_node = TrainCarNode(car_id)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node       # type: ignore[union-attr]
            new_node.prev = self.tail
            self.tail = new_node

    def detach_last_car(self) -> str | None:
        """Remove the last train car and return its ID. Returns None if empty."""
        if self.tail is None:
            return None

        removed_id = self.tail.car_id

        if self.head == self.tail:  # only one node
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None           # type: ignore[union-attr]

        return removed_id

    def to_reverse_list(self) -> list[str]:
        """Return all car IDs from tail to head (reverse order)."""
        result: list[str] = []
        current = self.tail

        while current:
            result.append(current.car_id)
            current = current.prev

        return result


def is_valid_ticket_code(code: str) -> bool:
    """Return True only if code starts with 'MM-' and ends with exactly 4 digits."""
    if not code.startswith("MM-"):
        return False
    suffix = code[3:]
    return len(suffix) == 4 and suffix.isdigit()


def count_priority_labels(labels: list[str], target: str) -> int:
    """Recursively count how many times target appears in labels. No loops allowed."""
    if not labels:
        return 0
    match = 1 if labels[0] == target else 0
    return match + count_priority_labels(labels[1:], target)


def clean_radio_message(message: str) -> str:
    """Recursively return message with all spaces removed. No loops allowed."""
    if message == "":
        return ""
    if message[0] == " ":
        return clean_radio_message(message[1:])
    return message[0] + clean_radio_message(message[1:])


# ── Optional stretch ──────────────────────────────────────────────────────────

def count_priority_labels_iterative(labels: list[str], target: str) -> int:
    """Iterative version of count_priority_labels for comparison."""
    count = 0
    for label in labels:
        if label == target:
            count += 1
    return count


def clean_radio_message_iterative(message: str) -> str:
    """Iterative version of clean_radio_message for comparison."""
    result = ""
    for char in message:
        if char != " ":
            result += char
    return result
