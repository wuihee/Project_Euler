# Challenge 5: Smallest Multiple


def gcf_formula(num1, num2):
    # r is remainder
    r = num1 % num2
    if r == 0:
        return num2
    else:
        return gcf_formula(num2, r)


def lcm_formula(num1, num2):
    return num1 * num2 / gcf_formula(num1, num2)


# Based on the concept that given a, b, c...
# lCM of the numbers == lcm(lcm(a, b), c)
def find_lcm(args):
    nums = args
    nums.sort()

    if len(args) < 2:
        return 'You do not have enough numbers.'

    for i in range(len(nums)):
        lcm = lcm_formula(nums[0], nums[1])  # LCM of first two numbers
        if nums[1] == max(nums):  # Check if second number is equal to the largest (or last) number in the list
            return lcm  # If so, this is the LCM of the list
        else:
            nums.remove(nums[i])  # Remove first two numbers of the list (numbers used to find LCM)
            nums.remove(nums[i])  # Not doing num.remove(nums[i + 1]) because what's left of the list is [a, b] and nums[i + i] would remove b
            nums.append(lcm)  # Add LCM to the list
            find_lcm(nums)  # Repeat function


print(find_lcm(list(range(1, 21))))
