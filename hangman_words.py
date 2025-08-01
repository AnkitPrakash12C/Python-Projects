import csv

word_list = ["nurse", "hospital", "medicine", "surgery", "patient"]

with open(r'D:\Sem6\Python Projects\Hangman\Dictionary_eng\Aword.csv', mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    for word in word_list:
        writer.writerow([word])