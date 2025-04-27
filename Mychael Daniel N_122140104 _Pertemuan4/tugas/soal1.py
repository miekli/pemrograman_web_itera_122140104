berat = float(input("Input Berat: "))
tinggi = float(input("Input tinggi : "))
bmi = berat / (tinggi * tinggi)

print(f"7Body Mass Index Anda: {bmi:.2f}")

if bmi < 18.5:
    keterangan = "Berat badan kurang"
elif 18.5 <= bmi < 25:
    keterangan = "Berat badan normal"
elif 25 <= bmi < 30:
    keterangan = "Berat badan berlebih"
else:
    keterangan = "Obesitas"

print(f"Kategori BMI: {keterangan}")
