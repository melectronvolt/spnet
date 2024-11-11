# 🚧 Site en construction 🚧

# Courbes et points
```python
# matplotlib est la bibliothèque qui permet de tracer les graphiques
import matplotlib.pyplot as plt

plt.clf()

X = [0, 0.021, 0.039, 0.063]  # Valeur des x
Y = [0, 0.54, 1.08, 1.62]  # Valeur des y

plt.plot(X, Y, '-x', color='blue')  # On relie les points
plt.plot(X, Y, 'x', color='red')  # On ne relie pas les points

X2 = [0.045]
Y2 = [0.85]

plt.plot(X2, Y2, 'o', color='green', markersize=20) # Ajoute un gros point vert 

plt.xlabel("Légende des abscisses")
plt.ylabel("Légende des ordonnées")
plt.title("Titre du graphique")

plt.grid()  # Si on veut afficher une grille
plt.show()  # Afficher l'image
```
## Changer les axes
```python
plt.xlim(-0.01, 0.07)  # Limites pour l'axe des abscisses (x)
plt.ylim(-0.1, 2)      # Limites pour l'axe des ordonnées (y)
```
## Changer les graduations
```python
# graduation majeur de [0 à 1[ de 0.1 en 0.1
plt.xticks(np.arange(0,1,0.1))
# Affiche les sous-graduations
plt.minorticks_on()
```
## Tracer une régression linéaire (conductimétrie)
Copier ce bout de code en haut du script : 
```python
import numpy as np
def trace_regression_lineaire(plt, X, Y, nb_points_depart, nb_points_fin, intervalle, couleur):
    # Sélectionner les sous-listes des X et Y entre nb_points_depart et nb_points_fin
    X_sub = X[nb_points_depart:nb_points_fin+1]
    Y_sub = Y[nb_points_depart:nb_points_fin+1]
    
    # Effectuer la régression linéaire
    fit = np.polyfit(X_sub, Y_sub, 1)  # Polyfit de degré 1 pour la régression linéaire
    pente, intercept = fit
    
    # Créer les valeurs de X pour tracer la ligne dans l'intervalle fourni
    X_ligne = np.linspace(intervalle[0], intervalle[1], 100)
    Y_ligne = pente * X_ligne + intercept
    
    # Tracer la ligne de régression avec la couleur choisie en pointillé
    plt.plot(X_ligne, Y_ligne, linestyle='--', color=couleur, label=f"Régression linéaire (indices {nb_points_depart}-{nb_points_fin})")
```
Que l’on utilisera ensuite ainsi : 
```python
trace_regression_lineaire(plt, X, Y, 1, 2, [0.02, 0.1], 'green')
```
# Tracer une droite
## Verticale
```python
import matplotlib.pyplot as plt
plt.clf()
plt.figure()

# Tracer une ligne verticale à x=5
plt.axvline(x=5, color='green', linestyle='--', label="Ligne verticale (x=5)")

plt.grid(True)
plt.legend()
plt.show()
```
## Horizontale
```python
# Tracer une ligne verticale à x=5
plt.axhline(y=10, color='purple', linestyle='-', label="Ligne horizontale (y=10)")
```
# Ajouter du texte
```python
# Importation de la bibliothèque matplotlib
import matplotlib.pyplot as plt

plt.clf()
plt.figure()

# Ajouter du texte à des endroits spécifiques
plt.text(6, 12, "Texte1", fontsize=12, color='blue')  # Texte au point (6, 12)
plt.text(2, 8, "Texte2", fontsize=12, color='red')   # Texte au point (2, 8)
plt.text(8, 4, "Texte3", fontsize=12, color='orange')  # Texte au point (8, 4)

# Ajouter un titre et des légendes aux axes
plt.title("Exemple de ligne verticale, horizontale et de texte")
plt.xlabel("Axe des X")
plt.ylabel("Axe des Y")

plt.xlim(0,10)
plt.ylim(0,15)

plt.grid(True)
plt.legend()
plt.show()
```

