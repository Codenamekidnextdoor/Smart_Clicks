/**
 * Reusable Button Component
 * Supports multiple variants and sizes
 */

import type { ButtonHTMLAttributes, ReactNode } from 'react';

interface ButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
  children: ReactNode;
  variant?: 'primary' | 'secondary' | 'danger' | 'success';
  size?: 'sm' | 'md' | 'lg';
  fullWidth?: boolean;
}

const variantStyles = {
  primary: 'bg-accent-dark hover:bg-accent-hover text-accent border-accent',
  secondary: 'bg-blue-dark hover:bg-blue-hover text-blue border-blue',
  danger: 'bg-red-dark hover:bg-red-hover text-red border-red',
  success: 'bg-accent-dark hover:bg-accent-hover text-accent border-accent',
};

const sizeStyles = {
  sm: 'h-8 px-3 text-sm',
  md: 'h-10 px-4 text-base',
  lg: 'h-12 px-6 text-lg',
};

export function Button({
  children,
  variant = 'primary',
  size = 'md',
  fullWidth = false,
  className = '',
  disabled,
  ...props
}: ButtonProps) {
  return (
    <button
      className={`
        rounded-lg border font-bold
        transition-all duration-200
        hover:scale-[1.02] active:scale-[0.98]
        disabled:opacity-50 disabled:cursor-not-allowed
        disabled:hover:scale-100
        flex items-center justify-center gap-2
        ${variantStyles[variant]}
        ${sizeStyles[size]}
        ${fullWidth ? 'w-full' : ''}
        ${className}
      `}
      disabled={disabled}
      {...props}
    >
      {children}
    </button>
  );
}

// Made with Bob
