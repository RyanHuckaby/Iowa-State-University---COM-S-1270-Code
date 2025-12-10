"""
Ryan Huckaby
Lab #11 (Week Fifteen)
Date Started: 12/3/2025
Description: Multiple ways to find the indicies of two numbers that add up to the target.
"""

#CITATION - URL: https://interviewing.io/questions/two-sum
#CITATION - Author: Tom Wagner and Dominic Platt
#CITATION - Date Accessed: 12/3/2025

def twoSumLoops(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == target - nums[j]:
                return [i, j]
    return None


def twoSumDict(nums, target):
    seen = {}
    for i in range(len(nums)):
        needed = target - nums[i]
        if needed in seen:
            return [seen[needed], i]
        seen[nums[i]] = i
    return None


def twoSumLoopsAll(nums, target):
    result = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                result.append([i, j])
    return result


def twoSumDictAll(nums, target):
    seen = {}
    result = []
    for i in range(len(nums)):
        needed = target - nums[i]
        if needed in seen:
            for index in seen[needed]:
                result.append([index, i])
        if nums[i] not in seen:
            seen[nums[i]] = []
        seen[nums[i]].append(i)
    return result


def main():
    nums = [2, 7, 11, 15, 7]
    target = 9

    print(twoSumLoops(nums, target))
    print(twoSumDict(nums, target))
    print(twoSumLoopsAll(nums, target))
    print(twoSumDictAll(nums, target))


if __name__ == "__main__":
    main()