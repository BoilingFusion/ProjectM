from MailSendingScript import *
from reddit_quote_extractor import *
import time

try:
    time.sleep(86400)
    SendMail(get_reddit())
    print("mission sucsesfull")
    
except:
    CloseConnection()
    print("mission failed, better luck next time")
