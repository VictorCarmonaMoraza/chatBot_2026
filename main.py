

def chatbot():
    print("Hola: yo soy un chatbot")
    while True:
        #Le pide al usuario que ingrese un mensaje
        user_input =input("Tu: ").lower()
        if user_input == "exit":
            print("Chatbot: ¡Adiós!")
            break
        else:
            print("Chatbot: No se como responder a eso.")


chatbot()