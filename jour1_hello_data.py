"""
Jour 1 - Mon Premier Script Data
Formation Data Analyst/Engineer
Démarré le : 3 Décembre 2024
"""

# ========================================
# PARTIE 1 : HELLO WORLD
# ========================================

print("=" * 50)
print("🎯 BIENVENUE DANS VOTRE FORMATION DATA !")
print("=" * 50)

# Variables simples
nom = "Christophe"
objectif = "Data Analyst/Engineer"
duree_mois = 5
heures_semaine = 20

# Affichage
print(f"\n👋 Bonjour {nom} !")
print(f"🎯 Objectif : {objectif}")
print(f"📅 Durée : {duree_mois} mois")
print(f"⏰ Engagement : {heures_semaine}h/semaine")

# ========================================
# PARTIE 2 : TYPES DE DONNÉES
# ========================================

print("\n" + "=" * 50)
print("📊 TYPES DE DONNÉES PYTHON")
print("=" * 50)

langage = "Python"
age = 30
salaire_cible = 45000.50
est_motive = True

print(f"\n1. String: {langage} (type: {type(langage).__name__})")
print(f"2. Integer: {age} (type: {type(age).__name__})")
print(f"3. Float: {salaire_cible}€ (type: {type(salaire_cible).__name__})")
print(f"4. Boolean: {est_motive} (type: {type(est_motive).__name__})")

# ========================================
# PARTIE 3 : CALCULS
# ========================================

print("\n" + "=" * 50)
print("🔢 CALCULS SIMPLES")
print("=" * 50)

heures_totales = duree_mois * 4 * heures_semaine
projets_totaux = duree_mois * 2
salaire_mensuel = salaire_cible / 12

print(f"\n⏱️  Heures totales formation : {heures_totales}h")
print(f"💻 Projets à réaliser : {projets_totaux}")
print(f"💰 Salaire mensuel cible : {salaire_mensuel:.2f}€")

# ========================================
# PARTIE 4 : LISTES
# ========================================

print("\n" + "=" * 50)
print("📋 TECHNOLOGIES À APPRENDRE")
print("=" * 50)

technologies = ["Python", "SQL", "Pandas", "Git", "Airflow", "Docker"]

print(f"\n📚 Nombre de technologies : {len(technologies)}")
print(f"🥇 Première : {technologies[0]}")
print(f"🏆 Dernière : {technologies[-1]}")

print("\n🗂️  Liste complète :")
for i, tech in enumerate(technologies, 1):
    print(f"   {i}. {tech}")

# ========================================
# PARTIE 5 : DICTIONNAIRE
# ========================================

print("\n" + "=" * 50)
print("📊 MON PROFIL DATA")
print("=" * 50)

profil = {
    "nom": nom,
    "objectif": objectif,
    "niveau_actuel": "Débutant",
    "niveau_cible": "Junior Data Engineer",
    "semaine": 1,
    "projets_completes": 0
}

print("\n👤 Profil :")
for cle, valeur in profil.items():
    print(f"   • {cle}: {valeur}")

# ========================================
# PARTIE 6 : STATISTIQUES
# ========================================

print("\n" + "=" * 50)
print("📈 PREMIERS CALCULS DATA")
print("=" * 50)

notes_python = [15, 18, 14, 19, 16, 17, 20]

moyenne = sum(notes_python) / len(notes_python)
note_max = max(notes_python)
note_min = min(notes_python)

print(f"\n📝 Notes : {notes_python}")
print(f"📊 Moyenne : {moyenne:.2f}/20")
print(f"🏆 Max : {note_max}/20")
print(f"⚠️  Min : {note_min}/20")

# ========================================
# CONCLUSION
# ========================================

print("\n" + "=" * 50)
print("✅ JOUR 1 TERMINÉ !")
print("=" * 50)

print(f"""
🎉 Félicitations {nom} !

Acquis aujourd'hui :
✅ Variables (string, int, float, boolean)
✅ Opérations mathématiques
✅ Listes et indexation
✅ Dictionnaires
✅ Boucles for
✅ Fonctions (len, sum, max, min)
✅ F-strings

🚀 Prochaine étape : Conditions et boucles avancées !
""")

print("=" * 50)
