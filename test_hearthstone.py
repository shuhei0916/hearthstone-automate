import unittest
from unittest.mock import patch
import pyautogui
from hearthstone import click_play_button, click_play_button_by_image

class TestClickPlayButton(unittest.TestCase):
    @patch('pyautogui.click')
    def test_click_at_specific_position(self, mock_click):
        # self.assertEqual(1, 2, "hoge")
        x, y = 100, 200
        
        click_play_button(x, y)
        
        mock_click.assert_called_once_with(x, y)
    
    @patch('pyautogui.click')
    @patch('pyautogui.locateOnScreen') 
    def test_click_play_button_by_image(self, mock_locate, mock_click):
        # ボタンの画像位置をモック
        mock_locate.return_value = (100, 200, 50, 50) # ボタンの座標(x, y, width, height)
        
        # 実行
        click_play_button_by_image('data/play_button.png')

        # pyautogui.locateOnScreenが正しく呼び出されたかを確認
        mock_locate.assert_called_once_with('data/play_button.png')

        # ボタンの中央をクリックしたかを確認
        mock_click.assert_called_once_with(125, 225) # 中央 (x + width/2, y + height/2)

        
if __name__ == '__main__':
    unittest.main()