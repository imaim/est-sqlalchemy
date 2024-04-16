from unittest import mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from infra.entities.filmes import Filmes
#from infra.entities.atores import Atores
from .filmes_repository import FilmesRepository

class ConnectionHandlerMock:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [
                        mock.call.query(Filmes),
                    ],
                    [Filmes(titulo="Alice", genero="drama", ano=22)]
                ),                
                (
                    [
                        mock.call.query(Filmes),
                        mock.call.filter(Filmes.genero == "trasf")
                    ],
                    [Filmes(titulo="Rafael", genero="trasf", ano=12)]
                )
            ]
        )
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()

def test_select():
    filme_repository = FilmesRepository(ConnectionHandlerMock)
    
    response = filme_repository.select()
    print()
    print(response)
    assert isinstance(response, list)
    assert isinstance(response[0], Filmes)
        
def test_select_drama_filmes():
    filme_repository = FilmesRepository(ConnectionHandlerMock)
    
    response = filme_repository.select_drama_filmes()
    print()
    print(response)
    assert isinstance(response, Filmes)
    assert response.titulo == 'Rafael'
    