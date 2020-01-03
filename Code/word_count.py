from pathlib import Path
from nltk.tokenize import word_tokenize

def extract_word(file):
    with open(file, "r", encoding='utf-8') as f:
        text = f.read()
        en_list = word_tokenize(text)
        count = len(en_list)
    print("Count:", count)
    return count
news = Path(r"")
num = 0
total = 0
for file in news.glob(r"*.txt"):
    if (num<40):
        print(file)
        total = total + extract_word(file)
        num = num + 1

    else:
        break
print("FILE_WORD:",total,"words")