import sys

# Mapper for Character Count
def char_mapper():
    for line in sys.stdin:
        line = line.strip()
        for char in line:
            print(f"{char}\t1")

# Reducer for Character Count
def char_reducer():
    current_char = None
    current_count = 0

    for line in sys.stdin:
        parts = line.strip().split('\t')
        if len(parts) != 2:
            continue
        char, count = parts
        count = int(count)

        if current_char == char:
            current_count += count
        else:
            if current_char:
                print(f"{current_char}\t{current_count}")
            current_char = char
            current_count = count

    if current_char:
        print(f"{current_char}\t{current_count}")

# Mapper for Word Count
def word_mapper():
    for line in sys.stdin:
        line = line.strip()
        words = line.split()
        for word in words:
            print(f"{word}\t1")

# Reducer for Word Count
def word_reducer():
    current_word = None
    current_count = 0

    for line in sys.stdin:
        parts = line.strip().split('\t')
        if len(parts) != 2:
            continue
        word, count = parts
        count = int(count)

        if current_word == word:
            current_count += count
        else:
            if current_word:
                print(f"{current_word}\t{current_count}")
            current_word = word
            current_count = count

    if current_word:
        print(f"{current_word}\t{current_count}")

# Execution based on argument passed
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py [char_mapper|char_reducer|word_mapper|word_reducer]")
        sys.exit(1)

    mode = sys.argv[1]

    if mode == "char_mapper":
        char_mapper()
    elif mode == "char_reducer":
        char_reducer()
    elif mode == "word_mapper":
        word_mapper()
    elif mode == "word_reducer":
        word_reducer()
    else:
        print(f"Unknown mode: {mode}")
        print("Valid options: char_mapper, char_reducer, word_mapper, word_reducer")

        #echo "hello world" | python mapper_reducer.py char_mapper | sort | python mapper_reducer.py char_reducer
        #echo "Shubham Shubham" | python mapper_reducer.py word_mapper | sort | python mapper_reducer.py word_reducer
