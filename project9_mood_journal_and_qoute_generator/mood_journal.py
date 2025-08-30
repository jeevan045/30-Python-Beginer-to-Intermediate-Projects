import datetime
import random

quotes = [
    "Keep going, you're doing great! 🌟",
    "Every day is a new beginning. 🌸",
    "Believe in yourself and all that you are. 💪",
    "Small steps every day lead to big results. 🚀",
    "Your future is created by what you do today. ✨"
]

def log_mood():
    mood = input("How are you feeling today? (happy/sad/tired/etc.): ")
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    with open("mood_log.txt", "a") as f:
        f.write(f"{date} - {mood}\n")
    print(f"✅ Mood logged: {mood}")
    print("💡 Positive Quote: " + random.choice(quotes))

def show_stats():
    try:
        with open("mood_log.txt", "r") as f:
            lines = f.readlines()
        moods = {}
        for line in lines:
            mood = line.strip().split(" - ")[1]
            moods[mood] = moods.get(mood, 0) + 1
        print("\n--- Mood Stats ---")
        for mood, count in moods.items():
            print(f"{mood}: {count} times")
    except FileNotFoundError:
        print("No moods logged yet.")

def main():
    while True:
        print("\n=== Mood Journal ===")
        print("1. Log Mood")
        print("2. Show Mood Stats")
        print("3. Exit")
        choice = input("Choose option: ")

        if choice == "1":
            log_mood()
        elif choice == "2":
            show_stats()
        elif choice == "3":
            print("👋 Goodbye! Stay positive!")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
