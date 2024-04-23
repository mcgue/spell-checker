# Proofreading program made with assistance from ChatGPT

# import needed
from autocorrect import Speller

# function to check spelling and return error if can't suggest word
def proofread_text(text):
    spell = Speller()
    words = text.split()
    corrected_words = []
    for word in words:
        corrected_word = spell(word)
        if corrected_word == word:
            corrected_words.append(f"<ERROR: {word} (Word not found)>")
        else:
            corrected_words.append(corrected_word)
    corrected_text = " ".join(corrected_words)
    return corrected_text

# Main function
def main():
    # Welcome message
    print("Welcome to the Proofreading Program!")

    # Obtain user input
    text = input("Enter the text you want to proofread:\n")

    # Check text
    corrected_text = proofread_text(text)

    # Return correct text or error message
    print("\nCorrected Text:")
    print(corrected_text)

if __name__ == "__main__":
    main()

