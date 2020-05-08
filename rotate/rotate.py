import sys
import pdb
import string


def main():
    rotate = int(sys.argv[1])
    input_file = sys.argv[2]
    char_to_num = {}
    for a, i in enumerate(sorted(string.ascii_lowercase)):
        char_to_num[i] = a
    for a, i in enumerate(sorted(string.ascii_uppercase)):
        char_to_num[i] = a

    num_to_char = {}
    for a, i in enumerate(sorted(string.ascii_uppercase)):
        num_to_char[a] = i
    
    with open(input_file, "r") as f:
        txts = f.readlines()

    for txt in txts:
        new_txt = ""
        for t in txt:
            if t == "\n":
                continue
            num_of_char = char_to_num[t]
            new_num_of_char = (num_of_char + rotate) % 26
            new_char = num_to_char[new_num_of_char]
            new_txt += new_char
        print(new_txt)

if __name__ == "__main__":
    main()
