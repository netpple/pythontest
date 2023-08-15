import sys


def max_profit(nums: [int]) -> int:
    n = len(nums)
    result: int = None

    for i in range(n):
        buy = nums[i]
        for k in range(i+1, n):
            sell = nums[k]
            gap = sell - buy
            if not result:
                result = gap
            else:
                result = max(gap, result)

    return result


def cal_profit(profit: int, sell: int, buy: int):
    return sell - buy if not profit else max(profit, sell - buy)


def max_profit2(nums: [int]) -> int:
    n = len(nums)
    profit: int = None
    buy: int = nums[0]
    sell: int = None

    for i in range(1, n):
        if buy > nums[i]:
            if sell :
               profit = cal_profit(profit, sell, buy)
            buy = nums[i]
            sell = None
        else:
            sell = nums[i]
            profit = cal_profit(profit, sell, buy)

    profit = cal_profit(profit, sell, buy)

    return profit


def max_profit3(prices: [int]) -> int:
    buy = None
    profit = None
    for price in prices:
        buy = min(buy, price) if buy else price
        profit = max(profit, price - buy) if profit else (price - buy)

    return profit


if __name__ == "__main__":
    print(max_profit3([7, 1, 5, 3, 6, 4]))