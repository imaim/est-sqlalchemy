from models.connection.reddis_connection import RedisConnectionHandler
from models.redis.redis_repository import RedisRepository
from models.mysql.mysql_repository import MysqlRepository

redis_conn = RedisConnectionHandler().connect()
redis_repository = RedisRepository(redis_conn)
mysql_repository = MysqlRepository()

name = "Aroudo"

## logica
print("Buscando no redis ")
value = redis_repository.get(name)

if value:
    print("achei no redis ")
    print(value)
else:
    print("Buscando no mysql")
    value_2 = mysql_repository.select_by_name(name)
    if value_2:
        print(f"Achei no Mysql {value_2}")
        redis_repository.insert_ex(name, value_2, 40)
    else:
        print("não encontrado")