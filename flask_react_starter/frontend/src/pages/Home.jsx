import React, { Component } from 'react';
import { Link } from 'react-router-dom';

export default class Home extends Component {
  render() {
    return(
      <div>
        <h1>Good morning {window.localStorage.getItem('username')||"Friend"}</h1>
        <Link to="/login">Goto Login</Link><br/>
        <Link to="/signup">Goto Signup</Link><br />
        <Link to="/profile">View Profile</Link>
      </div>
    ) 
  }
}
