# 인덱스로 결과를 리턴 - 문제는 엘리먼트로 리턴하라고 했으므로 틀림
def threesum_sol1(nums: [int], target: int) -> [[]]:
    result = []
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (nums[i] + nums[j] + nums[k]) == 0:
                    result.append([i, j, k])

    return result


# 엘리먼트로 결과를 리턴하도록 수정함
def threesum_sol2(nums: [int], target: int) -> [[]]:
    result = []
    nums.sort()
    print(nums)
    n = len(nums)

    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            for k in range(j + 1, n):
                if k > j + 1 and nums[k] == nums[k - 1]:
                    continue
                if (nums[i] + nums[j] + nums[k]) == 0:
                    result.append([nums[i], nums[j], nums[k]])

    return result


# two pointer
def threesum_sol3(nums: [int], target: int) -> [[]]:
    result = []
    nums.sort()
    n = len(nums)

    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        left, right = i+1, n-1

        while (left < right):
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                left, right = left+1, right-1

    return result


if __name__ == '__main__':
    print(threesum_sol3([-1, 0, 1, 2, -1, -4], 0))
