from unittest.mock import patch

from src.main import main


def test_main(capsys):
    """Test the main function outputs the project name."""
    with patch("src.main.settings.PROJECT_NAME", "test_project"):
        main()
        captured = capsys.readouterr()
        assert captured.out.strip() == "test_project"


def test_main_is_callable():
    """Test that main function exists and is callable."""
    assert callable(main)
