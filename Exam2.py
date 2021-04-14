def func(deposit, sum_for_all_month, percent):
    sum_for_month = deposit
    month = 0
    while sum_for_month < sum_for_all_month:
        month += 1
        sum_for_month += (percent / 100) / 12 * sum_for_all_month
    return month


print(int(func(1000000, 1061520, 12)))
