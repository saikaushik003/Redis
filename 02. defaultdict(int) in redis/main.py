import redis

r = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

r.set("count", 0)

r.incr("count", 2)
r.incr("count", 2)

r.decr("count", 2)

print(r.get("count"))
