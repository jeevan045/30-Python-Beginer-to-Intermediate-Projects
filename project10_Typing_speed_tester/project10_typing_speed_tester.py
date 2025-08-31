import time
import random

WORDS = [
    "python", "keyboard", "function", "variable", "developer",
    "algorithm", "programming", "challenge", "syntax", "debug",
    "terminal", "performance", "accuracy", "project", "speed"
]


def typing_test(rounds=5):
    print("⌨️ Typing Speed Test ⌨️")
    print(f"You will be given {rounds} words to type.")
    input("Press Enter when ready...")

    correct = 0
    total_chars = 0
    correct_chars = 0

    start_time = time.time()

    for i in range(rounds):
        word = random.choice(WORDS)
        print(f"\nWord {i + 1}: {word}")
        typed = input("Type here: ").strip()

        total_chars += len(word)
        correct_chars += sum(1 for a, b in zip(word, typed) if a == b)

        if typed == word:
            print("✅ Correct!")
            correct += 1
        else:
            print(f"❌ Wrong! You typed: {typed}")

    end_time = time.time()
    elapsed = end_time - start_time
    wpm = (correct_chars / 5) / (elapsed / 60)
    accuracy = (correct_chars / total_chars) * 100

    print("\n📊 Results 📊")
    print(f"Time taken: {elapsed:.2f} seconds")
    print(f"Correct words: {correct}/{rounds}")
    print(f"Accuracy: {accuracy:.2f}%")
    print(f"Speed: {wpm:.2f} WPM")


if __name__ == "__main__":
    typing_test(rounds=5)
