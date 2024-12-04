def matrix_operation(array1,array2,a):
    if str(a)=='matrix':
        row_A1,col_A1=array1.shape
        row_A2,col_A2=array2.shape
        if col_A1!=row_A2:
            raise ValueError("Matrix multiplication cannot be performed")
        else:
            C = np.zeros((row_A1, col_A2))
            for i in range(row_A1):
                for j in range(col_A2):
                    for k in range(col_A1):
                        C[i, j] += array1[i, k] * array2[k, j]
            return C
    elif str(a)=='dot':
        if array1.shape!=array2.shape:
            raise ValueError('Given operation cannot be performed as arrays have different shape')
            
        else:
            array3=array1*array2
        return array3
            
    
