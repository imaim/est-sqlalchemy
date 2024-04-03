from infra.repository.filmes_repository import FilmesRepository

repo = FilmesRepository()

data = repo.select()

print(data)
