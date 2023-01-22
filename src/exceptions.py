
from http import HTTPStatus


class AppError(Exception):
    """Class Default to Error in application."""

    status: int


class ErrorNotListValid(AppError):
    status = HTTPStatus.BAD_REQUEST


class ErrorBody(AppError):
    status = HTTPStatus.BAD_REQUEST


class ErrorContentTypeInvalid(AppError):
    status = HTTPStatus.BAD_REQUEST


class ErrorOrderInvalid(AppError):
    status = HTTPStatus.BAD_REQUEST
