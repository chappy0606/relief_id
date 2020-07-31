import time

from PIL import Image
import pyocr.builders
import re
import pyperclip
import pyautogui
import sys


def save_id(tool, repatter):

    txt = tool.image_to_string(
        Image.open('ReliefId.png'),
        lang="jpn",
        builder=pyocr.builders.TextBuilder()
    )

    if len(txt) == 0:
        return None

    else:
        content = txt
        result = repatter.search(content)

        if result is not None:
            return result.group(1)

        else:
            return None


def search_images():
    search_result = pyautogui.locateOnScreen('search.png', confidence=0.8)
    return search_result


def save_screen_shot(search_result):
    screen_shot = pyautogui.screenshot(region=search_result)
    screen_shot.save('ReliefId.png')


def set_clipboard(result):
    pyperclip.copy(result)


if __name__ == '__main__':

    tools = pyocr.get_available_tools()

    if len(tools) == 0:
        print("No OCR tool found")
        sys.exit(1)

    tool = tools[0]

    pattern = '参戦ID : ([a-zA-Z0-9]{8})'
    repatter = re.compile(pattern)

    try:
        while True:
            
            if search_images() is not None:
                save_screen_shot(search_images())

                relief_id = save_id(tool, repatter)

                if relief_id is not None:
                    set_clipboard(relief_id)

                else:
                    pass

            else:
                pass

    except KeyboardInterrupt:
        sys.exit()
