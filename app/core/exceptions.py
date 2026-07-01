class UserAlreadyExistsException(Exception):
    """Raised when a user with the same email already exists."""

    def __init__(self):
        self.message = "Email already registered."
        super().__init__(self.message)


class InvalidCredentialsException(Exception):
    """Raised when login credentials are invalid."""

    def __init__(self):
        self.message = "Invalid email or password."
        super().__init__(self.message)