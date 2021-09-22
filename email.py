import smtplib
sender=input("type sender mamil :" )
login_password=input("type your login password :")
server=smtplib.SMTP_SSL("smtp.gmail.com",465)
receiver_mail=input("type receiver mail :")
server.login(sender,login_password)
message=input("type your message :")
server.sendmail(sender,receiver_mail,message)
server.quit()
