### Redis String / Counter

Redis Strings can be used as **counters**.

#### Set

```python
r.set("count", 0)
```

Similar to:

```python
d["count"] = 0
```

---

#### Increment

`INCR` → increments the value.

```python
r.incr("count", 2)
```

Similar to:

```python
d["count"] += 2
```

Example:

```python
r.set("count", 0)

r.incr("count", 2)
r.incr("count", 2)

print(r.get("count"))    # 4
```

---

#### Decrement

`DECR` → decrements the value.

```python
r.decr("count", 2)
```

Similar to:

```python
d["count"] -= 2
```

Example:

```python
r.set("count", 0)

r.incr("count", 2)
r.incr("count", 2)
r.decr("count", 2)

print(r.get("count"))    # 2
```

---

#### Get

```python
r.get("count")
```

Similar to:

```python
d["count"]
```

---

#### Missing Key

Redis automatically treats a missing key as `0` when using `INCR`.

```python
r.incr("count")
```

If `"count"` doesn't exist:

```text
count → 0 → 1
```

Similar to:

```python
from collections import defaultdict

d = defaultdict(int)

d["count"] += 1
```

Here:

```text
defaultdict(int)
      ↓
missing key → 0

Redis INCR
      ↓
missing key → 0
```

---

#### Quick Reference

| Redis | Python |
|---|---|
| `SET -> r.set(key, value)` | `d[key] = value` |
| `GET -> r.get(key)` | `d[key]` |
| `INCR -> r.incr(key)` | `d[key] += 1` |
| `INCRBY -> r.incr(key, n)` | `d[key] += n` |
| `DECR -> r.decr(key)` | `d[key] -= 1` |
| `DECRBY -> r.decr(key, n)` | `d[key] -= n` |

### Example

```python
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
```

Output:

```text
2
```
