import redis

r = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)


r.zadd("leaderboard", {"Sai": 70, "Kaushik": 65, "Sam": 90})

a = r.zrange("leaderboard", 0, -1)
b = r.zrevrange("leaderboard", 0, -1)

print(a, b)

c = r.zrevrange("leaderboard", 0, -1, withscores=True)

print(c)

r.zincrby("leaderboard", 5, "Sam")

print(r.zscore("leaderboard", "Sam"))

r.zrem("leaderboard", "Sam")

print(r.zrange("leaderboard", 0, -1))

r.zadd("leaderboard", {"Sam": 94})

print(r.zrevrange("leaderboard", 0, -1, withscores =True))

n = r.zcard("leaderboard")

r.zincrby("leaderboard", 30, "Kaushik")

rank_asc = r.zrank("leaderboard", "Sam")

rank_desc = r.zrevrank("leaderboard", "Sam")

print(r.zrange("leaderboard", 0, -1, withscores=True))
print(rank_asc, rank_desc)
