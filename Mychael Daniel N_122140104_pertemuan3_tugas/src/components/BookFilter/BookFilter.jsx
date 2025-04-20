import React, { useContext, useState } from "react";
import { BookContext } from "../../context/BookContext";
import "./BookFilter.css";

const BookFilter = () => {
  const { filterStatus, setFilterStatus, searchQuery, setSearchQuery } = useContext(BookContext);

  const handleStatusChange = (e) => {
    setFilterStatus(e.target.value);
  };

  const handleSearchChange = (e) => {
    setSearchQuery(e.target.value);
  };

  return (
    <div className="book-filter-container">
      <div className="filter-label">Filter Buku</div>
      <select value={filterStatus} onChange={handleStatusChange}>
        <option value="all">Semua</option>
        <option value="owned">Dimiliki</option>
        <option value="reading">Sedang Dibaca</option>
        <option value="wishlist">Ingin Dibeli</option>
      </select>
      <input
        type="text"
        placeholder="Cari judul atau penulis..."
        value={searchQuery}
        onChange={handleSearchChange}
      />
    </div>
  );
};

export default BookFilter;
