# Web Client - Detailed Folder Structure & Purpose

## **Web Client Architecture Summary**

The web-client is structured as a **modern, production-ready React application** that serves as the primary interface for your GenAI voice platform. Here are the key architectural highlights:

## **🎯 Primary Purpose & Target Users**

 **Target Audience** : Content creators, podcasters, and movie creators who need professional AI voice processing tools

 **Core Functionality** :

* **10 AI Voice Processing Features** with intuitive interfaces
* **Real-time job tracking** with WebSocket connections
* **Credit-based payment system** with multiple payment options
* **Voice library management** for custom voices
* **Professional audio editing tools**

## **🏗️ Architecture Patterns Used**

### **1. Feature-Based Organization**

* Each AI capability has its own component folder
* Reusable components in `shared/` directory
* Page-level components for routing

### **2. State Management Strategy**

```
Global State (Redux) → API calls, user auth, jobs, payments
Local State (useState) → UI interactions, form data
Custom Hooks → Complex logic abstraction
```

### **3. Real-time Architecture**

* **WebSocket connections** for live job updates
* **Progress tracking** for all AI processing
* **Instant notifications** for completed jobs

### **4. Performance Optimization**

* **Code splitting** by routes and features
* **Lazy loading** for heavy AI processing components
* **Optimistic UI updates** for better UX
* **Memoization** for expensive calculations

## **🎨 User Experience Design**

### **Professional Workflow Design**

* **Dashboard-centric** approach for power users
* **Drag-and-drop** file uploads
* **Visual waveform editing** for audio
* **Real-time preview** capabilities
* **Batch processing** support

### **Mobile-First Responsive Design**

* **TailwindCSS** for consistent styling
* **Touch-friendly** interfaces
* **Progressive enhancement** for desktop features
* **Optimized uploads** for mobile networks

## **🔧 Key Technical Features**

### **Audio Processing Interface**

* **Web Audio API** integration for real-time processing
* **Waveform visualization** with editing capabilities
* **Multi-format support** (WAV, MP3, FLAC, M4A)
* **Quality preview** before downloading

### **Payment Integration**

```typescript
Payment Methods Supported:
├── Stripe (International cards)
├── Razorpay (UPI, Net Banking)
└── PayPal (Digital wallet)

Credit System:
├── 60 minutes = $20 (base package)
├── Bulk discounts for larger packages
└── Pay-per-download model
```

### **Developer API Interface**

* **API key management** dashboard
* **Code examples** and documentation
* **Usage analytics** and rate limiting
* **Webhook configuration** tools

## **🚀 Development Workflow**

### **Modern Development Stack**

```
Build Tool: Vite (fast HMR, optimized builds)
Language: TypeScript (type safety)
Styling: TailwindCSS (utility-first)
Testing: Vitest + React Testing Library
Bundling: Code splitting + tree shaking
```

### **Quality Assurance**

* **ESLint + Prettier** for code quality
* **Type checking** with TypeScript
* **Unit & integration tests** for components
* **E2E testing** for critical user flows

## **📱 Progressive Web App Features**

* **Offline capability** for basic operations
* **Push notifications** for job completion
* **App-like experience** on mobile devices
* **Background sync** for uploads

## **🔐 Security Implementation**

* **JWT token management** with refresh tokens
* **Input sanitization** for all user inputs
* **File validation** before uploads
* **HTTPS enforcement** in production
* **CSP headers** for XSS protection

## **🎯 Why This Structure Works**

### **For Content Creators**

* **Intuitive workflow** from upload to download
* **Professional audio editing** capabilities
* **Real-time feedback** on processing status
* **Library management** for voice collections

### **For Developers**

* **Clean component architecture** for easy maintenance
* **Type safety** throughout the application
* **Comprehensive testing** setup
* **Clear separation of concerns**

### **For Business Growth**

* **Scalable architecture** for feature additions
* **Performance optimized** for user retention
* **Payment system** ready for global markets
* **Analytics integration** for business insights

This web-client architecture provides a **professional-grade interface** that can compete with industry-leading audio processing tools while maintaining the flexibility to rapidly add new AI capabilities as your platform grows.


# Overview

The web-client is a modern React Single Page Application (SPA) built with TypeScript, Vite, and TailwindCSS. It provides the user interface for content creators, podcasters, and movie creators to access all AI voice processing capabilities through an intuitive and responsive web interface.

## Complete Folder Structure

