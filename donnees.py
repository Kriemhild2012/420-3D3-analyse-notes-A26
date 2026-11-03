from models.etudiant import Etudiant
from models.groupe_cours import GroupeCours
from models.session import Session
from models.cours import Cours
from models.programme import Programme
from models.departement import Departement


def construire_programme() -> Programme:

    # --- Étudiants ---
    alice   = Etudiant("Alice",   "Tremblay", {"TP1": 78, "TP2": 85, "Examen": 91})
    bob     = Etudiant("Bob",     "Nguyen",   {"TP1": 65, "TP2": 70, "Examen": 74})
    carla   = Etudiant("Carla",   "Diaz",     {"TP1": 92, "TP2": 88, "Examen": 95})
    david   = Etudiant("David",   "Chen",     {"TP1": 55, "TP2": 62, "Examen": 68})
    fatima  = Etudiant("Fatima",  "Roy",      {"TP1": 80, "TP2": 75, "Examen": 77})
    gabriel = Etudiant("Gabriel", "Côté",     {"TP1": 71, "TP2": 69, "Examen": 73})
    hana    = Etudiant("Hana",    "Park",     {"TP1": 88, "TP2": 91, "Examen": 89})
    ivan    = Etudiant("Ivan",    "Leblanc",  {"TP1": 60, "TP2": 58, "Examen": 64})

    # --- 3D3 — Automne 2026 ---
    groupe_3d3_01 = GroupeCours("Groupe 01")
    groupe_3d3_01.ajouter(alice)
    groupe_3d3_01.ajouter(bob)

    groupe_3d3_02 = GroupeCours("Groupe 02")
    groupe_3d3_02.ajouter(carla)
    groupe_3d3_02.ajouter(david)

    session_3d3_a26 = Session("Automne 2026")
    session_3d3_a26.ajouter(groupe_3d3_01)
    session_3d3_a26.ajouter(groupe_3d3_02)

    # --- 3D3 — Automne 2025 ---
    groupe_3d3_a25_01 = GroupeCours("Groupe 01")
    groupe_3d3_a25_01.ajouter(Etudiant("Eva", "Martin", {"TP1": 85, "TP2": 90, "Examen": 88}))

    session_3d3_a25 = Session("Automne 2025")
    session_3d3_a25.ajouter(groupe_3d3_a25_01)

    cours_3d3 = Cours("3D3 — Programmation orientée objet")
    cours_3d3.ajouter(session_3d3_a26)
    cours_3d3.ajouter(session_3d3_a25)

    # --- 3R1 — Automne 2026 ---
    groupe_3r1_01 = GroupeCours("Groupe 01")
    groupe_3r1_01.ajouter(fatima)
    groupe_3r1_01.ajouter(gabriel)
    groupe_3r1_01.ajouter(hana)
    groupe_3r1_01.ajouter(ivan)

    session_3r1_a26 = Session("Automne 2026")
    session_3r1_a26.ajouter(groupe_3r1_01)

    cours_3r1 = Cours("3R1 — Réseaux informatiques")
    cours_3r1.ajouter(session_3r1_a26)

    # --- Départements ---
    departement_info = Departement("Département de l'informatique")
    departement_info.ajouter(cours_3d3)
    departement_info.ajouter(cours_3r1)

    # --- Programme ---
    programme = Programme("Techniques de l'informatique")
    programme.ajouter(departement_info)

    return programme
