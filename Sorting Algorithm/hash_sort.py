import math

def hash_sort(array):
  mlen = 0
  for a in array:
    leng = math.floor(math.log10(a))
    mlen = max(mlen, leng)
  hasher(array, 0, len(array)-1, mlen)
		
def hasher(array, left, right, pos):
  if left >= right or pos < 0: return
  group = [[] for _ in range(11)]
  for i in range(left, right+1):
    temp = (array[i] // (10**pos)) % 10
    group[temp].append(array[i])
  ind = left
  start = left
  for g in group:
    for x in g:
      array[ind] = x
      ind += 1
    hasher(array, start, start+len(g)-1, pos-1)
    start += len(g)
		
def main():
	arr = []
	s = input("Enter the list number : ").split(' ')
	for i in range(len(s)):
		arr.append(int(s[i]))

	print("Unsorted list: ")
	print(arr)
	
	hash_sort(arr)
	print("Sorted list: ")
	print(arr)


main()
