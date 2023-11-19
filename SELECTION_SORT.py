array =[913, 578, 245, 754, 321, 987, 502, 689, 123, 876,
        450, 265, 831, 164, 729, 593, 316, 871, 104, 618,
        937, 782, 349, 516, 190, 847, 682, 415, 578, 236,
        691, 327, 864, 509, 147, 734, 602, 879, 394, 128,
        863, 578, 241, 756, 312, 988, 508, 684, 120, 879,
        444, 269, 834, 172, 725, 589, 321, 875, 108, 612,
        943, 788, 356, 523, 196, 857, 692, 425, 588, 230,
        701, 333, 868, 524, 161, 749, 615, 892, 387, 142,
        881, 556, 223, 742, 308, 974, 489, 657, 279, 810,
        173, 926, 671, 343, 790, 258, 925, 603, 216, 671]

def Select(arr):
    sorting_area = len(arr)-1
    
    while sorting_area > 0 :
        largest = 0
        for i in range(sorting_area):
            if arr[largest] < arr[i]:
                largest = i
        arr[largest] ,arr[sorting_area] = arr[sorting_area] ,arr[largest]
        sorting_area -= 1
    return arr
Select(array)
#Time Complexity : O(n^2)
#Space Complexity : O(1)