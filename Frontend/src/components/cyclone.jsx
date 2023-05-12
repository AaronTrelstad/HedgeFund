import React from 'react'
import './cyclone.css'
import Nav from './nav.jsx';

const Cyclone = () => {
    return (
        <>
            <h1>Cyclone Fund</h1>
            <Nav/>
            <h2 className='box2'>
                We analyze stock pairs to find inefficencies within the market
            </h2>
        </>
    )
}

export default Cyclone