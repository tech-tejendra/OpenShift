#!/usr/bin/python

import smtplib

sender = 'student@workstation.lab.example.com'
receivers = ['student@workstation.lab.example.com']

message = """From: From Peron <student@workstation.lab.example.com>
To: To Person <student@workstation.lab.example.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)         
   print "Successfully sent email"
except Exception:
   print "Error: unable to send email"
