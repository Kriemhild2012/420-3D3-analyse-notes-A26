from models.cours import Cours


class Programme:
    def __init__(self, nom: str):
        self.nom = nom
        self.cours: list[Cours] = []

    def ajouter_cours(self, cours: Cours) -> None:
        self.cours.append(cours)

    def moyenne(self) -> float:
        if not self.cours:
            return 0.0
        return round(sum(c.moyenne() for c in self.cours) / len(self.cours), 1)

    def nb_etudiants(self) -> int:
        return sum(c.nb_etudiants() for c in self.cours)

    def to_dict(self) -> dict:
        return {
        "type": "programme",
        "nom": self.nom,
        "moyenne": self.moyenne(),
        "nb_etudiants": self.nb_etudiants(),
        "enfants": [c.to_dict() for c in self.cours]
    }