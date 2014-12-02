import OSC

def test():	
    print 'This is running'
    c = OSC.OSCClient()
    c.connect(('127.0.0.1', 57120))
    oscmsg = OSC.OSCMessage()
    oscmsg.setAddress("/startup")   
    
    c.send(oscmsg)
    