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


def main():
    # マッチの開始処理
    click_button_by_image('data/play_button.png')
    time.sleep(1)
    click_button_by_image('data/demon_hunter.png') # select opponent
    time.sleep(1)
    click_button_by_image('data/play_button2.png')
    
    # マリガン画面まで待機
    print("Waiting for the confirm button to appear...")
    while True:
        try:
            location = pyautogui.locateOnScreen('data/confirm_button.png', confidence=0.8)
            if location:
                break
        except pyautogui.ImageNotFoundException:
            pass
        time.sleep(0.5)  # 短い間隔で確認
    print("Confirm button appeared!")
    
    
    # マリガンせずにコンシード
    pyautogui.press('esc')
    time.sleep(0.5)
    click_button_by_image('data/concede_button.png')
    time.sleep(10)
    pyautogui.click(100, 501) # 適当な場所をクリックしてdeck選択画面に戻る
    
    # 
    while True:
        try:
            location = pyautogui.locateOnScreen('data/play_button.png', confidence=0.8)
            if location:
                break
        except pyautogui.ImageNotFoundException:
            pass
        time.sleep(0.5)  # 短い間隔で確認 
    

        
if __name__ == '__main__':
    main()