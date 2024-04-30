from datetime import datetime
from models.connection.reddis_connection import RedisConnectionHandler
from models.redis_repository import RedisRepository
from configs.start_form import start_form

""" redis_repository.insert("teste_01", 2024)
value = redis_repository.get('teste_01')

redis_repository.insert_hash("MeuHash", "campo_01", "este é meu valor")
value01 = redis_repository.get_hash("MeuHash", "campo_01")

redis_repository.insert_ex("cave_com_expirar", "vai_expirar", 5)

data_atual = datetime.now()
data_formatada = data_atual.strftime('%y-%m-%d')

redis_repository.insert_hash_ex(data_formatada, "banana", 3.12, 40)
redis_repository.insert_hash(data_formatada, "uva", 3.12)
redis_repository.insert_hash(data_formatada, "morango", 3.12)
"""
# 1. Conectar ao banco de dados(redis) e buscar elementos
redis_conn = RedisConnectionHandler().connect()
redis_repository = RedisRepository(redis_conn)

data_atual = datetime.now()
data_formatada = data_atual.strftime('%y-%m-%d')

hash_items = redis_conn.hgetall(data_formatada)
print(hash_items)

#######################################################################
# 2. Carregar dados ao formulario
python_dict = {}
for key, value in hash_items.items():
    python_dict[key.decode('utf-8')] = value.decode('utf-8')
    
print(python_dict)
start_form.load_info(python_dict)
#######################################################################
# 3. utilizar valor armazenado

value = start_form.get_info('morango')
print(value)