class Etudiant:
    def __init__(self, prenom: str, nom_famille: str, evaluations: dict[str, float]):
        self.prenom = prenom
        self.nom_famille = nom_famille
        self.evaluations = evaluations

    def nom_complet(self) -> str:
        return f"{self.prenom} {self.nom_famille}"

    def moyenne(self) -> float:
        if not self.evaluations:
            return 0.0
        return round(sum(self.evaluations.values()) / len(self.evaluations), 1)

    def to_dict(self) -> dict:
        return {
            "type": "etudiant",
            "nom": self.nom_complet(),
            "moyenne": self.moyenne(),
            "nb_etudiants": 1,
            "evaluations": self.evaluations
        }