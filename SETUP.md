# Environment Setup Guide

## Local vs Production: Key Differences

### **Local Development (Your Computer)**
- **Purpose**: Testing and development
- **Database**: SQLite (simple file-based database)
- **Image Storage**: Local filesystem (saved in `media/` folder)
- **Debug Mode**: ON (shows detailed error messages)
- **Security**: Relaxed (for easier development)

### **Production (Live Server)**
- **Purpose**: Real users accessing your application
- **Database**: PostgreSQL or MySQL (robust, scalable)
- **Image Storage**: Cloud storage (AWS S3, Cloudinary, etc.)
- **Debug Mode**: OFF (hides sensitive information)
- **Security**: Strict (protects user data)

## Image Upload: Local vs Production

### **Local Development (Simple)**
- Images saved directly on your computer in `media/` folder
- Easy to test and view
- **Problem**: Not accessible from internet, lost if server restarts

### **Production (Cloud Storage - Recommended)**
- Images saved on cloud services (AWS S3, Cloudinary)
- Accessible from anywhere
- Scalable and reliable
- **Best Options**:
  1. **Cloudinary** (Easiest for beginners)
  2. **AWS S3** (Most popular, more complex)

## Setup Instructions

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Create Environment File
Create a `.env` file in the project root with these variables:

```env
# Environment: 'local' or 'production'
ENVIRONMENT=local

# Secret Key (generate new one for production!)
SECRET_KEY=your-secret-key-here

# Debug Mode (False in production!)
DEBUG=True

# Allowed Hosts (comma-separated)
ALLOWED_HOSTS=*

# Database (for local, use sqlite3)
DATABASE_ENGINE=sqlite3

# Image Storage Type: 'local' or 'cloud'
STORAGE_TYPE=local

# For Cloud Storage (only if STORAGE_TYPE=cloud):
# AWS_ACCESS_KEY_ID=your_key
# AWS_SECRET_ACCESS_KEY=your_secret
# AWS_STORAGE_BUCKET_NAME=your_bucket

# OR for Cloudinary:
# CLOUDINARY_CLOUD_NAME=your_cloud_name
# CLOUDINARY_API_KEY=your_api_key
# CLOUDINARY_API_SECRET=your_api_secret
```

### Step 3: Run Migrations
```bash
python manage.py migrate
```

### Step 4: Run Server
```bash
python manage.py runserver
```

## Production Deployment Checklist

1. ✅ Set `ENVIRONMENT=production` in `.env`
2. ✅ Set `DEBUG=False`
3. ✅ Generate new `SECRET_KEY`
4. ✅ Set `ALLOWED_HOSTS` to your domain
5. ✅ Use PostgreSQL or MySQL database
6. ✅ Set up cloud storage for images
7. ✅ Use environment variables (never hardcode secrets!)
8. ✅ Set up proper web server (Nginx + Gunicorn)

## Image Upload Best Practices

### Option 1: Local Storage (Development Only)
- ✅ Simple setup
- ✅ No additional services needed
- ❌ Not suitable for production
- ❌ Images lost if server restarts

### Option 2: Cloudinary (Recommended for Beginners)
- ✅ Easy setup (just 3 API keys)
- ✅ Free tier available
- ✅ Automatic image optimization
- ✅ CDN included

### Option 3: AWS S3 (Production Standard)
- ✅ Industry standard
- ✅ Highly scalable
- ✅ Very reliable
- ❌ More complex setup
- ❌ Requires AWS account

## Security Notes

⚠️ **NEVER commit `.env` file to git!**
- It contains sensitive information
- Already in `.gitignore`
- Use `.env.example` as template

⚠️ **Production Requirements:**
- `DEBUG=False` (always!)
- Strong `SECRET_KEY`
- Use HTTPS
- Proper database (not SQLite)
- Cloud storage for files
