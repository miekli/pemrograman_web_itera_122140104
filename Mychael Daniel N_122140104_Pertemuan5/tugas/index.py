from library import Library
from items.book import Book
from items.magazine import Magazine

def main():
    library = Library()
    print("=== Sistem Manajemen Perpustakaan ===")

    while True:
        print("\nMenu:")
        print("1. Tambah Item")
        print("2. Tampilkan Semua Item")
        print("3. Cari Item")
        print("4. Keluar")

        pilihan = input("Pilih menu (1-4): ")

        if pilihan == "1":
            print("\nJenis item:")
            print("1. Book")
            print("2. Magazine")
            jenis = input("Pilih jenis (1/2): ")

            title = input("Judul: ")
            item_id = input("ID: ")

            if jenis == "1":
                author = input("Penulis: ")
                book = Book(title, item_id, author)
                library.add_item(book)
            elif jenis == "2":
                issue_number = input("Edisi: ")
                magazine = Magazine(title, item_id, issue_number)
                library.add_item(magazine)
            else:
                print("Jenis item tidak valid.")

        elif pilihan == "2":
            library.display_all_items()

        elif pilihan == "3":
            keyword = input("Masukkan judul atau ID: ")
            library.search_item(keyword)

        elif pilihan == "4":
            print("Terima kasih telah menggunakan sistem.")
            break

        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
