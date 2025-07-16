import React from 'react';
import ChatInterface from './components/ChatInterface';
import Header from './components/Header';

function App() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-black to-dark-50">
      <Header />
      <ChatInterface />
    </div>
  );
}

export default App;