import pyttsx3

if __name__ == '__main__':
    print("Welcome to Melody 1.1. Created by Aarushi")
    # Initialize the pyttsx3 engine
    engine = pyttsx3.init()

    while True:
        x = input("Enter what you want me to speak: ")
        if x == "q":
            engine.say("Bye Bye friend!")
            engine.runAndWait()
            break

        # Speak the user input
        engine.say(x)
        engine.runAndWait()
