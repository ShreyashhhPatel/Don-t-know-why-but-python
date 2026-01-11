def insertion_sort(arry):
# 5    2.  9.   1.    5.  6
# j    i(k)
    for i in range (1,len(arry)):
        key = arry[i]
        j = i - 1
        while arry[j]>key and j >= 0:
            arry[j+1] = arry[j]
            j -= 1
    # 5    2.  9.   1.    5.  6
    # j    i(k)
    #      j+1
    #       j

        arry[j+1] = key


def display(arry):
    for i in range(len(arry)):
        print(arry[i],end= " ")
    print()

if __name__ == "__main__":
    arry = [12,11,13,5,6]
    insertion_sort(arry)
    display(arry)





















# num = [5,2,9,1,5,6]
# def insertion_sort(arr)
# for i in range (1, len(num)):
#     j = i

#     while arr



# arr = [2,6,5,1,3,4]
# print(num)



# # for i in range (1,len(num)):
# #     key = num[i]
# #     j = i -1

# #     while j >= 0 and num[j] > key:
# #         num[j+1] = num[j]
# #         j -= 1
# #     num[j+1] = key
