import utils, fileinput

def add_score(new_score, diff, name = 'Asaf_Smadja'):
    new_score = (diff * 3) + 5 + new_score
    old_score = ''
    
    #reading saved score.
    with open(utils.SCORES_FILE_NAME, 'r+') as reading:
        old_score = reading.read()
    update_score = new_score + int(old_score)
    
    #updating the file with the new score
    with fileinput.FileInput(utils.SCORES_FILE_NAME, inplace=True, backup='.bak') as writing:
        for line in writing:
            print (line.replace(str(old_score), str(update_score)), end='')

res = scoring(5, 2)
