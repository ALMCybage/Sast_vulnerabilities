"""
buggy_sample.py

Deliberately contains several bugs so SonarCloud's static analysis
flags them under "Bugs" (not vulnerabilities or code smells).
This file exists only to verify that SonarCloud bug detection works
in the CI pipeline. Do not use in production.
"""


def divide(a, b):
    """Bug: no check for b == 0 -> ZeroDivisionError at runtime.
    SonarCloud rule: python:S3518 (division by zero)."""
    result = a / b
    return result


def get_first_item(items):
    """Bug: no check for an empty list before indexing.
    SonarCloud rule: python:S5644 / IndexError risk."""
    return items[0]


def sum_values(values):
    """Bug: 'total' is used in a way that assumes it's always a number,
    but if 'values' is empty the loop body never runs and later code
    that expects total to reflect all values silently gives a wrong
    result masked as success (logic bug, not exception)."""
    total = 0
    for v in values:
        total = total + v
    average = total / len(values)  # Bug: len(values) can be 0 -> ZeroDivisionError
    return average


def compare_values(a, b):
    """Bug: comparing mutable default argument, unreachable branch.
    SonarCloud flags always-true/always-false conditions."""
    if a == b and a != b:  # Bug: condition can never be true (S2589)
        return "equal and not equal"
    return "normal"


def open_and_read(path):
    """Bug: file handle is never closed and no exception handling,
    so a failure leaves the file open / unhandled.
    SonarCloud rule: python:S2093 (use 'with' for resource management)."""
    f = open(path, "r")
    data = f.read()
    return data


class Counter:
    """Bug: mutable default argument shared across all instances.
    SonarCloud rule: python:S5717 (mutable default arguments)."""

    def __init__(self, items=[]):
        self.items = items

    def add(self, item):
        self.items.append(item)
        return self.items


def unreachable_code(x):
    """Bug: code after return is unreachable (S1763)."""
    if x > 0:
        return True
        print("This line will never execute")  # unreachable
    return False


if __name__ == "__main__":
    # Intentionally triggering the bugs above for demonstration only.
    print(divide(10, 0))
