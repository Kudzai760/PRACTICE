knowledge_base = {
    "What academic programs do you offer?": "We offer a wide range of undergraduate and  post graduate programs and shourt courses in fields such as Faculty of Business Management and IT, Faculty of theology, arts, and sciences. Please visit our website for a complete list.",
    "How do I apply for admission?": "You can apply for admission through our online application portal on the university website. Make sure to review the admission requirements and deadlines.",
    "What are the admission requirements?": "Admission requirements vary depending on the program you are applying for. Generally, you will need a high school diploma or equivalent, transcripts, letters of recommendation, and standardized test scores (if required).",
    "What is the deadline for applications?": "The application deadline for undergraduate programs is typically January 15th. Graduate program deadlines vary, so please check the specific program's webpage.",
    "Do you offer financial aid?": "Yes, we offer various forms of financial aid, including scholarships, grants, and loans. Visit our financial aid office website for more information.",
    "Where is the student services office located?": "The student services office is located in the Student Union building, room 203.",
    "How do I register for courses?": "You can register for courses through our online registration system during the registration period. Check the academic calendar for specific dates.",
    "What is the academic calendar?": "The academic calendar is available on the university website and contains important dates such as registration deadlines, holidays, and exam periods.",
    "What is the university's mission statement?": "Our mission is to provide a transformative educational experience that prepares students to be leaders and innovators in a global society."
}

def preprocess_text(text):
    """
    Preprocesses the input text by lowercasing and removing punctuation.


    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    return text

def find_best_match(user_input, knowledge_base):


    user_input = preprocess_text(user_input)
    best_match = None
    best_score = 0

    for question, answer in knowledge_base.items():
        question = preprocess_text(question)
        # Simple keyword matching score
        score = sum(1 for word in user_input.split() if word in question.split())

        if score > best_score:
            best_score = score
            best_match = answer

    def chat():
        """
    Runs
    the
    chatbot
    interaction

    print("Welcome to the University Chatbot! How can I help you today?")
    while True:
        user_input = input("> ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        answer = find_best_match(user_input, knowledge_base)

        if answer:
            print(answer)
        else:
            print(
                "I'm sorry, I don't have an answer to that question. Please try rephrasing or contact the university directly.")


knowledge_base = {
    "What academic programs do you offer?": "We offer a wide range of undergraduate and graduate programs in fields such as engineering, business, arts, and sciences. Please visit our website for a complete list.",
    "How do I apply for admission?": "You can apply for admission through our online application portal on the university website. Make sure to review the admission requirements and deadlines.",
    "What are the admission requirements?": "Admission requirements vary depending on the program you are applying for. Generally, you will need at least 5'O'level passes including maths and english and at least 2 A level passes , so please check the specific program's webpage.",
    "Do you offer financial aid?": "Yes, we offer various forms of financial aid, including scholarships, grants, and loans. Visit our financial aid office website for more information.",
    "Where are your offices  located?": "The  office is located on NUmber18443, Cranborne Avenue, Hatfield, Harare.",
    "How do I register for courses?": "You can register for courses through our online registration system during the registration period. Check the academic calendar for specific dates.",
    "What is the academic calendar?": "The academic calendar is available on the university website and contains important dates such as registration deadlines, holidays, and exam periods.",
    "What is the university's mission statement?": "Our mission statement is to provide inclusive, holistic, and adaptive education in a Christian environment, encompassing teaching, research, innovation, industrialization, and service programs, accessible to all regardless of religion, nationality, or any other designation."
}


def preprocess_text(text):
    text = text.lower()
    return text








def find_best_match(user_input, knowledge_base):
    user_input = preprocess_text(user_input)
    best_match = None
    best_score = 0

    for question, answer in knowledge_base.items():
        question = preprocess_text(question)
        score = sum(1 for word in user_input.split() if word in question.split())

        if score > best_score:
            best_score = score
            best_match = answer

    return best_match


def chat():
    print("Welcome to the University Chatbot! How can I help you today?")
    while True:
        user_input = input("> ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        answer = find_best_match(user_input, knowledge_base)

        if answer:
            print(answer)
        else:
            print(
                "I'm sorry, I don't have an answer to that question. Please try rephrasing or contact the university directly.")


# Run the chatbot
if __name__ == "__main__":
    chat()