```
services/web-client/
│
├── public/                          # Static assets served directly
│   ├── favicon.ico                  # Browser tab icon
│   ├── logo192.png                  # App logo (192x192)
│   ├── logo512.png                  # App logo (512x512)
│   ├── manifest.json                # PWA manifest
│   ├── robots.txt                   # Search engine instructions
│   ├── audio-samples/               # Demo audio files
│   │   ├── sample-voice1.wav
│   │   ├── sample-voice2.wav
│   │   └── demo-music.mp3
│   └── icons/                       # Various app icons
│       ├── microphone.svg
│       ├── speaker.svg
│       └── waveform.svg
│
├── src/                             # Source code directory
│   ├── components/                  # Reusable UI components
│   │   ├── auth/                    # Authentication components
│   │   │   ├── LoginForm.tsx        # User login form
│   │   │   ├── RegisterForm.tsx     # User registration form
│   │   │   ├── ForgotPassword.tsx   # Password reset form
│   │   │   ├── ProtectedRoute.tsx   # Route protection wrapper
│   │   │   └── AuthGuard.tsx        # Authentication guard
│   │   │
│   │   ├── dashboard/               # Main dashboard components
│   │   │   ├── DashboardLayout.tsx  # Main layout wrapper
│   │   │   ├── Sidebar.tsx          # Navigation sidebar
│   │   │   ├── Header.tsx           # Top navigation header
│   │   │   ├── StatsCard.tsx        # Statistics display cards
│   │   │   ├── RecentJobs.tsx       # Recent processing jobs
│   │   │   ├── QuickActions.tsx     # Quick action buttons
│   │   │   └── UsageOverview.tsx    # Credit usage overview
│   │   │
│   │   ├── voice-processing/        # Core AI processing components
│   │   │   ├── TextToSpeech/        # TTS functionality
│   │   │   │   ├── TTSForm.tsx      # Text input and options
│   │   │   │   ├── VoiceSelector.tsx # Voice selection component
│   │   │   │   ├── ModelSelector.tsx # AI model selection
│   │   │   │   ├── TTSPreview.tsx   # Audio preview player
│   │   │   │   └── TTSSettings.tsx  # Advanced TTS settings
│   │   │   │
│   │   │   ├── SpeechToText/        # STT functionality
│   │   │   │   ├── STTUploader.tsx  # Audio file uploader
│   │   │   │   ├── STTProgress.tsx  # Processing progress
│   │   │   │   ├── STTResults.tsx   # Transcription results
│   │   │   │   └── LanguageSelector.tsx # Language selection
│   │   │   │
│   │   │   ├── VoiceCloning/        # Voice cloning features
│   │   │   │   ├── VoiceUploader.tsx    # Sample voice uploader
│   │   │   │   ├── VoiceLibrary.tsx     # User's voice collection
│   │   │   │   ├── ClonePreview.tsx     # Cloned voice preview
│   │   │   │   └── VoiceAnalyzer.tsx    # Voice characteristics
│   │   │   │
│   │   │   ├── AccentChanger/       # Accent modification
│   │   │   │   ├── AccentSelector.tsx   # Accent options
│   │   │   │   ├── AccentPreview.tsx    # Before/after comparison
│   │   │   │   └── AccentSettings.tsx   # Fine-tuning options
│   │   │   │
│   │   │   ├── LanguageDubbing/     # Language dubbing
│   │   │   │   ├── DubLanguageSelector.tsx # Target language
│   │   │   │   ├── DubPreview.tsx       # Dubbed audio preview
│   │   │   │   └── DubSettings.tsx      # Dubbing parameters
│   │   │   │
│   │   │   ├── AudioEditor/         # Audio editing tools
│   │   │   │   ├── Waveform.tsx         # Audio waveform display
│   │   │   │   ├── TimelineEditor.tsx   # Timeline-based editor
│   │   │   │   ├── BlooperRemoval.tsx   # Remove bloopers tool
│   │   │   │   ├── WordMuter.tsx        # Mute specific words
│   │   │   │   └── AudioTrimmer.tsx     # Trim audio segments
│   │   │   │
│   │   │   ├── NoiseRemoval/        # Noise reduction
│   │   │   │   ├── NoiseAnalyzer.tsx    # Noise level analysis
│   │   │   │   ├── DenoisePreview.tsx   # Before/after preview
│   │   │   │   └── NoiseSettings.tsx    # Noise removal settings
│   │   │   │
│   │   │   ├── MusicGeneration/     # Background music
│   │   │   │   ├── MusicGenerator.tsx   # Music generation form
│   │   │   │   ├── GenreSelector.tsx    # Music genre selection
│   │   │   │   ├── MoodSelector.tsx     # Mood/vibe selection
│   │   │   │   ├── MusicPreview.tsx     # Generated music preview
│   │   │   │   └── MusicSettings.tsx    # Music parameters
│   │   │   │
│   │   │   ├── SoundEffects/        # Sound effects generation
│   │   │   │   ├── SFXGenerator.tsx     # SFX generation interface
│   │   │   │   ├── SFXLibrary.tsx       # Predefined SFX library
│   │   │   │   ├── SFXPreview.tsx       # Sound effect preview
│   │   │   │   └── SFXCustomizer.tsx    # Custom SFX parameters
│   │   │   │
│   │   │   └── SocialMediaMusic/    # Social media optimized music
│   │   │       ├── PlatformSelector.tsx  # WhatsApp/Instagram
│   │   │       ├── VibeGenerator.tsx     # Vibe-based generation
│   │   │       ├── SocialPreview.tsx     # Platform-specific preview
│   │   │       └── SocialExport.tsx      # Export optimization
│   │   │
│   │   ├── payment/                 # Payment and billing components
│   │   │   ├── CreditPackages.tsx   # Available credit packages
│   │   │   ├── PaymentForm.tsx      # Payment processing form
│   │   │   ├── PaymentMethods.tsx   # Payment method selection
│   │   │   ├── BillingHistory.tsx   # Payment history
│   │   │   ├── CreditBalance.tsx    # Current credit display
│   │   │   ├── UsageTracking.tsx    # Usage analytics
│   │   │   └── SubscriptionPlan.tsx # Subscription management
│   │   │
│   │   ├── shared/                  # Shared/common components
│   │   │   ├── ui/                  # Basic UI components
│   │   │   │   ├── Button.tsx       # Custom button component
│   │   │   │   ├── Input.tsx        # Custom input component
│   │   │   │   ├── Select.tsx       # Custom select component
│   │   │   │   ├── Modal.tsx        # Modal dialog component
│   │   │   │   ├── Tooltip.tsx      # Tooltip component
│   │   │   │   ├── Progress.tsx     # Progress bar component
│   │   │   │   ├── Card.tsx         # Card container component
│   │   │   │   ├── Badge.tsx        # Badge/tag component
│   │   │   │   ├── Spinner.tsx      # Loading spinner
│   │   │   │   └── Alert.tsx        # Alert/notification component
│   │   │   │
│   │   │   ├── layout/              # Layout components
│   │   │   │   ├── MainLayout.tsx   # Main application layout
│   │   │   │   ├── AuthLayout.tsx   # Authentication layout
│   │   │   │   ├── Navigation.tsx   # Main navigation
│   │   │   │   ├── Footer.tsx       # Application footer
│   │   │   │   └── Breadcrumb.tsx   # Breadcrumb navigation
│   │   │   │
│   │   │   ├── audio/               # Audio-related components
│   │   │   │   ├── AudioPlayer.tsx  # Universal audio player
│   │   │   │   ├── AudioUploader.tsx # File upload component
│   │   │   │   ├── AudioVisualizer.tsx # Audio waveform visualizer
│   │   │   │   ├── RecordingButton.tsx # Voice recording
│   │   │   │   └── PlaybackControls.tsx # Playback controls
│   │   │   │
│   │   │   ├── forms/               # Form components
│   │   │   │   ├── FormField.tsx    # Reusable form field
│   │   │   │   ├── FileUpload.tsx   # File upload field
│   │   │   │   ├── TextArea.tsx     # Text area component
│   │   │   │   ├── CheckboxGroup.tsx # Checkbox group
│   │   │   │   └── RadioGroup.tsx   # Radio button group
│   │   │   │
│   │   │   ├── feedback/            # User feedback components
│   │   │   │   ├── Toast.tsx        # Toast notifications
│   │   │   │   ├── LoadingState.tsx # Loading indicators
│   │   │   │   ├── ErrorBoundary.tsx # Error boundary wrapper
│   │   │   │   ├── EmptyState.tsx   # Empty state display
│   │   │   │   └── SuccessMessage.tsx # Success notifications
│   │   │   │
│   │   │   └── charts/              # Data visualization
│   │   │       ├── UsageChart.tsx   # Usage analytics chart
│   │   │       ├── ProgressChart.tsx # Progress visualization
│   │   │       └── StatsChart.tsx   # Statistics charts
│   │   │
│   │   └── developer/               # Developer API components
│   │       ├── APIKeyManager.tsx    # API key management
│   │       ├── APIDocumentation.tsx # API docs viewer
│   │       ├── CodeExamples.tsx     # Code examples
│   │       ├── APIUsageStats.tsx    # API usage statistics
│   │       └── WebhookManager.tsx   # Webhook configuration
│   │
│   ├── pages/                       # Page components (route handlers)
│   │   ├── HomePage.tsx             # Landing/home page
│   │   ├── LoginPage.tsx            # User login page
│   │   ├── RegisterPage.tsx         # User registration page
│   │   ├── DashboardPage.tsx        # Main dashboard
│   │   ├── TextToSpeechPage.tsx     # TTS feature page
│   │   ├── SpeechToTextPage.tsx     # STT feature page
│   │   ├── VoiceCloningPage.tsx     # Voice cloning page
│   │   ├── AccentChangePage.tsx     # Accent modification page
│   │   ├── LanguageDubbingPage.tsx  # Language dubbing page
│   │   ├── AudioEditorPage.tsx      # Audio editing page
│   │   ├── NoiseRemovalPage.tsx     # Noise reduction page
│   │   ├── MusicGenerationPage.tsx  # Music generation page
│   │   ├── SoundEffectsPage.tsx     # Sound effects page
│   │   ├── SocialMusicPage.tsx      # Social media music page
│   │   ├── VoiceLibraryPage.tsx     # Voice library management
│   │   ├── PaymentPage.tsx          # Payment processing page
│   │   ├── BillingPage.tsx          # Billing and usage page
│   │   ├── ProfilePage.tsx          # User profile page
│   │   ├── DeveloperPage.tsx        # Developer API page
│   │   ├── HelpPage.tsx             # Help and documentation
│   │   ├── SettingsPage.tsx         # User settings page
│   │   ├── NotFoundPage.tsx         # 404 error page
│   │   └── MaintenancePage.tsx      # Maintenance mode page
│   │
│   ├── hooks/                       # Custom React hooks
│   │   ├── useAuth.ts               # Authentication hook
│   │   ├── useAudio.ts              # Audio processing hook
│   │   ├── usePayment.ts            # Payment processing hook
│   │   ├── useWebSocket.ts          # WebSocket connection hook
│   │   ├── useLocalStorage.ts       # Local storage hook
│   │   ├── useFileUpload.ts         # File upload hook
│   │   ├── useJobStatus.ts          # Job status tracking hook
│   │   ├── useCredits.ts            # Credit management hook
│   │   ├── useRecording.ts          # Audio recording hook
│   │   ├── useNotifications.ts      # Notification system hook
│   │   ├── useTheme.ts              # Theme management hook
│   │   └── useDebounce.ts           # Debounce utility hook
│   │
│   ├── store/                       # Redux store configuration
│   │   ├── index.ts                 # Store configuration
│   │   ├── rootReducer.ts           # Root reducer
│   │   ├── middleware.ts            # Custom middleware
│   │   ├── slices/                  # Redux Toolkit slices
│   │   │   ├── authSlice.ts         # Authentication state
│   │   │   ├── audioSlice.ts        # Audio processing state
│   │   │   ├── paymentSlice.ts      # Payment state
│   │   │   ├── jobSlice.ts          # Job tracking state
│   │   │   ├── userSlice.ts         # User profile state
│   │   │   ├── voiceSlice.ts        # Voice library state
│   │   │   ├── uiSlice.ts           # UI state (modals, etc.)
│   │   │   └── notificationSlice.ts # Notification state
│   │   │
│   │   └── api/                     # RTK Query API definitions
│   │       ├── authApi.ts           # Authentication API
│   │       ├── audioApi.ts          # Audio processing API
│   │       ├── paymentApi.ts        # Payment API
│   │       ├── userApi.ts           # User management API
│   │       ├── voiceApi.ts          # Voice library API
│   │       └── developerApi.ts      # Developer API
│   │
│   ├── utils/                       # Utility functions
│   │   ├── api.ts                   # API client configuration
│   │   ├── constants.ts             # Application constants
│   │   ├── helpers.ts               # General helper functions
│   │   ├── validation.ts            # Form validation utilities
│   │   ├── formatting.ts            # Data formatting utilities
│   │   ├── audio.ts                 # Audio processing utilities
│   │   ├── file.ts                  # File handling utilities
│   │   ├── storage.ts               # Storage utilities
│   │   ├── encryption.ts            # Client-side encryption
│   │   ├── analytics.ts             # Analytics tracking
│   │   └── errors/                  # Error handling utilities
│   │       ├── ErrorHandler.ts      # Error handling class
│   │       ├── ApiError.ts          # API error class
│   │       └── ValidationError.ts   # Validation error class
│   │
│   ├── types/                       # TypeScript type definitions
│   │   ├── auth.types.ts            # Authentication types
│   │   ├── audio.types.ts           # Audio processing types
│   │   ├── payment.types.ts         # Payment types
│   │   ├── user.types.ts            # User types
│   │   ├── api.types.ts             # API response types
│   │   ├── ui.types.ts              # UI component types
│   │   ├── job.types.ts             # Job processing types
│   │   └── global.types.ts          # Global type definitions
│   │
│   ├── api/                         # API service layer
│   │   ├── client.ts                # Axios client configuration
│   │   ├── endpoints.ts             # API endpoint definitions
│   │   ├── interceptors.ts          # Request/response interceptors
│   │   ├── websocket.ts             # WebSocket client
│   │   └── services/                # API service functions
│   │       ├── authService.ts       # Authentication services
│   │       ├── audioService.ts      # Audio processing services
│   │       ├── paymentService.ts    # Payment services
│   │       ├── userService.ts       # User management services
│   │       ├── voiceService.ts      # Voice library services
│   │       └── uploadService.ts     # File upload services
│   │
│   ├── styles/                      # Styling files
│   │   ├── globals.css              # Global CSS styles
│   │   ├── components.css           # Component-specific styles
│   │   ├── animations.css           # CSS animations
│   │   ├── themes/                  # Theme definitions
│   │   │   ├── light.css            # Light theme
│   │   │   ├── dark.css             # Dark theme
│   │   │   └── high-contrast.css    # High contrast theme
│   │   └── responsive.css           # Responsive design styles
│   │
│   ├── assets/                      # Asset files
│   │   ├── images/                  # Image assets
│   │   │   ├── logo.png             # Application logo
│   │   │   ├── hero-bg.jpg          # Hero background
│   │   │   ├── feature-icons/       # Feature icons
│   │   │   └── illustrations/       # UI illustrations
│   │   ├── fonts/                   # Custom fonts
│   │   │   ├── Inter.woff2          # Primary font
│   │   │   └── Roboto-Mono.woff2    # Monospace font
│   │   └── animations/              # Lottie animations
│   │       ├── loading.json         # Loading animation
│   │       ├── success.json         # Success animation
│   │       └── processing.json      # Processing animation
│   │
│   ├── locales/                     # Internationalization
│   │   ├── en/                      # English translations
│   │   │   ├── common.json          # Common translations
│   │   │   ├── auth.json            # Authentication text
│   │   │   ├── audio.json           # Audio feature text
│   │   │   ├── payment.json         # Payment text
│   │   │   └── errors.json          # Error messages
│   │   ├── es/                      # Spanish translations
│   │   ├── fr/                      # French translations
│   │   └── hi/                      # Hindi translations
│   │
│   ├── config/                      # Configuration files
│   │   ├── environment.ts           # Environment configuration
│   │   ├── api.config.ts            # API configuration
│   │   ├── theme.config.ts          # Theme configuration
│   │   ├── audio.config.ts          # Audio configuration
│   │   └── payment.config.ts        # Payment configuration
│   │
│   ├── App.tsx                      # Main App component
│   ├── main.tsx                     # Application entry point
│   ├── index.css                    # Global styles entry
│   └── vite-env.d.ts                # Vite type definitions
│
├── tests/                           # Test files
│   ├── setup.ts                     # Test setup configuration
│   ├── utils/                       # Test utilities
│   │   ├── test-utils.tsx           # Testing utilities
│   │   ├── mocks/                   # Mock data
│   │   └── fixtures/                # Test fixtures
│   ├── components/                  # Component tests
│   │   ├── auth/                    # Auth component tests
│   │   ├── dashboard/               # Dashboard tests
│   │   └── voice-processing/        # Voice processing tests
│   ├── pages/                       # Page tests
│   ├── hooks/                       # Hook tests
│   ├── store/                       # Redux store tests
│   └── integration/                 # Integration tests
│
├── docs/                            # Documentation
│   ├── components.md                # Component documentation
│   ├── deployment.md                # Deployment guide
│   ├── development.md               # Development guide
│   └── architecture.md              # Frontend architecture
│
├── public/                          # Static assets
├── package.json                     # Dependencies and scripts
├── vite.config.ts                   # Vite configuration
├── tsconfig.json                    # TypeScript configuration
├── tailwind.config.js               # TailwindCSS configuration
├── postcss.config.js                # PostCSS configuration
├── vitest.config.ts                 # Vitest testing configuration
├── .eslintrc.js                     # ESLint configuration
├── .prettierrc                      # Prettier configuration
├── .env.example                     # Environment variables template
├── Dockerfile                       # Docker container definition
├── .dockerignore                    # Docker ignore file
└── README.md                        # Project documentation
```

