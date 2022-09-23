def hanoi(n, from_po, to_po, spare_po):
    if n == 1:
        print(from_po, to_po)
        return
    hanoi(n-1, from_po, spare_po, to_po)
    print(from_po, to_po)
    hanoi(n-1, spare_po, to_po, from_po)
    
n = int(input())
print(2**n - 1)
hanoi(n, 1, 3, 2)