from typing import override
from typing import Any

from models.composant import Composant
from abc import ABC


class Composite(Composant, ABC):
    """Nœud intermédiaire — délègue à ses enfants."""

    def __init__(self, nom: str):
        super().__init__(nom)
        self._enfants: list[Composant] = []

    def ajouter(self, enfant: Composant) -> None:
        self._enfants.append(enfant)

    def retirer(self, enfant: Composant) -> None:
        self._enfants.remove(enfant)

    @override
    def moyenne(self) -> float:
        if not self._enfants:
            return 0.0
        return round(sum(e.moyenne() for e in self._enfants) / len(self._enfants), 1)

    @override
    def nb_etudiants(self) -> int:
        return sum(e.nb_etudiants() for e in self._enfants)

    @override
    def to_dict(self) -> dict:
        return {
            "type": self.__class__.__name__.lower(),  # ← "groupecours", "session", etc.
            "nom": self.nom,
            "moyenne": self.moyenne(),
            "nb_etudiants": self.nb_etudiants(),
            "enfants": [e.to_dict() for e in self._enfants]
        }
