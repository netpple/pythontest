def twosum_sol1(nums: [], target: int) -> [tuple]:
    num_to_index = {}
    result = []  # 결과를 저장할 리스트 생성

    for i, num in enumerate(nums):
        complement = target - num

        if complement in num_to_index:
            # target을 만족하는 쌍을 발견하면 두 인덱스를 tuple로 변환하여 리스트에 추가
            result.append((num_to_index[complement], i))

        num_to_index[num] = i

    return result


if __name__ == '__main__':
    print(twosum_sol1([2, 7, 11, 15, 5, 4, 3], 9))