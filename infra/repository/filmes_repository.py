from infra.configs.connection import DBConnectionHandler
from infra.entities.filmes import Filmes
# teste
class FilmesRepository:
    def select(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Filmes).all()
            return data
        