## Detailed Component Purposes

### 1. Core Voice Processing Components

#### Text-to-Speech (TTS) Flow

```typescript
// TTSForm.tsx - Main TTS interface
export const TTSForm: React.FC = () => {
  const [text, setText] = useState('');
  const [selectedModel, setSelectedModel] = useState('tacotron2');
  const [selectedVoice, setSelectedVoice] = useState('');
  const [isProcessing, setIsProcessing] = useState(false);
  
  const handleGenerateSpeech = async () => {
    setIsProcessing(true);
    try {
      const result = await audioService.generateTTS({
        text,
        model: selectedModel,
        voice_id: selectedVoice,
        parameters: {
          speed: 1.0,
          pitch: 1.0,
          emotion: 'neutral'
        }
      });
    
      // Handle real-time job updates via WebSocket
      useJobStatus(result.jobId, (status) => {
        if (status.completed) {
          setIsProcessing(false);
          // Show preview player with generated audio
        }
      });
    } catch (error) {
      handleError(error);
    }
  };
  
  return (
    <Card className="p-6">
      <TextArea
        value={text}
        onChange={setText}
        placeholder="Enter text to convert to speech..."
        maxLength={10000}
      />
    
      <div className="grid grid-cols-2 gap-4 mt-4">
        <ModelSelector
          options={['tacotron2', 'waveglow']}
          value={selectedModel}
          onChange={setSelectedModel}
        />
      
        <VoiceSelector
          voices={userVoices}
          value={selectedVoice}
          onChange={setSelectedVoice}
        />
      </div>
    
      <Button
        onClick={handleGenerateSpeech}
        disabled={!text || isProcessing}
        className="mt-4"
      >
        {isProcessing ? <Spinner /> : 'Generate Speech'}
      </Button>
    
      {isProcessing && (
        <Progress
          value={jobProgress}
          className="mt-4"
          label="Processing audio..."
        />
      )}
    </Card>
  );
};
```

