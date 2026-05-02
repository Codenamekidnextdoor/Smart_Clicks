# SmartClick Project Folder Structure

## Complete Directory Layout

```
smart-clicks/
├── .github/
│   └── workflows/
│       ├── build.yml                 # CI/CD pipeline for builds
│       ├── test.yml                  # Automated testing
│       └── release.yml               # Release automation
│
├── .vscode/
│   ├── settings.json                 # VSCode workspace settings
│   ├── launch.json                   # Debug configurations
│   └── extensions.json               # Recommended extensions
│
├── docs/
│   ├── ARCHITECTURE.md               # System architecture (created)
│   ├── FOLDER_STRUCTURE.md           # This file
│   ├── API_INTEGRATION.md            # IBM watsonx integration guide
│   ├── DEVELOPMENT.md                # Development guidelines
│   ├── DEPLOYMENT.md                 # Deployment instructions
│   └── USER_GUIDE.md                 # End-user documentation
│
├── src/
│   ├── main/                         # Electron main process
│   │   ├── index.ts                  # Main entry point
│   │   ├── app.ts                    # Application lifecycle
│   │   ├── ipc/                      # IPC handlers
│   │   │   ├── index.ts
│   │   │   ├── settings.handler.ts
│   │   │   ├── overlay.handler.ts
│   │   │   └── ai.handler.ts
│   │   ├── services/                 # Background services
│   │   │   ├── text-selection/
│   │   │   │   ├── index.ts
│   │   │   │   ├── detector.ts
│   │   │   │   ├── windows.detector.ts
│   │   │   │   ├── macos.detector.ts
│   │   │   │   └── linux.detector.ts
│   │   │   ├── overlay/
│   │   │   │   ├── index.ts
│   │   │   │   ├── manager.ts
│   │   │   │   └── window-factory.ts
│   │   │   ├── keyboard/
│   │   │   │   ├── index.ts
│   │   │   │   └── shortcut-manager.ts
│   │   │   ├── ai/
│   │   │   │   ├── index.ts
│   │   │   │   ├── watsonx-client.ts
│   │   │   │   ├── context-manager.ts
│   │   │   │   ├── prompt-builder.ts
│   │   │   │   └── cache.ts
│   │   │   └── storage/
│   │   │       ├── index.ts
│   │   │       ├── settings-store.ts
│   │   │       └── history-db.ts
│   │   ├── utils/
│   │   │   ├── logger.ts
│   │   │   ├── error-handler.ts
│   │   │   └── platform.ts
│   │   └── types/
│   │       ├── index.ts
│   │       ├── ipc.types.ts
│   │       └── services.types.ts
│   │
│   ├── renderer/                     # Electron renderer processes
│   │   ├── setup/                    # Setup/Configuration app
│   │   │   ├── index.html
│   │   │   ├── main.tsx
│   │   │   ├── App.tsx
│   │   │   ├── components/
│   │   │   │   ├── WelcomeScreen.tsx
│   │   │   │   ├── ApiKeySetup.tsx
│   │   │   │   ├── ShortcutConfig.tsx
│   │   │   │   ├── PermissionsRequest.tsx
│   │   │   │   └── CompletionScreen.tsx
│   │   │   ├── hooks/
│   │   │   │   ├── useSettings.ts
│   │   │   │   └── useSetupFlow.ts
│   │   │   ├── store/
│   │   │   │   └── setup.store.ts
│   │   │   └── styles/
│   │   │       └── setup.css
│   │   │
│   │   └── overlay/                  # Overlay/Popup UI
│   │       ├── index.html
│   │       ├── main.tsx
│   │       ├── App.tsx
│   │       ├── components/
│   │       │   ├── Popup/
│   │       │   │   ├── index.tsx
│   │       │   │   ├── ActionButtons.tsx
│   │       │   │   ├── QuickActions.tsx
│   │       │   │   └── ExpandButton.tsx
│   │       │   ├── Chat/
│   │       │   │   ├── index.tsx
│   │       │   │   ├── ChatInterface.tsx
│   │       │   │   ├── MessageList.tsx
│   │       │   │   ├── Message.tsx
│   │       │   │   ├── InputBox.tsx
│   │       │   │   └── ContextDisplay.tsx
│   │       │   └── shared/
│   │       │       ├── Button.tsx
│   │       │       ├── Input.tsx
│   │       │       ├── Spinner.tsx
│   │       │       └── Tooltip.tsx
│   │       ├── hooks/
│   │       │   ├── useAI.ts
│   │       │   ├── useChat.ts
│   │       │   ├── useSelection.ts
│   │       │   └── usePosition.ts
│   │       ├── store/
│   │       │   ├── overlay.store.ts
│   │       │   └── chat.store.ts
│   │       ├── utils/
│   │       │   ├── positioning.ts
│   │       │   └── animations.ts
│   │       └── styles/
│   │           └── overlay.css
│   │
│   ├── preload/                      # Preload scripts
│   │   ├── setup.preload.ts
│   │   └── overlay.preload.ts
│   │
│   ├── shared/                       # Shared code
│   │   ├── types/
│   │   │   ├── index.ts
│   │   │   ├── ai.types.ts
│   │   │   ├── settings.types.ts
│   │   │   └── chat.types.ts
│   │   ├── constants/
│   │   │   ├── index.ts
│   │   │   ├── shortcuts.ts
│   │   │   ├── prompts.ts
│   │   │   └── config.ts
│   │   └── utils/
│   │       ├── validation.ts
│   │       └── formatting.ts
│   │
│   └── native/                       # Native modules (optional)
│       ├── text-selection/
│       │   ├── binding.gyp
│       │   ├── windows/
│       │   │   └── selection.cc
│       │   ├── macos/
│       │   │   └── selection.mm
│       │   └── linux/
│       │       └── selection.cc
│       └── README.md
│
├── tests/
│   ├── unit/
│   │   ├── main/
│   │   │   ├── services/
│   │   │   │   ├── text-selection.test.ts
│   │   │   │   ├── overlay.test.ts
│   │   │   │   └── ai.test.ts
│   │   │   └── utils/
│   │   │       └── logger.test.ts
│   │   └── renderer/
│   │       ├── setup/
│   │       │   └── components.test.tsx
│   │       └── overlay/
│   │           └── components.test.tsx
│   ├── integration/
│   │   ├── text-selection.test.ts
│   │   ├── overlay-display.test.ts
│   │   └── ai-integration.test.ts
│   ├── e2e/
│   │   ├── setup-flow.test.ts
│   │   ├── text-selection-flow.test.ts
│   │   └── chat-flow.test.ts
│   ├── fixtures/
│   │   ├── mock-settings.json
│   │   └── mock-responses.json
│   └── helpers/
│       ├── test-utils.ts
│       └── mock-electron.ts
│
├── scripts/
│   ├── build.js                      # Build script
│   ├── dev.js                        # Development script
│   ├── package.js                    # Packaging script
│   ├── notarize.js                   # macOS notarization
│   └── clean.js                      # Clean build artifacts
│
├── resources/                        # Static resources
│   ├── icons/
│   │   ├── icon.icns                 # macOS icon
│   │   ├── icon.ico                  # Windows icon
│   │   ├── icon.png                  # Linux icon
│   │   └── tray/
│   │       ├── tray.png
│   │       ├── tray@2x.png
│   │       └── tray-active.png
│   ├── images/
│   │   └── logo.png
│   └── sounds/
│       └── notification.mp3
│
├── build/                            # Build configuration
│   ├── entitlements.mac.plist        # macOS entitlements
│   ├── icon.icns
│   ├── icon.ico
│   └── notarize.js
│
├── dist/                             # Build output (gitignored)
│   ├── main/
│   ├── renderer/
│   └── preload/
│
├── release/                          # Release packages (gitignored)
│   ├── SmartClick-1.0.0.dmg
│   ├── SmartClick-1.0.0.exe
│   └── SmartClick-1.0.0.AppImage
│
├── .env.example                      # Environment variables template
├── .env                              # Environment variables (gitignored)
├── .eslintrc.json                    # ESLint configuration
├── .prettierrc                       # Prettier configuration
├── .gitignore                        # Git ignore rules
├── electron-builder.yml              # Electron Builder config
├── package.json                      # Project dependencies
├── package-lock.json                 # Locked dependencies
├── tsconfig.json                     # TypeScript config (base)
├── tsconfig.main.json                # TypeScript config (main)
├── tsconfig.renderer.json            # TypeScript config (renderer)
├── vite.config.ts                    # Vite configuration
├── vitest.config.ts                  # Vitest configuration
├── README.md                         # Project README
└── LICENSE                           # License file
```

