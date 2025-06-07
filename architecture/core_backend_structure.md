# Core Backend - Detailed Folder Structure & Purpose

I'll provide a detailed explanation of the core-backend folder structure and the purpose of each component.The core-backend is essentially the **central nervous system** of your GenAI voice platform. Here's a summary of its key roles:

## **Primary Responsibilities:**

### 🔐 **Authentication & Security Hub**

* Handles user registration, login, and JWT token management
* Implements rate limiting and security middleware
* Manages API keys for developer access
* Protects against common cyber attacks

### 🎵 **Audio Processing Orchestrator**

* Receives audio processing requests from clients
* Queues jobs for the AI processing service
* Tracks job progress and status
* Manages file uploads and downloads

### 💳 **Payment & Credit Management**

* Processes payments through multiple providers
* Manages the credit system (60 minutes for $20)
* Tracks usage and enforces download limits
* Handles billing and subscription management

### 📊 **Data & Analytics Center**

* Manages user accounts and profiles
* Stores voice library and processing history
* Generates usage analytics and reports
* Maintains audit logs for compliance

### 🔌 **Integration Layer**

* Connects frontend clients with AI services
* Interfaces with external payment providers
* Manages file storage (S3/MinIO)
* Handles email notifications

## **Key Design Patterns Used:**

1. **MVC Architecture** : Controllers handle requests, Services contain business logic, Models manage data
2. **Middleware Pipeline** : Security, authentication, validation, and logging layers
3. **Service Layer Pattern** : Separation of concerns with dedicated services for payments, audio, etc.
4. **Repository Pattern** : Database abstraction through models
5. **Queue-based Processing** : Asynchronous AI job processing with Redis/Bull

## **Why This Structure?**

* **Scalability** : Each component can be scaled independently
* **Maintainability** : Clear separation of concerns makes debugging easier
* **Security** : Layered security approach with multiple validation points
* **Testability** : Each component can be unit tested independently
* **Flexibility** : Easy to add new AI models or payment providers

This structure ensures your platform can handle the demands of content creators, podcasters, and movie creators while maintaining professional-grade reliability and security.


## Overview

The core-backend service is the main API server that handles all business logic, user management, payment processing, and orchestrates AI processing jobs. It acts as the central hub that connects the frontend clients with the AI processing services.

## Complete Folder Structure

