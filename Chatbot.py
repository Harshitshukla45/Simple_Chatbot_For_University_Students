from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *

bot = ChatBot('GEHU BOT')
    
my_file=open("D:\mybot.txt","r")
content=my_file.read()

list1=content.split(",")
my_file.close()

trainer = ListTrainer(bot)
trainer.train(list1)

print("Ask to bot")

def ask_bot():
    query=user_input.get()
    answer=bot.get_response(query)
    chatBox.insert(END,"You: "+query)
    chatBox.insert(END,"Bot: "+str(answer))
    user_input.delete(0,END)
    chatBox.yview(END)
   
root=Tk()
root.geometry("650x750")
root.title("GEHU CHATBOT")

img=PhotoImage(file="D:\Hill_Univ_pic.png")
lblPhoto=Label(root,image=img,bg="black",bd=3);
lblPhoto.pack(pady=5)

frame=Frame(root)
sc=Scrollbar(frame)

chatBox=Listbox(frame,width=60,height=10)
chatBox.config(yscrollcommand=sc.set)
sc.config(command=chatBox.yview)
sc.pack(side=RIGHT,fill=BOTH)

chatBox.pack(side=LEFT,fill=BOTH,pady=10)
frame.pack()

user_input=Entry(root,font=("Arial",20))
user_input.pack(fill=BOTH)

btn=Button(root,bg="royalblue",fg="white",text="Ask To Bot",font=("Arial",20),command=ask_bot)
btn.pack(pady=10)
root.mainloop()
