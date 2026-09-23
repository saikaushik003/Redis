import redis

r = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)


# Tollywood - using LPUSH
r.lpush("tollywood", "NTR")
r.lpush("tollywood", "AA")
r.lpush("tollywood", "Prabhas")
r.lpush("tollywood", "MB")

# Bollywood - using RPUSH
r.rpush("bollywood", "Salman")
r.rpush("bollywood", "SRK")
r.rpush("bollywood", "Aamir")
r.rpush("bollywood", "Amithabh")

keys = r.keys("*")

for i in keys:
    print(f"{i}: {r.lrange(i, 0, -1)}")


r.rpop("bollywood")
r.lpop("tollywood")

print("__________________")

for i in keys:
    print(f"{i}: {r.lrange(i, 0, -1)}")

