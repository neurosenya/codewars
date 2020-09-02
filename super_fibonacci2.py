def fib(n):
    def mult(x,y):
        if ( len(y) == 2 ):
            a = x[0]*y[0]+x[1]*y[1]
            b = x[2]*y[0]+x[3]*y[1]
            return [a,b]
        a = x[0]*y[0] + x[1]*y[2]
        b = x[0]*y[1] + x[1]*y[3]
        c = x[2]*y[0] + x[3]*y[2]
        d = x[2]*y[1] + x[3]*y[3]
        return [a,b,c,d]
    # Only works for positive powers!
    def matrix_power( x, n0 ):
        if ( n0 == 1 ):
            return x
        if ( n0%2 == 0 ):
            return matrix_power( mult(x, x), n0//2 )
        return mult(x, matrix_power( mult(x, x), n0//2 ) )
    # fibonacci example:
    A = [1,1,1,0]
    v = [1,0]
    if n < 0:
        if n + 1 != 0:
            return -1 * mult(matrix_power(A,n-1),v)[0]
    return mult(matrix_power(A,n-1),v)[0]

n = int(input())

print(fib(n))

