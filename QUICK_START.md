# Quick Start: Local vs Production Setup

## 🚀 Quick Setup (5 Minutes)

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Create `.env` File
Create a `.env` file in project root:

**For Local Development:**
```env
ENVIRONMENT=local
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=*
STORAGE_TYPE=local
```

**For Production:**
```env
ENVIRONMENT=production
DEBUG=False
SECRET_KEY=generate-new-secret-key
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
STORAGE_TYPE=cloud
# Add cloud storage credentials (Cloudinary or AWS S3)
```

### 3. Run Server
```bash
python manage.py migrate
python manage.py runserver
```

---

## 📋 Key Differences Summary

| Setting | Local | Production |
|---------|-------|------------|
| **ENVIRONMENT** | `local` | `production` |
| **DEBUG** | `True` | `False` (MUST!) |
| **Database** | SQLite | PostgreSQL/MySQL |
| **Image Storage** | Local folder | Cloud (S3/Cloudinary) |
| **SECRET_KEY** | Any | Strong, unique key |
| **ALLOWED_HOSTS** | `*` | Your domain only |

---

## 🖼️ Image Upload: Simple Explanation

### Local (Your Computer)
- Images saved in `media/` folder
- Only you can see them
- Good for testing

### Production (Internet)
- Images saved on cloud (AWS/Cloudinary)
- Everyone can see them
- Professional solution

**Your code doesn't change!** Just change `STORAGE_TYPE` in `.env`.

---

## ⚠️ Important Notes

1. **Never commit `.env` file** - It contains secrets!
2. **Always set `DEBUG=False` in production**
3. **Generate new SECRET_KEY for production**
4. **Use cloud storage in production** (not local)

---

## 📚 More Information

- **Full Setup Guide**: See `SETUP.md`
- **Image Upload Details**: See `IMAGE_UPLOAD_GUIDE.md`
- **Django Docs**: https://docs.djangoproject.com/

---

## 🆘 Need Help?

**Common Issues:**
- Images not showing? → Check `STORAGE_TYPE` setting
- Server error? → Check `DEBUG=False` in production
- Database error? → Run `python manage.py migrate`

**Remember:** 
- Local = Development (your computer)
- Production = Live server (real users)
