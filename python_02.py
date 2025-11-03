while True:
   
    user_input = input("You: ").lower()
    
    if user_input == "hello":
        print("Bot: Hey!")
    elif user_input == "how are you":
        print("Bot: I'm fine, thank you!")
    elif user_input == "bye":
        print("Bot: Goodbye!")
        break  
    else:
        print("Bot: Sorry, I don't understand that.")