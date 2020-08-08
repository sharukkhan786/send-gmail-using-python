#Python code to illustrate Sending mail from  
# your Gmail account  
import smtplib 
  
# creates SMTP session 
mail = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
mail.starttls()

#identify to server
mail.ehlo()
  
# Authentication 
mail.login("sharukkhan160@gmail.com", "banu12345") 
  
# message to be sent 
message = "hi onu ila summa bore adichudhu adhan hahaha........"
  
# sending the mail 
mail.sendmail("sharukkhan", "meharinarifa25@gmail.com", message) 
  
# terminating the session 
mail.quit() 
