import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Head from "./components/Head";
import Footer from "./components/Footer";
import Home from "./components/Home";
import List from "./components/List";

export default function App() {
  return (
    <Router>
      <Head />
      <Routes>
        <Route path="/" element={<List />} />
        <Route path="/new" element={<Home />} />
      </Routes>
      <Footer />
    </Router>
  );
}