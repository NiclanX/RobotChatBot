import json
from difflib import get_close_matches

def load_kb(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data

def save_kb(file_path: str, data: dict):
    with open(file_path, 'w') as file:
       json.dump(data, file, indent=2)

 
def find_best_match(user_question: str, questions: list[str]) -> str | None:
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None

def get_answer(question: str,  kb: dict) -> str | None:
    for q in kb["questions"]:
        if q["question"] == question:
            return q["answer"]
        
def learn(question, answer):
    kb: dict = load_kb('chatbot/kb.json')

    kb['questions'].append({"question": question, "answer": answer})
    save_kb('chatbot/kb.json', kb)
    return "Thanks for Teaching me! What else can I help your with today?"
          
     
def chat_bot(message):

    kb: dict = load_kb('chatbot/kb.json')
    
    if message.lower() != 'quit':
        question = message
            
        best_match: str | None = find_best_match(question, [q["question"] for q in kb["questions"]])

        if best_match:
            answer: str = get_answer(best_match, kb)
            return answer
        else:
            return "I Don't know how to respond &#128531;... Perhaps I could help you with something else? &#128526; or.. You could teach me. Type the answer to your message or type 'skip' to skip"
            
if __name__ == '__main__':
    chat_bot()
