def average_num(nums):
    Total_nums = 0
    n = float(len(nums))
    for num in nums:
        Total_nums += num

    return Total_nums/n


interger_array = [80, 19, 20, 22, 100, 14, 19, 22]
result = average_num(interger_array)
print "n: ", len(interger_array)
print "Average: ", result

