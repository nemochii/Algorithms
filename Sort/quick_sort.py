def Partiton(array, front, end):
	i = front - 1
	for j in range(front, end):
		if array[j] < array[end]:
			i += 1
			temp = array[j]
			array[j] = array[i]
			array[i] = temp
	i += 1
	temp = array[end]
	array[end] = array[i]
	array[i] = temp

	return (i)

def QuickSort(array, front, end):
	if front < end:
		pivot = Partiton(array, front, end)
		QuickSort(array, front, pivot - 1)
		QuickSort(array, pivot + 1, end)

array = [9, 4, 1, 6, 7, 3, 8, 2, 5]
front = 0
end = len(array) - 1
QuickSort(array, front, end)
print (array)