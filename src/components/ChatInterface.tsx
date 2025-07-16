import React, { useState, useRef, useEffect } from 'react';
import VideoPlayer from './VideoPlayer';
import ChatWindow from './ChatWindow';
import InputSection from './InputSection';
import { Message } from '../types';

const ChatInterface: React.FC = () => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [currentVideoUrl, setCurrentVideoUrl] = useState<string>('');
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSendMessage = async (url: string, question: string) => {
    // Add user message
    const userMessage: Message = {
      id: Date.now().toString(),
      text: question,
      isUser: true,
      timestamp: new Date(),
    };

    setMessages(prev => [...prev, userMessage]);
    setCurrentVideoUrl(url);
    setIsLoading(true);

    try {
      const response = await fetch('http://localhost:8000/chatbot', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          url: url,
          Question: question,
        }),
      });

      const data = await response.json();
      
      const botMessage: Message = {
        id: (Date.now() + 1).toString(),
        text: data.answer || 'Sorry, I couldn\'t process your request.',
        isUser: false,
        timestamp: new Date(),
      };

      setMessages(prev => [...prev, botMessage]);
    } catch (error) {
      const errorMessage: Message = {
        id: (Date.now() + 1).toString(),
        text: 'Sorry, there was an error connecting to the server. Please try again.',
        isUser: false,
        timestamp: new Date(),
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="max-w-7xl mx-auto px-6 py-8">
      <div className="grid lg:grid-cols-2 gap-8 h-[calc(100vh-140px)]">
        {/* Video Section */}
        <div className="space-y-6">
          <VideoPlayer videoUrl={currentVideoUrl} />
        </div>

        {/* Chat Section */}
        <div className="flex flex-col h-full">
          <div className="glass-effect rounded-2xl flex-1 flex flex-col overflow-hidden">
            <div className="p-6 border-b border-apple-gray-200">
              <h2 className="text-lg font-semibold text-apple-gray-900">Chat with Video</h2>
              <p className="text-sm text-apple-gray-600 mt-1">
                Enter a YouTube URL and ask questions about the video content
              </p>
            </div>
            
            <ChatWindow 
              messages={messages} 
              isLoading={isLoading}
              messagesEndRef={messagesEndRef}
            />
            
            <InputSection onSendMessage={handleSendMessage} />
          </div>
        </div>
      </div>
    </div>
  );
};

export default ChatInterface;