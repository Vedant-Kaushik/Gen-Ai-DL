import React from 'react';
import { MessageCircle, Youtube } from 'lucide-react';

const Header: React.FC = () => {
  return (
    <header className="glass-effect sticky top-0 z-50 px-6 py-4">
      <div className="max-w-7xl mx-auto flex items-center justify-between">
        <div className="flex items-center space-x-3">
          <div className="flex items-center justify-center w-10 h-10 bg-gradient-to-br from-red-500 to-red-600 rounded-xl shadow-lg">
            <Youtube className="w-6 h-6 text-white" />
          </div>
          <div>
            <h1 className="text-xl font-semibold text-apple-gray-900">YouTube AI Chat</h1>
            <p className="text-sm text-apple-gray-600">Ask questions about any YouTube video</p>
          </div>
        </div>
        
        <div className="flex items-center space-x-2 text-apple-gray-600">
          <MessageCircle className="w-5 h-5" />
          <span className="text-sm font-medium">Powered by AI</span>
        </div>
      </div>
    </header>
  );
};

export default Header;