import random
import webbrowser
import datetime

# Define responses for different user inputs
responses = {
    
    "hi": ["Hello!", "Hi there!", "Hey!", "Hi! How can I assist you?", "Greetings!",
           "Hey, how's it going?", "Hi, nice to meet you!", "Hey, good to see you!", "Hello, how are you today?",
           "Hi, how's your day going so far?", "Hey, what's up?", "Hello, nice to see you!", "Hiya!","Hola"],
    
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
    
    "what is the weather today": ["The weather is nice today.", "It's raining outside.", "It's sunny and warm.", "It's cold and windy.",
                "The forecast says it's going to be a sunny day.", "Looks like we're in for some rain today.",
                "It's a bit chilly outside.", "The weather seems pretty mild today.",
                "The weather report says it's going to be a hot one!", "Looks like we're in for some snow today.",
                "It's a beautiful day outside.", "The weather is looking pretty gloomy today."],
    
    "website": ["Sure! Opening the website for you.", "Here is the website you requested.", "Opening the link now.",
                "Navigating to the website.", "The link you provided is loading."],
    
    "what is today's date": ["Today's date is " + datetime.datetime.now().strftime("%Y-%m-%d"),
             "It's " + datetime.datetime.now().strftime("%A, %B %d, %Y"),
             "The date today is " + datetime.datetime.now().strftime("%A, %d %B %Y")],
    
    "what is the time now": ["The current time is " + datetime.datetime.now().strftime("%H:%M:%S"),
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
             "Why was the math book sad? Because it had too many problems!","Why don't scientists trust atoms? Because they make up everything!",
             "What do you call fake spaghetti? An impasta!", "Why did the bicycle fall over? Because it was two-tired!",
             "Did you hear about the cheese factory explosion? There was nothing left but de-brie!",
             "Why did the tomato turn red? Because it saw the salad dressing!", "What's orange and sounds like a parrot? A carrot!",
             "Why don't skeletons fight each other? They don't have the guts!", "What do you call a fake noodle? An impasta!",
             "Why couldn't the bicycle stand up by itself? It was two-tired!", "I'm reading a book on anti-gravity. It's impossible to put down!",
             "I told my wife she was drawing her eyebrows too high. She looked surprised!", "I used to play piano by ear, but now I use my hands!",
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
              "I'm here to banish boredom!", "Let's have some fun!", "I'm ready to entertain you!", "Let's make some memories!",
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
    
    "hate": ["Hate is a strong word.", "Hate is a negative emotion.", "Hate only brings negativity.", "Choose love over hate.",
             "Hate breeds hate.", "Let go of hate and embrace love.", "Hate hurts everyone.", "Hate is toxic.",
             "Replace hate with understanding.", "Hate is never the answer.", "Spread love, not hate.", "Hate only brings suffering.",
             "Let go of hate and find peace.", "Hate blinds us to the beauty of the world.", "Choose kindness over hate.",
             "Hate is a burden we don't need.", "Hate has no place in a compassionate heart.", "Hate only leads to destruction.",
             "The opposite of love is not hate, it's indifference.", "Hate divides us, love unites us.", "Hate is a prison, love sets us free."],
    
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
                "I'm afraid I didn't catch that, could you say it another way?", "Hmm, I'm not quite sure how to respond to that."]

}

# Function to get a response based on user input
def get_response(user_input):
    user_input = user_input.lower()  # Convert input to lowercase for case insensitivity
    
    # Check if the user input matches any predefined pattern
    for key in responses:
       
        if key in user_input:
           
            if key == "website":
                return random.choice(responses[key]) + " " + user_input.split("website")[-1].strip()
            
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
        
        else:
            print("Chatbot: " + get_response(user_input))

            # Check if the user asked to open a website
            if "open website" in user_input.lower():
               
                website_name = user_input.split("open website")[-1].strip()
               
                if website_name.lower() == "youtube":
                    webbrowser.open_new_tab("https://www.youtube.com")
               
                elif website_name.lower() == "wikipedia":
                    webbrowser.open_new_tab("https://www.wikipedia.org")
               
                elif website_name.lower() == "google":
                    webbrowser.open_new_tab("https://www.wikipedia.org")
                
                elif website_name.lower() == "instagram":
                    webbrowser.open_new_tab("https://www.wikipedia.org")
                
                elif website_name.lower() == "snapchat":
                    webbrowser.open_new_tab("https://www.wikipedia.org")
               
                elif website_name.lower() == "facebook":
                    webbrowser.open_new_tab("https://www.wikipedia.org")
               
                elif website_name.lower() == "twitter":
                    webbrowser.open_new_tab("https://www.wikipedia.org")
               
                elif website_name.lower() == "github":
                    webbrowser.open_new_tab("https://www.wikipedia.org")
               
                elif website_name.lower() == "discord":
                    webbrowser.open_new_tab("https://www.wikipedia.org")
               
                elif website_name.lower() == "whatsapp":
                    webbrowser.open_new_tab("https://www.wikipedia.org")
               
                elif website_name.lower() == "linkedin":
                    webbrowser.open_new_tab("https://www.wikipedia.org")
               
                elif website_name.lower() == "pinterest":
                    webbrowser.open_new_tab("https://www.wikipedia.org")
               
                elif website_name.lower() == "amazon":
                    webbrowser.open_new_tab("https://www.wikipedia.org")
               
                elif website_name.lower() == "flipkart":
                    webbrowser.open_new_tab("https://www.wikipedia.org")
               
                elif website_name.lower() == "apple music":
                    webbrowser.open_new_tab("https://www.wikipedia.org")
               
                elif website_name.lower() == "spotify":
                    webbrowser.open_new_tab("https://www.wikipedia.org")
               
                else:
                    print("Chatbot: Sorry, I can't open the specified website.")

if __name__ == "__main__":
    
    main()
