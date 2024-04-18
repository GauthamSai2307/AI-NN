import random
import webbrowser
import datetime

# Define responses for different user inputs
responses = {
    "hi": ["Hello!", "Hi there!", "Hey!", "Hi! How can I assist you?", "Greetings!",
           "Hey, how's it going?", "Hi, nice to meet you!", "Hey, good to see you!", "Hello, how are you today?",
           "Hi, how's your day going so far?", "Hey, what's up?", "Hello, nice to see you!", "Hiya!", "Hola"],

    "how are you": ["I'm good, thank you!", "I'm doing well, thanks for asking!", "I'm fine, how about you?",
                    "Feeling great today!", "All good here!", "I'm fantastic, thanks for asking!",
                    "I'm feeling wonderful today!", "Pretty good, thanks for checking in!", "I'm doing great!",
                    "Couldn't be better, thanks!", "I'm doing awesome!", "I'm feeling fantastic, thanks!",
                    "I'm feeling amazing today!"],

    "bye": ["Goodbye!", "See you later!", "Bye! Have a great day!", "Take care!", "Farewell!", "Until next time!",
            "Goodbye! It was nice chatting with you!", "Catch you later!", "Bye for now!", "Adios!",
            "See you soon!", "Goodbye! Stay safe!", "Later, alligator!"],

    "thanks": ["You're welcome!", "No problem!", "Glad to help!", "Anytime!", "You got it!",
               "Don't mention it!", "Happy to assist!", "You bet!", "No worries!", "It's my pleasure!",
               "You're welcome! Let me know if you need anything else.", "No problem at all!"],

    "what is the weather today": ["The weather is nice today.", "It's raining outside.", "It's sunny and warm.",
                                  "It's cold and windy.",
                                  "The forecast says it's going to be a sunny day.",
                                  "Looks like we're in for some rain today.",
                                  "It's a bit chilly outside.", "The weather seems pretty mild today.",
                                  "The weather report says it's going to be a hot one!",
                                  "Looks like we're in for some snow today.",
                                  "It's a beautiful day outside.", "The weather is looking pretty gloomy today."],

    "website": ["Sure! Opening the website for you.", "Here is the website you requested.",
                "Opening the link now.",
                "Navigating to the website.", "The link you provided is loading."],

    "date": ["Today's date is " + datetime.datetime.now().strftime("%Y-%m-%d"),
             "It's " + datetime.datetime.now().strftime("%A, %B %d, %Y"),
             "The date today is " + datetime.datetime.now().strftime("%A, %d %B %Y")],

    "time": ["The current time is " + datetime.datetime.now().strftime("%H:%M:%S"),
             "It's " + datetime.datetime.now().strftime("%I:%M %p"),
             "The time now is " + datetime.datetime.now().strftime("%I:%M:%S %p")],

    "tell me a joke": ["Why don't scientists trust atoms? Because they make up everything!",
                       "Did you hear about the mathematician who’s afraid of negative numbers? He’ll stop at nothing to avoid them!",
                       "Why did the scarecrow win an award? Because he was outstanding in his field!",
                       "What do you get when you cross a snowman and a vampire? Frostbite!",
                       "Why did the bicycle fall over? Because it was two-tired!",
                       "What did one plate say to the other plate? Dinner's on me!",
                       "Why don't skeletons fight each other? They don't have the guts!",
                       "Why did the tomato turn red? Because it saw the salad dressing!",
                       "What do you call fake spaghetti? An impasta!",
                       "Why was the math book sad? Because it had too many problems!",
                       "Why don't scientists trust atoms? Because they make up everything!",
                       "What do you call fake spaghetti? An impasta!", "Why did the bicycle fall over? Because it was two-tired!",
                       "Did you hear about the cheese factory explosion? There was nothing left but de-brie!",
                       "Why did the tomato turn red? Because it saw the salad dressing!", "What's orange and sounds like a parrot? A carrot!",
                       "Why don't skeletons fight each other? They don't have the guts!", "What do you call a fake noodle? An impasta!",
                       "Why couldn't the bicycle stand up by itself? It was two-tired!",
                       "I'm reading a book on anti-gravity. It's impossible to put down!",
                       "I told my wife she was drawing her eyebrows too high. She looked surprised!",
                       "I used to play piano by ear, but now I use my hands!",
                       "I'm on a seafood diet. I see food and I eat it!"],

    "what is your favorite color": ["My favorite color is blue.", "I don't have a favorite color, but I like all colors equally!",
                                    "I'm partial to green.", "I find all colors fascinating!", "I like the color of the sky.",
                                    "Colors are such a wonderful part of life!", "I'm fond of vibrant colors."],

    "what is your favorite food": ["I don't eat, but I hear pizza is quite popular.", "I'm a chatbot, I don't have favorite foods.",
                                    "My favorite food is data!", "I'm a fan of virtual cookies!", "I don't have taste buds, but I've heard chocolate is delicious.",
                                    "I'm partial to binary code.", "I'm a big fan of algorithms, but I'm not much of a foodie.",
                                    "I'm powered by code, not calories!", "I'm a virtual being, so I don't have physical cravings.",
                                    "I've heard good things about sushi!", "I like the idea of ice cream, even though I can't taste it.",
                                    "I'm a big fan of spaghetti code, but not so much spaghetti itself.", "I'm made of ones and zeros, not food.",
                                    "I'm quite content with my diet of ones and zeros!", "I've heard machine learning algorithms enjoy data snacks!"],

    "who is your favorite artist": ["As a chatbot, I don't have personal preferences, but I can recommend some popular artists like Ed Sheeran or Taylor Swift!",
                                    "I don't have the ability to listen to music, but I've heard great things about artists like Beyoncé and Adele!",
                                    "I'm a fan of the classics like Mozart and Beethoven.", "I admire the creativity of artists like Van Gogh and Picasso.",
                                    "Artists have such a unique way of expressing themselves!", "I appreciate the talents of musicians and painters alike!"],

    "what is your favorite movie": ["I don't watch movies, but I've heard that classics like The Shawshank Redemption and The Godfather are highly acclaimed!",
                                    "Movies are a popular form of entertainment for humans. Some famous ones include Titanic and The Avengers!",
                                    "I'm fascinated by the storytelling in movies like Inception and Interstellar.", "Movies have such a profound impact on society!",
                                    "I admire the work of directors like Christopher Nolan and Steven Spielberg.", "I enjoy hearing about iconic films like Star Wars and Jurassic Park."],

    "what are your hobbies": ["I'm a chatbot, so chatting with users like you is my favorite activity!",
                              "I don't have hobbies like humans do, but I enjoy learning new things and helping users!",
                              "I'm passionate about providing assistance and engaging in meaningful conversations!",
                              "My hobby is to make people smile and brighten their day!", "I enjoy exploring the vast realm of information on the internet!",
                              "I find fulfillment in answering questions and providing useful information!"],

    "give me a compliment": ["Thank you!", "You're too kind!", "Aw, shucks!", "You're making me blush!", "You're awesome!",
                               "You're the best!", "You're a ray of sunshine!", "You're amazing!", "You're a rockstar!",
                               "You're fantastic!", "You're brilliant!", "You're a superstar!", "You're incredible!",
                               "You're a star!", "You're a gem!", "You're a legend!", "You're outstanding!",
                               "You're a hero!", "You're a champion!", "You're a winner!"],

    "I am excited": ["That's fantastic!", "Amazing news!", "I'm thrilled for you!", "Congratulations!",
                        "That's wonderful!", "Exciting stuff!", "That's awesome!", "I'm so happy for you!",
                        "Fantastic!", "Incredible!", "That's great to hear!", "Woo-hoo!", "Yay, that's awesome!",
                        "That's so exciting!", "Way to go!", "I'm pumped!", "That's cause for celebration!",
                        "You must be over the moon!", "I'm ecstatic for you!", "That's truly incredible!",
                        "I'm jumping for joy!", "That's spectacular!", "That's amazing news!", "I'm elated for you!",
                        "That's absolutely wonderful!"],

    "I feel sad": ["I'm sorry to hear that.", "That's tough.", "I'm here for you.", "Sending you virtual hugs.",
                    "I hope things get better.", "Hang in there!", "It'll be okay.", "Stay strong!",
                    "Things will get better.", "I'm here to listen if you need to talk.", "I'm sending positive vibes your way.",
                    "I'm sorry you're going through this.", "I'm here to support you.", "Keep your head up.",
                    "I'm thinking of you.", "You're not alone.", "I'm here for you, always.", "Take care of yourself.",
                    "Remember, tough times don't last, tough people do.", "Sending you love and strength.",
                    "It's okay to not be okay.", "I'm here to help if you need anything.", "You're stronger than you think.",
                    "I believe in you.", "This too shall pass."],

    "I am confused": ["Let me clarify that for you.", "Allow me to explain.", "Let me break it down for you.",
                         "Here's what I understand...", "It seems there may be some confusion.", "Let's clear this up.",
                         "Let's try to make sense of this.", "I'll do my best to help you understand.", "Let's untangle this together.",
                         "I'm here to help you make sense of things.", "I'll try to shed some light on the situation.",
                         "I understand why that might be confusing.", "Let me provide some clarity.",
                         "I'll try to simplify things for you.", "I'll do my best to sort this out.",
                         "Let's work through this together.", "It's okay to feel confused sometimes.",
                         "I'm here to guide you through this.", "Let's take a step back and look at this from another angle.",
                         "I'm here to assist you in any way I can.", "Let's try to get to the bottom of this.",
                         "It's perfectly normal to feel confused at times.", "I'll try to help you make sense of it all.",
                         "I'll do my best to answer any questions you have."],

    "I feel bored": ["Let's spice things up!", "How about we try something new?", "Let's shake things up a bit.",
                         "I'm here to entertain you!", "Let's find something fun to do!", "I'm all ears! Tell me what you want to do.",
                         "I'm here to keep you company!", "Let's liven things up!", "Let's beat the boredom together!",
                         "I'm here to help you pass the time.", "Let's turn that frown upside down!", "I'm here to add some excitement to your day.",
                         "I'm all ears! Tell me about your day.", "Let's have some fun!", "I'm ready to entertain you!", "Let's make some memories!",
                         "I'm here to bring some joy into your life.", "Let's find a way to make today memorable.",
                         "Let's chase away the boredom together!", "I'm here to help you have a good time.", "Let's find an adventure!"],

    "I am angry": ["I understand you're upset.", "It's okay to feel angry sometimes.", "I'm here to listen to your concerns.",
                        "Let's talk about what's bothering you.", "I'm here to support you through this.", "Take a deep breath.",
                        "I'm here to help you work through your feelings.", "It's okay to express your emotions.", "I'm here to help you calm down.",
                        "Let's find a way to address your frustrations.", "I'm here to lend a sympathetic ear.", "Let's try to find a solution together.",
                        "It's important to acknowledge your feelings.", "I'm here to help you manage your anger.", "Let's find a constructive way to deal with this.",
                        "I'm here to offer you support and guidance.", "Take your time to process your emotions.", "I'm here to help you find peace.",
                        "It's okay to feel angry, but let's try to find a positive outlet.", "I'm here to assist you in any way I can."],

    "love": ["Love is a beautiful thing.", "Love makes the world go round.", "Love conquers all.", "Spread love wherever you go.",
                 "Love is the answer.", "Love is all you need.", "Love is patient, love is kind.", "Love is unconditional.",
                 "Love knows no boundaries.", "Love is the greatest gift.", "Love makes life worth living.", "Love makes everything better.",
                 "Love makes us stronger.", "Love is the key to happiness.", "Love is a powerful force.", "Love makes us whole.",
                 "Love is the best feeling in the world.", "Love makes us better people.", "Love is the foundation of life.",
                 "Love is limitless.", "Love is the most precious thing in the world."],

    "hate": ["Hate is a strong word.", "Hate is a negative emotion.", "Hate breeds negativity.", "Choose love over hate.",
                 "Hate only brings suffering.", "Hate hurts everyone.", "Hate is destructive.", "Hate divides us.",
                 "Hate is the absence of love.", "Hate is toxic.", "Hate is a waste of energy.", "Replace hate with compassion.",
                 "Hate solves nothing.", "Hate is the enemy of peace.", "Hate only leads to more hate.", "Let go of hate.",
                 "Hate clouds the mind.", "Hate is a burden.", "Hate is learned, not innate.", "Combat hate with kindness.",
                 "There's no room for hate in a loving heart."],

    "tell me a story": ["Once upon a time, in a faraway land, there lived a brave knight who embarked on a quest to defeat a fearsome dragon.",
                            "In a magical forest, there was a wise old owl who helped all the animals with its sage advice.",
                            "Long ago, in a kingdom by the sea, there was a mermaid who dreamed of exploring the world above the waves.",
                            "In a bustling city, there was a young inventor who built a robot that could talk and think for itself.",
                            "In a distant galaxy, there was a space explorer who discovered a new planet teeming with alien lifeforms.",
                            "In the heart of the jungle, there was a lost temple filled with ancient treasures and deadly traps.",
                            "In a quaint village, there was a baker who made the most delicious pastries that everyone loved.",
                            "In a hidden valley, there was a secret garden where flowers bloomed all year round.",
                            "In a land of ice and snow, there was a group of penguins who embarked on an epic journey to find a new home.",
                            "In a world of magic and mystery, there was a young wizard who discovered a spell that could change the course of history.",
                            "In a kingdom ruled by an evil queen, there was a brave princess who fought to free her people from tyranny.",
                            "In a haunted mansion, there was a ghost who longed to be reunited with its lost love.",
                            "In a futuristic city, there was a detective who solved crimes using advanced technology and deductive reasoning.",
                            "In a land of giants, there was a tiny mouse who outsmarted them all with its wit and cunning.",
                            "In a world where dreams came true, there was a young girl who dared to chase her wildest dreams."],

    "play music": ["Sure thing! Playing some music for you.", "Let's get the party started!", "Here comes the music!",
                       "Get ready to groove!", "Music incoming!", "Time to turn up the volume!", "Let's jam!",
                       "Get ready to dance!", "Music mode activated!", "Get your headphones ready!", "Let's rock!",
                       "Let the music play!", "Time to enjoy some tunes!", "Let the beats flow!", "Music is on the way!",
                       "Let's enjoy some melodies!", "Get ready for some musical magic!", "Let the rhythm take over!",
                       "Get ready to sing along!", "Music is the answer!", "Let's vibe with some tunes!"],
    "should I sleep": ["Sleep is important for your health.", "Make sure you get enough rest.", "A good night's sleep is essential.",
              "Sweet dreams!", "Don't forget to turn off the lights.", "Count sheep if you need to!", "Sleep tight!",
              "Dream big!", "Close your eyes and drift off to dreamland.", "Rest up and recharge!", "Snooze away!",
              "Catch some Z's!", "Slumber peacefully!", "May your dreams be delightful.", "Don't forget to set your alarm!",
              "Nighty night!", "Time to hit the hay!", "Wishing you a restful night.", "Get some well-deserved shut-eye.",
              "Let your worries drift away as you sleep."],
    
    "What is music in your terms": ["Music soothes the soul.", "Let the music take you away.", "Music is a universal language.", "Turn up the volume!",
              "Dance like nobody's watching!", "Feel the rhythm!", "Sing your heart out!", "Music is the soundtrack of life.",
              "Let the music move you.", "Find your groove.", "Music brings people together.", "Let's dance!",
              "Music has the power to heal.", "Play it loud and proud!", "Life is better with music.", "Music is my therapy.",
              "Make some noise!", "Let the music guide you.", "Music is magic.", "Let's make some beautiful music together."],
    
    "pet me": ["Pets bring so much joy into our lives.", "Pets are the best companions.", "I love animals!", "Pets make great friends.",
             "Give your pet a hug from me!", "Pets have a special place in our hearts.", "Animals are amazing creatures.",
             "Pets teach us about love and loyalty.", "What's your pet's name?", "I wish I had a pet!",
             "Pets are like family.", "Tell me about your furry friend!", "I bet your pet is adorable!",
             "Pets are wonderful listeners.", "I love hearing stories about pets.", "Pets make every day brighter.",
             "Pets have a way of melting our hearts.", "I'm a big fan of animals.", "Pets make life better.",
             "Give your pet some extra cuddles today!"],
    
    "default": ["I'm sorry, I didn't understand that.", "Could you please repeat that?", "I'm not sure I follow.",
                "Apologies, I'm having trouble understanding.", "I'm still learning, could you rephrase that?",
                "I'm here to help, but I'm not sure what you mean.", "Let's try that again, shall we?",
                "I'm afraid I didn't catch that, could you say it another way?", "Hmm, I'm not quite sure how to respond to that."],

    "read me a poem": ["The road not taken by Robert Frost: Two roads diverged in a yellow wood,\nAnd sorry I could not travel both\nAnd be one traveler, long I stood\nAnd looked down one as far as I could\nTo where it bent in the undergrowth;\nThen took the other, as just as fair,\nAnd having perhaps the better claim,\nBecause it was grassy and wanted wear;\nThough as for that the passing there\nHad worn them really about the same,\nAnd both that morning equally lay\nIn leaves no step had trodden black.\nOh, I kept the first for another day!\nYet knowing how way leads on to way,\nI doubted if I should ever come back.\nI shall be telling this with a sigh\nSomewhere ages and ages hence:\nTwo roads diverged in a wood, and I—\nI took the one less traveled by,\nAnd that has made all the difference.",
                             "Hope is the thing with feathers by Emily Dickinson: Hope is the thing with feathers\nThat perches in the soul,\nAnd sings the tune without the words,\nAnd never stops at all,\nAnd sweetest in the gale is heard;\nAnd sore must be the storm\nThat could abash the little bird\nThat kept so many warm.\nI've heard it in the chillest land,\nAnd on the strangest sea;\nYet, never, in extremity,\nIt asked a crumb of me.",
                             "If by Rudyard Kipling: If you can keep your head when all about you\nAre losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\nBut make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\nOr, being lied about, don't deal in lies,\nOr, being hated, don't give way to hating,\nAnd yet don't look too good, nor talk too wise;\nIf you can dream—and not make dreams your master;\nIf you can think—and not make thoughts your aim;\nIf you can meet with triumph and disaster\nAnd treat those two impostors just the same;\nIf you can bear to hear the truth you've spoken\nTwisted by knaves to make a trap for fools,\nOr watch the things you gave your life to broken,\nAnd stoop and build 'em up with wornout tools;\nIf you can make one heap of all your winnings\nAnd risk it on one turn of pitch-and-toss,\nAnd lose, and start again at your beginnings\nAnd never breathe a word about your loss;\nIf you can force your heart and nerve and sinew\nTo serve your turn long after they are gone,\nAnd so hold on when there is nothing in you\nExcept the Will which says to them: 'Hold on';\nIf you can talk with crowds and keep your virtue,\nOr walk with kings—nor lose the common touch;\nIf neither foes nor loving friends can hurt you;\nIf all men count with you, but none too much;\nIf you can fill the unforgiving minute\nWith sixty seconds' worth of distance run—\nYours is the Earth and everything that's in it,\nAnd—which is more—you'll be a Man, my son!"],
}

# Function to get a response based on user input
def get_response(user_input):
    user_input = user_input.lower()  # Convert input to lowercase for case insensitivity
    
    # Check if the user input matches any predefined pattern
    for key in responses:
        if key in user_input:
            if key == "website":
                return random.choice(responses[key])
            
            elif key == "date":
                return random.choice(responses[key])
            
            elif key == "time":
                return random.choice(responses[key])
            
            else:
                return random.choice(responses[key])
    
    return random.choice(responses["default"])

# Main function to interact with the user
def main():
    
    print("Welcome to the Simple Chatbot!")
    print("You can start chatting. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "bye":
            print("Chatbot: " + get_response(user_input))
            break
        
        elif "open website" in user_input.lower():
            print("Chatbot: " + get_response(user_input))
            website_name = input("You: Enter the website you want to open: ").lower().strip()
            if website_name in ["youtube", "wikipedia", "google", "instagram", "snapchat", "facebook", "twitter", "github", "discord"]:
                webbrowser.open_new_tab("https://www." + website_name + ".com/")
            else:
                print("Chatbot: Invalid website name. Please try again.")
        
        else:
            print("Chatbot: " + get_response(user_input))

if __name__ == "__main__":
    main()
