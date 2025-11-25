def chatbot():
    print('Hello Its me python made by Ankitbhattarai!!!')
    user = input("Yourname: ")
    print("Nice to meet you, My lovely user ", user)

    while True:
        userinput= input("You: ")
        
        if "hello" in userinput.lower():
            print("Chatbot: Hello, How can i help you....")

        elif "how are you" in userinput.lower():
            print("Am i alright how are you mother fucker")

        elif "bye" in userinput.lower():
            print("Bye Bye have a good day")
            break
        else:
            print("What you is that a question you jerk????? ask me hard things")

chatbot()
        




