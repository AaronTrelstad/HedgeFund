import './App.css';
import React from 'react';
import Main from './components/main.jsx';
import AboutMe from './components/aboutme.jsx';
import {
  Routes,
  Route
} from "react-router-dom";

const App = () => {
  return (
    <>
      <Routes>
        <Route index element={<Main />} />
        <Route path="/Home" element={<Main/>} />
        <Route path="/AboutMe" element={<AboutMe />} />
      </Routes>
    </>
  );
}

export default App;
