#function for merging two array does not matter whether they are sorted or not 
def merge(arr1,arr2):
    l =[]
    i=0
    j=0
    while len(l)<(len(arr2)+len(arr1)):
        if i == len(arr1) or j==len(arr2):
            if i == len(arr1):
                l.extend(arr2[j:])
            else:
                l.extend(arr1[i:])
        elif arr1[i] < arr2[j]:
            l.append(arr1[i])
            i=i+1
        else :
            l.append(arr2[j])
            j=j+1
    return l
#function for splitting two arrays #method :- even in one list odds in one list 
def split(arr):
    n=len(arr)
    if n==0:
        return [],[]
    elif n==1:
        return arr,[]
    else :
        a,b = split(arr[2:])
        return [arr[0]]+a,[arr[1]]+b
#function for sorting an array which is being recursively called to split and then merge         
def sort(arr):
    if len(arr) ==1 :
        return arr
    else:
        a,b = split(arr)
        return merge(sort(a),sort(b))
print(sort([100,156,1016,10645,13465,1384312,123,413541,687468]))