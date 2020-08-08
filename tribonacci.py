def tribonacci(signature, n):
    sign_idx = 2
    if n <= sign_idx:
        return signature[:n]
    else:
        for i in range(3,n):
            signature.append(sum(signature[i-3 : i]))
        return signature


print(tribonacci([.5, .5, .5], 10))
