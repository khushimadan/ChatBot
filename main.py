#Task-4 Chat Bot

import json
import re
import random_responses #random responses file that has already been created

def load_json(file):
    with open(file) as bot_responses:
        return json.load(bot_responses)

responses_data = load_json("bot.json") #file containing appropriate responses

def generate_response(input_string):
    split_message = re.split(r'\s+|[,;?!.-]\s*',input_string.lower()) #for splitting the input string and converting it all in lower case
    score_list = [] #containing scores to find the accurate response

    for response in responses_data:
        #setting up scores for accurate response

        response_score = 0
        required_score = 0

        required_words = response["required_words"] #accessing the recquired words from json file

        if required_words: #compulsory to have all the required words
            for word in split_message:
                if word in required_words:
                    required_score += 1
        
        if required_score == len(required_words): #if all the required words are present in the input
            for word in split_message:
                if word in response["user_input"]:
                    response_score += 1
        
        score_list.append(response_score)

    best_response = max(score_list) #best response would be the one having maximum response score giving an appropriate answer

    best_response_index = score_list.index(best_response) #getting its index

    if input_string == "": #empty string
        return "Please type something so we can chat :)"
    
    if best_response != 0:
        return responses_data[best_response_index]["bot_response"]
    
    # if the response_score is 0
    return random_responses.random_string() #generating a random response   

#chat experience

while True:
    user_input = input("You: ")
    print("Bot: " + generate_response(user_input))
    if generate_response(user_input) == "See you later!": #exiting the loop once user writes bye/goodbye
        break
