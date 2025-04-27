def select_balloons_id(balloons: list[tuple[int, str, int]]) -> list[tuple[int, str, int]]:
    best_balloons = {}

    for balloons_id, color, height in balloons:
        if color not in best_balloons:
            best_balloons[color] = [balloons_id, height]
        else:
            if height > best_balloons[color][1]:
                best_balloons[color] = [balloons_id, height]

    result = [(balloons_id, height, color) for color, (balloons_id, height) in best_balloons.items()]
    return result


data = [
  (1, "merah", 10),
  (2, "biru", 15),
  (3, "merah", 20),
  (4, "kuning", 5),
  (5, "biru", 12),
  (6, "hijau", 8)
]

print(select_balloons_id(data))
