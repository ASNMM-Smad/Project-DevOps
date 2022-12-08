import time, os

current_path = os.getcwd()
print (current_path)
SCORES_FILE_NAME = rf"{current_path}\score.txt"
BAD_RETURN_CODE = 666

def screenCleaner():
    print ("TEST", end='\r')
    time.sleep(2)



