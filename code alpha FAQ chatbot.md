
#### 🔹 Task 2: Chatbot for FAQs README
```markdown
# CodeAlpha FAQ Chatbot

This project is a chatbot that answers Frequently Asked Questions using regular expressions and basic NLP.

## Features
- Basic pattern matching
- Simple and lightweight

## Technologies Used
- Python
- Regex
- NLTK (optional)

## Sample Code
```python
import re

def chatbot_response(query):
    faqs = {
        "what is your name": "I am a FAQ Bot.",
        "how can I help you": "You can ask me any FAQ.",
    }
    for key in faqs:
        if re.search(key, query.lower()):
            return faqs[key]
    return "Sorry, I don't understand."

print(chatbot_response("What is your name?"))
