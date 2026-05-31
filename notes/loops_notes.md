
# Les Structures Répétitives (Les Boucles) en Python || Loops for/while

Une structure répétitive (plus communément appelée boucle) sert à répéter un bloc d'instructions plusieurs fois d'affilée sans avoir à dupliquer le code.

## À quoi ça sert ?
- **Éviter la duplication de code :** Ne pas écrire 100 fois la même ligne.
- **Automatiser des tâches :** Traiter des volumes de données (listes, fichiers).
- **Gérer des processus continus :** Attendre une action de l'utilisateur ou surveiller un événement.
- **Maintenir le code :** Si la logique change, on ne modifie qu'un seul endroit au lieu de corriger chaque ligne répétée.

---

## 1. La boucle `for` (Itération Déterminée)
On l'utilise lorsque l'on connaît **à l'avance** le nombre de répétitions à effectuer, ou pour parcourir tous les éléments d'une collection (liste, dictionnaire, chaîne de caractères).

### Syntaxe & Exemple :
```python
# Parcourir une plage de nombres de 1 à 5 inclus
for i in range(1, 6):
    print(f"Tour numéro {i}")
```

---

## 2. La boucle `while` (Itération Indéterminée)
On l'utilise lorsque le nombre de répétitions est **inconnu à l'avance**. La boucle s'exécute **tant qu'une condition spécifique reste vraie (`True`)**.

### Syntaxe & Exemple :
```python
continuer = True
while continuer:
    reponse = input("Voulez-vous rejouer ? (o/n) : ")
    if reponse.lower() == 'n':
        continuer = False # Arrête la boucle au prochain contrôle
```
*⚠️ **Danger :** Si la condition ne devient jamais fausse, la boucle devient **infinie** et fait planter le programme.*

---

## 3. Les instructions de contrôle
Ces mots-clés permettent de modifier le flux normal d'une boucle en cours de route :
- **`break`** : Stoppe et quitte immédiatement la boucle (sortie définitive).
- **`continue`** : Saute la fin du bloc actuel et passe directement à l'itération suivante (saut d'étape).