```
services/core-backend/
│
├── src/                           # Source code directory
│   ├── controllers/               # Request handlers & business logic
│   │   ├── audio.controller.ts    # Audio processing endpoints
│   │   ├── user.controller.ts     # User management endpoints
│   │   ├── payment.controller.ts  # Payment & billing endpoints
│   │   ├── voice.controller.ts    # Voice library management
│   │   ├── admin.controller.ts    # Admin panel endpoints
│   │   ├── developer.controller.ts # Developer API management
│   │   └── health.controller.ts   # System health checks
│   │
│   ├── middleware/                # Express middleware functions
│   │   ├── auth.middleware.ts     # JWT authentication
│   │   ├── rateLimiter.middleware.ts # API rate limiting
│   │   ├── upload.middleware.ts   # File upload handling
│   │   ├── validation.middleware.ts # Input validation
│   │   ├── cors.middleware.ts     # CORS configuration
│   │   ├── security.middleware.ts # Security headers
│   │   ├── logging.middleware.ts  # Request logging
│   │   └── error.middleware.ts    # Error handling
│   │
│   ├── models/                    # Database models & schemas
│   │   ├── User.model.ts          # User entity model
│   │   ├── ProcessingJob.model.ts # AI job tracking model
│   │   ├── Payment.model.ts       # Payment records model
│   │   ├── VoiceLibrary.model.ts  # Voice samples model
│   │   ├── UsageTracking.model.ts # Usage analytics model
│   │   ├── ApiKey.model.ts        # Developer API keys
│   │   └── index.ts               # Model exports & DB connection
│   │
│   ├── routes/                    # API route definitions
│   │   ├── auth.routes.ts         # Authentication routes
│   │   ├── audio.routes.ts        # Audio processing routes
│   │   ├── payment.routes.ts      # Payment & billing routes
│   │   ├── user.routes.ts         # User management routes
│   │   ├── voice.routes.ts        # Voice library routes
│   │   ├── admin.routes.ts        # Admin panel routes
│   │   ├── developer.routes.ts    # Developer API routes
│   │   ├── webhook.routes.ts      # Payment webhooks
│   │   └── index.ts               # Route aggregation
│   │
│   ├── services/                  # Business logic services
│   │   ├── audio.service.ts       # Audio processing orchestration
│   │   ├── payment.service.ts     # Payment processing logic
│   │   ├── queue.service.ts       # Job queue management
│   │   ├── storage.service.ts     # File storage operations
│   │   ├── email.service.ts       # Email notifications
│   │   ├── analytics.service.ts   # Usage analytics
│   │   ├── credit.service.ts      # Credit system management
│   │   ├── notification.service.ts # Real-time notifications
│   │   └── model.service.ts       # AI model management
│   │
│   ├── utils/                     # Utility functions
│   │   ├── logger.ts              # Winston logging configuration
│   │   ├── validator.ts           # Input validation helpers
│   │   ├── encryption.ts          # Encryption/hashing utilities
│   │   ├── jwt.ts                 # JWT token utilities
│   │   ├── file.ts                # File handling utilities
│   │   ├── constants.ts           # Application constants
│   │   ├── helpers.ts             # General helper functions
│   │   └── errors/                # Custom error classes
│   │       ├── AppError.ts        # Base error class
│   │       ├── ValidationError.ts # Validation error class
│   │       └── PaymentError.ts    # Payment error class
│   │
│   ├── types/                     # TypeScript type definitions
│   │   ├── express.d.ts           # Express type extensions
│   │   ├── auth.types.ts          # Authentication types
│   │   ├── audio.types.ts         # Audio processing types
│   │   ├── payment.types.ts       # Payment types
│   │   ├── user.types.ts          # User types
│   │   ├── api.types.ts           # API response types
│   │   └── database.types.ts      # Database types
│   │
│   ├── config/                    # Configuration files
│   │   ├── database.ts            # Database configuration
│   │   ├── redis.ts               # Redis configuration
│   │   ├── storage.ts             # File storage config
│   │   ├── payment.ts             # Payment provider config
│   │   ├── email.ts               # Email service config
│   │   ├── security.ts            # Security settings
│   │   └── index.ts               # Config aggregation
│   │
│   ├── migrations/                # Database migrations
│   │   ├── 001_create_users.sql   # User table creation
│   │   ├── 002_create_jobs.sql    # Jobs table creation
│   │   ├── 003_create_payments.sql # Payment tables
│   │   └── 004_add_indexes.sql    # Performance indexes
│   │
│   ├── seeds/                     # Database seed data
│   │   ├── users.seed.ts          # Sample users
│   │   ├── voices.seed.ts         # Default voice library
│   │   └── admin.seed.ts          # Admin user creation
│   │
│   ├── jobs/                      # Background job definitions
│   │   ├── cleanup.job.ts         # File cleanup jobs
│   │   ├── analytics.job.ts       # Analytics processing
│   │   ├── email.job.ts           # Email sending jobs
│   │   └── monitoring.job.ts      # System monitoring jobs
│   │
│   ├── websockets/                # WebSocket handlers
│   │   ├── job-status.ws.ts       # Real-time job updates
│   │   ├── notifications.ws.ts    # User notifications
│   │   └── admin.ws.ts            # Admin real-time updates
│   │
│   ├── swagger/                   # API documentation
│   │   ├── schemas/               # OpenAPI schemas
│   │   ├── paths/                 # API path definitions
│   │   └── swagger.config.ts      # Swagger configuration
│   │
│   ├── app.ts                     # Express app configuration
│   ├── server.ts                  # Server startup file
│   └── database.ts                # Database connection setup
│
├── tests/                         # Test files
│   ├── unit/                      # Unit tests
│   │   ├── controllers/           # Controller tests
│   │   ├── services/              # Service tests
│   │   ├── middleware/            # Middleware tests
│   │   └── utils/                 # Utility tests
│   ├── integration/               # Integration tests
│   │   ├── api/                   # API endpoint tests
│   │   └── database/              # Database tests
│   ├── fixtures/                  # Test data fixtures
│   └── setup.ts                   # Test environment setup
│
├── docs/                          # Documentation
│   ├── api.md                     # API documentation
│   ├── deployment.md              # Deployment guide
│   └── architecture.md            # Architecture overview
│
├── scripts/                       # Utility scripts
│   ├── build.sh                   # Build script
│   ├── migrate.sh                 # Database migration
│   ├── seed.sh                    # Database seeding
│   └── cleanup.sh                 # Cleanup script
│
├── package.json                   # Node.js dependencies
├── tsconfig.json                  # TypeScript configuration
├── jest.config.js                 # Jest testing configuration
├── .eslintrc.js                   # ESLint configuration
├── .prettierrc                    # Prettier configuration
├── .env.example                   # Environment variables template
├── Dockerfile                     # Docker container definition
├── .dockerignore                  # Docker ignore file
└── README.md                      # Service documentation
```

