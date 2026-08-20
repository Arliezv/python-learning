# belajar control flow

# 1. percabangan if / elif / else
nilai = 75

print("=== if elif else ===")
if nilai >= 70:
    print("nilai kamu bagus")
elif nilai >= 50:
    print("nilai kamu cukup")
else:
    print("nilai kamu kurang")

# 2. cek bilangan positif / negatif / nol
angka = -5

print("=== cek bilangan ===")
if angka > 0:
    print(angka, "adalah bilangan positif")
elif angka < 0:
    print(angka, "adalah bilangan negatif")
else:
    print(angka, "adalah nol")

# 3. cek ganjil / genap
angka = -5

print("=== ganjil genap ===")
if angka % 2 == 0:
    print(angka, "adalah bilangan genap")
else:
    print(angka, "adalah bilangan ganjil")

# 4. for loop dengan range
print("=== for loop range ===")
for i in range(1, 6):
    print("perulangan ke-", i)

# 5. for loop dengan list
nama_sahabat = ["Lhaes", "Rizik", "Parit"]

print("=== for loop list ===")
for nama in nama_sahabat:
    print("sahabat:", nama)

# 6. while loop
n = 0

print("=== while loop ===")
while n < 3:
    n = n + 1
    print("n =", n)

# 7. break - stop loop lebih awal
print("=== break ===")
for i in range(1, 8):
    if i == 6:
        break
    print("i =", i)

# 8. continue - skip satu iterasi
print("=== continue ===")
for i in range(1, 8):
    if i % 2 == 0:
        continue
    print("bilangan ganjil:", i)

# 9. latihan: ubah nilai
nilai = 75  # coba ganti: 85, 70, 50

print("=== latihan nilai ===")
if nilai >= 80:
    print("nilai kamu bagus")
elif nilai >= 65:
    print("nilai kamu cukup")
else:
    print("nilai kamu kurang")

# 10. input + cek list dengan in
nama_sahabat = ["Lhaes", "Rizik", "Parit"]

print("=== input nama ===")
input_nama = input("masukkan nama: ")
if input_nama == "gie":
    print("halo bosss")
elif input_nama in nama_sahabat:
    print("halo", input_nama)
else:
    print("halo sahabat")
