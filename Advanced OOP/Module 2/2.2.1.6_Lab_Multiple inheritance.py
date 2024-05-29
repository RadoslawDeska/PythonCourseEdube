'''
Estimated time

20 minutes
Level of difficulty

Easy
Objectives

    improving the student's skills in operating with multiple inheritance;
    pointing out the nature of multiple inheritance problems.

Scenario

    Your task is to build a multifunction device (MFD) class consisting of methods responsible for document scanning, printing, and sending via fax.
    The methods are delivered by the following classes:
        scan(), delivered by the Scanner class;
        print(), delivered by the Printer class;
        send() and print(), delivered by the Fax class.
    Each method should print a message indicating its purpose and origin, like:
        'print() method from Printer class'
        'send() method from Fax class'
    create an MFD_SPF class ('SPF' means 'Scanner', 'Printer', 'Fax'), then instantiate it;
    create an MFD_SFP class ('SFP' means 'Scanner', 'Fax', 'Printer'), then instantiate it;
    on each object call the methods: scan(), print(), send();
    observe the output differences. Was the Printer class utilized each time?

'''

class Device:
    pass

class Scanner:
    def scan(self):
        print('scan() method from Scanner class')

class Printer:
    def print(self):
        print('print() method from Printer class')

class Fax:
    def send(self):
        print('send() method from Fax class')
    def print(self):
        print('print() method from Fax class')


class MFD_SPF(Scanner, Printer, Fax):
    pass

class MFD_SFP(Scanner, Fax, Printer):
    pass

spf = MFD_SPF()
sfp = MFD_SFP()

spf.print() # Printer class is resolved before Fax, so Printer.print is used
spf.scan()
spf.send()

sfp.print() # Fax class is resolved before Printer, so Fax.print is used
sfp.scan()
sfp.send()