from src.core.exceptions.base import AppError


def test_app_error_stores_context():
    """Test that app errors keep message, code, and details."""
    error = AppError("Something failed", code="something_failed", details={"id": 1})

    assert error.message == "Something failed"
    assert error.code == "something_failed"
    assert error.details == {"id": 1}
    assert str(error) == "Something failed"
