import tkinter
from tkinter import *

root = Tk()
root.title('ToDo List')
root.geometry("430x650+400+100")
root.resizable(False, False) #resizability
root.configure(bg='#326273') #background

task_list = []
def addTask():
    task = task_entry.get()
    task_entry.delete(0, END)

    if task:
        with open('takslist.txt', 'a') as taskfile:
            taskfile.write(task + '\n')
            # taskfile.write(f'\n'{task})
            task_list.append(task)
            list.insert(END, task)


def deleteTask():
    global task_list
    task = str(list.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open('tasklist.txt', 'w') as taskfile:
            for task in task_list:
                taskfile.write(task + '\n')


def openTaskFile():

    try:
        global task_list
        with open("tasklist.txt", "r") as taskfile:
            tasks = taskfile.readlines()
            
        for task in tasks:
            if task != '\n':
                task_list.append(task)
                list.insert(END, task)

    except:
        file = open('tasklist.txt', 'w')
        file.close()

#window icon
icon_image = PhotoImage(file='icon.png')
root.iconphoto(False, icon_image)

#top bar
# TopImage = PhotoImage(file="topbar.png")
# Label(root, image = TopImage).pack()

dockImage = PhotoImage(file="dock.png")
Label(root, image=dockImage, bg='#326273').place(x=30, y=25)

noteImage = PhotoImage(file='task.png')
Label(root, image=noteImage, bg='#326273').place(x=340, y=25)

#heading
heading = Label(root, text="Tasks", font="Exo 14 bold", bg='#326273', fg="#fff")
heading.place(x=180, y=25)

#main frame
mainFrame = Frame(root, width=400, height=50 , bg='#eeeee4')
mainFrame.place(x=30, y=180)

task = StringVar()
task_entry = Entry(root, width=20, font='Raleway 18', bd=0)
task_entry.place(x=10, y=120)

button = Button(root, text='ADD', font='Raleway 13', width=6, bg='white', fg='black', bd=0, command=addTask)
button.place(x=350, y=120)

#listbox
boxframe = Frame(root, bd=1, width=700, height=280, bg='#eeeee4')
boxframe.pack(pady=(160, 0))

list = Listbox(boxframe, font=('Raleway', 12), width=40, height=16, bg='#32405b', fg='white', cursor='hand2', selectbackground='#5a95ff')
list.pack(side=LEFT, fill=BOTH, padx=2)
scrollbar = Scrollbar(boxframe)
scrollbar.pack(side=RIGHT, fill=BOTH)

list.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=list.yview)

openTaskFile()

#delete button
delete_icon = PhotoImage(file='delete.png')
Button(root, image=delete_icon, bd=0, bg='#326273', command=deleteTask).pack(side=BOTTOM, pady=13)



root.mainloop()