## Directory Descriptions

### Root Level

- **`.github/`** - GitHub Actions workflows for CI/CD
- **`.vscode/`** - VSCode workspace configuration
- **`docs/`** - All project documentation
- **`src/`** - Source code (main application)
- **`tests/`** - Test suites
- **`scripts/`** - Build and utility scripts
- **`resources/`** - Static assets (icons, images, sounds)
- **`build/`** - Build configuration files
- **`dist/`** - Compiled output (generated, not committed)
- **`release/`** - Packaged installers (generated, not committed)

### Source Code Structure (`src/`)

#### `main/` - Electron Main Process
The Node.js backend that runs with full system access:

- **`index.ts`** - Entry point, initializes Electron app
- **`app.ts`** - Application lifecycle management
- **`ipc/`** - Inter-Process Communication handlers
- **`services/`** - Core business logic services
  - **`text-selection/`** - Platform-specific text detection
  - **`overlay/`** - Window management for popup/chat
  - **`keyboard/`** - Global keyboard shortcut handling
  - **`ai/`** - IBM watsonx integration
  - **`storage/`** - Settings and chat history persistence
- **`utils/`** - Utility functions (logging, error handling)
- **`types/`** - TypeScript type definitions

#### `renderer/` - Electron Renderer Processes
The UI layer built with React:

