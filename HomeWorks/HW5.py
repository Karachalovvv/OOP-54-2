# 1)
def require_admin(func):
    def wrapper(user):
        if user.get("is_admin"):
            return "OK"
        else:
            return "Access denied"
    return wrapper


@require_admin
def delete_user(user):
    print(f"User {user['name']} deleted")

print(delete_user({"name": "John", "is_admin": True}))# OK
print(delete_user({"name": "Alice", "is_admin": False}))  # Access denied

# 2)
# def logger(func):
#     def wrapper():
#         print(f"Вызов функции {func.__name__}")
#         func()
#         print(f"Функция {func.__name__} завершена")
#
#     return wrapper
#
# @logger
# def say_hello():
#     print("Hello")
#
# say_hello()