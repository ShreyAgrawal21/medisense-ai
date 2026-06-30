class UserAlreadyExistsException(Exception):
    """Raised when a user with the same email already exists."""

    def __init__(self):
        self.message = "Email already registered."
        super().__init__(self.message)