## Detailed Component Purposes

### 1. Controllers (`src/controllers/`)

Controllers handle HTTP requests and responses. They contain the endpoint logic and coordinate between middleware, services, and models.

```typescript
// audio.controller.ts - Example structure
export class AudioController {
  // Text-to-Speech endpoint
  async textToSpeech(req: Request, res: Response) {
    // 1. Validate input
    // 2. Check user credits
    // 3. Queue AI processing job
    // 4. Return job ID to client
  }
  
  // Speech-to-Text endpoint
  async speechToText(req: Request, res: Response) {
    // 1. Handle file upload
    // 2. Validate audio file
    // 3. Queue STT processing
    // 4. Return job status
  }
  
  // Download processed audio (consumes credits)
  async downloadAudio(req: Request, res: Response) {
    // 1. Verify job completion
    // 2. Deduct user credits
    // 3. Generate signed download URL
    // 4. Track usage analytics
  }
}
```

### 2. Middleware (`src/middleware/`)

Middleware functions process requests before they reach controllers.

```typescript
// auth.middleware.ts - JWT Authentication
export const authenticateToken = async (req: Request, res: Response, next: NextFunction) => {
  const token = req.headers.authorization?.split(' ')[1];
  
  if (!token) {
    return res.status(401).json({ error: 'Access token required' });
  }
  
  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    req.user = await User.findById(decoded.userId);
    next();
  } catch (error) {
    return res.status(403).json({ error: 'Invalid token' });
  }
};

// validation.middleware.ts - Input Validation
export const validateAudioRequest = [
  body('text').isLength({ min: 1, max: 10000 }).trim(),
  body('model').isIn(['tacotron2', 'waveglow']),
  body('voice_id').optional().isUUID(),
  handleValidationErrors
];
```

### 3. Models (`src/models/`)

Database models define data structure and relationships.

```typescript
// User.model.ts - User entity
export interface User {
  id: string;
  email: string;
  password_hash: string;
  name: string;
  subscription_tier: 'free' | 'premium' | 'enterprise';
  credits_remaining: number;
  total_minutes_downloaded: number;
  created_at: Date;
  updated_at: Date;
}

// ProcessingJob.model.ts - AI job tracking
export interface ProcessingJob {
  id: string;
  user_id: string;
  job_type: 'tts' | 'stt' | 'voice_clone' | 'denoise' | etc;
  model_name: string;
  input_file_path?: string;
  output_file_path?: string;
  parameters: Record<string, any>;
  status: 'pending' | 'processing' | 'completed' | 'failed';
  progress: number; // 0-100
  error_message?: string;
  processing_time_seconds?: number;
  created_at: Date;
  completed_at?: Date;
}
```

