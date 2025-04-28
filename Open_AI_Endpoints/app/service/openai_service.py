def generate_feedback(payload):
    print("Feedback service called with:", payload)
    return{"message": "Feedback Generated successfully", "input": payload}

def generate_questions(payload):
    print("Questions service called with:", payload)
    return{"message": "Questions Generated successfully", "input": payload}

def generate_response():
    print("Response service called")
    return {"message": "Here is the response"}