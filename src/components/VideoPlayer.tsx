import React from 'react';
import { Play, ExternalLink } from 'lucide-react';

interface VideoPlayerProps {
  videoUrl: string;
}

const VideoPlayer: React.FC<VideoPlayerProps> = ({ videoUrl }) => {
  const getVideoId = (url: string): string | null => {
    if (!url) return null;
    const match = url.match(/(?:youtube\.com\/watch\?v=|youtu\.be\/)([^&\n?#]+)/);
    return match ? match[1] : null;
  };

  const videoId = getVideoId(videoUrl);
  const embedUrl = videoId ? `https://www.youtube.com/embed/${videoId}` : null;

  if (!videoUrl) {
    return (
      <div className="glass-effect rounded-2xl p-8 h-full flex flex-col items-center justify-center text-center">
        <div className="w-20 h-20 bg-gradient-to-br from-red-500 to-red-600 rounded-full flex items-center justify-center mb-6 shadow-lg">
          <Play className="w-10 h-10 text-white ml-1" />
        </div>
        <h3 className="text-xl font-semibold text-apple-gray-900 mb-2">
          No Video Selected
        </h3>
        <p className="text-apple-gray-600 max-w-sm">
          Enter a YouTube URL in the chat to start watching and asking questions about the video
        </p>
      </div>
    );
  }

  if (!embedUrl) {
    return (
      <div className="glass-effect rounded-2xl p-8 h-full flex flex-col items-center justify-center text-center">
        <div className="w-16 h-16 bg-red-100 rounded-full flex items-center justify-center mb-4">
          <ExternalLink className="w-8 h-8 text-red-500" />
        </div>
        <h3 className="text-lg font-semibold text-apple-gray-900 mb-2">
          Invalid YouTube URL
        </h3>
        <p className="text-apple-gray-600">
          Please enter a valid YouTube video URL
        </p>
      </div>
    );
  }

  return (
    <div className="glass-effect rounded-2xl overflow-hidden h-full flex flex-col">
      <div className="flex-1 relative">
        <iframe
          src={embedUrl}
          title="YouTube video player"
          className="w-full h-full rounded-t-2xl"
          frameBorder="0"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
          allowFullScreen
        />
      </div>
      
      <div className="p-4 bg-white/50 backdrop-blur-sm">
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-2">
            <div className="w-2 h-2 bg-green-500 rounded-full animate-pulse-subtle"></div>
            <span className="text-sm font-medium text-apple-gray-700">Video Loaded</span>
          </div>
          
          <a
            href={videoUrl}
            target="_blank"
            rel="noopener noreferrer"
            className="flex items-center space-x-1 text-apple-blue hover:text-blue-600 transition-colors duration-200"
          >
            <span className="text-sm font-medium">Open in YouTube</span>
            <ExternalLink className="w-4 h-4" />
          </a>
        </div>
      </div>
    </div>
  );
};

export default VideoPlayer;