import React, { Component, Fragment } from 'react';
import { Outlet } from 'react-router';
import Footer from './Footer.jsx';
import Header from './Header.jsx';

export default class Layout extends Component {
  render() {
    return(
        <>
            <Header/>
              <div style={{ minHeight: '70vh' }}>
                <Outlet/>
              </div>
            <Footer/>
        </>
    );  
  }
}
