import pyautogui
import time

def click_play_button(x, y):
    pyautogui.click(x, y)
    
def click_button_by_image(image_path): 
    # pyautogui.screenshot('data/debug_screenshot.png')
    
    location = pyautogui.locateOnScreen(image_path, confidence=0.8)
    if location: 
        x, y, width, height = location
        # ボタンの中央をクリック
        pyautogui.click(x + width / 2, y + height / 2)


# def choose_opponent(image_path):
#     location = pyautogui.locateOnScreen(image_path, confidence=0.8)
#     if location: 
#         x, y, width, height = location
#         # ボタンの中央をクリック
#         pyautogui.click(x + width / 2, y + height / 2)

def main():
    # マッチの開始処理
    click_button_by_image('data/play_button.png')
    time.sleep(1)
    click_button_by_image('data/demon_hunter.png') # select opponent
    time.sleep(1)
    click_button_by_image('data/play_button2.png')
    
    
        
        
if __name__ == '__main__':
    main()