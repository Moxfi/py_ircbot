# -*- coding: cp1252 -*-
#author Mox @quakenet

#
#NOTE: CURRENTLY INSECURE IN TERMS OF ACCEPTING COMMANDS.
#To fix: instead of nickname, use mask, ip or a combination of things
#

from time import time
from twisted.internet.protocol import ClientFactory
from twisted.words.protocols.irc import IRCClient
from twisted.internet import reactor

#Next time, use variables as array instead of "news1, news2..."
chnnl = '#channel_to_join'
news1 = 'Emptied'
news2 = ''
news3 = ''
news4 = ''
news5 = ''
news6 = ''
news7 = ''
news8 = ''
time1 = time()

##Creating an Ircbot
class IrcBot(IRCClient):


##Connection made, setting nickname
    def connectionMade(self):
        self.nickname = 'InfodeskV2'
        IRCClient.connectionMade(self)
        print time.strftime('%X')
        
	#Debugging lines for console
    def clientConnectionLost(self, connector, reason):
        connector.connect()
        print time.strftime('%X')
        
    def connectionLostNotify(self):
        print '<-- CONNECTION LOST --> '+ time.strftime('%X %x')
        print time.strftime('%X %x')

##Joining the channel
    def signedOn(self):
        IRCClient.signedOn(self)
        self.join(chnnl)
        print time.strftime('%X %x')
        
##Rejoin if kicked
    def kickedFrom(self, channel, kicker, message):
        self.join(chnnl)
        print time.strftime('%X')
        
## Slap back
    def action(self, user, channel, data):
        nick, hostmask = user.split("!") #Split nicks from Mask <Mox!Mox@noreply.quakenet.org>
        if 'slaps '+self.nickname in data:
            self.me (chnnl,'slaps '+nick+' around a bit with a wrapped newspaper.')
            
##Defining Privmsg
    def privmsg(self, user, channel, message):
        global chnnl, news1, news2, news3, news4, news5, news6, news7, news8, time1
##        nick, hostmask = user.split("!") #Splitting the nick from the
                                             ##nick!user@mask


## DENY OTHERS -- Insecure, use Mask next time
        if not any(s in user for s in ['Moxx','Moxx_','Mox','Mox_']) and message == '!quit':
            self.msg (chnnl,'Denied.')

## MOX ALLOWED COMMANDS -- Insecure, use Mask next time
        if any(s in user for s in ['Moxx','Moxx_','Mox','Mox_']):
            if message == '!quit':
                self.quit()
                reactor.stop()
                sys.exit(0)

			#Handling commands
            if message == '!clear all':
                news1 = ''
                news2 = ''
                news3 = ''
                news4 = ''
                news5 = ''
                news6 = ''
                news7 = ''
                news8 = ''

            if message == '!clear news1':
                news1 = ''
            if message == '!clear news2':
                news2 = ''
            if message == '!clear news3':
                news3 = ''
            if message == '!clear news4':
                news4 = ''
            if message == '!clear news5':
                news5 = ''
            if message == '!clear news6':
                news6 = ''
            if message == '!clear news7':
                news7 = ''
            if message == '!clear news8':
                news8 = ''

            
            if '!set news1 ' in message:
                snakes, planes1, news_1 = message.split(" ", 2) #Splitting the msg
                news1 = news_1

            if '!set news2 ' in message:
                snakes, planes1, news_2 = message.split(" ", 2) #Splitting the msg
                news2 = news_2

            if '!set news3 ' in message:
                snakes, planes1, news_3 = message.split(" ", 2) #Splitting the msg
                news3 = news_3

            if '!set news4 ' in message:
                snakes, planes1, news_4 = message.split(" ", 2) #Splitting the msg
                news4 = news_4

            if '!set news5 ' in message:
                snakes, planes1, news_5 = message.split(" ", 2) #Splitting the msg
                news5 = news_5

            if '!set news6 ' in message:
                snakes, planes1, news_6 = message.split(" ", 2) #Splitting the msg
                news6 = news_6

            if '!set news7 ' in message:
                snakes, planes1, news_7 = message.split(" ", 2) #Splitting the msg
                news7 = news_7

            if '!set news8 ' in message:
                snakes, planes1, news_8 = message.split(" ", 2) #Splitting the msg
                news8 = news_8



##If !info in message...

            if time1-time() < 15:
                if message == '!info':
                    time1 = time()
                    self.msg (chnnl, news1)
                    self.msg (chnnl, news2)
                    self.msg (chnnl, news3)
                    self.msg (chnnl, news4)
                    self.msg (chnnl, news5)
                    self.msg (chnnl, news6)
                    self.msg (chnnl, news7)
                    self.msg (chnnl, news8)
            
## Pinging Ponging and printing for Console
    def lineReceived(self, line):
        print '<- %s' % line + ' ' + time.strftime('%X %x')
        IRCClient.lineReceived(self, line)
        

    def lineSent(self, line):
        print '-> %s' % line + ' ' + time.strftime('%X %x')
        IRCClient.lineSent(self, line)
        

class IrcBotFactory(ClientFactory):
    protocol = IrcBot

#Connecting after all the Defs etc have been made
reactor.connectTCP('gameservers.il.us.quakenet.org', 6668, IrcBotFactory())
reactor.run()
