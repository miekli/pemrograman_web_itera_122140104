
mahasiswa = [
    {"nama": "Mycahel N", "nim": "122140104", "nilai_uts": 90, "nilai_uas": 90, "nilai_tugas": 90},
    {"nama": "Adit", "nim": "122144562", "nilai_uts": 70, "nilai_uas": 65, "nilai_tugas": 75},
    {"nama": "Sopo", "nim": "125353135", "nilai_uts": 60, "nilai_uas": 55, "nilai_tugas": 65},
    {"nama": "Jarwo", "nim": "122412412", "nilai_uts": 90, "nilai_uas": 95, "nilai_tugas": 85},
    {"nama": "Adit Tolongin", "nim": "24112422", "nilai_uts": 50, "nilai_uas": 45, "nilai_tugas": 55},
]

for mhs in mahasiswa:
    nilai_akhir = (0.3 * mhs['nilai_uts']) + (0.4 * mhs['nilai_uas']) + (0.3 * mhs['nilai_tugas'])
    mhs['nilai_akhir'] = nilai_akhir

    if nilai_akhir >= 80:
        mhs['grade'] = 'A'
    elif nilai_akhir >= 70:
        mhs['grade'] = 'B'
    elif nilai_akhir >= 60:
        mhs['grade'] = 'C'
    elif nilai_akhir >= 50:
        mhs['grade'] = 'D'
    else:
        mhs['grade'] = 'E'

print("\n Nilai Akhir Mahasiswa :")
print(f"{'Nama':<15} {'NIM':<10} {'UTS':<5} {'UAS':<5} {'Tugas':<7} {'Akhir':<7} {'Grade':<5}")
for mhs in mahasiswa:
    print(f"{mhs['nama']:<15} {mhs['nim']:<10} {mhs['nilai_uts']:<5} {mhs['nilai_uas']:<5} {mhs['nilai_tugas']:<7} {mhs['nilai_akhir']:<7.2f} {mhs['grade']:<5}")

nilai_tertinggi = max(mahasiswa, key=lambda x: x['nilai_akhir'])
nilai_terendah = min(mahasiswa, key=lambda x: x['nilai_akhir'])

print("\nMahasiswa dengan nilai tertinggi:")
print(f"{nilai_tertinggi['nama']} ({nilai_tertinggi['nim']}) - Nilai Akhir: {nilai_tertinggi['nilai_akhir']:.2f}")

print("\nMahasiswa dengan nilai terendah:")
print(f"{nilai_terendah['nama']} ({nilai_terendah['nim']}) - Nilai Akhir: {nilai_terendah['nilai_akhir']:.2f}")
