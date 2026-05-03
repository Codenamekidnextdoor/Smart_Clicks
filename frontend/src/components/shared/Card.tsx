/**
 * Reusable Card Component
 * Container with consistent styling
 */

import type { ReactNode } from 'react';

interface CardProps {
  children: ReactNode;
  title?: string;
  className?: string;
  noPadding?: boolean;
}

export function Card({ children, title, className = '', noPadding = false }: CardProps) {
  return (
    <div
      className={`
        bg-bg-surface rounded-lg border border-border
        ${className}
      `}
    >
      {title && (
        <>
          <div className={`${noPadding ? 'px-4 pt-4' : 'p-4 pb-3'}`}>
            <h3 className="text-accent font-bold text-sm">{title}</h3>
          </div>
          <div className="h-px bg-accent/20 mx-4" />
        </>
      )}
      <div className={noPadding ? '' : 'p-4'}>{children}</div>
    </div>
  );
}

// Made with Bob
