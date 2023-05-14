import React from 'react';
import './nav.css';

const Nav = () => {
    return (
        <>
            <a href='/home'>
                <button className='button'>
                    Home
                </button>
            </a>
            <a href='/aboutus'>
                <button className='button'>
                    About Us
                </button>
            </a>
            <a href='/methods'>
                <button className='button'>
                    Methods
                </button>
            </a>
            <a href='/cyclone'>
                <button className='button'>
                    Cyclone Fund
                </button>
            </a>
            <a href='./derivative'>
                <button className='button'>
                    Derivatives
                </button>
            </a>
            <a href="./contact">
                <button className='button'>
                    Contact Us
                </button>
            </a>
        </>
    )
}

export default Nav