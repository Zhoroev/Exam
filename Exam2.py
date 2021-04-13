def func(deposit, month, percent):
    sum_for_all_month = [(percent / 100) / 12 * deposit + deposit]
    for i in range(month - 1):
        for j in sum_for_all_month:
            sum_for_month = (percent / 100) / 12 * j + j
            sum_for_all_month.clear()
            sum_for_all_month.append(sum_for_month)
    return sum(sum_for_all_month)


print(int(func(1000000, 6, 12)))