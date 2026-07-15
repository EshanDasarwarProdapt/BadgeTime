from user_auth import UserAuth

def test_register_login():
    auth = UserAuth()
    assert auth.register_user("testuser", "password123") == True
    assert auth.login_user("testuser", "password123") == True


def test_register_existing_user():
    auth = UserAuth()
    assert auth.register_user("admin", "newpassword") == False

def test_login_wrong_password():
    auth = UserAuth()
    auth.register_user("newuser","passs")
    assert auth.login_user("newuser", "wrongpassword") == False