### 4. Routes (`src/routes/`)

Route definitions map HTTP endpoints to controller methods.

```typescript
// audio.routes.ts - Audio processing routes
const router = express.Router();

// Apply authentication to all audio routes
router.use(authenticateToken);

// Text-to-Speech
router.post('/tts', 
  validateAudioRequest, 
  rateLimiters.audioProcessing,
  audioController.textToSpeech
);

// Speech-to-Text
router.post('/stt', 
  upload.single('audio'),
  validateAudioFile,
  audioController.speechToText
);

// Voice cloning
router.post('/voice-clone',
  upload.single('audio'),
  validateVoiceCloneRequest,
  audioController.voiceClone
);

// Download processed audio (costs credits)
router.post('/download/:jobId',
  checkUserCredits,
  audioController.downloadAudio
);
```

### 5. Services (`src/services/`)

Services contain business logic and coordinate between different components.

```typescript
// audio.service.ts - Audio processing orchestration
export class AudioService {
  async processTextToSpeech(userId: string, request: TTSRequest) {
    // 1. Validate user has sufficient credits for experimentation
    const user = await User.findById(userId);
  
    // 2. Create processing job record
    const job = await ProcessingJob.create({
      user_id: userId,
      job_type: 'tts',
      model_name: request.model,
      parameters: request.parameters,
      status: 'pending'
    });
  
    // 3. Queue job for AI processing
    await this.queueService.addJob('tts-processing', {
      jobId: job.id,
      userId,
      ...request
    });
  
    // 4. Set up real-time progress updates
    this.websocketService.joinRoom(userId, `job-${job.id}`);
  
    return { jobId: job.id, status: 'queued' };
  }
  
  async handleJobCompletion(jobId: string, result: ProcessingResult) {
    // 1. Update job status in database
    await ProcessingJob.update(jobId, {
      status: result.success ? 'completed' : 'failed',
      output_file_path: result.outputPath,
      error_message: result.error,
      processing_time_seconds: result.processingTime
    });
  
    // 2. Notify user via WebSocket
    const job = await ProcessingJob.findById(jobId);
    this.websocketService.emit(`job-${jobId}`, {
      status: job.status,
      progress: 100,
      downloadUrl: result.success ? await this.generateDownloadUrl(result.outputPath) : null
    });
  
    // 3. Send email notification if enabled
    if (result.success) {
      await this.emailService.sendJobCompletionEmail(job.user_id, job);
    }
  }
}

// payment.service.ts - Payment processing
export class PaymentService {
  async createPaymentIntent(userId: string, packageId: string) {
    const package = CREDIT_PACKAGES.find(p => p.id === packageId);
    const user = await User.findById(userId);
  
    // Create payment record
    const payment = await Payment.create({
      user_id: userId,
      amount: package.price,
      currency: package.currency,
      credits_to_add: package.minutes,
      status: 'pending'
    });
  
    // Create Stripe payment intent
    const paymentIntent = await stripe.paymentIntents.create({
      amount: package.price * 100, // Convert to cents
      currency: package.currency.toLowerCase(),
      metadata: {
        userId,
        paymentId: payment.id,
        credits: package.minutes.toString()
      }
    });
  
    await Payment.update(payment.id, {
      transaction_id: paymentIntent.id
    });
  
    return {
      clientSecret: paymentIntent.client_secret,
      paymentId: payment.id
    };
  }
  
  async handleWebhook(signature: string, payload: any) {
    // Verify webhook signature
    const event = stripe.webhooks.constructEvent(payload, signature, process.env.STRIPE_WEBHOOK_SECRET);
  
    if (event.type === 'payment_intent.succeeded') {
      const paymentIntent = event.data.object;
      const { userId, paymentId, credits } = paymentIntent.metadata;
    
      // Update payment status
      await Payment.update(paymentId, { status: 'completed' });
    
      // Add credits to user account
      await User.updateCredits(userId, parseInt(credits));
    
      // Send confirmation email
      await this.emailService.sendPaymentConfirmation(userId, credits);
    }
  }
}
```

