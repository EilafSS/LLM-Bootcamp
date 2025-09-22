
def analyze_txt(text):  #take the text and then makes analyze to count the charachters

  
    count_chars = len(text)   # Count characters with spaces -> return int
    
 
    words = text.split()    # this function to Count words, so we need to spliting between each word -> return int
    count_words = len(words)
    
    
    if count_words > 20:       #doing the condition ->  If the text has more than 20 words
        print("Long Text")
    

    return count_chars, count_words      # Return results


# Example usage
text = "Hello I want to say that, I started my LLM bootcamp"
chars, words = analyze_txt(text)

print("Characters:", chars)
print("Words:", words)