#### Voice Cloning Interface

```typescript
// VoiceUploader.tsx - Voice sample upload
export const VoiceUploader: React.FC = () => {
  const [uploadedFile, setUploadedFile] = useState<File | null>(null);
  const [voiceName, setVoiceName] = useState('');
  const [isAnalyzing, setIsAnalyzing] = useState(false);
  
  const handleFileUpload = (file: File) => {
    setUploadedFile(file);
    // Auto-analyze voice characteristics
    analyzeVoiceCharacteristics(file);
  };
  
  const analyzeVoiceCharacteristics = async (file: File) => {
    setIsAnalyzing(true);
    try {
      const analysis = await voiceService.analyzeVoice(file);
      // Display voice characteristics (pitch, tone, accent, etc.)
      setVoiceCharacteristics(analysis);
    } catch (error) {
      handleError(error);
    }
    setIsAnalyzing(false);
  };
  
  return (
    <div className="space-y-6">
      <FileUpload
        accept="audio/*"
        maxSize={50 * 1024 * 1024} // 50MB
        onFileSelect={handleFileUpload}
        description="Upload a clear voice sample (30 seconds recommended)"
      />
    
      {uploadedFile && (
        <div className="space-y-4">
          <AudioPlayer src={URL.createObjectURL(uploadedFile)} />
        
          <Input
            value={voiceName}
            onChange={(e) => setVoiceName(e.target.value)}
            placeholder="Enter voice name (e.g., 'John - Professional')"
          />
        
          {isAnalyzing ? (
            <div className="flex items-center space-x-2">
              <Spinner size="sm" />
              <span>Analyzing voice characteristics...</span>
            </div>
          ) : (
            voiceCharacteristics && (
              <VoiceAnalyzer characteristics={voiceCharacteristics} />
            )
          )}
        </div>
      )}
    </div>
  );
};
```

