import timeit

coins = [50, 25, 10, 5, 2, 1]

def find_coins_greedy(sum_: int):
    count_coins = {}
    for coin in coins:
        count = sum_ // coin
        if count > 0:
            count_coins[coin] = count
        sum_ = sum_ - count * coin
    return count_coins

def find_min_coins(sum_ :int):
    min_coins_required = [0] + [float('inf')] * sum_
    last_coin_used = [0] * (sum_ + 1)
    for s in range(1, sum_ + 1):
        for coin in coins:
            if (s >= coin) and (min_coins_required[s-coin]+1 < min_coins_required[s]):
                min_coins_required[s] = min_coins_required[s - coin] + 1
                last_coin_used[s] = coin
    count_coins = {}
    current_sum = sum_
    while current_sum > 0:
        coin = last_coin_used[current_sum]
        count_coins[coin] = count_coins.get(coin, 0) + 1
        current_sum = current_sum - coin
    return count_coins


def main():
    result = find_coins_greedy(113)
    print('Функція жадібного алгоритму для суми 113: ', result)

    result = find_min_coins(113)
    print('Функція динамічного програмування для суми 113: ', result)

    summs = [34, 56, 88, 96, 144, 188, 244, 288, 484, 668, 868, 1001, 1486, 1848, 4848, 14848]

    time_greedy = []
    time_min = []

    for i in range(0, len(summs)):
        time_greedy.append(round(timeit.timeit(lambda: find_coins_greedy(summs[i]), number=800), 5))
        time_min.append(round(timeit.timeit(lambda: find_min_coins(summs[i]), number=800),5))

    print('\nТестові значення сум: ', summs)
    print('\nОцінювання часу виконання алгоритмів:')
    print('Жадібного алгоритму, час виконання (800 повторів): \n', time_greedy)
    print('Динамічного програмування, час виконання (800 повторів): \n', time_min)


if __name__ == '__main__':
    main()