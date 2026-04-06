# =============================================================
# SenSante - Script d'exploration des donnees patients
# Fichier : notebooks/exploration.py
# Auteur  : Fabrice
# Cours   : Integration de Modeles IA - Dr. El Hadji Bassirou TOURE
# =============================================================

import pandas as pd

# ------------------------------------------------------------
# 1. CHARGEMENT DES DONNEES
# ------------------------------------------------------------
print("=" * 50)
print("CHARGEMENT DES DONNEES")
print("=" * 50)

df = pd.read_csv("data/patients_dakar.csv")

print(f"Fichier charge avec succes !")
print(f"Nombre de patients : {df.shape[0]}")
print(f"Nombre de colonnes : {df.shape[1]}")

# ------------------------------------------------------------
# 2. APERCU DES DONNEES
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("APERCU DES 5 PREMIERES LIGNES")
print("=" * 50)
print(df.head())

print("\n" + "=" * 50)
print("TYPES DES COLONNES")
print("=" * 50)
print(df.dtypes)

# ------------------------------------------------------------
# 3. STATISTIQUES GENERALES
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("STATISTIQUES GENERALES")
print("=" * 50)
print(df.describe())

# ------------------------------------------------------------
# 4. VERIFICATION DES VALEURS MANQUANTES
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("VALEURS MANQUANTES PAR COLONNE")
print("=" * 50)
valeurs_manquantes = df.isnull().sum()
print(valeurs_manquantes)

if valeurs_manquantes.sum() == 0:
    print("=> Aucune valeur manquante ! Donnees completes.")
else:
    print(f"=> Attention : {valeurs_manquantes.sum()} valeurs manquantes detectees.")

# ------------------------------------------------------------
# 5. REPARTITION DES DIAGNOSTICS
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("REPARTITION DES DIAGNOSTICS")
print("=" * 50)
repartition_diagnostic = df["diagnostic"].value_counts()
print(repartition_diagnostic)
print()
for diagnostic, nombre in repartition_diagnostic.items():
    pourcentage = (nombre / len(df)) * 100
    print(f"  {diagnostic:<12} : {nombre} patients ({pourcentage:.1f}%)")

# ------------------------------------------------------------
# 6. REPARTITION PAR REGION
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("REPARTITION PAR REGION")
print("=" * 50)
print(df["region"].value_counts())

# ------------------------------------------------------------
# 7. REPARTITION PAR SEXE
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("REPARTITION PAR SEXE")
print("=" * 50)
print(df["sexe"].value_counts())

# ------------------------------------------------------------
# 8. STATISTIQUES PAR DIAGNOSTIC
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("AGE MOYEN PAR DIAGNOSTIC")
print("=" * 50)
print(df.groupby("diagnostic")["age"].mean().round(1))

print("\n" + "=" * 50)
print("TEMPERATURE MOYENNE PAR DIAGNOSTIC")
print("=" * 50)
print(df.groupby("diagnostic")["temperature"].mean().round(2))

# ------------------------------------------------------------
# 9. RESUME FINAL
# ------------------------------------------------------------
print("\n" + "=" * 50)
print("RESUME DU DATASET")
print("=" * 50)
print(f"  Total patients     : {len(df)}")
print(f"  Regions couvertes  : {df['region'].nunique()}")
print(f"  Age minimum        : {df['age'].min()} ans")
print(f"  Age maximum        : {df['age'].max()} ans")
print(f"  Age moyen          : {df['age'].mean():.1f} ans")
print(f"  Temperature min    : {df['temperature'].min()} C")
print(f"  Temperature max    : {df['temperature'].max()} C")
print("\nExploration terminee !")
