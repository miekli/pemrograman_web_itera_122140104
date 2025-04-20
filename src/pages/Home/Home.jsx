// src/pages/Home/index.jsx

import "./Home.css";
import React from "react";
import Stats from "../../pages/Stats/stats.jsx";
import BookForm from "../../components/BookForm/BookForm";
import BookList from "../../components/BookList/BookList";
import BookFilter from "../../components/BookFilter/BookFilter";

const Home = () => {
  return (
    <div className="home-wrapper">
      <div className="home-container">
        <header className="home-header">
          <h1> Manajemen Buku Pribadi</h1>
          <p>Catat, kelola, dan pantau buku favoritmu dengan mudah!</p>
        </header>

        <Stats /> {/* Tambahkan bagian statistik di sini */}

        <section className="card book-section">
          <h2> Daftar Buku</h2>
          <BookFilter />
          <BookList />
        </section>

        <section className="card form-section">
          <h2> Tambah  Buku </h2>
          <BookForm />
        </section>
      </div>
    </div>
  );
};

export default Home;
