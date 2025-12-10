def twoSumLoops(ints, target):
    for i in range(len(ints)):
        for j in range(i+1, len(ints)):
            if ints[i] + ints[j] == target:
                return i, j

def TwoSumDict():
    return

def twoSumLoopsAll():
    return

def TwoSumDictAll():
    return

def main():
    ints = [1, 67, 98, 2, 8, 0]
    target = 1
    print(twoSumLoops(ints, target))

if __name__ == "__main__": 
    main()