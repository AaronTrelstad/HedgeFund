import './App.css';
import React from 'react';
import Main from './components/main.jsx';
import AboutUs from './components/aboutus.jsx';
import Methods from './components/methods.jsx';
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
        <Route path="/Methods" element={<Methods />} />
      </Routes>
    </>
  );
}

export default App;
