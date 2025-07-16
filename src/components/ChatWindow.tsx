import React from 'react';
import { Bot, User, Loader2 } from 'lucide-react';
import { Message } from '../types';

interface ChatWindowProps {
  messages: Message[];
  isLoading: boolean;
  messagesEndRef: React.RefObject<HTMLDivElement>;
}

const ChatWindow: React.FC<ChatWindowProps> = ({ messages, isLoading, messagesEndRef }) => {
  const formatTime = (date: Date) => {
    return date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
  };

  return (
    <div className="flex-1 overflow-y-auto p-6 space-y-4">
      {messages.length === 0 && (
        <div className="text-center py-12">
          <div className="w-16 h-16 bg-dark-200 rounded-full flex items-center justify-center mx-auto mb-4">
            <Bot className="w-8 h-8 text-dark-500" />
          </div>
          <h3 className="text-lg font-medium text-white mb-2">
            Start a Conversation
          </h3>
          <p className="text-dark-500 max-w-sm mx-auto">
            Paste a YouTube URL and ask me anything about the video content. I'll analyze the transcript and provide detailed answers.
          </p>
        </div>
      )}

      {messages.map((message) => (
        <div
          key={message.id}
          className={`flex items-start space-x-3 ${
            message.isUser ? 'flex-row-reverse space-x-reverse' : ''
          }`}
        >
          <div className={`flex-shrink-0 w-8 h-8 rounded-full flex items-center justify-center ${
            message.isUser 
              ? 'bg-apple-blue text-white' 
              : 'bg-dark-200 text-dark-600'
          }`}>
            {message.isUser ? (
              <User className="w-4 h-4" />
            ) : (
              <Bot className="w-4 h-4" />
            )}
          </div>
          
          <div className={`flex flex-col ${message.isUser ? 'items-end' : 'items-start'}`}>
            <div className={`message-bubble ${
              message.isUser ? 'user-message' : 'bot-message'
            }`}>
              <p className="text-sm leading-relaxed whitespace-pre-wrap">{message.text}</p>
            </div>
            <span className="text-xs text-dark-400 mt-1 px-2">
              {formatTime(message.timestamp)}
            </span>
          </div>
        </div>
      ))}

      {isLoading && (
        <div className="flex items-start space-x-3">
          <div className="flex-shrink-0 w-8 h-8 rounded-full bg-dark-200 text-dark-600 flex items-center justify-center">
            <Bot className="w-4 h-4" />
          </div>
          <div className="message-bubble bot-message">
            <div className="flex items-center space-x-2">
              <Loader2 className="w-4 h-4 animate-spin" />
              <span className="text-sm">Analyzing video...</span>
            </div>
          </div>
        </div>
      )}

      <div ref={messagesEndRef} />
    </div>
  );
};

export default ChatWindow;