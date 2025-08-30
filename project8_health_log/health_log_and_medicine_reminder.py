import datetime
import time
import os

medicines = {}

def add_medicine():
    name = input("Enter medicine name: ")
    times = input("Enter times (HH:MM, comma separated): ").split(",")
    times = [t.strip() for t in times]
    medicines[name] = times
    print(f"✅ Added {name} at {', '.join(times)}")

def start_reminder():
    print("🔔 Reminder system started (Ctrl+C to stop)...")
    try:
        while True:
            now = datetime.datetime.now().strftime("%H:%M")
            for med, times in medicines.items():
                if now in times:
                    print(f"\n⏰ Take your medicine: {med} ({now})")
                    # Beep sound (Windows only)
                    if os.name == "nt":
                        import winsound
                        winsound.Beep(1000, 700)
            time.sleep(60)
    except KeyboardInterrupt:
        print("\n❌ Reminder system stopped.")

# -------- MAIN --------
def main():
    print("=== Medicine Reminder ===")
    while True:
        print("\n1. Add medicine schedule")
        print("2. Start reminders")
        print("3. Exit")
        choice = input("Choose option: ")

        if choice == "1":
            add_medicine()
        elif choice == "2":
            if medicines:
                start_reminder()
            else:
                print("⚠️ Please add at least one medicine first.")
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
