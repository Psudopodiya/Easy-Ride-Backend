import logging
from rest_framework.response import Response
from rest_framework import status


def success_response(data=None, message="Request was successful", status_code=status.HTTP_200_OK):
    """
    Returns a standardized success response.
    """
    return Response(
        {
            "status": "success",
            "message": message,
            "data": data
        },
        status=status_code
    )


def error_response(error=None, error_message="An error occurred", status_code=status.HTTP_400_BAD_REQUEST):
    """
    Returns a standardized error response with detailed error messages.
    """
    return Response(
        {
            "status": "error",
            "message": error_message,
            "error": error
        },
        status=status_code
    )


def validation_error_response(errors, error_message="Validation failed", status_code=status.HTTP_400_BAD_REQUEST):
    """
    Returns a standardized validation error response.
    """
    return Response(
        {
            "status": "error",
            "message": error_message,
            "errors": errors
        },
        status=status_code
    )


def get_logger(name):
    return logging.getLogger(name)
