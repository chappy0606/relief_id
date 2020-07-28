from PIL import Image
import pyocr.builders
import re
import pyperclip
import pyautogui
import sys


def save_id():
    tools = pyocr.get_available_tools()
    tool = tools[0]

    txt = tool.image_to_string(
        Image.open('ReliefId.png'),
        lang="jpn",
        builder=pyocr.builders.TextBuilder()
    )

    content = txt
    pattern = '参戦ID : ([a-zA-Z0-9]{8})'

    repatter = re.compile(pattern)
    result = repatter.search(content)

    if result is not None:
        return result.group(1)

    else:
        pass


def save_screen_shot():
    screen_shot = pyautogui.screenshot()
    screen_shot.save('ReliefId.png')


def set_clipboard(result):
    pyperclip.copy(result)


if __name__ == '__main__':
    try:
        while True:
            save_screen_shot()

            relief_id = save_id()

            if relief_id is not None:
                set_clipboard(relief_id)
                print(relief_id)

            else:
                pass

    except KeyboardInterrupt:
        sys.exit()