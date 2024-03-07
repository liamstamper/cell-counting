# tests/test_counting.py
import pytest
import os
from app.routes import process_and_count

test_images_directory = 'path/to/test_images'
test_cases = [
    # (image_filename, expected_count)
    ("image_1.jpg", 100),
    ("image_2.jpg", 200),
    # Add other test cases here
]

@pytest.mark.parametrize("filename,expected_count", test_cases)
def test_cell_counting_accuracy(filename, expected_count):
    """Test cell counting function for accuracy."""
    image_path = os.path.join(test_images_directory, filename)
    actual_count, _ = process_and_count(image_path)
    assert actual_count == expected_count, f"Expected {expected_count} cells, but counted {actual_count} in {filename}"
