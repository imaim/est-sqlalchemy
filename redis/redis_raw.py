""" Comandos Redis Basicos"""
import redis

redis_connection = redis.Redis(host='192.168.100.48', port=6379, db=0)
#print(redis_connection)
redis_connection.set("chave_1", "outrovalor")
valor = redis_connection.get('chave_1').decode("utf-8")
print(valor)

redis_connection.hset('meu_hash', 'nome', 'imaim')
redis_connection.hset('meu_hash', 'idade', 30)
redis_connection.hset('meu_hash', 'cidade', 'goiania')

nome = redis_connection.hget('meu_hash', 'nome').decode("utf-8")
cidade = redis_connection.hget('meu_hash', 'cidade').decode("utf-8")

print(nome)
print(cidade)