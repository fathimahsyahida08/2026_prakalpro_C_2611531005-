is_lulus = True
is_cumlaude = True

# Menggunakan Booleann
nilai = 85
batas_lulus = 75

# Menentukan nilai Boolean dari kondisi
status_kelulusan = nilai >= batas_lulus # Hasilnya akan True

print("=== Check kelulusan ===")
print("Nilai:", nilai)
print("Apakah Lulus?:", status_kelulusan)
if is_lulus and is_cumlaude:
    print("Selamat, Anda lulus dengan predikat Cumlaude!")