### 6. Utils (`src/utils/`)

Utility functions provide reusable functionality across the application.

```typescript
// logger.ts - Centralized logging
export const logger = winston.createLogger({
  level: process.env.LOG_LEVEL || 'info',
  format: winston.format.combine(
    winston.format.timestamp(),
    winston.format.errors({ stack: true }),
    winston.format.json()
  ),
  defaultMeta: { service: 'genai-voice-api' },
  transports: [
    new winston.transports.File({ filename: 'logs/error.log', level: 'error' }),
    new winston.transports.File({ filename: 'logs/combined.log' }),
    ...(process.env.NODE_ENV !== 'production' ? [
      new winston.transports.Console({ format: winston.format.simple() })
    ] : [])
  ]
});

// jwt.ts - JWT token management
export const generateTokens = async (userId: string) => {
  const accessToken = jwt.sign(
    { userId, type: 'access' },
    process.env.JWT_SECRET,
    { expiresIn: '15m' }
  );
  
  const refreshToken = jwt.sign(
    { userId, type: 'refresh' },
    process.env.JWT_REFRESH_SECRET,
    { expiresIn: '7d' }
  );
  
  // Store refresh token in database
  await RefreshToken.create({
    user_id: userId,
    token: refreshToken,
    expires_at: new Date(Date.now() + 7 * 24 * 60 * 60 * 1000)
  });
  
  return { accessToken, refreshToken };
};
```

### 7. Configuration (`src/config/`)

Configuration files manage environment-specific settings.

```typescript
// database.ts - Database configuration
export const databaseConfig = {
  development: {
    host: process.env.DB_HOST || 'localhost',
    port: parseInt(process.env.DB_PORT) || 5432,
    database: process.env.DB_NAME || 'genai_voice_dev',
    username: process.env.DB_USER || 'developer',
    password: process.env.DB_PASS || 'password',
    dialect: 'postgres',
    logging: console.log,
    pool: {
      max: 5,
      min: 0,
      acquire: 30000,
      idle: 10000
    }
  },
  production: {
    host: process.env.DB_HOST,
    port: parseInt(process.env.DB_PORT),
    database: process.env.DB_NAME,
    username: process.env.DB_USER,
    password: process.env.DB_PASS,
    dialect: 'postgres',
    logging: false,
    pool: {
      max: 20,
      min: 5,
      acquire: 60000,
      idle: 10000
    },
    ssl: {
      require: true,
      rejectUnauthorized: false
    }
  }
};
```

## Key Responsibilities

### 1. **API Gateway Functions**

- Route incoming requests to appropriate controllers
- Handle authentication and authorization
- Apply rate limiting based on user tier
- Validate input data and sanitize requests

### 2. **Business Logic Orchestration**

- Coordinate between different AI processing services
- Manage user credits and billing
- Track usage analytics and generate reports
- Handle file uploads and storage management

### 3. **Real-time Communication**

- WebSocket connections for job progress updates
- Real-time notifications for users and admins
- Live dashboard updates for system monitoring

### 4. **Data Management**

- User account management and authentication
- Payment processing and credit management
- Job tracking and history maintenance
- Voice library and asset management

### 5. **Integration Hub**

- Connect with AI processing services via message queues
- Integrate with payment providers (Stripe, Razorpay, PayPal)
- Interface with file storage services (S3, MinIO)
- Connect with email and notification services

This core-backend serves as the central nervous system of your GenAI voice platform, handling all user interactions, business logic, and service coordination while maintaining security, scalability, and performance standards.
