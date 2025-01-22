import customtkinter as ctk
#Backend

    #Fonction de réponse du Bot
def chatbot_response(user_input):
    response= {
        "bonjour" : "Bonjour! Comment puis-je vous aider ?",
        "hello" : "Bonjour! Comment puis-je vous aider ?",
        "comment ça va" : "Je vais bien, j'espère que tu as la patate ?",
        "bonjour" : "Bonjour! Comment puis-je vous aider ?",
        "bonjour" : "Bonjour! Comment puis-je vous aider ?",
        "bonjour" : "Bonjour! Comment puis-je vous aider ?",
        "bonjour" : "Bonjour! Comment puis-je vous aider ?",
        "bonjour" : "Bonjour! Comment puis-je vous aider ?",
        "bonjour" : "Bonjour! Comment puis-je vous aider ?",
        "bonjour" : "Bonjour! Comment puis-je vous aider ?",
        "bonjour" : "Bonjour! Comment puis-je vous aider ?",
        "bonjour" : "Bonjour! Comment puis-je vous aider ?",
        "bonjour" : "Bonjour! Comment puis-je vous aider ?",
        "bonjour" : "Bonjour! Comment puis-je vous aider ?"
    }
    return response.get(user_input.lower(), "Désolé je ne suis pas en mesure de vous répondre")

    #Fonction d'envoie
def send_msg(event=None):
    user_msg=user_input.get()
    if user_msg.strip()!= "":
        chat_history.configure(state="normal")
        chat_history.insert("end", f"Vous: {user_msg}\n", "user")
        bot_response=chatbot_response(user_msg)
        chat_history.insert("end",f"Moi:{bot_response}\n", "bot")
        chat_history.configure(state="disabled")
        chat_history.see("end")
        user_input.delete(0,"end")
    

#Frontend
#configuration de l'IG
app=ctk.CTk()
app.geometry("500x600")
app.title("My CTk Bot ")
#en tête
header=ctk.CTkLabel(app, text="Bienvenue sur le BOT", font=("Arial",18,"bold"))
header.pack(pady=10)

#Affichage de message
#creation du composant
chat_history=ctk.CTkTextbox(app,height=400, state="disabled")
chat_history.tag_config("user",foreground="orange")
chat_history.tag_config("bot",foreground="red")
chat_history.pack(pady=10,padx=10,fill="both",expand=True)
chat_history.configure(font=("Gagalin",14, "bold"))
#champ de l'utilisateur
user_input_frame=ctk.CTkFrame(app)
user_input_frame.pack(pady=10,padx=10,fill="x")
user_input=ctk.CTkEntry(user_input_frame,placeholder_text="Ecris ton message ici pour discuter avec moi", width=350, text_color="black")
user_input.pack(side="right", padx=5)
#ajout du bouton
send_btn=ctk.CTkButton(user_input_frame,text="Envoyer",command=send_msg)
send_btn.pack(side="right")

#Associer la touche entrer à la fonction d'envoie de msg
app.bind(" <Return>",send_msg)

app.mainloop()