# Sorted Sets

Redis Sorted Set = **unique members + score**

Members are automatically ordered by their score.

```text
Member    Score
----------------
Kaushik    65
Sai        70
Sam        90
```

---

### `ZADD` → Add

Add members with their scores.

```python
r.zadd(
    "leaderboard",
    {
        "Sai": 70,
        "Kaushik": 65,
        "Sam": 90
    }
)
```

---

### `ZRANGE` → Ascending Score

Returns members from **lowest score → highest score**.

```python
r.zrange("leaderboard", 0, -1)
```

Output:

```text
['Kaushik', 'Sai', 'Sam']
```

With scores:

```python
r.zrange(
    "leaderboard",
    0,
    -1,
    withscores=True
)
```

Output:

```text
[
    ('Kaushik', 65.0),
    ('Sai', 70.0),
    ('Sam', 90.0)
]
```

`0, -1` → first member to last member.

---

### `ZREVRANGE` → Descending Score

Returns members from **highest score → lowest score**.

```python
r.zrevrange("leaderboard", 0, -1)
```

Output:

```text
['Sam', 'Sai', 'Kaushik']
```

With scores:

```python
r.zrevrange(
    "leaderboard",
    0,
    -1,
    withscores=True
)
```

Output:

```text
[
    ('Sam', 90.0),
    ('Sai', 70.0),
    ('Kaushik', 65.0)
]
```

---

### `ZINCRBY` → Increment / Decrement Score

Increment a member's score.

```python
r.zincrby("leaderboard", 5, "Sam")
```

```text
Sam → 90
Sam → 95
```

Decrement using a negative value:

```python
r.zincrby("leaderboard", -5, "Sam")
```

---

### `ZSCORE` → Get Score

```python
r.zscore("leaderboard", "Sam")
```

Output:

```text
95.0
```

---

### `ZREM` → Remove Member

```python
r.zrem("leaderboard", "Sam")
```

Now `Sam` is removed from the Sorted Set.

---

### Add Member Again

If a member doesn't exist, `ZADD` adds it.

```python
r.zadd("leaderboard", {"Sam": 94})
```

Now:

```text
Sam → 94
```

---

### `ZCARD` → Number of Members

```python
r.zcard("leaderboard")
```

Similar Python:

```python
len(scores)
```

---

### `ZRANK` → Ascending Rank

Returns the rank based on **lowest → highest score**.

```python
r.zrank("leaderboard", "Sam")
```

Ranks start from `0`.

```text
Lowest score → Rank 0
Highest score → Last rank
```

---

### `ZREVRANK` → Descending Rank

Returns the rank based on **highest → lowest score**.

```python
r.zrevrank("leaderboard", "Sam")
```

```text
Highest score → Rank 0
Lowest score  → Last rank
```

---

### Complete Example

```python
import redis

r = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

r.zadd(
    "leaderboard",
    {
        "Sai": 70,
        "Kaushik": 65,
        "Sam": 90
    }
)

# Ascending
print(r.zrange("leaderboard", 0, -1))

# Descending
print(r.zrevrange("leaderboard", 0, -1))

# Descending with scores
print(
    r.zrevrange(
        "leaderboard",
        0,
        -1,
        withscores=True
    )
)

# Increment Sam's score
r.zincrby("leaderboard", 5, "Sam")

# Get Sam's score
print(r.zscore("leaderboard", "Sam"))

# Remove Sam
r.zrem("leaderboard", "Sam")

print(r.zrange("leaderboard", 0, -1))

# Add Sam again
r.zadd("leaderboard", {"Sam": 94})

print(
    r.zrevrange(
        "leaderboard",
        0,
        -1,
        withscores=True
    )
)

# Number of members
n = r.zcard("leaderboard")

# Increment Kaushik
r.zincrby("leaderboard", 30, "Kaushik")

# Ranks
rank_asc = r.zrank("leaderboard", "Sam")
rank_desc = r.zrevrank("leaderboard", "Sam")

print(r.zrange("leaderboard", 0, -1, withscores=True))
print(rank_asc, rank_desc)
```

---

### Quick Reference

| Redis | Purpose |
|---|---|
| `ZADD -> r.zadd(outer_key, {inner_key: val})` | Add / update member + score |
| `ZRANGE -> r.zrange(outer_key, 0, -1)` | Lowest → highest |
| `ZREVRANGE -> r.zrevrange(outer_key, 0, -1)` | Highest → lowest |
| `ZINCRBY -> r.zincrby(outer_key, value_to_be_incremented, inner_key)` | Increment / decrement score |
| `ZSCORE -> r.zscore(outer_key, inner_key)` | Get score |
| `ZREM -> r.zrem(outer_key, inner_key)` | Remove member |
| `ZCARD -> r.zcard(outer_key)` | Number of members |
| `ZRANK -> r.zrank(outer_key, inner_key)` | Ascending rank |
| `ZREVRANK -> r.zrevrank(outer_key, inner_key)` | Descending rank |

---

### Mental Model

```text
Sorted Set

Kaushik → 65
Sai     → 70
Sam     → 90

ZRANGE
   ↓
Kaushik → Sai → Sam

ZREVRANGE
   ↓
Sam → Sai → Kaushik
```
