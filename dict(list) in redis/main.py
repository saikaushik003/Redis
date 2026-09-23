import redis

r = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

r.lpush("tollywood", "NTR")
r.lpush("tollywood", "AA")
r.lpush("tollywood", "Prabhas")
r.lpush("tollywood", "MB")
r.lpush("bollywood", "Salman")
r.lpush("bollywood", "SRK")
r.lpush("bollywood", "Aamir")
r.lpush("bollywood", "Amithabh")

keys = r.keys("*")

for i in keys:
    print(f"{i}: {r.lrange(i, 0, )}")
