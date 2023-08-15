# 시간복잡도가 O(n제곱)
def productexceptself_sol1(nums: [int]) -> []:
    result = []
    n = len(nums)
    for i in range(n):
        mul = 1
        if i == 0:
            right = i + 1
            while right < n:
                mul *= nums[right]
                right += 1
        elif i == n - 1:
            left = i - 1
            while left >= 0:
                mul *= nums[left]
                left -= 1
        else:
            left, right = i - 1, i + 1
            while left >= 0:
                mul *= nums[left]
                left -= 1
            while right < n:
                mul *= nums[right]
                right += 1

        result.append(mul)

    return result


def productexceptself_sol2(nums: [int]) -> []:
    n = len(nums)
    result = [1] * n

    left = 1 # 좌측곱 누적
    for i in range(1, n):
        left *= nums[i-1] # 자신을 제외한
        result[i] = left # 왼쪽곱 누적값 저장

    right = 1 # 오른쪽 곱 누적
    for i in range(n-2, -1, -1):  # 배열의 우측에서 좌측으로 순회
        right *= nums[i+1] # 자신을 제외한 오른쪽곱 누적값
        result[i] *= right # 자신의 왼쪽곱 x 오른쪽곱

    return result


if __name__ == "__main__":
    print(productexceptself_sol2([1, 2, 3, 4]))
