from .library_item import LibraryItem

# Subclass Magazine yang mewarisi dari LibraryItem
class Magazine(LibraryItem):
    def __init__(self, title, item_id, issue_number):
        super().__init__(title, item_id)
        self.__issue_number = issue_number  # Private attribute

    def display_info(self):
        status = "Tersedia" if self.available else "Dipinjam"
        print(f"[Magazine] ID: {self._item_id}, Judul: {self._title}, Edisi: {self.__issue_number}, Status: {status}")
