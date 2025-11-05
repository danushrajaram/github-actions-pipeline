from src.logger import DailyLogger
import os

def test_log_entry(tmp_path):
    test_file = tmp_path / "test_log.csv"
    logger = DailyLogger(test_file)
    logger.log_entry("2025-11-05", "Test Intern", "Test Task", "None", "Learned testing", "Add more tests", 8)

    assert test_file.exists()
    with open(test_file) as f:
        content = f.read()
        assert "Test Intern" in content
