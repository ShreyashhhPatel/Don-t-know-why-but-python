num = [5,2,9,1,5,6]

for i in range(len(num)):

    min_index = i
    for j in range(i + 1, len(num)):
        if num[j] < num[min_index]:
            # num[min_index], num[j] = num[j],num[min_index]
            min_index = j

    if min_index != i:
        num[i], num[min_index] = num[min_index],num[i]

print(num)
