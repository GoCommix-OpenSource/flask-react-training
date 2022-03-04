import React, { Fragment } from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Layout from './components/Layout.jsx';
import Profile from './pages/Profile.jsx';
import Home from './pages/Home.jsx';
import Login from './pages/Login.jsx';
import Signup from './pages/Signup.jsx';
export default function App() {
  return (
  <>
    <BrowserRouter>
      <Routes>
        {/* root components */}
        <Route path="/" element={<Layout/>}>
          <Route index element={<Home/>}/>
          
          {/* login component */}

          <Route path="signup" element={<Signup />}/>
          <Route path="login" element={<Login />}/>
          <Route path="profile" element={<Profile />}/>
        </Route>
      </Routes>
    </BrowserRouter>
  </>
  );
}