### 2. Audio Editor Component

```typescript
// Waveform.tsx - Audio waveform visualization and editing
export const Waveform: React.FC<{ audioUrl: string }> = ({ audioUrl }) => {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const [audioBuffer, setAudioBuffer] = useState<AudioBuffer | null>(null);
  const [selections, setSelections] = useState<AudioSelection[]>([]);
  const [playhead, setPlayhead] = useState(0);
  
  useEffect(() => {
    loadAudioBuffer(audioUrl);
  }, [audioUrl]);
  
  const loadAudioBuffer = async (url: string) => {
    const audioContext = new AudioContext();
    const response = await fetch(url);
    const arrayBuffer = await response.arrayBuffer();
    const buffer = await audioContext.decodeAudioData(arrayBuffer);
    setAudioBuffer(buffer);
    drawWaveform(buffer);
  };
  
  const drawWaveform = (buffer: AudioBuffer) => {
    const canvas = canvasRef.current;
    if (!canvas) return;
  
    const ctx = canvas.getContext('2d');
    const data = buffer.getChannelData(0);
    const width = canvas.width;
    const height = canvas.height;
  
    ctx.clearRect(0, 0, width, height);
    ctx.strokeStyle = '#3b82f6';
    ctx.lineWidth = 1;
  
    const sliceWidth = width / data.length;
    let x = 0;
  
    ctx.beginPath();
    for (let i = 0; i < data.length; i++) {
      const v = data[i] * height / 2;
      const y = height / 2 + v;
    
      if (i === 0) {
        ctx.moveTo(x, y);
      } else {
        ctx.lineTo(x, y);
      }
    
      x += sliceWidth;
    }
    ctx.stroke();
  
    // Draw selections and markers
    drawSelections();
    drawPlayhead();
  };
  
  const handleCanvasClick = (event: React.MouseEvent) => {
    const rect = canvasRef.current?.getBoundingClientRect();
    if (!rect || !audioBuffer) return;
  
    const x = event.clientX - rect.left;
    const timePosition = (x / rect.width) * audioBuffer.duration;
  
    // Handle selection logic based on current tool
    if (currentTool === 'blooper-removal') {
      handleBlooperSelection(timePosition);
    } else if (currentTool === 'word-mute') {
      handleWordMuteSelection(timePosition);
    }
  };
  
  return (
    <div className="w-full bg-gray-50 rounded-lg p-4">
      <canvas
        ref={canvasRef}
        width={800}
        height={200}
        className="w-full cursor-crosshair"
        onClick={handleCanvasClick}
      />
    
      <div className="flex justify-between items-center mt-4">
        <PlaybackControls
          onPlay={() => playAudio(playhead)}
          onPause={pauseAudio}
          onStop={() => { stopAudio(); setPlayhead(0); }}
        />
      
        <div className="flex space-x-2">
          <Button
            variant={currentTool === 'blooper-removal' ? 'primary' : 'outline'}
            onClick={() => setCurrentTool('blooper-removal')}
          >
            Remove Blooper
          </Button>
        
          <Button
            variant={currentTool === 'word-mute' ? 'primary' : 'outline'}
            onClick={() => setCurrentTool('word-mute')}
          >
            Mute Word
          </Button>
        </div>
      </div>
    </div>
  );
};
```

### 3. Payment Integration Component

