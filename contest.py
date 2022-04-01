
def pairORSum(arr) :
    n=len(arr)
    ans = []    # Initialize result
 
    # Consider all pairs (arr[i], arr[j)
    # such that i < j
    for i in range(0, n) :
         
        for j in range(i + 1, n) :
             
            ans.append(arr[i] ^ arr[j])
             
    return ans
     
 
# Driver Code
arr = [ 3,3 ]
n = len(arr)
 
print(pairORSum(arr))
 