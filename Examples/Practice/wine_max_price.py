'''
Imagine you have a collection of N wines placed next to each other on a shelf. For simplicity, let’s
number the wines from left to right as they are standing on the shelf with integers from 1 to N,
respectively. The price of the ith wine is pi. (prices of different wines can be different).
Because the wines get better every year, supposing today is the year 1, on year ythe price of the ith
wine will be y*pi, i.e. y-times the value that current year.
You want to sell all the wines you have, but you want to sell exactly one wine per year, starting on this
year. One more constraint - on each year you are allowed to sell only either the leftmost or the
rightmost wine on the she lf and you are not allowed to reorder the wines on the shelf (i.e. they must
stay in the same order as they are in the beginning).
You want to find out, what is the maximum profit you can get, if you sell the wines in optimal order?
So, for example, if the prices of the wines are (in the order as they are
placed on the shelf, from left to right): p1=1, p2=4, p3=2, p4=3. The optimal solution would be to sell
the wines in the order p1, p4, p3, p2 for a total profit 1 * 1 + 3 * 2 + 2 * 3 + 4 * 4 = 29.
'''


def get_max_price(current_year, current_total, available_prices):
    if not available_prices:
        return current_total
    if len(available_prices) == 1:
        current_total += current_year * available_prices[0]
        return current_total
    price_with_leftmost_wine_taken = current_total + current_year * available_prices[0]
    price_with_rightmost_wine_taken = current_total + current_year * available_prices[-1]
    return max(get_max_price(current_year + 1, price_with_leftmost_wine_taken, available_prices[1:]),
               get_max_price(current_year + 1, price_with_rightmost_wine_taken, available_prices[:-1]))


def get_max_price_dp(start, end, total_wines, prices, dp):
    if dp[start][end] != 0:
        return dp[start][end]
    if start > end:
        return 0
    current_year = total_wines - (end - start)
    include_leftside = prices[start] * current_year + get_max_price_dp(start + 1, end, total_wines, prices, dp)
    include_rightside = prices[end] * current_year + get_max_price_dp(start, end - 1, total_wines, prices, dp)
    dp[start][end] = max(include_leftside, include_rightside)
    return dp[start][end]


def main():
    prices = list(map(int, input("Enter the prices separated by spaces : ").split()))
    print(get_max_price(1, 0, prices[:]))
    dp = [[0] * (len(prices) + 1) for _ in range(len(prices) + 1)]
    print(get_max_price_dp(0, len(prices) - 1, len(prices), prices, dp))


if __name__ == "__main__":
    main()