# Regression linéaire
```python
import matplotlib.pyplot as plt
import numpy as np # Bibliothèque scientifique

plt.clf()
X = np.array([0, 0.021, 0.039, 0.063])
Y = np.array([0, 0.84, 1.45, 2.4])

plt.plot(X, Y, 'x', color='blue')  # On trace

plt.xlabel("Légende des abscisses")
plt.ylabel("Légende des ordonnées")
plt.title("Titre du graphique")

plt.grid()

# Demande à Numpy de trouver les coefficients a et b pour y = a x + b
fit = np.polyfit(X, Y, 1)

coefficient_directeur = fit[0] #a dans y = ax + b
print("coefficient directeur :", coefficient_directeur)

ordonnee_origine = fit[1] #b dans y = ax + b
print("ordonnée à l'origine:", ordonnee_origine)

print("Equation : y = " + str(coefficient_directeur) + ' x + ' + str(ordonnee_origine) )
Modelisation = coefficient_directeur * X + ordonnee_origine
plt.plot(X, Modelisation, color='red')

plt.show()
```
# Modélisation par une parabole
```python
import numpy as np
import matplotlib.pyplot as plt

dt = 0.03333333333333333
y= np.array([42.719, 42.719, 42.719, 43.263, 43.263, 43.535, 43.535, 43.824, 44.096, 44.367999999999995, 44.367999999999995, 44.64, 44.929, 45.745000000000005, 45.473, 46.306, 46.306, 46.577999999999996, 46.577999999999996, 47.68299999999999, 47.955, 47.955, 48.227, 48.788, 49.06, 49.332, 50.437, 50.437, 50.437, 51.27, 52.086, 52.64699999999999, 53.190999999999995, 53.752, 53.752, 54.023999999999994, 55.401, 55.961999999999996, 56.778000000000006, 57.339, 57.339, 57.883, 58.715999999999994, 59.821, 60.36500000000001, 61.19799999999999, 60.926, 62.303, 62.575, 63.952, 65.057, 65.329, 65.329, 66.706, 67.539, 68.37199999999999, 69.188, 70.565, 70.854, 71.398, 72.77499999999999, 73.88, 74.713, 76.09, 76.09, 76.92299999999999, 78.011, 79.405, 80.221, 81.887, 81.887, 82.99199999999999, 83.808, 85.47399999999999])

# Création du tableau de temps
t = np.arange(len(y)) * dt

# Ajustement par une parabole
coeffs = np.polyfit(t, y, 2)
a = coeffs[2]
b = coeffs[1]
c = coeffs[0]

print("Les coefficients de la parabole sont y(t) = a + b t + c t^2 :")
print("a = ", a)
print("b = ", b)
print("c = ", c)

# Génération des valeurs ajustées
t_fit = np.linspace(t[0], t[-1], 500)
y_fit = np.polyval(coeffs, t_fit)

# Tracé des points de données et de la courbe ajustée
plt.figure(figsize=(8, 6))
plt.plot(t, y, 'o', label='Données')
plt.plot(t_fit, y_fit, '-', label='Ajustement quadratique')
plt.xlabel('Temps t')
plt.ylabel('Valeur y')
plt.title('Ajustement parabolique des données')
plt.legend()
plt.grid(True)
plt.show()
```
# Histogramme
```python
import numpy as np
import matplotlib.pyplot as plt
plt.clf()
pH1 = [1,2,3,4,5,2,3,1,2] # A completer avec les mesures du papier pH
pH2 = [2,3,1,4,2,1,2,1,3] # A completer avec les mesures du pH-metre
plt.hist(pH1, 10, label='Mesures Serie 1') # 10 groupes de mesures
plt.hist(pH2, 10, label='Mesures Serie 2')

plt.xlabel("Mesures")
plt.ylabel("Nombre de mesures")
plt.title("Histogramme de la serie de mesures")
plt.legend()
plt.show()
```
# Dérivée (par exemple pour un dosage)

> [!WARNING] Deux axes
> Ici c’est plus délicat car il y a deux axes, un à droite et un à gauche. Cela correspond pour matplotlib à deux subplots

