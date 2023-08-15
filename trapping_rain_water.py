from typing import List


def traprain_sol1(height: []) -> int:
    if not height or len(height) <= 2:
        return 0

    n = len(height)
    left_max = [0] * n
    right_max = [0] * n

    # 현재 위치에서 왼쪽까지의 최대 높이 계산
    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], height[i])

    # 현재 위치에서 오른쪽까지의 최대 높이 계산
    right_max[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], height[i])

    trapped_water = 0
    for i in range(n):
        # 빗물이 쌓일 수 있는 최대 높이 계산
        min_height = min(left_max[i], right_max[i])

        # 빗물이 쌓이는 양 계산
        trapped_water += max(0, min_height - height[i])

    return trapped_water


def traprain_sol2(height: List[int]) -> int:
    if not height:
        return 0

    volume = 0
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]

    while left < right:
        left_max, right_max = max(height[left], left_max), max(height[right], right_max)

        if left_max <= right_max:
            volume += left_max - height[left]
            left += 1
        else:
            volume += right_max - height[right]
            right -= 1
    return volume


def traprain_sol3(heights: [int]) -> int:
    n = len(heights)
    if n <= 2:
        return 0

    trapped_water = 0
    stack = []

    for current in range(n):
        while stack and heights[current] > heights[stack[-1]]:
            top = stack.pop()

            if not stack:
                break

            distance = current - stack[-1] - 1
            height = min(heights[current], heights[stack[-1]]) - heights[top]
            trapped_water += height * distance

        stack.append(current)

    return trapped_water


if __name__ == '__main__':
    print(traprain_sol3([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
