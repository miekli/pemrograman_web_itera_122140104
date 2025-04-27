
# pemrograman_web_itera_122140104 Pertemuan 1
Tugas 1,2 dan 3 pertemuan 1 langsung dalam 1 file

# pemrograman_web_itera_122140104 Pertemuan 2
Dashboard Jadwal Kuliah dan Tugas – Mychael Daniel N
Halo! Ini aplikasi dashboard sederhana yang aku buat buat nyatet jadwal mata kuliah dan tugas-tugas. Jadi kita bisa lebih inget ada kelas apa aja dan tugas mana yang belum dikerjain untuk pribadilah dashboard ini cuy
a. Fungsinya ngapain aja?
- Nampilin daftar mata kuliah dan jadwalnya
- Bisa tambah mata kuliah sendiri dan jadwalnya
- Bisa hapus juga kalau udah gak perlu matkulnya
- Ada countdown ke jadwal kuliah biar tau kapan dimulai
- nah ada tombol acces yang bisa ngeliat google meet pembelajaran , serta tugas yang ada di pertemuan matakuliah tersebut , nanti bisa nambah deadline mata kuliah trus bisa ngenyimpan jawaban sementara yang mungkin sudah masuk ke dalam pikiran awalnya...

Fitur ES6+ yang aku pake:
- let dan const agar variabel gak kacau
- Arrow functions (kayak pas ngerender card, ambil data, mapping waktunya juga , converter data juga)
- Template literals (tujuan aku buat itu ya untuk nulis HTML di JS gampang)
- Async/Await (untuk ambil data dari localStorage, walaupun masih lokal sih )
- Classes (buat bikin objek Subject sama Task, jadi rapi)

Screenshot : 
![image](https://github.com/user-attachments/assets/a556c78b-e70c-4d97-ae74-33c5059b79b5)

![Screenshot (279)](https://github.com/user-attachments/assets/3f163152-1c83-4018-91f0-97c00612f015)

# pemrograman_web_itera_122140104 Pertemuan 3
Fitur utama:
- Tambah, edit, dan hapus buku
- Filter berdasarkan status: Dimiliki Sedang Dibaca, Ingin Dibeli
- Pencarian berdasarkan judul atau penulis
- Penyimpanan data permanen menggunakan localStorage
- Tampilan responsif dan modern
- Statistik jumlah buku berdasarkan status
- Navigasi antar halaman dengan React Router
  
Petunjuk Instalisasi dan Cara push github : 
- Buat Folder Praktikum lalu hidupkan terminal dengan klik kanan, atau bisa menggunakan bash git dan menuju ke directorynya dengan comant cd
- Instal Depedencies dengan : Install dependencies: npm install
- File yang berisikan public, src, dan lain lain akah langsung ada
- jalankan bentuk Website dengan : npm start
- code dengan mengubah bagian scr
- push dengan cara git add.
- namun sudah diketahui dulu reponya mau kemana

Screenshot ui ux :
![Screenshot 2025-04-20 224353](https://github.com/user-attachments/assets/d477ece9-c51c-4029-b5fc-39d4c8c5083d)
![Screenshot 2025-04-20 224342](https://github.com/user-attachments/assets/4a8877e0-9aa5-4aa6-898d-fd7ab693e87d)

Fitur React	Implementasi
- useState	Untuk mengelola state lokal seperti daftar buku dan filter nya
- useEffect	Untuk menyimpan dan memuat data dari localStorage yang nantinya klo di relog atau refresh web tidak akan hilang cuy
- Context API	Mengelola state global buku dan pencarian, jadi mempermudah pencarian
- Custom Hooks	Digunakan di useBookStats dan hook lainnya untuk memisahkan logika
- React Router	Untuk navigasi antara halaman home nya , agar rapi dan mudah make router
- PropTypes	Validasi props di komponen seperti BookProvider, BookForm, dll

Hasil screenshot pencobaan : 
![Screenshot 2025-04-20 234515](https://github.com/user-attachments/assets/fa42ff9c-458d-4676-baa2-d583260dca90)


