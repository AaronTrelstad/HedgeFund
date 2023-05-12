import './App.css';
import React from 'react';
import Main from './components/main.jsx';
import AboutUs from './components/aboutus.jsx';
import Methods from './components/methods.jsx';
import {
  Routes,
  Route
} from "react-router-dom";
import Cyclone from './components/cyclone';
import Derivative from './components/derivative';
import Contact from './components/contact';

const App = () => {
  return (
    <>
      <Routes>
        <Route index element={<Main />} />
        <Route path="/Home" element={<Main />} />
        <Route path="/Aboutus" element={<AboutUs />} />
        <Route path="/Methods" element={<Methods />} />
        <Route path="/cyclone" element={<Cyclone />} />
        <Route path="/derivative" element={<Derivative />} />
        <Route path="/contact" element={<Contact />} />
      </Routes>
    </>
  );
}

export default App;