```python
# Importation de la bibliothèque matplotlib pour tracer les graphiques
import matplotlib.pyplot as plt
import numpy as np

plt.clf()

# Liste des volumes de NaOH en mL
volumes = [
    0, 0.75, 2.16, 3.42, 4.52, 5.48, 6.29, 6.98, 7.55, 8.02, 8.41, 8.72, 8.97,
    9.18, 9.34, 9.48, 9.58, 9.67, 9.74, 9.79, 9.83, 9.91, 9.93, 9.96, 9.98,
    9.99, 10.00, 10.01, 10.02, 10.04, 10.07, 10.12, 10.15, 10.27, 10.34, 10.43,
    10.54, 10.69, 10.87, 11.11, 11.41, 11.79, 12.29, 12.94, 13.8, 14.95
]

# Liste des valeurs de pH correspondantes
pH = [
    1.3, 1.35, 1.45, 1.55, 1.65, 1.76, 1.85, 1.95, 2.05, 2.15, 2.26, 2.36, 2.45,
    2.55, 2.66, 2.75, 2.85, 2.95, 3.05, 3.15, 3.25, 3.5, 3.6, 3.85, 4.1,
    4.35, 7.6, 8.6, 9.85, 10.1, 10.35, 10.6, 10.7, 10.95, 11.05, 11.15, 11.25,
    11.35, 11.45, 11.55, 11.65, 11.75, 11.85, 11.95, 12.05, 12.15
]

# Calcul de la dérivée (différence entre valeurs adjacentes)
dpH = np.diff(pH)
dV = np.diff(volumes)

# Calcul de la dérivée du pH par rapport au volume (dpH/dV)
derivative = dpH / dV

# Créer la figure et l'axe principal
fig, ax1 = plt.subplots()

# Tracer la courbe de pH en fonction du volume de NaOH ajouté sur l'axe principal (gauche)
ax1.plot(volumes, pH, 'o-', color='blue', label="pH en fonction du volume de NaOH ajouté")
ax1.set_xlabel("Volume ajouté (mL)")
ax1.set_ylabel("Valeur du pH", color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# Créer un deuxième axe y partageant le même axe x
ax2 = ax1.twinx()

# Tracer la courbe de la dérivée du pH par rapport au volume sur le second axe (droite)
ax2.plot(volumes[:-1], derivative, 'o-', color='red', label="Dérivée du pH par rapport au volume")
ax2.set_ylabel("Dérivée du pH (dpH/dV)", color='red')
ax2.tick_params(axis='y', labelcolor='red')

# Ajouter une grille à l'axe principal
ax1.grid(True)

# Afficher le graphique
plt.title("Courbe de titrage : pH et sa dérivée en fonction du volume ajouté")
plt.show()

```
## Changer l’échelle 
### Verticale
```python
ax2.set_ylim(0,20)
```
### Horizontale
```python
ax2.set_ylim(0,20)
```
## Changer les graduations des axes
```python
# graduation majeur de [0 à 20[ de 1 en 1
ax1.set_xticks(np.arange(0,20,1))
# Sous graduation de [0 à 20[] de 0.5 à 0.5
ax1.set_xticks(np.arange(0,20,0.5),minor=True)
```
# Fonctions utiles
```python
import random
import numpy as np

# -------------------------
#   Générer des listes
# -------------------------

# Générer une liste de 50 valeurs aléatoires entre -100 et 100
valeurs_aleatoires = [random.randint(-100, 100) for _ in range(50)]
# Générer une liste de 50 valeurs entre 0, 49
valeurs = np.arange(50)

# -------------------------
#      Dérivée
# -------------------------

# Calcul de la dérivée de la liste des valeurs aléatoires
derivative_aleatoires = np.diff(valeurs_aleatoires)
derivative_valeurs = np.diff(valeurs)
derivative = derivative_aleatoires / derivative_valeurs

# -------------------------
#   Fonctions utiles
# -------------------------

# Trouver l'indice du maximum dans valeurs_aleatoires
indice_max = np.argmax(valeurs_aleatoires)
# Trouver la valeur correspondante dans la liste valeurs
valeur_correspondante = valeurs[indice_max]

# Calculer la moyenne et l'écart type
moyenne = np.mean(valeurs_aleatoires)
ecart_type = np.std(valeurs_aleatoires)
print("Moyenne : ", moyenne)
print("ecart_type : ", ecart_type)

```
## Trouver la valeur maximale d’une liste
```python
# Trouver l'indice du maximum dans valeurs_aleatoires
indice_max = np.argmax(valeurs_aleatoires)
# Trouver la valeur correspondante dans la liste valeurs
valeur_correspondante = valeurs[indice_max]
```
# Import / Exporter des fichiers CSV

```{admonition} Séparateurs décimaux et délimiteurs
:class: note

- Dans un fichier CSV, les données sont séparées par **délimiteurs**.
- Si nous travaillons avec des données numériques il faut aussi tenir compte du **séparateur décimal** qui peut être une virgule
```


## ⏬Importer des données
```python
import pandas as pd
import numpy as np

# Spécifier le chemin vers ton fichier CSV
fichier_csv = "ton_fichier.csv"

# Charger le fichier CSV avec les options spécifiques
df = pd.read_csv(
    fichier_csv,        # Le fichier CSV à charger
    skiprows=5,         # Omet les 5 premières lignes
    delimiter=';',      # Définit le délimiteur comme un point-virgule (;)
    decimal=',',        # Définit la virgule comme séparateur décimal
    header=2            # Utilise la 3ème ligne (index 2) pour les noms des colonnes
)

# Récupérer une colonne spécifique dans une liste numpy
# Ici, on suppose que la colonne qui nous intéresse s'appelle 'ColonneCible'
colonne_numpy = df['ColonneCible'].to_numpy()

# Afficher la colonne sous forme de tableau numpy
print(colonne_numpy)
```
## ⏫Exporter les données
```python
import pandas as pd
import numpy as np

# Exemple de trois listes NumPy
liste1 = np.array([1.2, 2.4, 3.6])
liste2 = np.array([10, 20, 30])
liste3 = np.array(['A', 'B', 'C'])

# Créer un DataFrame à partir des listes NumPy
df = pd.DataFrame({
    'Liste1': liste1,
    'Liste2': liste2,
    'Liste3': liste3
})

# Spécifier le chemin où tu veux sauvegarder le fichier CSV
fichier_csv_export = "mes_listes_exportees.csv"

# Exporter le DataFrame vers un fichier CSV
df.to_csv(
    fichier_csv_export,  # Le fichier CSV de destination
    sep=';',             # Utilise un point-virgule comme délimiteur
    decimal=',',         # Utilise la virgule comme séparateur décimal
    index=False,         # Omet l'index lors de l'exportation
    header=True          # Inclut les noms des colonnes dans l'export
)

print("Listes NumPy exportées avec succès dans le fichier CSV !")

```

```{toctree}
:caption: Contents:

about
```



