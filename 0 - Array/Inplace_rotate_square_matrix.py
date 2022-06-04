def Inplace_rotate_square_matrix():
    
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    
    res = []
    for i in range(len(m[0])-1, -1, -1):
        
        sub = []
        for j in range(len(m)):
            sub += [m[j][i]]

        res.append(sub)

    print(res)
        
        
Inplace_rotate_square_matrix()