```typescript
// PaymentForm.tsx - Credit purchase interface
export const PaymentForm: React.FC = () => {
  const [selectedPackage, setSelectedPackage] = useState<CreditPackage | null>(null);
  const [paymentMethod, setPaymentMethod] = useState<'stripe' | 'razorpay' | 'paypal'>('stripe');
  const [isProcessing, setIsProcessing] = useState(false);
  
  const creditPackages: CreditPackage[] = [
    { id: 'basic', name: 'Basic', minutes: 60, price: 20, currency: 'USD' },
    { id: 'pro', name: 'Pro', minutes: 180, price: 50, currency: 'USD', discount: 17 },
    { id: 'premium', name: 'Premium', minutes: 600, price: 150, currency: 'USD', discount: 25 }
  ];
  
  const handlePurchase = async () => {
    if (!selectedPackage) return;
  
    setIsProcessing(true);
    try {
      const paymentIntent = await paymentService.createPaymentIntent({
        packageId: selectedPackage.id,
        paymentMethod
      });
    
      // Handle different payment methods
      if (paymentMethod === 'stripe') {
        await handleStripePayment(paymentIntent);
      } else if (paymentMethod === 'razorpay') {
        await handleRazorpayPayment(paymentIntent);
      }
    
      // Show success message and update credits
      showToast('Payment successful! Credits added to your account.', 'success');
    
    } catch (error) {
      handleError(error);
    }
    setIsProcessing(false);
  };
  
  return (
    <div className="max-w-4xl mx-auto p-6">
      <h2 className="text-2xl font-bold mb-6">Choose Your Credit Package</h2>
    
      {/* Credit Packages */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
        {creditPackages.map((pkg) => (
          <Card
            key={pkg.id}
            className={`p-6 cursor-pointer transition-all ${
              selectedPackage?.id === pkg.id 
                ? 'ring-2 ring-blue-500 bg-blue-50' 
                : 'hover:shadow-lg'
            }`}
            onClick={() => setSelectedPackage(pkg)}
          >
            <div className="text-center">
              <h3 className="text-xl font-semibold mb-2">{pkg.name}</h3>
              <div className="text-3xl font-bold text-blue-600 mb-2">
                ${pkg.price}
              </div>
              <div className="text-gray-600 mb-4">
                {pkg.minutes} minutes of downloads
              </div>
              {pkg.discount && (
                <Badge variant="success" className="mb-4">
                  Save {pkg.discount}%
                </Badge>
              )}
              <div className="text-sm text-gray-500">
                ${(pkg.price / pkg.minutes).toFixed(2)} per minute
              </div>
            </div>
          </Card>
        ))}
      </div>
    
      {selectedPackage && (
        <Card className="p-6">
          <h3 className="text-lg font-semibold mb-4">Payment Method</h3>
        
          {/* Payment Method Selection */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
            <Button
              variant={paymentMethod === 'stripe' ? 'primary' : 'outline'}
              onClick={() => setPaymentMethod('stripe')}
              className="flex items-center justify-center space-x-2"
            >
              <CreditCardIcon className="w-5 h-5" />
              <span>Credit Card</span>
            </Button>
          
            <Button
              variant={paymentMethod === 'razorpay' ? 'primary' : 'outline'}
              onClick={() => setPaymentMethod('razorpay')}
              className="flex items-center justify-center space-x-2"
            >
              <PhoneIcon className="w-5 h-5" />
              <span>UPI / Net Banking</span>
            </Button>
          
            <Button
              variant={paymentMethod === 'paypal' ? 'primary' : 'outline'}
              onClick={() => setPaymentMethod('paypal')}
              className="flex items-center justify-center space-x-2"
            >
              <WalletIcon className="w-5 h-5" />
              <span>PayPal</span>
            </Button>
          </div>
        
          {/* Payment Summary */}
          <div className="bg-gray-50 p-4 rounded-lg mb-6">
            <div className="flex justify-between items-center">
              <span>Package: {selectedPackage.name}</span>
              <span>{selectedPackage.minutes} minutes</span>
            </div>
            <div className="flex justify-between items-center mt-2">
              <span className="font-semibold">Total:</span>
              <span className="font-semibold text-xl">
                ${selectedPackage.price} {selectedPackage.currency}
              </span>
            </div>
          </div>
        
          <Button
            onClick={handlePurchase}
            disabled={isProcessing}
            className="w-full"
            size="lg"
          >
            {isProcessing ? (
              <>
                <Spinner className="mr-2" />
                Processing Payment...
              </>
            ) : (
              `Purchase ${selectedPackage.minutes} Minutes`
            )}
          </Button>
        </Card>
      )}
    </div>
  );
};
```

### 4. Real-time Job Status Component

