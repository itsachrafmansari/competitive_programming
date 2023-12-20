class Solution:
    def buyChoco(self, prices: list[int], money: int) -> int:
        firstMin, secondMin = 101, 101

        for price in prices:
            if price < firstMin:
                secondMin = firstMin
                firstMin = price
            elif price < secondMin:
                secondMin = price

        if money >= (firstMin + secondMin):
            money -= firstMin + secondMin

        return money
