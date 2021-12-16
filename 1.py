def bubble(lis):
    l = len(lis)
    for i in range(l-1):
        for j in range(l-1):
            if (lis[j] > lis[j + 1]): 
                a = lis[j] 
                lis[j] = lis[j + 1] 
                lis[j + 1] = a
    return lis
#2 сложность сортировки n^2
