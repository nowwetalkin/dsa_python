
arr=[35,2,1,54,76,2,65,7]
def bubblesort(arr):
	length=len(arr)
	for x in range(0,length-1):
		for i in range(0,length-1):
			if arr[i]>arr[i+1]:
				temp= arr[i]
				arr[i]= arr[i+1]
				arr[i+1]=temp
	return arr

print(bubblesort(arr))

def selectionsort(arr):
	length=len(arr)
	for i in range(0,length):
		min=i
		for j in range(i+1,length):
			if arr[j]<arr[min]:
				min=j
		arr[i],arr[min]=arr[min],arr[i]
	return arr
print(selectionsort(arr))


def insertion(arr):
	i=1
	end=arr[0]
	while i<len(arr):
		if arr[i]< end:
			x= arr.pop(i)
			for j in range(0,i):
				if x< arr[j]:
					arr.insert(j,x)
					break
			end=arr[i]
		i+=1
	return arr

print(insertion(arr))
				










# def bubblesort(arr):
#   qw = 0
#   while qw < len(arr):
#     for i in range(0,len(arr)-1):
#       if arr[i] > arr[i+1]:
#         arr[i] , arr[i+1] = arr[i+1] , arr[i]
    
#     qw += 1
#   return arr

# arr = [5,9,1,2,7,3,8,2]
# print(bubblesort(arr))

#     