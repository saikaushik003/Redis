import redis

r = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)


r.sadd("tollywood", "NTR")
r.sadd("tollywood", "AA")
r.sadd("tollywood", "Prabhas")
r.sadd("tollywood", "NTR")
r.sadd("tollywood", "MB")

print(r.smembers("tollywood"))

r.srem("tollywood", "NTR")

#print(d["tollywood"])
print(r.smembers("tollywood"))

#if "AA" in d["tollywood"]
check = r.sismember("tollywood", "AA")

#len(d["tollywood"])
n = r.scard("tollywood")

print(f"if AA in check: {check}, len(d['tollywood']) = {n}")


r.sadd("bollywood", "Salman")
r.sadd("bollywood", "SRK")
r.sadd("bollywood", "Aamir")
r.sadd("bollywood", "Akshay")
r.sadd("bollywood", "AA")

#union
union = r.sunion("tollywood", "bollywood")

print(union)

#intersection
intersection = r.sinter("tollywood", "bollywood")
print(intersection)

#common is removed from the first with respect to first param
res = r.sdiff("tollywood", "bollywood")
print(res)
