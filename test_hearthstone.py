import unittest
from unittest.mock import patch
import pyautogui
from hearthstone import click_play_button

class TestClickPlayButton(unittest.TestCase):
    @patch('pyautogui.click')
    def test_click_at_specific_position(self, mock_click):
        # self.assertEqual(1, 2, "hoge")
        x, y = 100, 200
        
        click_play_button(x, y)
        
        
        mock_click.assert_called_once_with(x, y)
        
if __name__ == '__main__':
    unittest.main()