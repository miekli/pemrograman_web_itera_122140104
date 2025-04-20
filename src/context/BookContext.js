import React, { createContext, useState, useEffect } from "react";
import PropTypes from "prop-types";

// Helper functions for localStorage
const loadBooksFromStorage = () => {
  try {
    const stored = localStorage.getItem("books");
    return stored ? JSON.parse(stored) : [];
  } catch (error) {
    console.error("Error loading books from storage", error);
    return [];
  }
};

const saveBooksToStorage = (books) => {
  try {
    localStorage.setItem("books", JSON.stringify(books));
  } catch (error) {
    console.error("Error saving books to storage", error);
  }
};

export const BookContext = createContext();

export const BookProvider = ({ children }) => {
  const [books, setBooks] = useState(loadBooksFromStorage());
  const [filterStatus, setFilterStatus] = useState("all");
  const [searchQuery, setSearchQuery] = useState("");

  // Save books to localStorage when they change
  useEffect(() => {
    saveBooksToStorage(books);
  }, [books]);

  const addBook = (book) => {
    setBooks((prev) => [...prev, book]);
  };

  const updateBook = (updated) => {
    setBooks((prev) => prev.map((b) => (b.id === updated.id ? updated : b)));
  };

  const removeBook = (id) => {
    setBooks((prev) => prev.filter((b) => b.id !== id));
  };

  const filteredBooks = books.filter((book) => {
    const matchStatus = filterStatus === "all" || book.status === filterStatus;
    const matchSearch =
      book.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
      book.author.toLowerCase().includes(searchQuery.toLowerCase());
    return matchStatus && matchSearch;
  });

  return (
    <BookContext.Provider
      value={{
        books: filteredBooks,
        addBook,
        updateBook,
        removeBook,
        filterStatus,
        setFilterStatus,
        searchQuery,
        setSearchQuery,
      }}
    >
      {children}
    </BookContext.Provider>
  );
};

BookProvider.propTypes = {
  children: PropTypes.node.isRequired,
};
