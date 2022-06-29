
from flask_mail import Message
from flask import render_template
from myproject import mail

def sendmail(email, url ):
    
    
   #try:
    
    msg = Message('Change Password Request', sender = 'Movie app', 
    recipients = [email])
    
    msg.body = render_template('reset.txt',url = url)

    msg.html = render_template('reset.html',url = url)
    
    mail.send(msg)
 

    return 1 

   # except Exception as e:
    #    print("Error" + e)
     #   return 0

