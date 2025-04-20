// src/components/Stats/Stats.jsx

import React from "react";
import useBookStats from "../../hooks/useBookStats";
import "./stats.css";

const Stats = () => {
  const { total, owned, reading, wishlist } = useBookStats();

  return (
    <div className="stats-container">
      <div className="stat-card">
        <div className="stat-label">Total Buku</div>
        <div className="stat-value">{total}</div>
      </div>
      <div className="stat-card">
        <div className="stat-label">Dimiliki</div>
        <div className="stat-value">{owned}</div>
      </div>
      <div className="stat-card">
        <div className="stat-label">Sedang Dibaca</div>
        <div className="stat-value">{reading}</div>
      </div>
      <div className="stat-card">
        <div className="stat-label">Ingin Dibeli</div>
        <div className="stat-value">{wishlist}</div>
      </div>
    </div>
  );
};

export default Stats;
