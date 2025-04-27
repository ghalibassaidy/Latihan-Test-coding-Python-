📜 Soal Upgrade Level: "Festival Balon - ID Challenge"
Sekarang...
Setiap balon punya ID unik (integer) selain warna dan tinggi.

Format input sekarang:

python
Salin
Edit
(id, warna, tinggi)
🎯 Tugas Baru:
Buat fungsi:

python
Salin
Edit
def select_balloons_with_id(balloons: list[tuple[int, str, int]]) -> list[tuple[int, str, int]]:
Yang:

Tetap pilih 1 balon per warna (tinggi tertinggi).

Tapi sekarang... balikin ID balon terpilih juga!

Jadi, ID penting! Jangan ilangin!

📥 Contoh Input:
python
Salin
Edit
[
  (1, "merah", 10),
  (2, "biru", 15),
  (3, "merah", 20),
  (4, "kuning", 5),
  (5, "biru", 12),
  (6, "hijau", 8)
]
📤 Contoh Output:
python
Salin
Edit
[
  (3, "merah", 20),
  (2, "biru", 15),
  (4, "kuning", 5),
  (6, "hijau", 8)
]
Balon ID 3 (merah 20) dipilih karena lebih tinggi dari ID 1.

Balon ID 2 (biru 15) dipilih karena lebih tinggi dari ID 5.

