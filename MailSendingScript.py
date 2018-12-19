import email
import smtplib


target = input("target:")
target2 = input("target2:")
name = input("name:")
code = input("code:")

try:
    print("connection to server")
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    print("logging into server")
    s.login(name,code)
    print("logged in and ready to go")
    

except:
    print("mission failed, better luck next time")
    s.close()
    exit()




def SendMail(message):
    s.sendmail(name,[target,target2],message)


def CloseConnection():
    print("closing connection")
    print("done")
