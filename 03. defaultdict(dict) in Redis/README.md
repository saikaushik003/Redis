### Hashes

Redis Hash = **key → field → value**

Similar to a Python `dict`.

```text
"user"
   │
   ├── name → Kaushik
   ├── age  → 21
   └── city → Hyderabad
```

---

#### `HSET` → Add / Update

```python
r.hset("user", "name", "Kaushik")
```

Similar Python:

```python
d["user"]["name"] = "Kaushik"
```

Multiple fields:

```python
r.hset(
    "user",
    mapping={
        "name": "Kaushik",
        "age": 21,
        "city": "Hyderabad"
    }
)
```

---

#### `HGET` → Get one value

```python
r.hget("user", "name")
```

Similar Python:

```python
d["user"]["name"]
```

---

#### `HGETALL` → Get everything

```python
r.hgetall("user")
```

Similar Python:

```python
d["user"]
```

Example:

```text
{
    'name': 'Kaushik',
    'age': '21',
    'city': 'Hyderabad'
}
```

---

#### `HDEL` → Delete a field

```python
r.hdel("user", "age")
```

Similar Python:

```python
del d["user"]["age"]
```

---

#### `HEXISTS` → Check if field exists

```python
r.hexists("user", "name")
```

Returns:

```text
True
```

Similar Python:

```python
"name" in d["user"]
```

---

#### `HKEYS` → Get all fields

```python
r.hkeys("user")
```

Output:

```text
['name', 'age', 'city']
```

Similar Python:

```python
d["user"].keys()
```

---

#### `HVALS` → Get all values

```python
r.hvals("user")
```

Output:

```text
['Kaushik', '21', 'Hyderabad']
```

Similar Python:

```python
d["user"].values()
```

---

### Quick Reference

| Redis | Python `dict` |
|---|---|
| `HSET -> r.hset(outer_key, mapping={key1: val1, key2: val2})` | `d[key][field] = value` |
| `HGET -> r.hget(outer_key, inner_key)` | `d[key][field]` |
| `HGETALL -> rhgetall(outer_key)` | `d[key]` |
| `HDEL -> r.hdel(outer_key, inner_key)` | `del d[key][field]` |
| `HEXISTS -> r.hexists(outer_key, inner_key)` `if inner_key in outer_key` | `field in d[key]` |
| `HKEYS -> r.hkeys(outer_key)` | `d[key].keys()` |
| `HVALS -> r.hvals(outer_key)` | `d[key].values()` |
