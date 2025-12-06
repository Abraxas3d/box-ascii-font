#!/usr/bin/env python3
"""
Interactive character editor for box_ascii.py
Avoids the Unicode cursor nightmare in nano.
"""

# Box-drawing building blocks
PARTS = {
    # Single-line
    '1': '┌', '2': '─', '3': '┐',
    '4': '│', '5': ' ', '6': '│',
    '7': '└', '8': '─', '9': '┘',
    'q': '├', 'w': '┬', 'e': '┤',
    'a': '┴', 's': '┼', 'd': '╴',
    # Double-line
    'Q': '╔', 'W': '═', 'E': '╗',
    'A': '║', 'S': ' ', 'D': '║',
    'Z': '╚', 'X': '═', 'C': '╝',
    'r': '╠', 't': '╦', 'y': '╣',
    'f': '╩', 'g': '╬', 'h': '╡',
    # Mixed
    '!': '╤', '@': '╧', '#': '╪',
}

def show_palette():
    print("\n=== Single-line ===")
    print("  1=┌  2=─  3=┐")
    print("  4=│  5=   6=│")
    print("  7=└  8=─  9=┘")
    print("  q=├  w=┬  e=┤")
    print("  a=┴  s=┼")
    print("\n=== Double-line ===")
    print("  Q=╔  W=═  E=╗")
    print("  A=║  S=   D=║")
    print("  Z=╚  X=═  C=╝")
    print("  r=╠  t=╦  y=╣")
    print("  f=╩  g=╬")
    print("\n(Type literal chars for anything else)")

def decode_row(code):
    """Convert shorthand code to Unicode string."""
    result = []
    for c in code:
        result.append(PARTS.get(c, c))
    return ''.join(result)

def encode_row(unicode_str):
    """Convert Unicode string to shorthand (for display)."""
    reverse = {v: k for k, v in PARTS.items()}
    result = []
    for c in unicode_str:
        result.append(reverse.get(c, c))
    return ''.join(result)

def main():
    show_palette()
    
    print("\n" + "="*40)
    print("Enter three rows using the codes above.")
    print("Example for uppercase A:")
    print("  Row 1: QWE")
    print("  Row 2: rWy")
    print("  Row 3: f5f")
    print("="*40 + "\n")
    
    letter = input("Which letter? ").strip()
    case = input("Case (u)pper or (l)ower? ").strip().lower()
    
    print(f"\nEnter 3 rows for '{letter}' ({case}):")
    row1 = input("  Top:    ")
    row2 = input("  Middle: ")
    row3 = input("  Bottom: ")
    
    # Decode to Unicode
    u1 = decode_row(row1)
    u2 = decode_row(row2)
    u3 = decode_row(row3)
    
    print(f"\nPreview:")
    print(f"  {u1}")
    print(f"  {u2}")
    print(f"  {u3}")
    
    print(f"\nPython code to paste:")
    key = letter.upper() if case.startswith('u') else letter.lower()
    print(f"    '{key}': ['{u1}', '{u2}', '{u3}'],")

if __name__ == "__main__":
    main()
