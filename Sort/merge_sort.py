def Merge(array, front, mid, end):
	leftsub = array[front : mid + 1]
	rightsub = array[mid + 1 : end + 1]

	leftsub.append(float('inf'))
	rightsub.append(float('inf'))

	idxleft, idxright = 0, 0
	for i in range(front, end + 1):
		if leftsub[idxleft] < rightsub[idxright]:
			array[i] = leftsub[idxleft]
			idxleft += 1
		else:
			array[i] = rightsub[idxright]
			idxright += 1

def MergeSort(array, front, end):
	if front < end:
		mid = (front + end) // 2
		MergeSort(array, front, mid)
		MergeSort(array, mid + 1, end)
		Merge(array, front, mid, end)

array = [5, 3, 8, 6, 2, 7, 1, 4]
MergeSort(array, 0, len(array) - 1)
print (array)