def sentiment_analysis():
    print("\n[Sentiment Analysis - Learning]")
    text = input("Enter a sentence: ").lower()
    positive = ["good", "happy", "great", "love", "excellent"]
    negative = ["bad", "sad", "hate", "terrible", "poor"]
    
    if any(word in text for word in positive):
        print("Sentiment: Positive")
    elif any(word in text for word in negative):
        print("Sentiment: Negative")
    else:
        print("Sentiment: Neutral")

def spam_detection():
    print("\n[Spam Detection - Reasoning]")
    message = input("Enter message content: ").lower()
    spam_words = ["win", "free", "click", "offer", "urgent"]
    if any(word in message for word in spam_words):
        print("Result: This looks like SPAM!")
    else:
        print("Result: This seems safe.")

def movie_bot():
    print("\n[Movie Bot - Perception/NLP]")
    user_input = input("Ask me about movies: ").lower()
    if "recommend" in user_input:
        print("I recommend watching 'Interstellar' or 'The Matrix'.")
    elif "funny" in user_input:
        print("Try watching 'The Hangover' or 'Minions'.")
    elif "bye" in user_input:
        print("Goodbye! Enjoy your movie time!")
    else:
        print("I'm not sure, but I love all kinds of movies!")

def categorize_intelligent_systems():
    print("\nCategories of Intelligent Systems:")
    print("- Reactive Machines: No memory, responds to current input.")
    print("- Limited Memory: Uses past info, like self-driving cars.")
    print("- Theory of Mind: Understands emotions (future AI).")
    print("- Self-aware: AI with consciousness (hypothetical).")

def real_world_applications():
    print("\nReal-World AI Applications:")
    print("- Sentiment analysis on social media")
    print("- Spam filters in email services")
    print("- Virtual assistants like Alexa and Siri")
    print("- Self-driving cars using sensors and AI logic")

def main():
    while True:
        print("\n=== Advanced AI Demo ===")
        print("1. Sentiment Analysis (Learning)")
        print("2. Spam Detection (Reasoning)")
        print("3. Movie Bot (NLP & Perception)")
        print("4. Categorization of AI Systems")
        print("5. Real-World Applications")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            sentiment_analysis()
        elif choice == "2":
            spam_detection()
        elif choice == "3":
            movie_bot()
        elif choice == "4":
            categorize_intelligent_systems()
        elif choice == "5":
            real_world_applications()
        elif choice == "6":
            print("Exiting... Thank you for exploring AI!")
            break
        else:
            print("Invalid input. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
    print("Prathna Trivedi\n240905041035")
