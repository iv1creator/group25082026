import time
import jwt

SECRET_KEY = "my_secret_key"
WRONG_KEY = "wrong_secret_key"

payload_data = {
    "last_name": "Божко",
    "group": "25082026",
    "sub": "user1",
}

print("1. створення JWT та успішне декодування")
valid_payload = payload_data.copy()
valid_payload["exp"] = int(time.time()) + 600

encoded_token = jwt.encode(valid_payload, SECRET_KEY, algorithm="HS256")
print(f"згенерований JWT-токен:\n{encoded_token}\n")

decoded_payload = jwt.decode(encoded_token, SECRET_KEY, algorithms=["HS256"])
print(f"успішно декодовані дані:\n{decoded_payload}\n")


print("2. спроба декодування простроченого токена")
expired_payload = payload_data.copy()
expired_payload["exp"] = int(time.time()) - 10

expired_token = jwt.encode(expired_payload, SECRET_KEY, algorithm="HS256")

try:
    jwt.decode(expired_token, SECRET_KEY, algorithms=["HS256"])
except jwt.ExpiredSignatureError as e:
    print(f"Помилка: Токен прострочено ({e})\n")


print("3. спроба декодування з невірним підписом")
try:
    jwt.decode(encoded_token, WRONG_KEY, algorithms=["HS256"])
except jwt.InvalidSignatureError as e:
    print(f"Помилка: Невірний підпис ({e})\n")