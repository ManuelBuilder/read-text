# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename) as file:
        contents = file.read()
        return contents
def count_words(str):
    text = read_file_content("story.txt")
    # [assignment] Add your code here
    texts = str.split()
    counts = dict()

    for text in texts:
        if text in counts:
            counts[text] += 1
        else:
         counts[text] = 1
    return counts

    # return {"as": 10, "would": 20}

print(count_words(read_file_content("story.txt")))