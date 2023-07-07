from ng_model import question_model

while True:
        qn_model = question_model()
        question = qn_model.generate_questions()
        answer = input("Type 'x' to quit. What is " + question + " ? ")
        if answer.lower() == 'x':
            break
        response = qn_model.verify_answer(question, answer)
        print(response)
