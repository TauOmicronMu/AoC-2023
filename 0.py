memo = {0: 540, 1: 25} 

def code(n):
    if n not in memo.keys():
        memo[n] = code(n - 1) + code(n - 2) 
    return memo[n]

if __name__ == '__main__':
    print(code(250))
