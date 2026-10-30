from models.feuille import Feuille

class Etudiant(Feuille):
    def __init__(self, prenom: str, nom_famille: str, evaluations: dict[str, float]):
        super().__init__(f"{prenom} {nom_famille}")
        self.prenom = prenom
        self.nom_famille = nom_famille
        self.evaluations = evaluations

    def nom_complet(self) -> str:
        return self.nom

    def moyenne(self) -> float:
        if not self.evaluations:
            return 0.0
        return round(sum(self.evaluations.values()) / len(self.evaluations), 1)

    def nb_etudiants(self) -> int:
        return 1

    def to_dict(self) -> dict:
        return {
            "type": "etudiant",
            "nom": self.nom,
            "moyenne": self.moyenne(),
            "nb_etudiants": 1,
            "evaluations": self.evaluations
        }