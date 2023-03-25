from src.pre_built.counter import count_ocurrences


mocked_path = 'data/jobs.csv'
mocked_word = 'Design'


def test_counter():
    # Arrange
    expected = 3584
    # Act
    result = count_ocurrences(mocked_path, mocked_word)
    # Assert
    assert result == expected
