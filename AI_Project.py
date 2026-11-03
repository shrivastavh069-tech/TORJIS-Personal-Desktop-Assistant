import sys
import webbrowser
import inflect
import subprocess
import time
import queue
import random
import threading
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QApplication,QMainWindow
from PyQt6.QtGui import QMovie
from PyQt6.QtCore import QObject, pyqtSignal
from korjis import Ui_MainWindow as my_ai
 
class my_assistant(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=my_ai()
        self.ui.setupUi(self)
        self.ui.copy.hide()
        self.clear()
        self.brain()
        self.ui.cus.returnPressed.connect(self.cus_timer)
        self.ui.set.clicked.connect(self.what_timer)
        self.ui.line2.returnPressed.connect(self.calculations)
        self.ui.line1.returnPressed.connect(self.get_input)
        self.ui.line.returnPressed.connect(lambda: self.tasks(self.ui.line.text().strip()))
        self.ui.mike.mousePressEvent=lambda event:(self.listen("listen"))
        self.ui.mike_1.mousePressEvent=lambda event:(self.listen("note"))
        self.ui.mike_2.mousePressEvent=lambda event:(self.listen("numbers"))
        self.con=""
        self.no1 = 0
        self.no2 = 0
        self.ui.ok.clicked.connect(self.what_mode)
        self.ui.want.clicked.connect(self.action)
        self.ui.cle.clicked.connect(self.clear)
        self.ui.outputs.hide()
        self.ui.copy.clicked.connect(self.copykarna)
        display=9
        self.view(display)
        self.mila.connect(lambda kaam: kaam())
        QTimer.singleShot(500,self.greeting)
        
    def view (self,display):
        print("call aa gyi")
        if display == 1:
            print("1")
            self.ui.vid.hide()
            self.ui.v3.hide()
            self.ui.v8.hide()
            self.ui.v2.hide()
            self.ui.v4.hide()
            self.ui.v5.hide()
            self.ui.v6.hide()
            self.ui.v7.hide()
            self.ui.v1.show()
            self.movie=QMovie("vi1.gif")
            self.ui.v1.setMovie(self.movie)
            self.movie.start()
            
        elif display == 2 :
            print("2")
            self.ui.vid.hide()
            self.ui.v1.hide()
            self.ui.v5.hide()
            self.ui.v8.hide()
            self.ui.v6.hide()
            self.ui.v7.hide()            
            self.ui.v3.hide()
            self.ui.v4.hide()
            self.ui.v2.show()
            self.movie=QMovie("vi2.gif")
            self.ui.v2.setMovie(self.movie)
            self.movie.start()
            
        elif display == 3 :
            print("3")
            self.ui.vid.hide()
            self.ui.v1.hide()
            self.ui.v5.hide()
            self.ui.v6.hide()
            self.ui.v7.hide()
            self.ui.v8.hide()
            self.ui.v2.hide()
            self.ui.v4.hide()
            self.ui.v3.show()
            self.movie=QMovie("vi3.gif")
            self.ui.v3.setMovie(self.movie)
            self.movie.start()

        elif display ==4:
            self.ui.v1.hide()
            self.ui.v3.hide()
            self.ui.v2.hide()
            self.ui.v8.hide()
            self.ui.v5.hide()
            self.ui.v6.hide()
            self.ui.v7.hide()
            self.ui.v4.hide()
            self.ui.vid.show()
            self.movie=QMovie("vid.gif")
            self.ui.vid.setMovie(self.movie)
            self.movie.start()            

        elif display ==5:
            self.ui.v1.hide()
            self.ui.v3.hide()
            self.ui.v2.hide()
            self.ui.v5.hide()
            self.ui.v8.hide()
            self.ui.v6.hide()
            self.ui.v7.hide()
            self.ui.vid.hide()
            self.ui.v4.show()
            self.movie=QMovie("vi4.gif")
            self.ui.v4.setMovie(self.movie)
            self.movie.start()            

                      
        elif display ==6:
            self.ui.v1.hide()
            self.ui.v3.hide()
            self.ui.v2.hide()
            self.ui.v8.hide()
            self.ui.v5.hide()
            self.ui.v6.hide()
            self.ui.v7.show()
            self.ui.vid.hide()
            self.ui.v4.hide()
            self.movie=QMovie("vi7.gif")
            self.ui.v7.setMovie(self.movie)
            self.movie.start()            
            
        elif display ==7:
            self.ui.v1.hide()
            self.ui.v3.hide()
            self.ui.v2.hide()
            self.ui.v6.hide()
            self.ui.v8.hide()
            self.ui.v7.hide()
            self.ui.vid.hide()
            self.ui.v4.hide()
            self.ui.v5.show()
            self.movie=QMovie("vi5.gif")
            self.ui.v5.setMovie(self.movie)
            self.movie.start()            
       
        elif display == 8 :
            print("8")
            self.ui.vid.hide()
            self.ui.v1.hide()
            self.ui.v5.hide()
            self.ui.v8.hide()
            self.ui.v6.show()
            self.ui.v7.hide()            
            self.ui.v3.hide()
            self.ui.v4.hide()
            self.ui.v2.show()
            self.movie=QMovie("vi6.gif")
            self.ui.v6.setMovie(self.movie)
            self.movie.start()
            
        elif display ==9:
            self.ui.v1.hide()
            self.ui.v3.hide()
            self.ui.v2.hide()
            self.ui.v6.hide()
            self.ui.v8.show()
            self.ui.v7.hide()
            self.ui.vid.hide()
            self.ui.v4.hide()
            self.ui.v5.hide()
            self.movie=QMovie("vi8.gif")
            self.ui.v8.setMovie(self.movie)
            self.movie.start()            
                  
        
    def free_face(self):

         
        mood=random.choice([1,1,68,5])
        print(mood)
        display=mood
        self.view(display)

    def greeting(self):
        import time
        hour = int(time.strftime("%H"))

        if 6 <= hour < 12:
            self.great="morning"
            self.computer("Good morning.")
        elif 12 <= hour < 16:
            self.great="afternoon"
            self.computer("Good afternoon.")
        elif 16 <= hour < 22:
            self.great="evening"
            self.computer("Good evening.")
        else:
            self.great="night"
            self.computer("Good night.")

        time.sleep(0.03)
        self.computer("How can I help you")
        display=4
        self.view(display)
        self.clear()

    def computer(self, text):
        import pyttsx3
        def bolo():
            engine = pyttsx3.init()
            engine.say(text)
            engine.runAndWait()
            engine.stop()

        t = threading.Thread(target=bolo)
        t.start()
        while t.is_alive():                  # bolne tak GUI chalta rahe
            QApplication.processEvents()
            time.sleep(0.01)
        
    def intro(self):
        display=4
        self.view(display)
        self.computer(f"Good {self.great} everyone.")
        time.sleep(0.02)
        self.computer("MY name is TORJIS an AI perssonal assistant")
        time.sleep(0.02)
        self.computer("come with facial expression can also introduce your projects,calculate your bmi an also can do basic calculations")
        self.clear()
        
        
       

    def open_youtube(self):
        display=8
        self.view(display)
        self.computer("command executed")
        webbrowser.open("https://www.youtube.com/")
        self.clear()
      
        
        

    
                
    def copykarna(self):
        copy_password=self.ui.line.text()
        QApplication.clipboard().setText(copy_password)
        QTimer.singleShot(2000,self.clear)
        

    def open_snake(self):
        display=8
        self.view(display)
        self.computer("command executed ")
        time.sleep(0.03)
        self.computer("feel the pleasure")
        subprocess.Popen(
            ["python", r"C:\snake_game\snake\main.py"],
            cwd=r"C:\snake_game\snake"
        )        
        self.clear()
        
        

    def open_sps(self):
        display=8
        self.view(display)
        self.computer("enjoy your game ")
        time.sleep(0.03)
        subprocess.Popen(
            ["python", r"C:\Help_coder\help_coder\main.py"],
            cwd=r"C:\Help_coder\help_coder"
        )       
        self.clear()
        

    
    def des_snake (self):
        display=4
        self.view(display)
        self.computer("The game starts with an animated intro screen, background music, and a Play button to begin the game.")
        time.sleep(1.5)
        self.computer("Players can choose between Player vs Bot and 2 Player game modes before starting.")
        time.sleep(1)
        self.computer("first i will tell you about Player vs player board")
        time.sleep(1.5)
        self.computer("This is the player vs player board .")
        time.sleep(1)
        self.computer("on upper side there is An accessible menu bar lets players resume the game, return to the menu, or exit while playing.")
        time.sleep(1)
        self.computer("we are returning into menu ")
        self.computer("it is an completely diffrent board of player vs bot ")
        time.sleep(1)
        self.computer("TO save your time i would play this gameplay into 4x")
        time.sleep(180)
        self.computer("we can access the menubar from here also")
        time.sleep(120)
        self.computer("victory secene of bot wins")
        time.sleep(1)
        self.clear()
        

        
    def des_stone(self):
        display=4
        self.view(display)
        
        self.computer("The game starts with an animated intro screen, background music, and a Play button to begin the game.")
        time.sleep(1)
        self.computer("The story tells about coder life.")
        time.sleep(53)
        self.computer("this a game play mode in which the battle begins with brain and a coder to fix the bug right now or fix bug at tommorrow")
        time.sleep(60)
        self.computer("Here the coder is win")
        time.sleep(6)
        #self.timer("showing you winnig screen of brain")
        self.clear()

        
    mila = pyqtSignal(object)        
    def listen(self, staged):
        self.computer("i am listening")
        import speech_recognition as sr

    # ye GUI wala kaam hai, main thread mein chalega
        def gui_kaam(command):
            if staged == "listen":
                self.ui.line.setText(command)
                self.tasks(command)

            elif staged == "note":
                from word2number import w2n
                print("mike_1")
                self.number = w2n.word_to_num(command)
                self.ui.line1.setText(str(self.number))
                self.ui.line2.setText(str(self.number))
                self.ui.cus.setText(str(self.number))
                
            elif staged == "numbers":
                print("mike_2")
                self.kan=""
                self.typed = command
                self.typed=self.typed+self.kan
                self.ui.line.setText(self.typed)


                

    # ye sirf sunne wala kaam hai, background thread mein chalega
        def listen_audio():
            try:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    audio = r.listen(source, timeout=5)
                command = r.recognize_google(audio).lower()
                self.mila.emit(lambda: gui_kaam(command))   # GUI ko bhejo
            except:
                print("Awaaz samajh nahi aayi")

        thread = threading.Thread(target=listen_audio)
        thread.start()
  


            
#calculations torjis---------------
    def computer_calculator(self):
        self.con = "" 
        self.ui.feature.show()
        self.ui.feature.setCurrentIndex(2)
        self.computer("Please select the mode and press select")
    
        
   
    def what_mode(self):
        display=3
        self.view(display)
        self.ui.line2.show()
        self.ui.line.hide()
        self.ui.line1.hide()
        self.ui.line2.clear()
        
        if self.ui.basic.isChecked():
            self.ui.outputs.show()
            self.ui.outputs.setCurrentIndex(3)
            self.computer("What is the 1st number")    
            
        if self.ui.square.isChecked():
            self.ui.outputs.show()
            self.ui.outputs.setCurrentIndex(2)
            self.computer("What is the number")

        elif self.ui.cube.isChecked():
            self.ui.outputs.show()
            self.ui.outputs.setCurrentIndex(2)
            self.computer("What is the number")
            
        self.ui.feature.hide()    




    def calculations(self):
        self.number = int(self.ui.line2.text().strip())
            
        if self.con =="2":
            self.no2=self.number
            self.ui.feature.show()
            self.ui.feature.setCurrentIndex(1)
            self.ui.line2.hide()
            self.computer("what is your operations")
            self.ui.outputs.hide()
            

        elif self.ui.square.isChecked():
            self.ab = self.number ** 2
            self.computer(f"Your answer is {self.ab}")
            self.ui.outputs.hide()
            self.ui.line2.setText(str(self.ab))
            QTimer.singleShot(800,self.clear)
            
        elif self.ui.cube.isChecked():
            self.ab = self.number ** 3
            self.computer(f"Your answer is {self.ab}")
            self.ui.outputs.hide()
            self.ui.line2.setText(str(self.ab))
            QTimer.singleShot(800,self.clear)
            
        elif self.ui.basic.isChecked():  
            self.no1=self.number             
            self.ui.outputs.setCurrentIndex(4)
            self.ui.line2.clear()
            self.computer("what is your 2nd number")  
            self.con="2"
                 
       
        
    def action(self):
        
        if self.ui.add.isChecked():
            self.ab=self.no1+self.no2
            
        elif self.ui.sub.isChecked():
            self.ab=self.no1-self.no2
                    
        elif self.ui.into.isChecked():
            self.ab=self.no1*self.no2
            

        elif self.ui.div.isChecked():
            self.ab=self.no1/self.no2
            
        self.ui.outputs.hide()
        self.computer(f"Your answer is {self.ab}")
        self.ui.line2.setText(str(self.ab))
        self.ui.line2.clear()
        self.ui.line2.hide()       
        QTimer.singleShot(800,self.clear)
        

            
                
#my password generator roject----------            

    def des_password(self):
        display=1
        self.view(display)
        self.computer("keep it private")
        time.sleep(0.02)
        self.computer("Contacting Mr.safe")
        from passward_generator import GUI
        self.password_window = GUI()
        self.password_window.show()       
        self.clear()
        
        

#Torjis calculate BMI------------------
    def index(self):
        display=3
        self.view(display)
        self.staged ="numbers"
        self.mike_show("numb")
        self.ui.line.hide()
        self.computer("sure")
        time.sleep(0.15)
        self.ui.outputs.show()
        self.computer("what is your height")
        self.ui.line1.show()
        self.ui.outputs.setCurrentIndex(0)
        self.stage = "height"
        
        
           

    def get_input(self):
        print("L")
        self.number = int(self.ui.line1.text().strip())
        print(self.number)
        if self.stage == "height":
            self.height = int(self.number)
            self.clear()
            self.computer("what about weight")
            self.ui.outputs.setCurrentIndex(1)
            self.stage = "weight"
            self.ui.line1.clear()
            self.ui.line1.show()
            
        elif self.stage =="weight":
            print("weight")
            self.weight = int(self.number)
            results = self.weight / ((self.height / 100) ** 2)
            self.computer("calculating...")
            self.ui.outputs.hide()
            self.ui.line1.hide()
            time.sleep(0.10)
            self.computer(f"Your body mass index is {results:.2f}")
            self.ui.outputs.hide()
            self.number=0
            self.ui.line1.clear()
            self.stage = "listen"
            self.ui.line.show()            
            self.clear()
                        
        

            
    


#Torjis notepad-------------------
    def notepad (self):
        display=4
        self.view(display)
        staged="note"
        self.mike_show("not")
        self.computer("now i will listen to you")
        self.ui.copy.show()
        self.ui.cle.show()

        


#timer concept---------
    def timing(self):
        display=7
        self.view(display)
        self.ui.feature.show()
        self.staged="numbers"
        self.mike_show("numb")
        self.ui.feature.setCurrentIndex(0)
        self.computer("assigned the timer")
        

    def what_timer(self):
        if self.ui.sec3.isChecked():
            sec = 3

        elif self.ui.sec10_2.isChecked():
            sec = 5

        elif self.ui.sec10.isChecked():
            sec = 10
            
        self.computer("Timer is assigned")
        QTimer.singleShot(sec * 1000,lambda: self.computer("Time is over"))
        self.clear()
                       
    def cus_timer(self):
        secs = int(self.ui.cus.text().strip())
        self.computer("timer is assigned")        
        QTimer.singleShot(secs * 1000, lambda: self.computer("time is over"))                                                     
        self.staged = "listen"
        self.clear()
       
        

                  
            
#my bmi project showing---------------
    def bmi(self):
        display=5
        self.view(display)
        self.computer("Sure")
        time.sleep(0.05)
        self.computer("appointment with Dr.care is confirmed ")
        from body_mass import calculate
        self.bmi_cal=calculate()
        self.bmi_cal.show()
        self.clear()
      
        
            



#password torjis generate------------

    def password(self):
        display=1
        self.view(display)
        import random
        import string
        self.computer("executed")
        time.sleep(0.03)
        self.computer("request send for password to mr.safe")
        time.sleep(0.05)
        def generate():
            safe=random.choice(["dig","upp","low","pun"])
            return(safe)
        
        length=16
        un_pass=""
        i=1
        while i<length:
            hel=generate()
            if hel == "dig":
                un_pass +=random.choice(string.digits)
            if hel == "upp":
                un_pass +=random.choice(string.ascii_uppercase)
            if hel == "low":
                un_pass +=random.choice(string.ascii_lowercase)
            if hel == "pun":    
                un_pass +=random.choice(string.punctuation)
            i+=1

        
        self.computer("your password displayed below")
        self.ui.copy.show()
        self.ui.line.setText(un_pass)
        QTimer.singleShot(2000,self.clear)
        
        
        
        
    def down(self):
        self.computer("have a nice time with you")
        self.clear()
        self.ui.line.hide()
        self.ui.mike.hide()
        time.sleep(0.05)
        self.computer("bye")
        display=6
        self.view(display)
        QTimer.singleShot(3000,self.bye)

    def bye(self):
        QApplication.quit()



#Torjis brain--------------    
    def brain (self):    
        self.commands = {
            "hello":self.greeting,
            "yourself": self.intro,
            "youtube": self.open_youtube,
            "regenerated":self.password,
            "suggest a password":self.password,
            "generate a password":self.password,
            "password suggested":self.des_password,
            "calculator":self.computer_calculator,
            "shutdown":self.down,
            #"tell me about ":self.des_snake,
            "set a timer":self.timing,
            "mister care":self.bmi,
            "mr.care":self.bmi,
            "notepad":self.notepad,
            "calculate bmi":self.index,
            "tell me about my stone paper scissor game":self.des_stone,
            "snake":self.open_snake,
            "stone":self.open_sps,
        }
          
    

        
#clear the whole part-------------------        
    def clear(self):
        print("clear")
        self.staged="listen"
        self.ui.copy.hide()
        self.ui.line.clear()
        self.ui.line1.clear()
        self.ui.line2.hide()
        self.ui.line2.clear()
        self.ui.cle.hide()
        self.ui.feature.hide()
        self.ui.mike_1.hide()
        self.ui.mike_2.hide()
        self.ui.line1.hide()
        #mike Show -------------
        self.ui.line.show()
        self.ui.mike.show()
        self.free_face()
      
        
   
                    
    def mike_show(self,show):
        if show =="numb":
            self.ui.mike_2.hide()
            self.ui.mike.hide()
            self.ui.mike_1.show()
        elif show =="not":
            self.ui.mike_1.hide()
            self.ui.mike.hide()
            self.ui.mike_2.show()
            
    
            
#mike tasks gainer---------------------------        
    def tasks(self, command):
        command = command.lower().strip()
        for keyword, action in self.commands.items():
            if keyword in command:
                action()
                return

        # koi command match nahi hui
        self.view(2)
        self.computer("i cannot understand")
        time.sleep(0.03)
        self.computer("can you please repeat")
        self.ui.line.clear()


app=QApplication(sys.argv)
Window=my_assistant()
Window.show()
sys.exit(app.exec())



                
