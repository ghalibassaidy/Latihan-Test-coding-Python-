def select_balloons(balloons: list[tuple[str, int]]) -> list[tuple[str, int]]:
    best_ballons = {}

    for color, height in balloons:
        if color not in best_ballons:
            best_ballons[color] = height

        else:
            if height > best_ballons[color]:
                best_ballons[color] = height

    result = [(color, height) for color, height in best_ballons.items()]
    return result

data = [
  ("merah", 10),
  ("biru", 15),
  ("merah", 20),
  ("kuning", 5),
  ("biru", 12),
  ("hijau", 8)
]

print(select_balloons(data))
