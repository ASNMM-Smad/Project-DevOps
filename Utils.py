import time, os

current_path = os.getcwd()
SCORES_FILE_NAME = rf"{current_path}\project\score.txt"

BAD_RETURN_CODE = 666

def screenCleaner():
    print ("TEST", end='\r')
    time.sleep(2)



