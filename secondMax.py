if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    max1= -101
    max2= -101
    
    for num in arr:
        if num > max2:
            if num > max1:
                max2 = max1
                max1 = num
            elif num < max1:
                max2 = num
    print(max2)
                
    
        
