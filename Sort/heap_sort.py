def MaxHeapify(array, root, length):
	left = root * 2
	right = root * 2 + 1
	largest = root

	if left <= length and array[left] > array[largest]:
		largest = left
	if right <= length and array[right] > array[largest]:
		largest = right

	if largest != root:
		temp = array[largest]
		array[largest] = array[root]
		array[root] = temp
		MaxHeapify(array, largest, length)

def BuildMaxHeap(array):
	for i in range(len(array) // 2, 0, -1):
		MaxHeapify(array, i, len(array) - 1)

def HeapSort(array):
	array.insert(0, 0)

	BuildMaxHeap(array)

	size = len(array) - 1
	for i in range(size, 1, -1):
		temp = array[1]
		array[1] = array[i]
		array[i] = temp

		MaxHeapify(array, 1, i - 1)

	del array[0]

array = [9, 4, 1, 6, 7, 3, 8, 2, 5]
HeapSort(array)
print (array)