import React from 'react';
import 'css/App.css';
import Search from 'views/Search'

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>search roads, places and zip codes</h1>
      </header>
      <main className="App-main">
        <Search />
      </main>
    </div>
  );
}
export default App;
