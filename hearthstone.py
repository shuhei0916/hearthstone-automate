import pyautogui

def click_play_button(x, y):
    pyautogui.click(x, y)
    
def click_play_button_by_image(image_path): 
    
    pyautogui.screenshot('data/debug_screenshot.png')
    
    location = pyautogui.locateOnScreen(image_path, confidence=0.8)
    if location: 
        x, y, width, height = location
        # ボタンの中央をクリック
        pyautogui.click(x + width / 2, y + height / 2)


def main():
    click_play_button_by_image('data/play_button.png')
        
        
if __name__ == '__main__':
    main()