#belajar aritmatika

a = 12
b = 3

#tambah
print("===tambah===")
hasil = a + b
print("hasil = ", hasil)

#pengurangan
print("===pengurangan===")
hasil = a - b
print("hasil = ", hasil)

#perkalian
print("===perkalian===")
hasil = a * b
print("hasil = ", hasil)

#pembagian
print("===pembagian===")
hasil = a / b
print("hasil = ", hasil)

#pangkat
print("===pangkat===")
hasil = a ** b 
print("hasil = ", hasil)

#hasil (modulus) / sisa angka pembagian
print("===modulus===")
hasil = a % b 
print("hasil = ", hasil)

#floor division hasil (pembulatan pembagian)
print("===floor division===")  
hasil = a // b
print("hasil = ", hasil) 

# prioritas operasi, operational predance
x = 3
y = 2
z = 4

hasil = x + y * z
print(x,'+',y,'*',z, '=', hasil)
hasil = (x + y) * z
print('(',x,'+',y,')','*',z,'=', hasil)