### Lists / Queue / Deque

#### `LPUSH` → Left Push

Adds an element to the **left**.

```python
r.lpush("Tollywood", "NBK")
```

Similar Python `deque`:

```python
d["Tollywood"].appendleft("NBK")
```

---

#### `RPUSH` → Right Push

Adds an element to the **right**.

```python
r.rpush("Bollywood", "Salman")
```

Similar Python `deque`:

```python
d["Bollywood"].append("Salman")
```

---

#### Retrieve List

`LRANGE` retrieves elements from a Redis List.

```python
r.lrange("Bollywood", 0, -1)
```

`LRANGE` uses an **inclusive range**.

Example:

```text
['Salman', 'SRK', 'Aamir', 'Amithabh']
```

Similar Python:

```python
d["Bollywood"]
```

`0, -1` → from the first element to the last element.

---

#### Queue

**FIFO → First In, First Out**

```python
r.rpush("queue", "A")
r.rpush("queue", "B")
r.rpush("queue", "C")

r.lpop("queue")
```

```text
RPUSH → Add
LPOP  → Remove
```

---

#### Deque

**Double-Ended Queue**

Can add/remove from both ends.

```text
LPUSH → [ A B C ] ← RPUSH
LPOP  ← [ A B C ] → RPOP
```

```python
r.lpush("deque", "A")
r.rpush("deque", "B")

r.lpop("deque")
r.rpop("deque")
```

---

#### Keys

Get all Redis keys:

```python
r.keys("*")
```

Similar Python:

```python
d.keys()
```

---

#### Quick Reference

| Redis | Python `deque` |
|---|---|
| `LPUSH` | `appendleft()` |
| `RPUSH` | `append()` |
| `LPOP` | `popleft()` |
| `RPOP` | `pop()` |
| `LRANGE` | `deque` / slicing equivalent |
| `KEYS` | `dict.keys()` |
