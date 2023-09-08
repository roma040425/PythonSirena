важно-чтобы приложение правильно работало ярлык терминала грз должен наодиться в верхнем левом углу экрана.Так же данный код написан для разрешения fullHD 1920х1080
впоследствии в коде нужно внести изменение password='пароль марины александровны'
для того чтобы поменять код для другого разрешения используйте команду:

import pyautogui
 
# Wait for the app to open and navigate to the desired element
# ...
 
# Get the coordinates of the current mouse position
current_position = pyautogui.position()
 
# Print the coordinates
print("x:", current_position.x)
print("y:", current_position.y)
 
эта команда даст координаты которые нужно будет заменить в коде.
Если вдруг программа терминала вдруг будет 64 битная напишите мне я отправлю вам другой код с функциями чтения свс и автоввода.

для конвертации кода питон в exe файл я использовал 
pyinstaller --onefile main.py
если будут еще вопросы-пишите.Удачи
