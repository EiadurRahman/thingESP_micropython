# note all the Pins(output,adc etc) were initialize in the boot file
# Examples :
# adc = ADC(0)
# d1 = Pin(5, Pin.IN, Pin.PULL_UP)
# d2 = Pin(4 , Pin.OUT)
# d5 = Pin(14, Pin.OUT)
# d4 = Pin(2, Pin.OUT)
# d5 = Pin(14 ,Pin.OUT)
# d6 = Pin(12 , Pin.IN , Pin.PULL_UP)
# btn = Pin(0, Pin.IN , Pin.PULL_UP)

import ThingESP
thing = ThingESP.Client('user_name', 'project_name', 'password')
ThingESP.send_msg('device is back online ')

led_1 = False
led_2 = False

def interrupt(Pin):
    global btn_trig
    btn_trig = False
    if btn.value() == 0 and not btn_trig :
        btn_trig = True
        d4.off()
        print('Button was pressed !!!!')
        ThingESP.send_msg('Button was pressed !!!!')
        sleep(.5)
        d4.on()
btn.irq(trigger=Pin.IRQ_FALLING,handler=interrupt)
btn_trig = False

def handleResponse(query):
    
    global led_1
    global led_2
    #led part
    if 'led' in query:
        #on~~~~~~~~
        if 'on' in query:
            if '1' in query:
                if not led_1:
                    led_1 = True
                    d2.on()
                    return 'led 1 is on'
                else:
                    return 'led 1 is already on'
            elif  '2' in query:
                if not led_2 :
                    led_2 = True
                    d5.on()
                    return 'led 2 is on'
                else:
                    return 'led 2 is already on'
            elif 'all' in query :
                if not led_1 or not led_2:
                    d2.on()
                    d5.on()
                    led_1 = True
                    led_2 = True
                    return 'Turning all leds on'
            else :
                return 'no led found '
        #off~~~~~~~~
        elif 'off' in query:
            if '1' in query:
                if led_1:
                    led_1 = False
                    d2.off()
                    return 'led 1 is off'
                else:
                    return 'led 1 is already off'
            elif  '2' in query:
                if led_2:
                    led_2 = False
                    d5.off()
                    return 'led 2 is off'
                else :
                    return 'led 2 is already off'
            elif 'all' in query:
                if led_1 or led_2:
                    d2.off()
                    d5.off()
                    led_1 = False
                    led_2 = False
                    return 'Turning all leds off'
            else :
                return 'no led found'
        else :
            return 'unknown state of led is declared'
        
    #other stuff
    elif  query == 'light':
        light = adc.read()
        stats = ' room lights are on'
        if light < 10: # change the value according to your preference 
            stats = ' light sources are dim/off, prahaps lights are off '
        elif light >40:
            stats = ' light source is pretty bright !'
        return 'lightness state : '+str(light)+ stats
    elif 'ki11' in query: #just a fun way to turnoff all leds
        if led_1 or  led_2:
            d2.off()
            d5.off()
            led_1 = False
            led_2 = False
            return "Turning all led's off"
        else:
            return "led's are already off"
    elif 'on' in query:
        if not led_1 or not led_2:
            d2.on()
            d5.on()
            led_1 = True
            led_2 = True
            return 'Turning all on leds'
        else:
            return "led's are already on"
    elif 'status' in query:
        state = str('is on? \nled_1 : %s'%led_1+'\nled_2 : %s'%led_2)
        print(state)
        return state
    
    else:
        return 'no task is set for [%s]'%query


thing.setCallback(handleResponse).start()

print('END_TASK')




