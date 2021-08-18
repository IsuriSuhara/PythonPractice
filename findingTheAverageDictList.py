if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        
        #The * is being used to grab additional returns from the split statement.
        name, *line = input().split()
        #map(function, iterables)
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    scoreAverage=sum(student_marks[query_name])/len(student_marks[query_name])
    formal_float = "{:.2f}".format(scoreAverage)
    print(formal_float)
    
    
