from models.session import Session


class Cours:
    def __init__(self, nom: str):
        self.nom = nom
        self.sessions: list[Session] = []

    def ajouter_session(self, session: Session) -> None:
        self.sessions.append(session)

    def moyenne(self) -> float:
        if not self.sessions:
            return 0.0
        return round(sum(s.moyenne() for s in self.sessions) / len(self.sessions), 1)

    def nb_etudiants(self) -> int:
        return sum(s.nb_etudiants() for s in self.sessions)

    def to_dict(self) -> dict:
        return {
            "type": "cours",
            "nom": self.nom,
            "moyenne": self.moyenne(),
            "nb_etudiants": self.nb_etudiants(),
            "enfants": [s.to_dict() for s in self.sessions]
        }
