# passcode range: 206938-679128
from collections import Counter

passcodes = range(206938, 679129)


def rule_one(passcode: str) -> bool:
    return len(set(passcode)) <= 5


def rule_two(passcode: str) -> bool:
    return passcode == ''.join(sorted(passcode))


def rule_one_modified(passcode: str) -> bool:
    counts = Counter(passcode)
    return any(v == 2 for v in counts.values())


def rule_check(passcode: str) -> bool:
    return all([rule_one(passcode), rule_two(passcode)])


def rule_check_modified(passcode: str) -> bool:
    return all([rule_one_modified(passcode), rule_two(passcode)])


def find_correct_passwords():
    return sum(rule_check(str(passcode)) for passcode in passcodes)


def find_correct_passwords_modified():
    return sum(rule_check_modified(str(passcode)) for passcode in passcodes)


part1 = find_correct_passwords()
part2 = find_correct_passwords_modified()
print(part1)
print(part2)
