from abc import ABC, abstractmethod


class Composant(ABC):

    def __init__(self, nom: str):
        self.nom = nom

    @abstractmethod
    def moyenne(self) -> float:
        pass

    @abstractmethod
    def nb_etudiants(self) -> int:
        pass

    @abstractmethod
    def to_dict(self) -> dict:
        pass