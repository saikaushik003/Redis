import redis

r = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

r.set("fruit", "apple")
r.set("vegetable", "tomato")

print(r.get("vegetable"))