```typescript
// JobStatusTracker.tsx - Real-time job progress tracking
export const JobStatusTracker: React.FC = () => {
  const { jobs, updateJobStatus } = useJobStatus();
  const { isConnected } = useWebSocket();
  
  useEffect(() => {
    // Subscribe to job updates via WebSocket
    jobs.forEach(job => {
      if (job.status === 'processing') {
        subscribeToJobUpdates(job.id, (update) => {
          updateJobStatus(job.id, update);
        });
      }
    });
  }, [jobs]);
  
  const getStatusIcon = (status: JobStatus) => {
    switch (status) {
      case 'pending':
        return <ClockIcon className="w-5 h-5 text-yellow-500" />;
      case 'processing':
        return <Spinner className="w-5 h-5 text-blue-500" />;
      case 'completed':
        return <CheckCircleIcon className="w-5 h-5 text-green-500" />;
      case 'failed':
        return <XCircleIcon className="w-5 h-5 text-red-500" />;
    }
  };
  
  const getJobTypeLabel = (type: JobType) => {
    const labels = {
      tts: 'Text to Speech',
      stt: 'Speech to Text',
      voice_clone: 'Voice Cloning',
      accent_change: 'Accent Change',
      language_dub: 'Language Dubbing',
      audio_edit: 'Audio Editing',
      denoise: 'Noise Removal',
      music_gen: 'Music Generation',
      sfx_gen: 'Sound Effects',
      social_music: 'Social Media Music'
    };
    return labels[type] || type;
  };
  
  return (
    <Card className="p-6">
      <div className="flex items-center justify-between mb-4">
        <h3 className="text-lg font-semibold">Processing Jobs</h3>
        <div className="flex items-center space-x-2">
          <div className={`w-2 h-2 rounded-full ${isConnected ? 'bg-green-500' : 'bg-red-500'}`} />
          <span className="text-sm text-gray-500">
            {isConnected ? 'Connected' : 'Disconnected'}
          </span>
        </div>
      </div>
    
      {jobs.length === 0 ? (
        <EmptyState
          icon={<MicrophoneIcon className="w-12 h-12 text-gray-400" />}
          title="No active jobs"
          description="Start processing audio to see jobs here"
        />
      ) : (
        <div className="space-y-4">
          {jobs.map((job) => (
            <div
              key={job.id}
              className="flex items-center justify-between p-4 bg-gray-50 rounded-lg"
            >
              <div className="flex items-center space-x-3">
                {getStatusIcon(job.status)}
                <div>
                  <div className="font-medium">{getJobTypeLabel(job.type)}</div>
                  <div className="text-sm text-gray-500">
                    Started {formatDistanceToNow(job.createdAt)} ago
                  </div>
                </div>
              </div>
            
              <div className="flex items-center space-x-4">
                {job.status === 'processing' && (
                  <div className="flex items-center space-x-2">
                    <Progress value={job.progress} className="w-24" />
                    <span className="text-sm text-gray-500">{job.progress}%</span>
                  </div>
                )}
              
                {job.status === 'completed' && (
                  <Button
                    size="sm"
                    onClick={() => downloadProcessedAudio(job.id)}
                  >
                    Download
                  </Button>
                )}
              
                {job.status === 'failed' && (
                  <Tooltip content={job.errorMessage}>
                    <Button size="sm" variant="outline">
                      Retry
                    </Button>
                  </Tooltip>
                )}
              </div>
            </div>
          ))}
        </div>
      )}
    </Card>
  );
};
```

### 5. Custom Hooks Examples

#### useAudio Hook - Audio Processing Management

```typescript
// useAudio.ts - Custom hook for audio processing
export const useAudio = () => {
  const [isRecording, setIsRecording] = useState(false);
  const [audioBlob, setAudioBlob] = useState<Blob | null>(null);
  const [mediaRecorder, setMediaRecorder] = useState<MediaRecorder | null>(null);
  
  const startRecording = async () => {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ 
        audio: {
          sampleRate: 44100,
          channelCount: 1,
          echoCancellation: true,
          noiseSuppression: true
        }
      });
    
      const recorder = new MediaRecorder(stream, {
        mimeType: 'audio/webm;codecs=opus'
      });
    
      const chunks: BlobPart[] = [];
    
      recorder.ondataavailable = (event) => {
        if (event.data.size > 0) {
          chunks.push(event.data);
        }
      };
    
      recorder.onstop = () => {
        const blob = new Blob(chunks, { type: 'audio/webm' });
        setAudioBlob(blob);
        stream.getTracks().forEach(track => track.stop());
      };
    
      recorder.start();
      setMediaRecorder(recorder);
      setIsRecording(true);
    
    } catch (error) {
      console.error('Error starting recording:', error);
      throw new Error('Failed to start recording. Please check microphone permissions.');
    }
  };
  
  const stopRecording = () => {
    if (mediaRecorder && mediaRecorder.state === 'recording') {
      mediaRecorder.stop();
      setIsRecording(false);
    }
  };
  
  const playAudio = (audioUrl: string) => {
    const audio = new Audio(audioUrl);
    audio.play();
  };
  
  const downloadAudio = (audioUrl: string, filename: string) => {
    const link = document.createElement('a');
    link.href = audioUrl;
    link.download = filename;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };
  
  return {
    isRecording,
    audioBlob,
    startRecording,
    stopRecording,
    playAudio,
    downloadAudio
  };
};
```

#### useWebSocket Hook - Real-time Communication

```typescript
// useWebSocket.ts - WebSocket connection management
export const useWebSocket = () => {
  const [socket, setSocket] = useState<WebSocket | null>(null);
  const [isConnected, setIsConnected] = useState(false);
  const [lastMessage, setLastMessage] = useState<any>(null);
  const { user } = useAuth();
  
  useEffect(() => {
    if (user) {
      connectWebSocket();
    }
  
    return () => {
      disconnectWebSocket();
    };
  }, [user]);
  
  const connectWebSocket = () => {
    const wsUrl = `${process.env.VITE_WS_URL}?token=${user.accessToken}`;
    const ws = new WebSocket(wsUrl);
  
    ws.onopen = () => {
      setIsConnected(true);
      console.log('WebSocket connected');
    };
  
    ws.onmessage = (event) => {
      const message = JSON.parse(event.data);
      setLastMessage(message);
    
      // Handle different message types
      switch (message.type) {
        case 'job_update':
          handleJobUpdate(message.data);
          break;
        case 'credit_update':
          handleCreditUpdate(message.data);
          break;
        case 'notification':
          handleNotification(message.data);
          break;
      }
    };
  
    ws.onclose = () => {
      setIsConnected(false);
      console.log('WebSocket disconnected');
    
      // Attempt to reconnect after 3 seconds
      setTimeout(() => {
        if (user) {
          connectWebSocket();
        }
      }, 3000);
    };
  
    ws.onerror = (error) => {
      console.error('WebSocket error:', error);
    };
  
    setSocket(ws);
  };
  
  const disconnectWebSocket = () => {
    if (socket) {
      socket.close();
      setSocket(null);
      setIsConnected(false);
    }
  };
  
  const sendMessage = (message: any) => {
    if (socket && isConnected) {
      socket.send(JSON.stringify(message));
    }
  };
  
  const subscribeToJobUpdates = (jobId: string) => {
    sendMessage({
      type: 'subscribe',
      channel: `job_${jobId}`
    });
  };
  
  return {
    isConnected,
    lastMessage,
    sendMessage,
    subscribeToJobUpdates
  };
};
```

### 6. State Management (Redux Slices)

#### Audio Processing Slice

