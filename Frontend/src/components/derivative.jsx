import React from 'react';
import './derivative.css';
import Nav from './nav.jsx';

const Derivative = () => {
    return (
        <>
            <h1>Derivative Trading</h1>
            <Nav/>
            <h2 className='box2'>
                We use mathematical and computerized models to identify trades such as: <br/>
                1. Vanilla Options <br/>
                2. Futures <br/>
                We plan on eventually using some exotic options and bonds
            </h2>
        </>
    )
}

export default Derivative