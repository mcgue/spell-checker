# Proofreading program made with assistance from ChatGPT

from autocorrect import Speller

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

def main():
    print("Welcome to the Proofreading Program!")
    text = input("Enter the text you want to proofread:\n")
    corrected_text = proofread_text(text)
    print("\nCorrected Text:")
    print(corrected_text)

if __name__ == "__main__":
    main()

