import { useEffect, useState } from "react";
import "./App.css";

const LiBook = ({ book, handleAdd, showButton }) => {
  return (
    <li>
      <h2>Title: {book.volumeInfo.title}</h2>
      <div>
        <img src={book.volumeInfo.imageLinks.smallThumbnail} alt="Book Thumbnail" />
        <p>Description: {book.volumeInfo.description}</p>
      </div>
    
      <p>Authors: {book.volumeInfo.authors}</p>
      <p>Categories: {book.volumeInfo.categories}</p>

      {showButton && <button onClick={() => handleAdd(book)}>Add To Saved</button>}
    </li>
  );
};


export default function App() {
  const [books, setBooks] = useState(null);
  const [savedBooks, setSavedBooks] = useState([]);

  const handleSubmit = async (e) => {
    e.preventDefault();

    const res = await fetch(
      `https://www.googleapis.com/books/v1/volumes?q=${e.target.name.value}`
    );
    const data = await res.json();

    setBooks(data.items);
  };

  const handleAdd = (book) => {
    setSavedBooks([...savedBooks, book]);
  };


  return (
    <main>
      <div>
        <section>
          <h2>Search by name</h2>

          <form onSubmit={handleSubmit}>
            <input type="text" name="name" placeholder="Book's name" />
            <button>Search</button>
          </form>
        </section>

        <section>
          <h2>Searched Books</h2>
          {books ? (
            <ul>
              {books.map((book, index) => {
                return <LiBook key={book.id} book={book} handleAdd={handleAdd} showButton={true}/>;
              })}
            </ul>
          ) : (
            <p>Please search first.</p>
          )}
        </section>
      </div>
      <section id="savedBooks">
        <h2>Saved Books</h2>
        {savedBooks ? (
          <ul>
            {savedBooks.map((book, index) => {
              return <LiBook key={book.id} book={book} handleAdd={handleAdd} showButton={false}/>;
            })}
          </ul>
        ) : (
          <p>Please add first.</p>
        )}
      </section>
    </main>
  );
}