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
mail.login("sender@gmail.com", "password") 
  
# message to be sent 
message = "message to be send ........"
  
# sending the mail 
mail.sendmail("sender", "reciver@gmail.com", message) 
  
# terminating the session 
mail.quit() 
