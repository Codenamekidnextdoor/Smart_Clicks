/**
 * Status Indicator Component
 * Shows whether SmartClick is enabled or disabled
 */

interface StatusIndicatorProps {
  enabled: boolean;
}

export function StatusIndicator({ enabled }: StatusIndicatorProps) {
  return (
    <div className="flex items-center gap-2">
      <div
        className={`
          w-2 h-2 rounded-full
          ${enabled ? 'bg-accent animate-pulse' : 'bg-red'}
        `}
      />
      <span className={`text-sm font-medium ${enabled ? 'text-accent' : 'text-red'}`}>
        {enabled ? 'Active' : 'Disabled'}
      </span>
    </div>
  );
}

// Made with Bob
