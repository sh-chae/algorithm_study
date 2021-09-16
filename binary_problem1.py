# n = int(input())
# nn = map(int, input().split())
# m = int(input())
# mm = map(int, input().split())

n = 5
nn = [8,3,7,9,2]
mm = [5,7,9]

nn.sort()
mm.sort()

def biSearch(array, target, start, end):
    if start>end:
        return None
    mid = (start+end)//2
    if array[mid] == target:
        return mid
    elif array[mid]>target:
        return biSearch(array, target, start, mid-1)
    else:
        return biSearch(array, target, mid+1, end)

for i in mm:
    if biSearch(nn, i, 0, n-1) != None:
        print("yes", end=" ")
    else:
        print("no", end=" ")

