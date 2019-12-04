# passcode range: 206938-679128
import numpy as np

passcodes = range(206938, 679129)


def rule_check(passcode: str) -> bool:
    check2, check3, check4 = False, False, True

    passcode = [int(num) for num in passcode]
    # print(passcode)
    passcode1 = passcode[:-1]
    passcode2 = passcode[1:]

    a = np.array(passcode1)
    b = np.array(passcode2)

    diff = list(b - a)
    # print(diff)
    if len(list(filter(lambda x: x < 0, diff))) == 0:
        check3 = True
    else:
        check3 = False

    if len(list(filter(lambda x: x == 0, diff))) == 0:
        check2 = False
    else:
        check2 = True

    # rule check4
    zeros_in_diff = [num for num in diff if num == 0]
    if len(zeros_in_diff) == 0:
        pass
    else:
        first_zero = diff.index(0)
        if len(zeros_in_diff) == 1:
            check4 = True
        elif len(zeros_in_diff) == 2:
            if diff[first_zero] == diff[first_zero + 1]:
                check4 = False
            else:
                check4 = True
        elif len(zeros_in_diff) == 3:
            if diff[first_zero] != diff[first_zero + 1]:
                check4 = True
            else:
                if diff[first_zero + 1] == diff[first_zero + 2]:
                    check4 = False
                else:
                    check4 = True
        elif len(zeros_in_diff) == 4:
            if diff[first_zero] != diff[first_zero + 1]:
                check4 = True
            else:
                if diff[first_zero + 1] == diff[first_zero + 2]:
                    if diff[first_zero + 2] == diff[first_zero + 3]:
                        check4 = False
                    else:
                        check4 = True
                else:
                    check4 = False
        else:  # len(zeros_in_diff) == 5
            check4 = False

        # print(check1, check2, check3)
    return all([check2, check3, check4])


# print(rule_check('112233'))
# print(rule_check('123444'))
# print(rule_check('111122'))
# print(rule_check('111111'))
# print(rule_check('223450'))
# print(rule_check('123789'))


def find_correct_passwords():
    results = []
    for passcode in passcodes:
        passcode = str(passcode)
        results.append(rule_check(passcode))

    # print(results)
    return sum(results)


print(find_correct_passwords())
