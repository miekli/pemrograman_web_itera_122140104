
import modulku_mtk
import modulku_mtk as mo
from modulku_mtk import celsius_ke_fahrenheit, celsius_ke_kelvin
from modulku_mtk import *

while True:
    print("\n=== Program Matematika ===")
    print("1. Hitung Luas dan Keliling Geometri")
    print("2. Konversi Suhu")
    pilihan = input("Pilih operasi (1/2): ")

    if pilihan == "1":
        print("\n=== Hitung Geometri ===")
        print("Pilih bentuk:")
        print("1. Persegi")
        print("2. Persegi Panjang")
        print("3. Lingkaran")
        bentuk = input("Masukkan pilihan bentuk (1/2/3): ")

        if bentuk == "1":
            sisi = float(input("Masukkan panjang sisi persegi: "))
            print(f"[modulku_mtk] Luas Persegi: {modulku_mtk.luas_persegi(sisi)}")
            print(f"[mo] Keliling Persegi: {mo.keliling_persegi(sisi)}")

        elif bentuk == "2":
            panjang = float(input("Masukkan panjang: "))
            lebar = float(input("Masukkan lebar: "))
            print(f"[luas_persegi_panjang()] Luas Persegi Panjang: {luas_persegi_panjang(panjang, lebar)}")
            print(f"[keliling_persegi_panjang()] Keliling Persegi Panjang: {keliling_persegi_panjang(panjang, lebar)}")

        elif bentuk == "3":
            jari_jari = float(input("Masukkan jari-jari lingkaran: "))
            print(f"[modulku_mtk] Luas Lingkaran: {modulku_mtk.luas_lingkaran(jari_jari):.2f}")
            print(f"[mo] Keliling Lingkaran: {mo.keliling_lingkaran(jari_jari):.2f}")

        else:
            print("Pilihan bentuk tidak valid.")

    elif pilihan == "2":
        print("\n=== Konversi Suhu ===")
        suhu_celsius = float(input("Masukkan suhu dalam Celsius: "))
        print(f"[celsius_ke_fahrenheit()] {suhu_celsius}°C = {celsius_ke_fahrenheit(suhu_celsius)}°F")
        print(f"[celsius_ke_kelvin()] {suhu_celsius}°C = {celsius_ke_kelvin(suhu_celsius)}K")

    else:
        print("Pilihan operasi tidak valid.")

    # Tanya apakah ingin mengulang
    ulang = input("\nIngin melakukan perhitungan lagi? (y/n): ").lower()
    if ulang != 'y':
        print("Terima kasih telah menggunakan program ini!")
        break
