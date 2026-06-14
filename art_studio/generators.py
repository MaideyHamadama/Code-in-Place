from __future__ import annotations

import math


def build_tree(height: int, char: str) -> str:
    lines = []
    for level in range(height):
        width = level * 2 + 1
        padding = height - level - 1
        lines.append(" " * padding + char * width)
    trunk_width = max(1, height // 4)
    trunk_padding = height - trunk_width // 2 - 1
    for _ in range(max(2, height // 6)):
        lines.append(" " * trunk_padding + char * trunk_width)
    return "\n".join(lines)


def build_spiral(size: int, char: str) -> str:
    canvas = [[" " for _ in range(size)] for _ in range(size)]
    x = y = 0
    dx, dy = 1, 0
    steps = size
    counter = 0
    while steps > 0:
        for _ in range(steps):
            canvas[y][x] = char
            x += dx
            y += dy
        x -= dx
        y -= dy
        dx, dy = -dy, dx
        if counter % 2 == 1:
            steps -= 1
        x += dx
        y += dy
        counter += 1
    return "\n".join("".join(row) for row in canvas)


def build_wave(width: int, amplitude: int, char: str) -> str:
    lines = []
    for x in range(width):
        y = int((math.sin(x / 6.0) + 1) * amplitude)
        line = " " * y + char
        lines.append(line)
    return "\n".join(lines)


def build_mosaic(text: str, width: int) -> str:
    words = text.strip().split()
    if not words:
        return "".join("Mosaic must contain at least one word.")
    grid = []
    current_line = ""
    for word in words:
        if len(current_line) + len(word) + 1 > width:
            grid.append(current_line.center(width))
            current_line = word
        else:
            current_line = (current_line + " " + word).strip()
    if current_line:
        grid.append(current_line.center(width))
    border = "+" + "-" * width + "+"
    framed = [border] + [f"|{line}|" for line in grid] + [border]
    return "\n".join(framed)


def build_magic_quote(quote: str) -> str:
    padding = 4
    lines = [f"\"{quote}\""]
    width = max(len(line) for line in lines) + padding * 2
    border = "*" * width
    framed = [border] + ["*" + line.center(width - 2) + "*" for line in lines] + [border]
    return "\n".join(framed)
