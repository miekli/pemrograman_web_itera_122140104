import React, { useState, useContext, useEffect } from "react";
import PropTypes from "prop-types";
import { BookContext } from "../../context/BookContext";
import "./BookForm.css";


const initialFormState = {
  title: "",
  author: "",
  status: "owned"
};

const BookForm = ({ editableBook, onEditComplete }) => {
  const [formData, setFormData] = useState(initialFormState);
  const { addBook, updateBook } = useContext(BookContext);

  useEffect(() => {
    if (editableBook) {
      setFormData(editableBook);
    }
  }, [editableBook]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!formData.title || !formData.author) {
      alert("Judul dan Penulis wajib diisi.");
      return;
    }

    if (editableBook) {
      updateBook(formData);
      onEditComplete();
    } else {
      addBook({ ...formData, id: Date.now() });
    }
    setFormData(initialFormState);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        name="title"
        placeholder="Judul Buku"
        value={formData.title}
        onChange={handleChange}
      />
      <input
        type="text"
        name="author"
        placeholder="Penulis"
        value={formData.author}
        onChange={handleChange}
      />
      <select name="status" value={formData.status} onChange={handleChange}>
        <option value="owned">Dimiliki</option>
        <option value="reading">Sedang Dibaca</option>
        <option value="wishlist">Ingin Dibeli</option>
      </select>
      <button type="submit">{editableBook ? "Update" : "Tambah"}</button>
    </form>
  );
};

BookForm.propTypes = {
  editableBook: PropTypes.object,
  onEditComplete: PropTypes.func
};

BookForm.defaultProps = {
  editableBook: null,
  onEditComplete: () => {}
};

export default BookForm;