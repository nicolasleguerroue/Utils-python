# Mails
Some tools to send emails

## Settings

For SMTP server, you must use 2-app security 

## Code

Edit Mails.py main function (set recipient mail)
and run Mail.py file :

```
python3 Mail.py
```

## Example
```
    recipient = "recipient@domain.end"


    mail = Mail()

    mail.setServer("smtp.gmail.com", 587)
    mail.setLogFile("log.txt")
    mail.setContentType("html")
    mail.setEncoding("utf-8")
    mail.setSender("senderEmail", "password")

    mail.addAttachment("log.txt", "log.txt")
    mail.setRecipient(recipient)
    mail.setTitle("Title")
    mail.setContent("<h1>Title</h1><h2>Sub-title</h2>Content edited by <b>Python</b>")
    mail.addAttachment("image.png", "outputName.png")
    mail.send()
```