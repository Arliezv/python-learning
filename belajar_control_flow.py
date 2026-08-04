#belajar control flow

nilai = 75
angka = -5
n = 0
nama_sahabat = ["Lhaes", "Rizik", "Parit"]

#percabangan if elif else
print("===if elif else===")
if nilai >= 70:
    print("nilai kamu bagus")
elif nilai >= 50:
    print("nilai kamu cukup")
else:
    print("nilai kamu kurang")

#cek bilangan positif negatif
print("===cek bilangan===")
if angka > 0:
    print(angka, "adalah bilangan positif")
elif angka < 0:
    print(angka, "adalah bilangan negatif")
else:
    print(angka, "adalah nol")

#cek bilangan ganjil genap
print("===ganjil genap===")
if angka % 2 == 0:
    print(angka, "adalah bilangan genap")
else:
    print(angka, "adalah bilangan ganjil")

#for loop dengan range
print("===for loop range===")
for i in range(1, 6):
    print("perulangan ke-", i)

#for loop dengan list
print("===for loop list===")
for nama in nama_sahabat:
    print("sahabat:", nama)

#while loop
print("===while loop===")
while n < 3:
    n = n + 1
    print("n =", n)

#break menghentikan loop lebih awal
print("===break===")
for i in range(1, 8):
    if i == 6:
        break
    print("i =", i)

#continue melewati iterasi tertentu
print("===continue===")
for i in range(1, 8):
    if i % 2 == 0:
        continue
    print("bilangan ganjil:", i)
