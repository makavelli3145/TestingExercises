from app.file_streams import *

def test_can_read_from_one_file_and_write_to_another(tmp_path):
    file_path = tmp_path / "mock_dir"
    file_path.mkdir()

    test_file_read = file_path / "test_file_read.txt"
    test_file_write = file_path / "test_file_write.txt"

    test_file_read.write_text("This is a test file, intended to be read...")

    copy_first_line(str(test_file_read), str(test_file_write))

    assert test_file_write.read_text() == "This is a test file, intended to be read..."