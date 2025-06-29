import { Link } from 'react-router-dom';
import React from 'react';

export default function Head() {
  return (
    <header>
      <h1>Metriics I/O</h1>
      <nav>
        <ul>
          <li><Link to="/">List</Link></li>
          <li><Link to="/new">New application</Link></li>
        </ul>
      </nav>
    </header>
  );
}
