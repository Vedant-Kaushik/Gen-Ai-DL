import React, { useState } from 'react';
import { Send, Link, MessageSquare } from 'lucide-react';

interface InputSectionProps {
  onSendMessage: (url: string, question: string) => void;
}

const InputSection: React.FC<InputSectionProps> = ({ onSendMessage }) => {
  const [url, setUrl] = useState('');
  const [question, setQuestion] = useState('');
  const [isUrlValid, setIsUrlValid] = useState(true);

  const validateYouTubeUrl = (url: string): boolean => {
    const youtubeRegex = /^(https?:\/\/)?(www\.)?(youtube\.com\/watch\?v=|youtu\.be\/)[\w-]+/;
    return youtubeRegex.test(url);
  };

  const handleUrlChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const newUrl = e.target.value;
    setUrl(newUrl);
    
    if (newUrl && !validateYouTubeUrl(newUrl)) {
      setIsUrlValid(false);
    } else {
      setIsUrlValid(true);
    }
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    
    if (!url.trim() || !question.trim()) return;
    
    if (!validateYouTubeUrl(url)) {
      setIsUrlValid(false);
      return;
    }

    onSendMessage(url, question);
    setQuestion('');
  };

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSubmit(e as any);
    }
  };

  return (
    <div className="p-6 border-t border-apple-gray-200 bg-white/50 backdrop-blur-sm">
      <form onSubmit={handleSubmit} className="space-y-4">
        {/* URL Input */}
        <div className="relative">
          <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
            <Link className={`w-5 h-5 ${isUrlValid ? 'text-apple-gray-400' : 'text-red-500'}`} />
          </div>
          <input
            type="url"
            value={url}
            onChange={handleUrlChange}
            placeholder="Paste YouTube video URL here..."
            className={`apple-input pl-10 ${
              !isUrlValid ? 'border-red-300 focus:ring-red-500 focus:border-red-500' : ''
            }`}
          />
          {!isUrlValid && (
            <p className="mt-1 text-sm text-red-600">Please enter a valid YouTube URL</p>
          )}
        </div>

        {/* Question Input */}
        <div className="relative">
          <div className="absolute top-3 left-0 pl-3 flex items-start pointer-events-none">
            <MessageSquare className="w-5 h-5 text-apple-gray-400" />
          </div>
          <textarea
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            onKeyPress={handleKeyPress}
            placeholder="Ask a question about the video..."
            rows={3}
            className="apple-input pl-10 resize-none"
          />
        </div>

        {/* Send Button */}
        <div className="flex justify-end">
          <button
            type="submit"
            disabled={!url.trim() || !question.trim() || !isUrlValid}
            className="apple-button disabled:opacity-50 disabled:cursor-not-allowed flex items-center space-x-2"
          >
            <span>Send</span>
            <Send className="w-4 h-4" />
          </button>
        </div>
      </form>

      {/* Quick Examples */}
      <div className="mt-4 pt-4 border-t border-apple-gray-100">
        <p className="text-xs text-apple-gray-500 mb-2">Try asking:</p>
        <div className="flex flex-wrap gap-2">
          {[
            "What is this video about?",
            "Summarize the main points",
            "What are the key takeaways?"
          ].map((example, index) => (
            <button
              key={index}
              onClick={() => setQuestion(example)}
              className="text-xs px-3 py-1 bg-apple-gray-100 hover:bg-apple-gray-200 rounded-full text-apple-gray-700 transition-colors duration-200"
            >
              {example}
            </button>
          ))}
        </div>
      </div>
    </div>
  );
};

export default InputSection;