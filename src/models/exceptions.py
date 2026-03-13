class SFMShopException(Exception):
    """базовый класс"""
    pass

class ValidationError(SFMShopException):
    """для ошибок валидации"""
    pass

class BusinessLogicError(SFMShopException):
    """для ошибок бизнес-логики"""
    pass

class DataBaseError(SFMShopException):
    """для ошибок базы данных"""
    pass

class NegativePriceError(ValidationError):
    """отрицательная цена"""
    pass

class InsufficientStockError(BusinessLogicError):
    """недостаточно товара"""
    pass

class InvalidOrderError(BusinessLogicError):
    """невалидный заказ"""
    pass

