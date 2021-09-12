#chatbot

bot_dict = {
    "how are you" : "I'm fine :) How are you too?",
    "weather" : "Its raining today :( Please try to stay indoor",
    "what name" : "My name is UswatBot!,may i know your name too?",
    "go to school" : "Yes! i do go to school",
    "at home" : "Nope :( I'm not at home"
    }
print("Welcome to my Chatbot!\nPress [q] to quit")

print("bot: Hello Friend!")

while True:
    u_input = input("You: ").lower()

    if u_input == 'q':
        break
    bot_reply = [ bot_dict[i] for i in bot_dict if i in u_input ]
    if len (bot_reply) > 0:
        print(f"Bot: {bot_reply[0]}")
        continue

        print("Bot: sorry :( I have no reply for this")
        
print("Thank you for chatting with me :)")