- **`setup/`** - One-time configuration interface
  - Components for each setup step
  - Setup flow state management
  - Styling specific to setup UI
  
- **`overlay/`** - Popup and chat interface
  - **`Popup/`** - Initial quick-action popup
  - **`Chat/`** - Expanded chat interface
  - **`shared/`** - Reusable UI components
  - Hooks for AI, chat, and positioning logic
  - State management with Zustand

#### `preload/` - Preload Scripts
Bridge between main and renderer processes with controlled API exposure

#### `shared/` - Shared Code
Code used by both main and renderer processes:
- Type definitions
- Constants
- Validation utilities

#### `native/` - Native Modules (Optional)
C++/Objective-C code for platform-specific features that Node.js can't handle

### Test Structure (`tests/`)

- **`unit/`** - Unit tests for individual functions/components
- **`integration/`** - Integration tests for service interactions
- **`e2e/`** - End-to-end tests for complete user flows
- **`fixtures/`** - Test data and mocks
- **`helpers/`** - Test utilities

## Key Configuration Files

### `package.json`
```json
{
  "name": "smartclick",
  "version": "1.0.0",
  "main": "dist/main/index.js",
  "scripts": {
    "dev": "node scripts/dev.js",
    "build": "node scripts/build.js",
    "package": "electron-builder",
    "test": "vitest",
    "test:e2e": "playwright test",
    "lint": "eslint src/",
    "format": "prettier --write src/"
  }
}
```

### `electron-builder.yml`
```yaml
appId: com.smartclick.app
productName: SmartClick
directories:
  output: release
  buildResources: build
files:
  - dist/**/*
  - resources/**/*
mac:
  category: public.app-category.productivity
  target:
    - dmg
    - zip
win:
  target:
    - nsis
    - portable
linux:
  target:
    - AppImage
    - deb
```

### `tsconfig.json` (Base)
```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "ESNext",
    "lib": ["ES2020"],
    "moduleResolution": "node",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "resolveJsonModule": true,
    "baseUrl": ".",
    "paths": {
      "@main/*": ["src/main/*"],
      "@renderer/*": ["src/renderer/*"],
      "@shared/*": ["src/shared/*"]
    }
  }
}
```

## File Naming Conventions

- **Components**: PascalCase (e.g., `ChatInterface.tsx`)
- **Utilities/Services**: camelCase (e.g., `textSelection.ts`)
- **Types**: PascalCase with `.types.ts` suffix (e.g., `ai.types.ts`)
- **Tests**: Same as source with `.test.ts` suffix (e.g., `overlay.test.ts`)
- **Constants**: UPPER_SNAKE_CASE in files (e.g., `MAX_CONTEXT_LENGTH`)

## Import Path Aliases

```typescript
// Instead of: import { something } from '../../../shared/types'
// Use: import { something } from '@shared/types'

// Available aliases:
// @main/* -> src/main/*
// @renderer/* -> src/renderer/*
// @shared/* -> src/shared/*
```

## Build Output Structure

```
dist/
├── main/
│   ├── index.js              # Compiled main process
│   └── [other compiled files]
├── renderer/
│   ├── setup/
│   │   ├── index.html
│   │   └── assets/
│   └── overlay/
│       ├── index.html
│       └── assets/
└── preload/
    ├── setup.preload.js
    └── overlay.preload.js
```

## Development Workflow

1. **Start Development**: `npm run dev`
   - Compiles TypeScript
   - Starts Vite dev server for renderer
   - Launches Electron with hot reload

2. **Run Tests**: `npm test`
   - Runs unit and integration tests
   - Watch mode for development

3. **Build for Production**: `npm run build`
   - Compiles all TypeScript
   - Bundles renderer code
   - Optimizes assets

4. **Package Application**: `npm run package`
   - Creates platform-specific installers
   - Signs and notarizes (if configured)

## Git Ignore Patterns

```
node_modules/
dist/
release/
.env
*.log
.DS_Store
Thumbs.db
*.swp
coverage/
.vscode/settings.json
```

## Notes

- All paths are relative to project root
- TypeScript is used throughout for type safety
- React 18+ with hooks for all UI components
- Zustand for lightweight state management
- Vite for fast development and optimized builds
- Electron Builder for cross-platform packaging
- Vitest for unit/integration tests
- Playwright for E2E tests

This structure supports:
- ✅ Clear separation of concerns
- ✅ Easy navigation and maintenance
- ✅ Scalable architecture
- ✅ Comprehensive testing
- ✅ Cross-platform development
- ✅ Professional build pipeline