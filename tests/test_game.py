from src.game.game import GuessNumber
from unittest import mock

def test_guess_number():
    GN = GuessNumber(0, 5)

    with mock.patch('builtins.input', return_value="yes"):
        assert GN.play_more() == True

    with mock.patch('builtins.input', return_value="no"):
        assert GN.play_more() == False

    with mock.patch('builtins.input', return_value="3"):
        # GN.play()
        assert type(GN.get_guess()) == int

