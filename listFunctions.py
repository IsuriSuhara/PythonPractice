if __name__ == '__main__':
    N = int(input())
    myList = []
    for _ in range(N):
        name, *line = input().split()
        myNumbers = list(map(int,line))
        if name == "insert":
            myList.insert(myNumbers[0],myNumbers[1])
        if name == "remove":
            myList.remove(myNumbers[0])
        if name == "append":
            myList.append(myNumbers[0])
        if name == "sort":
            myList.sort()
        if name == "pop":
            myList.pop()
        if name == "reverse":
            myList.reverse()
        elif name == "print":
            print(myList)
            
            
        
    
