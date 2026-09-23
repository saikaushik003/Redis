import redis

r = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)


r.hset("user", mapping = {"name": "Kaushik", "age": 21, "city": "Hyd"})


name = r.hget("user", "name")
print(name)


user_details = r.hgetall("user")
print(user_details)


r.hdel("user", "age")
print(r.hgetall("user"))


check = r.hexists("user", "name")

keys = r.hkeys("user")
print(keys)

vals = r.hvals("user")
print(vals)

