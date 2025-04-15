import { useState } from 'react'
import './App.css'
import { AuthProvider } from './context/AuthContext'
import { BrowserRouter } from 'react-router-dom'
import Login from './pages/Login'
import Register from './pages/Register'
import { Routes, Route, Navigate } from 'react-router-dom'

function App() {
    

  return (
    <>
      <AuthProvider>
        <BrowserRouter>
          <Routes>
            <Route path="./login" element={<Login />} />
            <Route path="./register" element={<Register />} />
          </Routes>
        </BrowserRouter>
      </AuthProvider>
    </>
  )
}

export default App
