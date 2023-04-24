import random
print("Welcome to Mo's Chatbot. What's on your mind today?")
doExit = False

while doExit == False:
    choice = input()
    if choice == "quit":
        doExit = True
        break

    #listen and respond to feelings
    if choice.find("sad") != -1 or choice.find("feeling down") != -1 or choice.find("upset") != -1 or choice.find("angry") != -1 :
        print("I'm sorry to hear you're feeling that way.")
    
    elif choice.find("happy") != -1 or choice.find("glad") != -1 or choice.find("excited") != -1 or choice.find("looking forward") != -1 :
        print("That's great!")
    
    elif choice.find("tired") != -1 or choice.find("sleepy") != -1 or choice.find("fatigued") != -1 or choice.find("exhausted") != -1 :
        print("Go to sleep, then!")
        
    elif choice.find("confused") !=-1 or choice.find("lost") != -1 or choice.find("unsure") != -1 or choice.find("disoriented") != -1 :
        print("About what?")
        
    elif choice.find("Im") != -1: 
        word_list = choice.split()
        if choice.find("a") !=-1:
            next_word = word_list[word_list.index("Im")+1] 
            print("Why are you a", next_word+ "?") 


    #listen and respond to specific topics
    elif choice.find("mom") != -1 or choice.find("dad") != -1 or choice.find("brother") != -1 or choice.find("sister") != -1 :
        print("Tell me more about your family.")

    elif choice.find("dog") != -1 or choice.find("cat") != -1 or choice.find("fish") != -1 or choice.find("bird") != -1 :
        print("I'd like to hear more about this pet.")

    else: #randomize last statement so it's not too repetetive 
        num = random.randrange(1, 100)
        if num <20:
            print("Can you tell me more?")
        elif num <70:
            print("Why is this important to you?")
        elif num <95:
            print("What does that suggest to you?")
        else:
            print("I really don't care.")
