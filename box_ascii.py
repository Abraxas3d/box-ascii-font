#!/usr/bin/env python3
"""
Box-drawing ASCII art generator for VHDL comment banners.
Uses Unicode box-drawing characters for a clean, compact look.
"""

# Lowercase characters (single-line box drawing)
LOWER = {
    'a': ['┌─┐', '├─┤', '┴ ┴'],
    'b': ['┌┐ ', '├┴┐', '└─┘'],
    'c': ['┌─┐', '│  ', '└─┘'],
    'd': ['┌┬─┐', ' │ │', '─┴─┘'],
    'e': ['┌─┐', '├┤ ', '└─┘'],
    'f': ['┌─┐', '├┤ ', '┴  '],
    'g': ['┌─┐', '│ ┬', '└─┘'],
    'h': ['┬ ┬', '├─┤', '┴ ┴'],
    'i': ['┬', '│', '┴'],
    'j': [' ┬', ' │', '└┘'],
    'k': ['┬┌─', '├┴┐', '┴└─'],
    'l': ['┬  ', '│  ', '└─┘'],
    'm': ['┌┬┐', '│││', '┴ ┴'],
    'n': ['┌┐┌', '│││', '┘└┘'],
    'o': ['┌─┐', '│ │', '└─┘'],
    'p': ['┌─┐', '├─┘', '┴  '],
    'q': ['┌─┐', '│ │', '└─┼'],
    'r': ['┬─┐', '├┬┘', '┴└─'],
    's': ['┌─┐', '└─┐', '└─┘'],
    't': ['┌┬┐', ' │ ', ' ┴ '],
    'u': ['┬ ┬', '│ │', '└─┘'],
    'v': ['┬  ┬', '└┐┌┘', ' └┘ '],
    'w': ['┬ ┬', '│││', '└┴┘'],
    'x': ['─┐┌─', ' └┘ ', '─┘└─'],
    'y': ['┬ ┬', '└┬┘', ' ┴ '],
    'z': ['┌─┐', '┌─┘', '└─┘'],
}

# Uppercase characters (double-line box drawing)
UPPER = {
    'A': ['╔═╗', '╠═╣', '╩ ╩'],
    'B': ['╔╗ ', '╠╩╗', '╚═╝'],
    'C': ['╔═╗', '║  ', '╚═╝'],
    'D': ['╔╦═╗', ' ║ ║', '═╩═╝'],
    'E': ['╔═╗', '║╣ ', '╚═╝'],
    'F': ['╔═╗', '║╣ ', '╩  '],
    'G': ['╔═╗', '║ ╦', '╚═╝'],
    'H': ['╦ ╦', '╠═╣', '╩ ╩'],
    'I': ['╦', '║', '╩'],
    'J': [' ╦', ' ║', '╚╝'],
    'K': ['╦╔═', '╠╩╗', '╩╚═'],
    'L': ['╦  ', '║  ', '╩═╝'],
    'M': ['╔╦╗', '║║║', '╩ ╩'],
    'N': ['╔╗╔', '║║║', '╝╚╝'],
    'O': ['╔═╗', '║ ║', '╚═╝'],
    'P': ['╔═╗', '╠═╝', '╩  '],
    'Q': ['╔═╗', '║ ║', '╚═╬'],
    'R': ['╦═╗', '╠╦╝', '╩╚═'],
    'S': ['╔═╗', '╚═╗', '╚═╝'],
    'T': ['╔╦╗', ' ║ ', ' ╩ '],
    'U': ['╦ ╦', '║ ║', '╚═╝'],
    'V': ['╦  ╦', '╚╗╔╝', ' ╚╝ '],
    'W': ['╦ ╦', '║║║', '╚╩╝'],
    'X': [' ╗╔ ', ' ╚╝ ', ' ╝╚ '],
    'Y': ['╦ ╦', '╚╦╝', ' ╩ '],
    'Z': ['╔═╗', '╔═╝', '╚═╝'],
}

# Shared characters (numbers, punctuation, space)
SHARED = {
    ' ': ['  ', '  ', '  '],
    '0': ['┌─┐', '│ │', '└─┘'],
    '1': ['┐', '│', '┴'],
    '2': ['┌─┐', '┌─┘', '└─┘'],
    '3': ['┌─┐', ' ─┤', '└─┘'],
    '4': ['┬ ┬', '└─┤', '  ┴'],
    '5': ['┌─┐', '└─┐', '└─┘'],
    '6': ['┌─┐', '├─┐', '└─┘'],
    '7': ['┌─┐', '  │', '  ┴'],
    '8': ['┌─┐', '├─┤', '└─┘'],
    '9': ['┌─┐', '└─┤', '└─┘'],
    '_': ['   ', '   ', '───'],
    '-': ['   ', '───', '   '],
}

# Combined lookup
CHARS = {**LOWER, **UPPER, **SHARED}

def generate(text: str, prefix: str = "-- ") -> str:
    """
    Generate box-drawing ASCII art for the given text.
    Uppercase letters use double-line characters (╔═╗).
    Lowercase letters use single-line characters (┌─┐).
    
    Args:
        text: The text to render (case-sensitive)
        prefix: Comment prefix (default VHDL style)
    
    Returns:
        Three-line ASCII art string
    """
    lines = [[], [], []]
    
    for char in text:
        if char in CHARS:
            for i, row in enumerate(CHARS[char]):
                lines[i].append(row)
        else:
            # Unknown char -> placeholder
            for i in range(3):
                lines[i].append('?')
    
    result = []
    for line in lines:
        result.append(prefix + ''.join(line))
    
    return '\n'.join(result)


def main():
    import sys
    
    if len(sys.argv) > 1:
        text = ' '.join(sys.argv[1:])
    else:
        text = input("Enter text: ")
    
    print()
    print(generate(text))
    print()


if __name__ == "__main__":
    main()
