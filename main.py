responses = {
    "hola": "¡Hola! ¿Cómo puedo ayudarte?",
    "¿cómo estás?": "Estoy bien, gracias por preguntar.",
    "¿qué puedes hacer?": "Puedo responder a tus preguntas y ayudarte con información.",
    "adiós": "¡Adiós! Que tengas un buen día."
}


def get_response(user_input):
    user_input = user_input.lower()
    if "hola" in user_input:
        return "¡Hola! ¿Cómo puedo ayudarte?"
    elif "cómo estás" in user_input:
        return "Estoy bien, gracias por preguntar."
    elif "qué puedes hacer" in user_input:
        return "Puedo responder a tus preguntas y ayudarte con información."
    elif "adiós" in user_input:
        return "¡Adiós! Que tengas un buen día."
    else:
        return "No se como responder a eso."


def chatbot():
    print("Hola: yo soy un chatbot")
    while True:
        # Le pide al usuario que ingrese un mensaje
        user_input = input("Tu: ").lower()
        if "exit" in user_input:
            print("Chatbot: ¡Adiós!")
            break
        responses = get_response(user_input)
        print(f"chatbot: {responses}")


if __name__ == "__main__":
    chatbot()
