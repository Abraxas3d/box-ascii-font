# VHDL Box-Drawing Banner Generator

Generate ASCII art section headers for VHDL source files using Unicode box-drawing characters.

```
-- ╔═╗┬─┐┌─┐┬ ┬┬┌┬┐┌─┐┌─┐┌┬┐┬ ┬┬─┐┌─┐
-- ╠═╣├┬┘│  ├─┤│ │ ├┤ │   │ │ │├┬┘├┤ 
-- ╩ ╩┴└─└─┘┴ ┴┴ ┴ └─┘└─┘ ┴ └─┘┴└─└─┘
```

## Usage

### Generate a banner

```bash
python3 box_ascii.py "Architecture"
```

Output:
```
-- ╔═╗┬─┐┌─┐┬ ┬┬┌┬┐┌─┐┌─┐┌┬┐┬ ┬┬─┐┌─┐
-- ╠═╣├┬┘│  ├─┤│ │ ├┤ │   │ │ │├┬┘├┤ 
-- ╩ ╩┴└─└─┘┴ ┴┴ ┴ └─┘└─┘ ┴ └─┘┴└─└─┘
```

### Case matters

The font has two weights:

- **Uppercase** → Double-line box characters (╔═╗) — use for emphasis
- **lowercase** → Single-line box characters (┌─┐) — standard weight

```bash
python3 box_ascii.py "Libraries"    # L is heavy, ibraries is light
python3 box_ascii.py "MSK Modem"    # MSK and M are heavy
python3 box_ascii.py "CRITICAL"     # All heavy
```

### Use in Python

```python
from box_ascii import generate

header = generate("Entity", prefix="-- ")
print(header)
```

### Change the comment prefix

```python
generate("Module", prefix="// ")   # Verilog/C style
generate("Section", prefix="# ")   # Python/shell style
generate("Title", prefix="")       # No prefix
```

## Editing Characters

The box-drawing characters cause cursor chaos in most terminal editors (nano, vim, etc.). Use the helper script instead:

```bash
python3 edit_char.py
```

It displays a palette mapping ASCII keys to box pieces:

```
=== Single-line ===
  1=┌  2=─  3=┐
  4=│  5=   6=│
  7=└  8=─  9=┘
  q=├  w=┬  e=┤
  a=┴  s=┼

=== Double-line ===
  Q=╔  W=═  E=╗
  A=║  S=   D=║
  Z=╚  X=═  C=╝
  r=╠  t=╦  y=╣
  f=╩  g=╬
```

Type your glyph row-by-row using these codes. For example, uppercase R:

```
Which letter? R
Case (u)pper or (l)ower? u
  Top:    tW3
  Middle: rw3
  Bottom: f7X
```

The script outputs Python code ready to paste into `box_ascii.py`:

```python
    'R': ['╦═┐', '╠┬┐', '╩└═'],
```

## Character Reference

### Lowercase (single-line)

```
a       b       c       d        e       f       g       h       i
┌─┐     ┌┐      ┌─┐     ┌┬─┐     ┌─┐     ┌─┐     ┌─┐     ┬ ┬     ┬
├─┤     ├┴┐     │        │ │     ├┤      ├┤      │ ┬     ├─┤     │
┴ ┴     └─┘     └─┘     ─┴─┘     └─┘     ┴       └─┘     ┴ ┴     ┴

j       k       l       m       n       o       p       q       r
 ┬      ┬┌─     ┬       ┌┬┐     ┌┐┌     ┌─┐     ┌─┐     ┌─┐     ┬─┐
 │      ├┴┐     │       │││     │││     │ │     ├─┘     │ │     ├┬┘
└┘      ┴└─     └─┘     ┴ ┴     ┘└┘     └─┘     ┴       └─┼     ┴└─

s       t       u       v       w       x       y       z
┌─┐     ┌┬┐     ┬ ┬     ┬  ┬    ┬ ┬     ─┐┌─    ┬ ┬     ┌─┐
└─┐      │      │ │     └┐┌┘    │││      └┘     └┬┘     ┌─┘
└─┘      ┴      └─┘      └┘     └┴┘     ─┘└─     ┴      └─┘
```

### Uppercase (double-line)

```
A       B       C       D        E       F       G       H       I
╔═╗     ╔╗      ╔═╗     ╔╦═╗     ╔═╗     ╔═╗     ╔═╗     ╦ ╦     ╦
╠═╣     ╠╩╗     ║        ║ ║     ║╣      ║╣      ║ ╦     ╠═╣     ║
╩ ╩     ╚═╝     ╚═╝     ═╩═╝     ╚═╝     ╩       ╚═╝     ╩ ╩     ╩

J       K       L       M       N       O       P       Q       R
 ╦      ╦╔═     ╦       ╔╦╗     ╔╗╔     ╔═╗     ╔═╗     ╔═╗     ╦═╗
 ║      ╠╩╗     ║       ║║║     ║║║     ║ ║     ╠═╝     ║ ║     ╠╦╝
╚╝      ╩╚═     ╩═╝     ╩ ╩     ╝╚╝     ╚═╝     ╩       ╚═╬     ╩╚═

S       T       U       V       W       X       Y       Z
╔═╗     ╔╦╗     ╦ ╦     ╦  ╦    ╦ ╦      ╗╔     ╦ ╦     ╔═╗
╚═╗      ║      ║ ║     ╚╗╔╝    ║║║      ╚╝     ╚╦╝     ╔═╝
╚═╝      ╩      ╚═╝      ╚╝     ╚╩╝      ╝╚      ╩      ╚═╝
```

Uppercase glyphs use double-line box characters for visual weight.

## Requirements

- Python 3.6+
- A terminal/font that supports Unicode box-drawing characters (most modern terminals do)

## License

Public domain. Use it however you like.

## Contributing

Found a glyph that looks off? Use `edit_char.py` to design a better one and submit a PR.
