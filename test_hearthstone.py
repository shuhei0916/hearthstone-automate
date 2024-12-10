import unittest
from unittest.mock import patch
import pyautogui
from hearthstone import click_play_button, click_button_by_image, wait_for_image

class TestClickPlayButton(unittest.TestCase):
    @patch('pyautogui.click')
    def test_click_at_specific_position(self, mock_click):
        # self.assertEqual(1, 2, "hoge")
        x, y = 100, 200
        
        click_play_button(x, y)
        
        mock_click.assert_called_once_with(x, y)
    
    @patch('pyautogui.click')
    @patch('pyautogui.locateOnScreen')
    def test_click_button_by_image(self, mock_locate, mock_click):
        # ボタンの画像位置をモック
        mock_locate.return_value = (100, 200, 50, 50) # ボタンの座標(x, y, width, height)
        
        # 実行
        click_button_by_image('data/play_button.png')

        # pyautogui.locateOnScreenが正しく呼び出されたかを確認
        mock_locate.assert_called_once_with('data/play_button.png', confidence=0.8)

        # ボタンの中央をクリックしたかを確認
        mock_click.assert_called_once_with(125, 225) # 中央 (x + width/2, y + height/2)
        

class TestWaitForImage(unittest.TestCase):
    @patch('pyautogui.locateOnScreen')
    def test_image_found_immediately(self, mock_locate):
        # 画像が最初の試行で見つかるケース
        mock_locate.return_value = (100, 100, 50, 50)
        result = wait_for_image('data/test_image.png', timeout=5)
        self.assertEqual(result, (100, 100, 50, 50))
        mock_locate.assert_called_once_with('data/test_image.png', confidence=0.8)

    @patch('pyautogui.locateOnScreen')
    def test_image_found_after_delay(self, mock_locate):
        # 画像が2回目の試行で見つかるケース
        mock_locate.side_effect = [None, (200, 200, 60, 60)]
        result = wait_for_image('data/test_image.png', timeout=5)
        self.assertEqual(result, (200, 200, 60, 60))
        self.assertEqual(mock_locate.call_count, 2)

    @patch('pyautogui.locateOnScreen')
    def test_image_not_found_within_timeout(self, mock_locate):
        # 画像がタイムアウトまで見つからないケース
        mock_locate.return_value = None
        with self.assertRaises(TimeoutError):
            wait_for_image('data/test_image.png', timeout=2)
        self.assertGreaterEqual(mock_locate.call_count, 1)
        

        
if __name__ == '__main__':
    unittest.main()