def arraypart_sol1(nums: [int]) -> int:
    nums.sort(reverse=True)
    a = min(nums[0], nums[1])
    b = min(nums[2], nums[3])

    result = a + b
    return result


def arraypart_sol2(nums: [int]) -> int:
    return sum(sorted(nums)[::2])


# n 개 pair 를 이용한 min(a, b)의 합으로 만들 수 있는 "가장 큰 수"를 출력하라
if __name__ == "__main__":
    print(arraypart_sol2([1, 4, 3, 2]))
