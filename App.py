import tkinter
import pyttsx3
import speech_recognition as sr
import smtplib
class App:
    def __init__(self):
        #m=tkinter.Tk()
        #m.mainloop()
        pass
    def audio(self,audio):
        engine = pyttsx3.init()
        engine.say(audio)
        engine.runAndWait()
    def listen(self):
        r = sr.Recognizer()
        try:
        # use the microphone as source for input.
            with sr.Microphone() as source2:
                    r.adjust_for_ambient_noise(source2, duration=0.2)
                    #listens for the user's input 
                    audio2 = r.listen(source2)
                    MyText = r.recognize_google(audio2)
                    MyText = MyText.lower()
                    print("Did you say "+MyText)
                    obj.audio(MyText)
        except sr.RequestError as e:
                print("Could not request results; {0}".format(e))
        except sr.UnknownValueError:
                print("unknown error occurred")
        return MyText 
    def mail(self,to,msg):
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            yourmail = "example@gmail.com"
            server.login(yourmail,"gmail_password")
            server.sendmail(yourmail, to, msg)
            server.close()
            print("iam working on it")

        except smtplib.SMTPException:
            print(smtplib.SMTPException)
            obj.audio(smtplib.SMTPException)
        except smtplib.SMTPServerDisconnected:
            print(smtplib.SMTPServerDisconnected)
            obj.audio(smtplib.SMTPServerDisconnected)
        except smtplib.SMTPResponseException:
            obj.audio(smtplib.SMTPResponseException)
        except smtplib.SMTPSenderRefused:
            print(smtplib.SMTPSenderRefused)
            obj.audio(smtplib.SMTPSenderRefused)
        except smtplib.SMTPRecipientsRefused:
            print(smtplib.SMTPRecipientsRefused)
            obj.audio(smtplib.SMTPRecipientsRefused)
        except smtplib.SMTPDataError:
            print(smtplib.SMTPDataError)
            obj.audio(smtplib.SMTPDataError)
        except smtplib.SMTPConnectError:
            print(smtplib.SMTPConnectError)
            obj.audio(smtplib.SMTPConnectError)
        except smtplib.SMTPHeloError:
            print(smtplib.SMTPHeloError)
            obj.audio(smtplib.SMTPHeloError)
        except smtplib.SMTPNotSupportedError:
            print(smtplib.SMTPNotSupportedError)
            obj.audio(smtplib.SMTPNotSupportedError)
        except smtplib.SMTPAuthenticationError:
            print(smtplib.SMTPAuthenticationError)
            obj.audio(smtplib.SMTPAuthenticationError)      
    def run(self):
        print("Audio BOT\n")
        print("please speak:\nMail to address:\t i'm listening") 
        obj.audio("mail to address:\t i'm listening")
        to =obj.listen()
        print("tell me message")
        msg = obj.listen()
        print("please verify the to address :\t",to,"\nand the  message is :\t",msg)
        val = "please verify the to address :\t"+to+"\nand the  message is :\t"+msg
        obj.audio(val)
        try:
            obj.mail(to,msg)
        except IOError:
            obj.audio("something mistake i ve done please fix me")
            breakpoint
        except EOFError:
            obj.audio("something mistake i ve done please fix me")
            breakpoint        
if __name__ == '__main__':
    obj = App()
    obj.run()