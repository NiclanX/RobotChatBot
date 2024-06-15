from flask import Flask, render_template
from flask_socketio import SocketIO, send
from chatbot import nick

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

learningTime: bool = False
lastQuestion: str = ""
easterEgg: str = "Hey!"

@app.route('/')
def index():
    return render_template('index.html')

answer = "None"

@socketio.on('message')
def handleMessage(msg):

    global learningTime
    global lastQuestion

    if learningTime == False:
        print('Message: ' + msg)
        lastQuestion = msg
        send(msg, broadcast=True)
        answer = nick.chat_bot(msg)
        if answer == "I Don't know how to respond &#128531;... Perhaps I could help you with something else? &#128526; or.. You could teach me. Type the answer to your message or type 'skip' to skip":
            print("Learnin Time!")
            socketio.emit('answer', answer)
            learningTime = True
        else:
            socketio.emit('answer', answer)

    elif learningTime == True:
            if msg.lower() != 'skip':
                send(msg, broadcast=True)
                answer = nick.learn(lastQuestion, msg)
                socketio.emit('answer', answer)
                learningTime = False

            else:
                learningTime = False
                answer = "Ok maybe next time!" 
                socketio.emit('answer', answer)
                


@socketio.on('answer')
def handleAnswer(ans):
    send(ans, broadcast = True)
    print('answer handled?')
   

@socketio.on('learn')
def handleLearning(prompt):
    send(prompt, broadcast = True)
    print('Okay: 200')

if __name__ == '__main__':
    socketio.run(app, debug=True)
