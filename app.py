from flask import Flask, request, render_template
import random

app = Flask(__name__)

# Define some responses
responses = {
  "hi": ["Hello!", "Hi there!", "Greetings!"],
  "how are you?": ["I'm doing well, thanks for asking.", "I'm fine, how about you?", "I'm good!"],
  "what's your name?": ["My name is Chatbot.", "I'm Chatbot to help you with a any doubt regaring EventZio, nice to meet you!"],
  "default": ["I'm sorry, I don't understand what you're saying.", "Can you please rephrase that?", "I'm not sure what you mean."]
}

# Define a function to handle user input
def respond(message):
  if message.lower() in responses:
    return random.choice(responses[message.lower()])
  else:
    return random.choice(responses["default"])

# Define the homepage route
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/newpage')
def new_page():
    return render_template('new_page.html')

# Define the chatbot route
@app.route('/chatbot', methods=['POST'])
def chatbot():
    message = request.form['message']
    response = respond(message)
    return response

if __name__ == '__main__':
    app.run(debug=True)
