# Week 12 regex

- [**`re`**](https://docs.python.org/3/library/re.html#module-re)
- [**Regular Expression HOWTO**](https://docs.python.org/3/howto/regex.html#regex-howto)
- regex101.com

### Some stuff

All metacharacters:

```python
. ^ $ * + ? { } [ ] \ | ( )
```
Lookahead: 
>`(?=...)`

Lookbehind:
>`(?<=...)`

Negative Lookahead:
>`(?!...)`

```python
# + taverna
# + versus
# + vera
# + zveri
# - zver
REGEXP_4 = r'(?!zver$)'  # Negative Lookahead!
```

Negatibe Lookbehind:
>`(?<!...)`


