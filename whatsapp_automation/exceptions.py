class InvalidPhoneNumber(Exception):
    def __init__(self, number, message="Invalid phone number format"):
        self.number = number
        self.message = message
        super().__init__(f"{message}: {number}")
