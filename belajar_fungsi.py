# belajar fungsi

# 1. fungsi paling sederhana
def sapa():
    print("halo, selamat belajar!")

sapa()

# 2. fungsi dengan parameter
def sapa_nama(nama):
    print("halo", nama)

sapa_nama("lhaes")

# 3. fungsi dengan return
def tambah(a, b):
    return a + b

hasil = tambah(3, 5)
print("3 + 5 =", hasil)

# 4. fungsi dengan banyak parameter
def hitung_luas(panjang, lebar):
    return panjang * lebar

print("luas:", hitung_luas(4, 6))

# 5. default argument
def sapa_lagi(nama="teman"):
    print("halo", nama)

sapa_lagi("lhaes")
sapa_lagi()  # pakai default: "teman"

# 6. local vs global
x = 10  # ini global

def coba():
    x = 5  # ini local, beda dari x global
    print("dalam fungsi:", x)

coba()
print("di luar fungsi:", x)
