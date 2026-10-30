from models.composant import Composant
from abc import ABC, abstractmethod

class Composite(Composant, ABC):
    """Nœud intermédiaire — délègue à ses enfants."""

    def __init__(self, nom: str, type_noeud: str):
        super().__init__(nom)
        self.type_noeud = type_noeud
        self._enfants: list[Composant] = []

    def ajouter(self, enfant: Composant) -> None:
        self._enfants.append(enfant)

    def retirer(self, enfant: Composant) -> None:
        self._enfants.remove(enfant)

    def moyenne(self) -> float:
        if not self._enfants:
            return 0.0
        return round(sum(e.moyenne() for e in self._enfants) / len(self._enfants), 1)

    def nb_etudiants(self) -> int:
        return sum(e.nb_etudiants() for e in self._enfants)

    def to_dict(self) -> dict:
        return {
            "type": self.type_noeud,
            "nom": self.nom,
            "moyenne": self.moyenne(),
            "nb_etudiants": self.nb_etudiants(),
            "enfants": [e.to_dict() for e in self._enfants]
        }