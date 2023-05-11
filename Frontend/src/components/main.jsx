import React from 'react';
import './main.css';
import Nav from './nav.jsx';
import Footer from './footer.jsx'

const Main = () => {
    return (
        <>
            <h1>
                Blue River Capital
            </h1>
            <Nav/>
            <div className='box2'>
                <h2>
                    For our "Cyclone Fund" we use Statistical Arbitrage on stock pairs to maximize gains off of daily price changes.
                    This fund will be released by the end of 2023, this model returned 87.19% when backtested over the past year
                    and we are currently testing. We also plan on releasing derivatives in the future.
                </h2>
            </div>
            <Footer/>
        </>
    )
}

export default Main
