def perform_action():
    try:
        sentence = input("Enter a sentence: ")
        words = sentence.split()
        unique_words = set(words)
        print(f"Unique words: {unique_words}")
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
