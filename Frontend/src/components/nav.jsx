import React from 'react';
import './nav.css';

const Nav = () => {
    return (
        <>
            <button className='button'>
                <a href='/home'>Home</a>
            </button>
            <button className='button'>
                <a href='/aboutus'>About Us</a>
            </button>
            <button className='button'>
                <a href='/methods'>Methods</a>
            </button>
            
        </>
    )
}

export default Nav