def InsertionSort(array):
	for i in range(1, len(array)):
		j = i - 1
		temp = array[i]
		while j > -1 and array[j] > temp:
			array[i] = array[j]
			j -= 1
			i -= 1
		array[j + 1] = temp

	print (array)

array = [5, 3, 1, 2, 6, 4]
InsertionSort(array)