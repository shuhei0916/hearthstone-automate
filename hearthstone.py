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
        
        
def wait_for_image(image_path, timeout=30):
    start_time = time.time()
    while True:
        try:
            location = pyautogui.locateOnScreen(image_path, confidence=0.8)
            if location:
                return location
        except pyautogui.ImageNotFoundException:
            pass
        if time.time() - start_time > timeout:
            raise TimeoutError(f'Timeout reached while waiting for {image_path}')
        time.sleep(0.5)

def start_match():
    # マッチの開始処理
    click_button_by_image('data/play_button.png')
    time.sleep(1)
    click_button_by_image('data/demon_hunter.png') # select opponent
    time.sleep(1)
    click_button_by_image('data/play_button2.png')

def concede_match():
    print('Condeding match...')
    pyautogui.press('esc')
    time.sleep(0.5)
    click_button_by_image('data/concede_button.png')
    time.sleep(10)
    pyautogui.click(100, 501) # 適当な場所をクリックしてdeck選択画面に戻る


def play_vs_innkeeper():
    start_match() # 試合開始
    wait_for_image('data/confirm_button.png') # マリガン画面まで待機
    concede_match()
    wait_for_image('data/play_button.png') # デッキ選択画面まで待機
    

def main():
    for i in range(3):
        play_vs_innkeeper()

        
if __name__ == '__main__':
    main()