def word_count():
    count = 0
    with open("C:\\users\\xxdima\\Desktop\\Course DevOps\\file.txt") as f:
        data = f.readlines()
        for line in data:
            words = line.split()
            for word in words:
                if word == "Alex":
                    count += 1
    return count