# IBM Cloud Database Setup Guide for SmartClick

## Overview

This guide walks you through setting up IBM Cloud Databases for PostgreSQL (recommended) or MongoDB for SmartClick, and connecting your application to it.

## Why IBM Cloud Database?

✅ **Cloud-native** - No local storage limitations
✅ **Scalable** - Grows with your user base
✅ **Reliable** - Built-in backups and high availability
✅ **Secure** - Encrypted connections and data at rest
✅ **Managed** - IBM handles maintenance and updates
✅ **Multi-user** - Sync across devices (future feature)

## Recommended Database: IBM Cloud Databases for PostgreSQL

PostgreSQL is recommended because:
- Excellent JSON support for flexible data
- ACID compliant for data integrity
- Powerful querying capabilities
- Great performance
- Wide ecosystem support

**Alternative**: IBM Cloud Databases for MongoDB (if you prefer document-based storage)

---

## Step 1: Create IBM Cloud Account

1. Go to https://cloud.ibm.com
2. Click **"Create an account"** (if you don't have one)
3. Complete registration and verify your email
4. Log in to IBM Cloud Console

---

## Step 2: Create Database Instance

### Option A: Using IBM Cloud Console (Recommended for beginners)

1. **Navigate to Catalog**
   - From IBM Cloud dashboard, click **"Catalog"** in top menu
   - Or go directly to: https://cloud.ibm.com/catalog

2. **Find Database Service**
   - In the search bar, type **"Databases for PostgreSQL"**
   - Click on **"Databases for PostgreSQL"**

3. **Configure Database Instance**
   
   **Basic Settings:**
   - **Service name**: `smartclick-db` (or your preferred name)
   - **Region**: Choose closest to your users (e.g., `us-south`, `eu-de`)
   - **Resource group**: `Default` (or create new)

   **Pricing Plan:**
   - **Standard**: Recommended for production
   - **Enterprise**: For high-availability needs
   - Start with **Standard** plan

   **Resource Allocation:**
   - **Memory**: Start with 1 GB (minimum)
   - **Disk**: Start with 5 GB (can scale later)
   - **CPU**: 0 dedicated cores (shared) for development
   
   **Version:**
   - Select latest PostgreSQL version (e.g., PostgreSQL 15)

4. **Configure Networking**
   - **Endpoints**: Select **"Public and Private"** or **"Public"** only
   - **IP Allowlist**: Add your IP addresses (or `0.0.0.0/0` for testing - NOT recommended for production)

5. **Create Instance**
   - Review configuration
   - Click **"Create"**
   - Wait 5-10 minutes for provisioning

### Option B: Using IBM Cloud CLI

```bash
# Install IBM Cloud CLI
curl -fsSL https://clis.cloud.ibm.com/install/linux | sh

# Login
ibmcloud login

# Target resource group
ibmcloud target -g Default

# Create PostgreSQL instance
ibmcloud resource service-instance-create smartclick-db \
  databases-for-postgresql \
  standard \
  us-south \
  -p '{
    "members_memory_allocation_mb": "1024",
    "members_disk_allocation_mb": "5120",
    "version": "15"
  }'
```

---

## Step 3: Get Connection Credentials

### Via IBM Cloud Console

1. **Navigate to Your Database**
   - Go to **Resource List** > **Databases**
   - Click on your database instance (`smartclick-db`)

2. **Access Service Credentials**
   - Click **"Service credentials"** in left sidebar
   - Click **"New credential"** button
   - Name it: `smartclick-app-credentials`
   - Click **"Add"**

3. **View Credentials**
   - Click **"View credentials"** on the newly created credential
   - You'll see a JSON object with connection details

**Example Credentials Structure:**
```json
{
  "connection": {
    "postgres": {
      "composed": [
        "postgres://ibm_cloud_xxx:password@host:port/ibmclouddb?sslmode=verify-full"
      ],
      "hosts": [
        {
          "hostname": "xxx.databases.appdomain.cloud",
          "port": 32541
        }
      ],
      "database": "ibmclouddb",
      "username": "ibm_cloud_xxx",
      "password": "your_password_here",
      "certificate": {
        "certificate_base64": "LS0tLS1CRUdJTi..."
      }
    }
  }
}
```

4. **Save Important Information**
   - **Host**: `xxx.databases.appdomain.cloud`
   - **Port**: `32541`
   - **Database**: `ibmclouddb`
   - **Username**: `ibm_cloud_xxx`
   - **Password**: `your_password_here`
   - **SSL Certificate**: The base64 encoded certificate

---

## Step 4: Configure SmartClick Application

### 4.1 Update Environment Variables

Create/update `.env` file in your project root:

```env
# IBM Cloud Database Configuration
DB_TYPE=postgresql
DB_HOST=xxx.databases.appdomain.cloud
DB_PORT=32541
DB_NAME=ibmclouddb
DB_USER=ibm_cloud_xxx
DB_PASSWORD=your_password_here
DB_SSL=true
DB_SSL_CERT_BASE64=LS0tLS1CRUdJTi...

# Connection Pool Settings
DB_POOL_MIN=2
DB_POOL_MAX=10
DB_CONNECTION_TIMEOUT=30000

# IBM watsonx Configuration (existing)
WATSONX_API_KEY=your_api_key_here
WATSONX_PROJECT_ID=your_project_id_here
WATSONX_ENDPOINT=https://us-south.ml.cloud.ibm.com
WATSONX_MODEL_ID=ibm/granite-13b-chat-v2
```

### 4.2 Install Required NPM Packages

```bash
# PostgreSQL client
npm install pg

# Connection pooling
npm install pg-pool

# SSL certificate handling
npm install node-forge

# TypeScript types
npm install -D @types/pg
```

### 4.3 Create Database Connection Module

**File**: `src/main/services/database/connection.ts`

```typescript
import { Pool, PoolConfig } from 'pg';
import fs from 'fs';
import path from 'path';
import { logger } from '@main/utils/logger';

class DatabaseConnection {
  private pool: Pool | null = null;
  private static instance: DatabaseConnection;

  private constructor() {}

  static getInstance(): DatabaseConnection {
    if (!DatabaseConnection.instance) {
      DatabaseConnection.instance = new DatabaseConnection();
    }
    return DatabaseConnection.instance;
  }

  async connect(): Promise<void> {
    if (this.pool) {
      logger.info('Database already connected');
      return;
    }

    try {
      // Decode SSL certificate from base64
      const certBase64 = process.env.DB_SSL_CERT_BASE64;
      let sslConfig: any = false;

      if (certBase64 && process.env.DB_SSL === 'true') {
        const certBuffer = Buffer.from(certBase64, 'base64');
        sslConfig = {
          rejectUnauthorized: true,
          ca: certBuffer.toString('utf-8'),
        };
      }

      const poolConfig: PoolConfig = {
        host: process.env.DB_HOST,
        port: parseInt(process.env.DB_PORT || '5432'),
        database: process.env.DB_NAME,
        user: process.env.DB_USER,
        password: process.env.DB_PASSWORD,
        ssl: sslConfig,
        min: parseInt(process.env.DB_POOL_MIN || '2'),
        max: parseInt(process.env.DB_POOL_MAX || '10'),
        connectionTimeoutMillis: parseInt(process.env.DB_CONNECTION_TIMEOUT || '30000'),
        idleTimeoutMillis: 30000,
      };

      this.pool = new Pool(poolConfig);

      // Test connection
      const client = await this.pool.connect();
      await client.query('SELECT NOW()');
      client.release();

      logger.info('Database connected successfully', {
        host: process.env.DB_HOST,
        database: process.env.DB_NAME,
      });

      // Handle pool errors
      this.pool.on('error', (err) => {
        logger.error('Unexpected database error', { error: err });
      });

    } catch (error) {
      logger.error('Database connection failed', { error });
      throw new Error(`Failed to connect to database: ${error.message}`);
    }
  }

  async disconnect(): Promise<void> {
    if (this.pool) {
      await this.pool.end();
      this.pool = null;
      logger.info('Database disconnected');
    }
  }

  getPool(): Pool {
    if (!this.pool) {
      throw new Error('Database not connected. Call connect() first.');
    }
    return this.pool;
  }

  async query(text: string, params?: any[]): Promise<any> {
    const pool = this.getPool();
    const start = Date.now();
    
    try {
      const result = await pool.query(text, params);
      const duration = Date.now() - start;
      
      logger.debug('Query executed', {
        query: text,
        duration,
        rows: result.rowCount,
      });
      
      return result;
    } catch (error) {
      logger.error('Query failed', {
        query: text,
        error,
      });
      throw error;
    }
  }

  async transaction<T>(callback: (client: any) => Promise<T>): Promise<T> {
    const pool = this.getPool();
    const client = await pool.connect();
    
    try {
      await client.query('BEGIN');
      const result = await callback(client);
      await client.query('COMMIT');
      return result;
    } catch (error) {
      await client.query('ROLLBACK');
      throw error;
    } finally {
      client.release();
    }
  }
}

export const db = DatabaseConnection.getInstance();
```

---

## Step 5: Create Database Schema

### 5.1 Create Migration Script

**File**: `src/main/services/database/migrations/001_initial_schema.sql`

```sql
-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Conversations table
CREATE TABLE IF NOT EXISTS conversations (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    selected_text TEXT NOT NULL,
    application_name VARCHAR(255),
    application_path TEXT,
    window_title TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    last_accessed_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    message_count INTEGER DEFAULT 0,
    is_pinned BOOLEAN DEFAULT FALSE,
    is_archived BOOLEAN DEFAULT FALSE,
    tags JSONB DEFAULT '[]'::jsonb,
    metadata JSONB DEFAULT '{}'::jsonb
);

-- Messages table
CREATE TABLE IF NOT EXISTS messages (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    conversation_id UUID NOT NULL REFERENCES conversations(id) ON DELETE CASCADE,
    role VARCHAR(20) NOT NULL CHECK (role IN ('user', 'assistant')),
    content TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    token_count INTEGER,
    model_id VARCHAR(100),
    prompt_template VARCHAR(50),
    metadata JSONB DEFAULT '{}'::jsonb
);

-- Settings table
CREATE TABLE IF NOT EXISTS settings (
    key VARCHAR(255) PRIMARY KEY,
    value JSONB NOT NULL,
    category VARCHAR(100),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    metadata JSONB DEFAULT '{}'::jsonb
);

-- Usage statistics table
CREATE TABLE IF NOT EXISTS usage_stats (
    id SERIAL PRIMARY KEY,
    event_type VARCHAR(100) NOT NULL,
    event_data JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    session_id VARCHAR(100)
);

-- Cache table
CREATE TABLE IF NOT EXISTS cache (
    key VARCHAR(255) PRIMARY KEY,
    prompt TEXT NOT NULL,
    response TEXT NOT NULL,
    token_count INTEGER,
    model_id VARCHAR(100),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    accessed_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    access_count INTEGER DEFAULT 1,
    expires_at TIMESTAMP WITH TIME ZONE
);

-- Indexes for performance
CREATE INDEX IF NOT EXISTS idx_conversations_created_at ON conversations(created_at DESC);
CREATE INDEX IF NOT EXISTS idx_conversations_updated_at ON conversations(updated_at DESC);
CREATE INDEX IF NOT EXISTS idx_conversations_application ON conversations(application_name);
CREATE INDEX IF NOT EXISTS idx_conversations_pinned ON conversations(is_pinned, created_at DESC);

CREATE INDEX IF NOT EXISTS idx_messages_conversation ON messages(conversation_id, created_at);
CREATE INDEX IF NOT EXISTS idx_messages_role ON messages(role);

CREATE INDEX IF NOT EXISTS idx_settings_category ON settings(category);

CREATE INDEX IF NOT EXISTS idx_usage_stats_event_type ON usage_stats(event_type, created_at);
CREATE INDEX IF NOT EXISTS idx_usage_stats_created_at ON usage_stats(created_at DESC);

CREATE INDEX IF NOT EXISTS idx_cache_expires_at ON cache(expires_at);
CREATE INDEX IF NOT EXISTS idx_cache_accessed_at ON cache(accessed_at);

-- Function to update updated_at timestamp
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ language 'plpgsql';

-- Trigger for conversations
CREATE TRIGGER update_conversations_updated_at 
    BEFORE UPDATE ON conversations 
    FOR EACH ROW 
    EXECUTE FUNCTION update_updated_at_column();
```

### 5.2 Run Migration

**File**: `src/main/services/database/migrate.ts`

```typescript
import { db } from './connection';
import fs from 'fs';
import path from 'path';
import { logger } from '@main/utils/logger';

export async function runMigrations(): Promise<void> {
  try {
    logger.info('Running database migrations...');

    // Read migration file
    const migrationPath = path.join(__dirname, 'migrations', '001_initial_schema.sql');
    const migrationSQL = fs.readFileSync(migrationPath, 'utf-8');

    // Execute migration
    await db.query(migrationSQL);

    logger.info('Database migrations completed successfully');
  } catch (error) {
    logger.error('Migration failed', { error });
    throw error;
  }
}
```

### 5.3 Initialize Database on App Start

**File**: `src/main/app.ts` (update)

```typescript
import { app } from 'electron';
import { db } from './services/database/connection';
import { runMigrations } from './services/database/migrate';
import { logger } from './utils/logger';

app.on('ready', async () => {
  try {
    // Connect to database
    await db.connect();
    
    // Run migrations
    await runMigrations();
    
    // Continue with app initialization
    // ...
  } catch (error) {
    logger.error('App initialization failed', { error });
    app.quit();
  }
});

app.on('quit', async () => {
  await db.disconnect();
});
```

---

## Step 6: Implement Database Operations

### Example: Conversation Repository

**File**: `src/main/services/database/repositories/conversation.repository.ts`

```typescript
import { db } from '../connection';
import { logger } from '@main/utils/logger';

export interface Conversation {
  id: string;
  selectedText: string;
  applicationName: string;
  windowTitle: string;
  createdAt: Date;
  updatedAt: Date;
  messageCount: number;
  isPinned: boolean;
  tags: string[];
}

export class ConversationRepository {
  async create(data: {
    selectedText: string;
    applicationName: string;
    windowTitle: string;
  }): Promise<string> {
    const result = await db.query(
      `INSERT INTO conversations (selected_text, application_name, window_title)
       VALUES ($1, $2, $3)
       RETURNING id`,
      [data.selectedText, data.applicationName, data.windowTitle]
    );
    
    return result.rows[0].id;
  }

  async findById(id: string): Promise<Conversation | null> {
    const result = await db.query(
      'SELECT * FROM conversations WHERE id = $1',
      [id]
    );
    
    return result.rows[0] || null;
  }

  async findRecent(limit: number = 50): Promise<Conversation[]> {
    const result = await db.query(
      `SELECT * FROM conversations 
       WHERE is_archived = FALSE 
       ORDER BY updated_at DESC 
       LIMIT $1`,
      [limit]
    );
    
    return result.rows;
  }

  async search(query: string): Promise<Conversation[]> {
    const result = await db.query(
      `SELECT * FROM conversations 
       WHERE selected_text ILIKE $1 OR window_title ILIKE $1
       ORDER BY updated_at DESC`,
      [`%${query}%`]
    );
    
    return result.rows;
  }

  async delete(id: string): Promise<void> {
    await db.query('DELETE FROM conversations WHERE id = $1', [id]);
  }
}
```

---

## Step 7: Test Connection

### Create Test Script

**File**: `scripts/test-db-connection.ts`

```typescript
import { db } from '../src/main/services/database/connection';

async function testConnection() {
  try {
    console.log('Testing database connection...');
    
    await db.connect();
    
    const result = await db.query('SELECT NOW() as current_time, version() as pg_version');
    
    console.log('✅ Connection successful!');
    console.log('Current time:', result.rows[0].current_time);
    console.log('PostgreSQL version:', result.rows[0].pg_version);
    
    await db.disconnect();
    
    process.exit(0);
  } catch (error) {
    console.error('❌ Connection failed:', error);
    process.exit(1);
  }
}

testConnection();
```

**Run test:**
```bash
npx ts-node scripts/test-db-connection.ts
```

---

## Step 8: Security Best Practices

### 8.1 Secure Credential Storage

Never commit credentials to Git:

```bash
# Add to .gitignore
.env
.env.local
.env.production
```

### 8.2 Use IBM Cloud Secrets Manager (Optional)

For production, consider using IBM Cloud Secrets Manager:

```typescript
import { SecretsManagerV2 } from '@ibm-cloud/secrets-manager';

const secretsManager = new SecretsManagerV2({
  authenticator: new IamAuthenticator({
    apikey: process.env.IBM_CLOUD_API_KEY,
  }),
  serviceUrl: 'https://secrets-manager.cloud.ibm.com',
});

async function getDbCredentials() {
  const secret = await secretsManager.getSecret({
    id: 'db-credentials-secret-id',
  });
  
  return secret.result.payload;
}
```

### 8.3 IP Allowlist

In IBM Cloud Console:
1. Go to your database instance
2. Click **"Settings"** > **"Allowlist"**
3. Add only necessary IP addresses
4. Remove `0.0.0.0/0` in production

---

## Step 9: Monitoring & Maintenance

### 9.1 Enable Monitoring

In IBM Cloud Console:
1. Go to your database instance
2. Click **"Monitoring"**
3. View metrics: CPU, Memory, Disk, Connections

### 9.2 Set Up Alerts

1. Click **"Alerts"** in database dashboard
2. Create alerts for:
   - High CPU usage (> 80%)
   - Low disk space (< 20%)
   - Connection pool exhaustion

### 9.3 Backup Configuration

IBM Cloud automatically backs up your database:
- **Continuous backup**: Point-in-time recovery
- **Daily snapshots**: Retained for 30 days
- **Manual backups**: Create on-demand

To restore:
1. Go to **"Backups"** tab
2. Select backup point
3. Click **"Restore"**

---

## Troubleshooting

### Connection Timeout

```typescript
// Increase timeout in .env
DB_CONNECTION_TIMEOUT=60000
```

### SSL Certificate Issues

```typescript
// Verify certificate is correctly decoded
const cert = Buffer.from(process.env.DB_SSL_CERT_BASE64, 'base64').toString('utf-8');
console.log(cert); // Should start with -----BEGIN CERTIFICATE-----
```

### Connection Pool Exhausted

```typescript
// Increase pool size in .env
DB_POOL_MAX=20
```

### Slow Queries

```sql
-- Enable query logging
ALTER DATABASE ibmclouddb SET log_statement = 'all';

-- View slow queries
SELECT * FROM pg_stat_statements 
ORDER BY total_exec_time DESC 
LIMIT 10;
```

---

## Cost Optimization

### 1. Right-size Your Instance
- Start small (1GB RAM, 5GB disk)
- Scale up as needed
- Monitor usage regularly

### 2. Use Connection Pooling
- Reuse connections
- Set appropriate pool limits
- Close idle connections

### 3. Implement Caching
- Cache frequent queries
- Use Redis for session data
- Reduce database load

### 4. Archive Old Data
- Move old conversations to cold storage
- Delete unused data
- Implement data retention policies

---

## Summary

You now have:
✅ IBM Cloud Database for PostgreSQL set up
✅ Secure connection from SmartClick
✅ Database schema created
✅ Repository pattern for data access
✅ Monitoring and backups configured

**Next Steps:**
1. Test connection with test script
2. Run migrations to create schema
3. Implement remaining repositories
4. Add error handling and retry logic
5. Set up monitoring alerts

**Estimated Monthly Cost:**
- Standard plan: ~$30-50/month (1GB RAM, 5GB disk)
- Scales with usage

Your SmartClick data is now in the cloud! 🚀