```typescript
// audioSlice.ts - Audio processing state management
interface AudioState {
  activeJobs: ProcessingJob[];
  jobHistory: ProcessingJob[];
  currentJob: ProcessingJob | null;
  uploadProgress: number;
  processingProgress: number;
  isUploading: boolean;
  isProcessing: boolean;
  error: string | null;
}

const initialState: AudioState = {
  activeJobs: [],
  jobHistory: [],
  currentJob: null,
  uploadProgress: 0,
  processingProgress: 0,
  isUploading: false,
  isProcessing: false,
  error: null
};

export const audioSlice = createSlice({
  name: 'audio',
  initialState,
  reducers: {
    startJob: (state, action: PayloadAction<ProcessingJob>) => {
      state.activeJobs.push(action.payload);
      state.currentJob = action.payload;
      state.isProcessing = true;
      state.error = null;
    },
  
    updateJobProgress: (state, action: PayloadAction<{ jobId: string; progress: number }>) => {
      const job = state.activeJobs.find(j => j.id === action.payload.jobId);
      if (job) {
        job.progress = action.payload.progress;
      }
      if (state.currentJob?.id === action.payload.jobId) {
        state.processingProgress = action.payload.progress;
      }
    },
  
    completeJob: (state, action: PayloadAction<{ jobId: string; result: any }>) => {
      const jobIndex = state.activeJobs.findIndex(j => j.id === action.payload.jobId);
      if (jobIndex !== -1) {
        const job = state.activeJobs[jobIndex];
        job.status = 'completed';
        job.result = action.payload.result;
        job.completedAt = new Date().toISOString();
      
        // Move to history
        state.jobHistory.unshift(job);
        state.activeJobs.splice(jobIndex, 1);
      
        if (state.currentJob?.id === action.payload.jobId) {
          state.currentJob = null;
          state.isProcessing = false;
          state.processingProgress = 0;
        }
      }
    },
  
    failJob: (state, action: PayloadAction<{ jobId: string; error: string }>) => {
      const job = state.activeJobs.find(j => j.id === action.payload.jobId);
      if (job) {
        job.status = 'failed';
        job.errorMessage = action.payload.error;
      }
    
      if (state.currentJob?.id === action.payload.jobId) {
        state.error = action.payload.error;
        state.isProcessing = false;
      }
    },
  
    setUploadProgress: (state, action: PayloadAction<number>) => {
      state.uploadProgress = action.payload;
      state.isUploading = action.payload < 100;
    },
  
    clearError: (state) => {
      state.error = null;
    }
  }
});

export const {
  startJob,
  updateJobProgress,
  completeJob,
  failJob,
  setUploadProgress,
  clearError
} = audioSlice.actions;

export default audioSlice.reducer;
```

## Key Architecture Principles

### 1. **Component Composition**

- Small, focused components with single responsibilities
- Composition over inheritance for building complex UIs
- Reusable components in the `shared/` directory

### 2. **State Management Strategy**

- Redux Toolkit for global state (user, jobs, payments)
- Local component state for UI-specific data
- Custom hooks for complex state logic

### 3. **Performance Optimization**

- Code splitting by route and feature
- Lazy loading of heavy components
- Memoization of expensive calculations
- Virtual scrolling for large lists

### 4. **User Experience Focus**

- Real-time progress updates via WebSocket
- Optimistic UI updates for better perceived performance
- Comprehensive error handling and user feedback
- Accessibility features throughout

### 5. **Developer Experience**

- TypeScript for type safety
- Comprehensive testing setup
- Clear folder structure and naming conventions
- Extensive documentation

## Page-Level Architecture

### Main Application Flow

```typescript
// App.tsx - Main application component
export const App: React.FC = () => {
  return (
    <Provider store={store}>
      <BrowserRouter>
        <QueryClientProvider client={queryClient}>
          <ThemeProvider>
            <NotificationProvider>
              <Routes>
                {/* Public routes */}
                <Route path="/" element={<HomePage />} />
                <Route path="/login" element={<LoginPage />} />
                <Route path="/register" element={<RegisterPage />} />
              
                {/* Protected routes */}
                <Route element={<ProtectedRoute />}>
                  <Route path="/dashboard" element={<DashboardPage />} />
                  <Route path="/tts" element={<TextToSpeechPage />} />
                  <Route path="/stt" element={<SpeechToTextPage />} />
                  <Route path="/voice-cloning" element={<VoiceCloningPage />} />
                  <Route path="/accent-change" element={<AccentChangePage />} />
                  <Route path="/language-dubbing" element={<LanguageDubbingPage />} />
                  <Route path="/audio-editor" element={<AudioEditorPage />} />
                  <Route path="/noise-removal" element={<NoiseRemovalPage />} />
                  <Route path="/music-generation" element={<MusicGenerationPage />} />
                  <Route path="/sound-effects" element={<SoundEffectsPage />} />
                  <Route path="/social-music" element={<SocialMusicPage />} />
                  <Route path="/voice-library" element={<VoiceLibraryPage />} />
                  <Route path="/payment" element={<PaymentPage />} />
                  <Route path="/billing" element={<BillingPage />} />
                  <Route path="/profile" element={<ProfilePage />} />
                  <Route path="/developer" element={<DeveloperPage />} />
                </Route>
              
                {/* Fallback */}
                <Route path="*" element={<NotFoundPage />} />
              </Routes>
            </NotificationProvider>
          </ThemeProvider>
        </QueryClientProvider>
      </BrowserRouter>
    </Provider>
  );
};
```

## Mobile Responsiveness Strategy

### Responsive Design Approach

- **Mobile-first design** with TailwindCSS breakpoints
- **Progressive enhancement** for larger screens
- **Touch-friendly interfaces** with appropriate sizing
- **Optimized file uploads** for mobile networks
- **Simplified navigation** for smaller screens

The web-client serves as the primary interface for your target audience of content creators, podcasters, and movie creators, providing a professional-grade tool for all AI voice processing needs while maintaining excellent user experience across all devices.

This architecture ensures scalability, maintainability, and excellent performance while delivering the full range of AI voice processing capabilities your platform offers.
