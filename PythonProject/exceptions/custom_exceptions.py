class ElementNotFoundException(Exception):
    """Raised when an element is not found"""
    def __init__(self, message="Element not found on page"):
        self.message = message
        super().__init__(self.message)
