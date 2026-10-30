from models.groupe_cours import GroupeCours


class Session:
    def __init__(self, nom: str):
        self.nom = nom
        self.groupes: list[GroupeCours] = []

    def ajouter_groupe(self, groupe: GroupeCours) -> None:
        self.groupes.append(groupe)

    def moyenne(self) -> float:
        if not self.groupes:
            return 0.0
        return round(sum(g.moyenne() for g in self.groupes) / len(self.groupes), 1)

    def nb_etudiants(self) -> int:
        return sum(g.nb_etudiants() for g in self.groupes)

    def to_dict(self) -> dict:
        return {
            "type": "session",
            "nom": self.nom,
            "moyenne": self.moyenne(),
            "nb_etudiants": self.nb_etudiants(),
            "enfants": [g.to_dict() for g in self.groupes]
        }
