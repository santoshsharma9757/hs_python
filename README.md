# Todo API with JWT Authentication

A production-ready Django REST Framework Todo application with JWT (JSON Web Token) authentication using `djangorestframework-simplejwt`.

## Features

- ✅ User Registration and Authentication
- ✅ JWT Token-based Authentication (Access & Refresh Tokens)
- ✅ CRUD Operations for Todo Items
- ✅ User-specific Todo Isolation (users can only see their own todos)
- ✅ Token Blacklisting for Secure Logout
- ✅ Production-ready with comprehensive error handling
- ✅ Well-commented code for beginners

## Tech Stack

- **Django 6.0** - Web framework
- **Django REST Framework** - API framework
- **djangorestframework-simplejwt** - JWT authentication
- **SQLite** - Database (can be switched to MySQL/PostgreSQL)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/santoshsharma9757/hs_python.git
   cd hs_python
   ```

2. **Create and activate virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   
   Or install manually:
   ```bash
   pip install django djangorestframework djangorestframework-simplejwt
   ```

4. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

The API will be available at `http://127.0.0.1:8000/`

## API Endpoints

### Authentication Endpoints

#### Register User
```http
POST /api/auth/register/
Content-Type: application/json

{
    "username": "john_doe",
    "email": "john@example.com",
    "password": "securepassword123"
}
```

#### Login (Custom View)
```http
POST /api/auth/login/
Content-Type: application/json

{
    "username": "john_doe",
    "password": "securepassword123"
}

Response:
{
    "message": "Login successful",
    "access": "<access_token>",
    "refresh": "<refresh_token>",
    "user_id": 1,
    "username": "john_doe"
}
```

#### Login (SimpleJWT Built-in)
```http
POST /api/auth/token/
Content-Type: application/json

{
    "username": "john_doe",
    "password": "securepassword123"
}

Response:
{
    "access": "<access_token>",
    "refresh": "<refresh_token>"
}
```

#### Refresh Access Token
```http
POST /api/auth/token/refresh/
Content-Type: application/json

{
    "refresh": "<refresh_token>"
}

Response:
{
    "access": "<new_access_token>"
}
```

#### Verify Token
```http
POST /api/auth/token/verify/
Content-Type: application/json

{
    "token": "<access_or_refresh_token>"
}
```

#### Logout
```http
POST /api/auth/logout/
Authorization: Bearer <access_token>
Content-Type: application/json

{
    "refresh": "<refresh_token>"
}
```

### Todo Endpoints

All Todo endpoints require JWT authentication. Include the access token in the Authorization header:
```
Authorization: Bearer <access_token>
```

#### Get All Todos
```http
GET /api/todo/
Authorization: Bearer <access_token>
```

#### Get Single Todo
```http
GET /api/todo/<id>/
Authorization: Bearer <access_token>
```

#### Create Todo
```http
POST /api/todo/
Authorization: Bearer <access_token>
Content-Type: application/json

{
    "title": "My Todo Title",
    "description": "Detailed description of the todo"
}
```

#### Update Todo
```http
PUT /api/todo/<id>/
Authorization: Bearer <access_token>
Content-Type: application/json

{
    "title": "Updated Title",
    "description": "Updated description"
}
```

#### Delete Todo
```http
DELETE /api/todo/<id>/
Authorization: Bearer <access_token>
```

## JWT Token Configuration

- **Access Token Lifetime**: 15 minutes
- **Refresh Token Lifetime**: 7 days
- **Token Rotation**: Enabled (new refresh token issued on refresh)
- **Token Blacklisting**: Enabled (for secure logout)

## Security Features

1. **User Isolation**: Users can only access their own todos
2. **JWT Authentication**: Secure token-based authentication
3. **Token Blacklisting**: Tokens can be invalidated on logout
4. **Token Rotation**: Enhanced security with refresh token rotation
5. **Password Validation**: Django's built-in password validators

## Project Structure

```
hs_python/
├── account/          # User authentication app
│   ├── views.py      # Registration, Login, Logout views
│   ├── serializers.py # User serializers
│   └── urls.py       # Authentication URLs
├── todo/             # Todo app
│   ├── models.py     # Todo model
│   ├── views.py      # Todo CRUD views
│   ├── serializers.py # Todo serializers
│   └── urls.py       # Todo URLs
├── config/           # Project settings
│   ├── settings.py   # Django settings with JWT config
│   └── urls.py       # Main URL configuration
└── manage.py         # Django management script
```

## Testing the API

You can use tools like:
- **Postman** - GUI tool for API testing
- **curl** - Command-line tool
- **httpie** - User-friendly command-line HTTP client
- **Thunder Client** - VS Code extension

### Example with curl:

```bash
# Register
curl -X POST http://127.0.0.1:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser","email":"test@example.com","password":"testpass123"}'

# Login
curl -X POST http://127.0.0.1:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"username":"testuser","password":"testpass123"}'

# Create Todo (replace <access_token> with actual token)
curl -X POST http://127.0.0.1:8000/api/todo/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <access_token>" \
  -d '{"title":"My First Todo","description":"This is my first todo item"}'

# Get All Todos
curl -X GET http://127.0.0.1:8000/api/todo/ \
  -H "Authorization: Bearer <access_token>"
```

## Code Comments

This project includes extensive comments throughout the codebase to help beginners understand:
- How JWT authentication works
- How Django REST Framework serializers function
- How to filter data by user for security
- How to handle errors properly
- Best practices for production-ready code

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source and available for learning purposes.

## Author

Created with ❤️ for learning Django REST Framework and JWT authentication.






