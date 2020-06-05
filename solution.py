# Write a function that accepts integer N and displays the smallest product of N that consists of number 5 and/or 7 only
# A student asked this question in the group, but nobody wants to answer him. However, I did not give him this solution. 
# I gave him a twist of the answer for him to think a bit.
# Hopefully he made it

def checkProduct(val,N):
    if (int(val)%N == 0):
        print("\nSmallest product: " + val )
        return 1
    else:
        return 0
    
def checkSmallest(N):
    arr = [0] * 1000 #just assuming the size
    size = 3 #limit to 4 digit number only
    arr[0] = ""
    i = 1; 
    mark = 0 #checking
    
    while(len(arr[i-1])<=size):
        arr[i] = arr[i-1] + "5"
        
        mark = checkProduct(arr[i],N)
        if (mark == 1):
            break
            
        i+=1
        arr[i] = arr[i-2] + "7"
        
        mark = checkProduct(arr[i],N)
        if (mark == 1):
            break
        
        i+=1
        
    if (mark == 0):
        print("\n No product of N consists of 5 and/or 7")
    
N = int(input("N: "))
checkSmallest(N)
