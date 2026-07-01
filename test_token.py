from app.core.auth import create_access_token

token = create_access_token(
    {
        "sub": "shrey_new@gmail.com"
    }
)

print(token)