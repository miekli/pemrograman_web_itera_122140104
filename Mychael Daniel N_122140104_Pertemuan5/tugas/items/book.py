from .library_item import LibraryItem

# Subclass Book yang mewarisi dari LibraryItem
class Book(LibraryItem):
    def __init__(self, title, item_id, author):
        super().__init__(title, item_id)
        self.__author = author  # Private attribute

    def display_info(self):
        status = "Tersedia" if self.available else "Dipinjam"
        print(f"[Book] ID: {self._item_id}, Judul: {self._title}, Penulis: {self.__author}, Status: {status}")
