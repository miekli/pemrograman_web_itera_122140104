import React, { useContext, useState } from "react";
import { BookContext } from "../../context/BookContext";
import BookForm from "../BookForm/BookForm";
import "./BookList.css";
import defaultBookImage from "../../assets/images/book.jpg";

const BookList = () => {
  const { books, removeBook } = useContext(BookContext);
  const [editingBook, setEditingBook] = useState(null);

  const handleEdit = (book) => {
    setEditingBook(book);
  };

  const handleEditComplete = () => {
    setEditingBook(null);
  };

  if (books.length === 0) {
    return <p className="book-list-empty">Tidak ada buku yang ditambahkan.</p>;
  }

  return (
    <div className="book-list-container">
      <table className="book-list-table">
        <thead>
          <tr>
            <th>Gambar</th>
            <th>Judul</th>
            <th>Penulis</th>
            <th>Status</th>
            <th>Aksi</th>
          </tr>
        </thead>
        <tbody>
          {books.map((book) => (
            <tr key={book.id}>
              <td>
                <img
                  src={defaultBookImage} // Gambar yang sama untuk semua buku
                  alt="Buku"
                  className="book-image"
                />
              </td>
              <td>{book.title}</td>
              <td>{book.author}</td>
              <td>{book.status}</td>
              <td>
                <button onClick={() => handleEdit(book)}>Edit</button>
                <p></p>
                <button onClick={() => removeBook(book.id)}>Hapus</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>

      {/* Menampilkan form edit buku di bawah */}
      {editingBook && (
        <div className="edit-book-form-container">
          <h3>Edit Buku</h3>
          <BookForm editableBook={editingBook} onEditComplete={handleEditComplete} />
        </div>
      )}
    </div>
  );
};

export default BookList;
