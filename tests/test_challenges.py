from src.challenges import (
    MidnightMailDLL,
    clean_radio_message,
    count_priority_labels,
    is_valid_ticket_code,
)


# ── Problem 1: MidnightMailDLL ────────────────────────────────────────────────

def test_append_and_reverse_list_basic() -> None:
    train = MidnightMailDLL()
    train.append_car("A1")
    train.append_car("B2")
    train.append_car("C3")
    assert train.to_reverse_list() == ["C3", "B2", "A1"]


def test_to_reverse_list_single_car() -> None:
    train = MidnightMailDLL()
    train.append_car("Z9")
    assert train.to_reverse_list() == ["Z9"]


def test_to_reverse_list_empty() -> None:
    train = MidnightMailDLL()
    assert train.to_reverse_list() == []


def test_detach_last_car_basic() -> None:
    train = MidnightMailDLL()
    train.append_car("A1")
    train.append_car("B2")
    assert train.detach_last_car() == "B2"
    assert train.to_reverse_list() == ["A1"]


def test_detach_last_car_empty() -> None:
    train = MidnightMailDLL()
    assert train.detach_last_car() is None


def test_detach_last_car_single() -> None:
    """Detaching the only car should leave an empty list."""
    train = MidnightMailDLL()
    train.append_car("X1")
    assert train.detach_last_car() == "X1"
    assert train.to_reverse_list() == []


def test_detach_all_cars_sequentially() -> None:
    train = MidnightMailDLL()
    train.append_car("A1")
    train.append_car("B2")
    train.append_car("C3")
    assert train.detach_last_car() == "C3"
    assert train.detach_last_car() == "B2"
    assert train.detach_last_car() == "A1"
    assert train.detach_last_car() is None


# ── Problem 2: is_valid_ticket_code ──────────────────────────────────────────

def test_ticket_code_valid_example() -> None:
    assert is_valid_ticket_code("MM-1234") is True


def test_ticket_code_invalid_too_few_digits() -> None:
    assert is_valid_ticket_code("MM-12") is False


def test_ticket_code_invalid_wrong_prefix() -> None:
    assert is_valid_ticket_code("XX-1234") is False


def test_ticket_code_edge_empty_string() -> None:
    assert is_valid_ticket_code("") is False


def test_ticket_code_invalid_letters_in_suffix() -> None:
    assert is_valid_ticket_code("MM-12AB") is False


def test_ticket_code_invalid_too_many_digits() -> None:
    assert is_valid_ticket_code("MM-12345") is False


# ── Problem 3: count_priority_labels ─────────────────────────────────────────

def test_count_priority_labels_basic() -> None:
    labels = ["PRIORITY", "NORMAL", "PRIORITY", "LATE"]
    assert count_priority_labels(labels, "PRIORITY") == 2


def test_count_priority_labels_empty() -> None:
    assert count_priority_labels([], "PRIORITY") == 0


def test_count_priority_labels_none_match() -> None:
    labels = ["NORMAL", "LATE", "NORMAL"]
    assert count_priority_labels(labels, "PRIORITY") == 0


def test_count_priority_labels_all_match() -> None:
    labels = ["PRIORITY", "PRIORITY", "PRIORITY"]
    assert count_priority_labels(labels, "PRIORITY") == 3


def test_count_priority_labels_single_match() -> None:
    assert count_priority_labels(["PRIORITY"], "PRIORITY") == 1


# ── Problem 4: clean_radio_message ───────────────────────────────────────────

def test_clean_radio_message_basic() -> None:
    assert clean_radio_message("go now") == "gonow"


def test_clean_radio_message_empty() -> None:
    assert clean_radio_message("") == ""


def test_clean_radio_message_leading_and_trailing_spaces() -> None:
    assert clean_radio_message(" a b ") == "ab"


def test_clean_radio_message_all_spaces() -> None:
    assert clean_radio_message("   ") == ""


def test_clean_radio_message_no_spaces() -> None:
    assert clean_radio_message("clear") == "clear"
