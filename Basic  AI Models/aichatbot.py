while True:
    user = input("You: ")
    if user.lower() == "hello":
        print("AI: Hi!, How can I help you today? ")
    elif user.lower()== "how are you":
        print("AI: I am Fine")
    elif user.lower()=="bye":
        print("AI: Bye!")
    else : 
        print("AI: I don't understand")
