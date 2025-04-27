📜 Soal Cerita Panjang: "Festival Balon Kerajaan"
Di sebuah kerajaan bernama CodeLandia, setiap tahun diadakan Festival Balon.
Ada N balon yang siap diterbangkan, masing-masing punya:

warna (string, misal "merah", "biru", dll)

tinggi terbang (integer, semakin besar semakin tinggi)

Karena raja perfeksionis, beliau hanya mau menerbangkan balon-balon dengan syarat:

Tidak ada dua balon dengan warna yang sama.

Total jumlah balon yang diterbangkan sebanyak-banyaknya.

Jika ada warna sama, ambil yang tingginya paling besar.

🎯 Tugas Anda:
Buat fungsi:

python
Salin
Edit
def select_balloons(balloons: list[tuple[str, int]]) -> list[tuple[str, int]]:
Yang menerima list balon (setiap balon = (warna, tinggi)),
dan mengembalikan list balon terpilih sesuai aturan di atas.

Balon terpilih:

Tidak ada warna kembar

Sudah otomatis pilih yang paling tinggi kalau warna kembar

Urutan balon hasil terserah (tidak perlu urut berdasarkan tinggi/warna)

📥 Contoh Input:
python
Salin
Edit
[
  ("merah", 10),
  ("biru", 15),
  ("merah", 20),
  ("kuning", 5),
  ("biru", 12),
  ("hijau", 8)
]
📤 Contoh Output:
python
Salin
Edit
[
  ("merah", 20),
  ("biru", 15),
  ("kuning", 5),
  ("hijau", 8)
]
(karena warna "merah" ada 2x, dipilih yang tinggi 20 — biru juga ambil yang tinggi 15)