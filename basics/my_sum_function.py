def ma_sum(liste):
    sum = 0
    for element in liste:
        sum = sum + element
    return sum

notes = [1, 5, 17, 19, 11, 8, 15, 12]

print("sum natif : ", sum(notes))
print("ma_sum : ", ma_sum(notes)) 

print(1+5+17+19+11+8+15+12)


