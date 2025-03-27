class MentalHealthChatbot:
    def __init__(self):
        self.responses = {
            "hello": "Hello! I'm MindSync. How can I support you today?",
            "sad": "I'm sorry to hear you're feeling sad. Remember that it's okay to feel this way. Would you like to talk about what's bothering you?",
            "anxious": "Anxiety can be challenging. Try taking slow, deep breaths. Can you tell me more about what's making you anxious?",
            "angry": "Anger is a natural emotion. It might help to take a short walk or count to ten. What's causing these feelings?",
            "stressed": "Stress affects us all. Maybe try breaking tasks into smaller steps. What's particularly stressful right now?",
            "default": "I'm here to listen. Can you tell me more about how you're feeling?"
        }
    
    def get_response(self, user_input):
        user_input = user_input.lower()
        
        if any(word in user_input for word in ["hi", "hello", "hey"]):
            return self.responses["hello"]
        elif any(word in user_input for word in ["sad", "depressed", "unhappy"]):
            return self.responses["sad"]
        elif any(word in user_input for word in ["anxious", "nervous", "worried"]):
            return self.responses["anxious"]
        elif any(word in user_input for word in ["angry", "mad", "frustrated"]):
            return self.responses["angry"]
        elif any(word in user_input for word in ["stress", "overwhelmed", "pressure"]):
            return self.responses["stressed"]
        else:
            return self.responses["default"]