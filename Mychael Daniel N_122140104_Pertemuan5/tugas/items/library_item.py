from abc import ABC, abstractmethod

# Abstract class sebagai dasar semua item perpustakaan
class LibraryItem(ABC):
    def __init__(self, title, item_id):
        self._title = title             # Protected attribute
        self._item_id = item_id         # Protected attribute
        self._available = True          # Protected attribute

    @abstractmethod
    def display_info(self):
        """Method abstract untuk menampilkan info item"""
        pass

    @property
    def available(self):
        """Property untuk mengecek ketersediaan item"""
        return self._available

    @available.setter
    def available(self, status):
        if isinstance(status, bool):
            self._available = status
        else:
            print("Status harus berupa boolean.")

    def matches(self, keyword):
        """Polymorphic method: cek apakah keyword cocok dengan judul atau id"""
        return keyword.lower() in self._title.lower() or keyword == self._item_id
