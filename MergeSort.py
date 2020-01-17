# Merge Sort Function
def mergeSort(sortList):
    # Put Sort Here
    mSortPiece = 0;
    lenSortList = len(sortList);
    
    midPos = int(len(sortList)/2);
    
    #mergeSort(sortList[0:midPos])
    #mergeSort(sortList[midPos+1:lenSortList-1])

    #print("1-h: " + list2string(sortList[0:midPos]) + " | 2-h: " + list2string(sortList[midPos:lenSortList]))

    # Return Sorted List
    if lenSortList == 1:
        return sortList

    a = []
    b = []

    #a = left, b = right
    a = mergeSort(sortList[:midPos])
    b = mergeSort(sortList[midPos:])

    i = 0 # position through a
    j = 0 # position through b
    k = 0 # position of sorted array

    #Start iterating through a and b until we reach the end of a or b
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            sortList[k]=a[i]
            i+=1
        else:
            sortList[k]=b[j]
            j+=1
        k+=1

    #add the rest of a to the sorted array if we reached the end of b
    while i < len(a):
        sortList[k]=a[i]
        i+=1
        k+=1

    #add the rest of b to the sorted array if we reached the end of a
    while j < len(b):
        sortList[k]=b[j]
        j+=1
        k+=1

    return sortList;

def list2string(toString):
    # Convert list to string for output
    stringList = list("[")

    for item in toString:
        stringList += str(item) + ", "

    for i in range(-2, 0):
        stringList[i] = ""

    stringList += "]"
    return "".join(stringList)

toSort = [77, 0, 23, 44, 41, 324, 11, 3, 33, 12, 12, 12, 12, 12, 334, 567, 896]

print("Unsorted string: " + list2string(toSort))

sortedList = []
sortedList = mergeSort(toSort)
print("Sorted list: " + list2string(sortedList));
