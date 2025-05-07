from items.library_item import LibraryItem

# Class Library untuk mengelola koleksi item
class Library:
    def __init__(self):
        self._collection = []  # Protected attribute untuk menyimpan koleksi item

    def add_item(self, item):
        """Menambahkan item ke dalam koleksi"""
        if isinstance(item, LibraryItem):
            self._collection.append(item)
            print(f"Item '{item._title}' berhasil ditambahkan.")
        else:
            print("Hanya item bertipe LibraryItem yang dapat ditambahkan.")

    def display_all_items(self):
        """Menampilkan semua item dalam koleksi"""
        if not self._collection:
            print("Perpustakaan kosong.")
        else:
            print("Daftar Koleksi Perpustakaan:")
            for item in self._collection:
                item.display_info()

    def search_item(self, keyword):
        """Mencari item berdasarkan judul atau ID"""
        print(f"Hasil pencarian untuk '{keyword}':")
        found = False
        for item in self._collection:
            if item.matches(keyword):
                item.display_info()
                found = True
        if not found:
            print("Tidak ditemukan.")
