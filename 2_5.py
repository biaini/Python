#Student Avakian Andranik

rating_list = [7,5,5,5,4,3,2,1]
score = 0
while score >= 0:
    i = 0
    score = int(input("Insert a rating score:\n"))
    
    
    for n in rating_list:
        if int(score) <= n:
            i += 1
        else:
            break
    rating_list.insert(i, int(score))
    print(rating_list)
    break
                
