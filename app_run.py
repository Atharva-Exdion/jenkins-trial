import time

def main():
    print("Hello, World! Application is running. Press Ctrl+C to stop.")
    try:
        while True:
            time.sleep(1)  # Keeps the app running
    except KeyboardInterrupt:
        print("\nApplication stopped.")

if __name__ == "__main__":
    main()
