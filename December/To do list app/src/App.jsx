import { useState } from 'react'
import ToDolist from './ToDoList'
import './App.css'


function App() {


  return (
    <>
      <header>
        <h1>To-Do List App</h1>
      </header>
      <p>Simple To Do List App, where you can add and remove tasks</p>
      <ToDolist />
    </>
  )
}

export default App
