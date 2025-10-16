
responses = {
    "hola": "¡Hola! ¿Cómo puedo ayudarte?",
    "¿cómo estás?": "Estoy bien, gracias por preguntar.",
    "¿qué puedes hacer?": "Puedo responder a tus preguntas y ayudarte con información.",
    "adiós": "¡Adiós! Que tengas un buen día."
}

def chatbot():
    print("Hola: yo soy un chatbot")
    while True:
        #Le pide al usuario que ingrese un mensaje
        user_input =input("Tu: ").lower()
        if user_input == "exit":
            print("Chatbot: ¡Adiós!")
            break
        elif user_input in responses:
            print("Chatbot: " + responses[user_input])
        else:
            print("Chatbot: No se como responder a eso.")


chatbot()