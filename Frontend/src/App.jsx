import './App.css';
import React from 'react';
import Main from './components/main.jsx';
import AboutUs from './components/aboutus.jsx';
import {
  Routes,
  Route
} from "react-router-dom";

const App = () => {
  return (
    <>
      <Routes>
        <Route index element={<Main />} />
        <Route path="/Home" element={<Main />} />
        <Route path="/Aboutus" element={<AboutUs />} />
      </Routes>
    </>
  );
}

export default App;
