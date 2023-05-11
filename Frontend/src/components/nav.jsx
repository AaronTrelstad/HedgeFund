import React from 'react';
import './nav.css';

const Nav = () => {
    return (
        <>
            <button className='button'>
                <a href='/home'>Home</a>
            </button>
            <button className='button'>
                <a href="/aboutme">About Me</a>
            </button>
        </>
    )
}

export default Nav