import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
  
fromaddr = "sgdzta@gmail.com"
toaddr = "frozenthrone.ashutosh.mishra@gmail.com"
  
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Doorbell alert!"
body = "PIR sensor detected an intruder!"
msg.attach(MIMEText(body, 'plain'))
 
filename = "Thief's photo.jpg"
attachment = open("/home/pi/my_project/thief.jpg", "rb")
 
p = MIMEBase('application', 'octet-stream')
p.set_payload((attachment).read())
encoders.encode_base64(p)
p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
msg.attach(p)
 
s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
s.login(fromaddr, "CS299299")
text = msg.as_string()
s.sendmail(fromaddr, toaddr, text)
s.quit()