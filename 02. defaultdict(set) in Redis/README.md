### Sets

Redis Set = **unordered collection of unique values**

Similar to Python `set`.

---

#### `SADD` → Add

```python
r.sadd("Tollywood", "NTR")
r.sadd("Tollywood", "AA")
r.sadd("Tollywood", "Prabhas")
r.sadd("Tollywood", "NTR")
```

Similar Python:

```python
s["Tollywood"].add("NTR")
```

Duplicate values are ignored.

---

#### `SREM` → Remove

```python
r.srem("Tollywood", "NTR")
```

Similar Python:

```python
s["Tollywood"].remove("NTR")
```

---

#### `SMEMBERS` → Get all values

```python
r.smembers("Tollywood")
```

Similar Python:

```python
s["Tollywood"]
```

Example:

```text
{'AA', 'Prabhas'}
```

Order is not guaranteed.

---

#### `SISMEMBER` → Check if value exists

```python
r.sismember("Tollywood", "AA")
```

Returns:

```text
True
```

Similar Python:

```python
"AA" in s["Tollywood"]
```

---

#### `SCARD` → Number of values

```python
r.scard("Tollywood")
```

Similar Python:

```python
len(s["Tollywood"])
```

---

### Set Operations

#### Union

Combines values from both sets.

```python
r.sunion("Tollywood", "Bollywood")
```

Similar Python:

```python
s["Tollywood"] | s["Bollywood"]
```

---

#### Intersection

Returns common values.

```python
r.sinter("Tollywood", "Bollywood")
```

Similar Python:

```python
s["Tollywood"] & s["Bollywood"]
```

---

#### Difference

Returns values present in the first set but not the second.

```python
r.sdiff("Tollywood", "Bollywood")
```

Similar Python:

```python
s["Tollywood"] - s["Bollywood"]
```

---

## Quick Reference

| Redis | Python `set` |
|---|---|
| `SADD -> r.sadd(key, val)` | `add()` |
| `SREM -> r.srem(key, val)` | `remove()` |
| `SMEMBERS -> r.smembers(key)` | `set` |
| `SISMEMBER -> r.sismember(key, val)` | `in` |
| `SCARD -> r.scard(key)` | `len()` |
| `SUNION -> r.sunion(key1, key2)` | `\|` |
| `SINTER -> r.sinter(key1, key2)` | `&` |
| `SDIFF -> r.sdiff(key1, key2)` | `-` |
