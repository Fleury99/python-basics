def ma_len(liste):
    compteur = 0
    for _ in liste:
        compteur += 1
    return compteur


notes = [1, 5, 17, 19, 11, 8, 15, 12]

print("len natif : ", len(notes))
print("ma_len : ", ma_len(notes)) 

