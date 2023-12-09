def get_diffs(arr): 
    return [j - i for (i, j) in zip(arr[:-1], arr[1:])]

def extrapolate(seq):
    curr = seq
    layers = [seq]
    while not all([x == 0 for x in curr]):
        layers.append(get_diffs(curr))
        curr = layers[-1] 
    layers.reverse() 
    for i in range(len(layers)):    
        layer = layers[i]     
        if i == 0:
            layer.append(0)
            continue
        layer.append(layers[i - 1][-1] + layer[-1])
    return layers[-1][-1]

with open('9-input.txt', 'r') as f:
    lines = f.readlines()
    seqs = [[int(x) for x in line.split(' ')] for line in lines]
    preds = [] 
    for seq in seqs:
        preds.append(extrapolate(seq)) 
    print(f'PART ONE: {sum(preds)}')
