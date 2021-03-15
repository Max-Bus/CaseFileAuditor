from pyexe.case_file_auditor_utils import *
folder = "C:\\Users\\mkbcu\\OneDrive\\Desktop\\cases\\Abreu, Anthony"
biggest = 0.0
words = get_words_goodie_bag(folder).split()
for i in range(len(words)):
    original = words[i]
    if(not re.search(r"\$",words[i])):
        continue
    else:
        words[i] = re.sub(r"[$,]","",words[i])
    try:
        num = float(words[i])
    except:
        continue
    if isinstance(num,float):
        if num > biggest:
            biggest = num

print(f"case is worth:{biggest}")