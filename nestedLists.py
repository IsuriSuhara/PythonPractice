from operator import itemgetter
if __name__ == '__main__':
    records=[]
    for _ in range(int(input())): 
        name = input()  
        score = float(input())
        record=[name,score]
        records.append(record)
    # min of all elements
    mn=min(records, key = itemgetter(1))[1]
    
    # remove elements equal to min
    filtered = [x for x in records if x[1] != mn]
    
    # get min of remaining
    mn_fil = min(filtered, key = itemgetter(1))[1]
    
    # filter remaining
    out = [x for x in filtered if x[1] == mn_fil]
    
    #sort by second element
    sortedOut = sorted(out, key = lambda x: x[0])
    
    #list with first elements in the sublists
    items = [item[0] for item in sortedOut]
    for i in items:
        print(i)
    
        
        
