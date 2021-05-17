# Olga Borysovska olgaborysovska@gmail.com

import sys

def read_lines_from_stdin(lines):
    """Read stdin the lines excluding the empty lines"""
    return [line for line in lines if line.strip()]

def write_words(lines):
    """Write the words from strip lines into list"""
    return [word.strip() for word in lines if word.strip().isalpha()]

def check_word(word, memo):
    """Takes in an single word and returns Bool if it can/can't be composed from other words"""
    if word in memo: 
        return True

    for i in range(1, len(word)):
            prefix = word[:i]
            suffix = word[i:]
                
            if prefix in memo and check_word(suffix, memo): # Checks if prefix is already in visited words
                return True                                 # and recursively runs with suffix input 
        
    return False 

def find_compound_words(words):
    """Takes input and returns list of words that are composed of other words"""
    if not words: 
        print("No data was provided")
        return
    
    output = set()
    memo= set()
    words.sort(key=len)

    for word in words:
        if check_word(word, memo): 
            output.add(word) 
        memo.add(word)

    return sorted(output)


def main():
    """Utilizes  write_words and read_lines_from_stdin to write words from stdin """
    words = write_words(read_lines_from_stdin(sys.stdin.readlines()))

    if not find_compound_words(words):
        sys.stdout.write('No words can be composed of given input' + '\n')   
    else:
        for word in find_compound_words(words):
            sys.stdout.write(word + '\n')    #writes words back to stdout  


if __name__ == "__main__":
    main()