class Error(Exception):
    """Base class for other exceptions

    Args:
        Exception (type): Base for all errors
    """
class ValueSmallError(Error):
    """Rised when input value is too small

    Args:
        Error (object): base error for this class
    """
    def __str__(self):
        return "This number is small"

class ValueLargeError(Error):
    """Rised when input value is too large

    Args:
        Error (object): base error for this class
    """
    def __str__(self):
        return "This number is large"
