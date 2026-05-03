/**
 * Loading Spinner Component
 * Animated loading indicator
 */

interface LoadingSpinnerProps {
  size?: 'sm' | 'md' | 'lg';
  className?: string;
}

const sizeStyles = {
  sm: 'w-4 h-4 border-2',
  md: 'w-8 h-8 border-2',
  lg: 'w-12 h-12 border-3',
};

export function LoadingSpinner({ size = 'md', className = '' }: LoadingSpinnerProps) {
  return (
    <div
      className={`
        ${sizeStyles[size]}
        border-accent border-t-transparent
        rounded-full animate-spin
        ${className}
      `}
    />
  );
}

export function LoadingDots({ className = '' }: { className?: string }) {
  return (
    <div className={`flex gap-1 ${className}`}>
      <div className="w-2 h-2 bg-accent rounded-full animate-pulse" style={{ animationDelay: '0ms' }} />
      <div className="w-2 h-2 bg-accent rounded-full animate-pulse" style={{ animationDelay: '150ms' }} />
      <div className="w-2 h-2 bg-accent rounded-full animate-pulse" style={{ animationDelay: '300ms' }} />
    </div>
  );
}

// Made with Bob
