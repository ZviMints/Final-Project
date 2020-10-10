with open("vocab_update.txt", 'w') as outfile, open("vocab_update2.txt", 'r', encoding='utf-8') as infile:
    for line, i in zip(infile,range(30000)):
        if len(line) > 4:
            outfile.write(line)


