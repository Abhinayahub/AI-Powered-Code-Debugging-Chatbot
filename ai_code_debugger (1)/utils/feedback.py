import os
def save_feedback(feedback_text):
    # Ensure the 'data' folder exists
    os.makedirs("data", exist_ok=True)
    
    # Save the feedback to feedback_log.txt inside the data folder
    with open("data/feedback_log.txt", "a", encoding="utf-8") as f:
        f.write(feedback_text.strip() + "\n")
