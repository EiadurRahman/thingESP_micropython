Imagine you want to use Whatsapp to control a microcontroller...

you search something similar on the internet and found a solution, a simple script/code which uses Twilio connected with the thingESP server.
But there is a problem. You are a hardcore Micropython user and ThinngESP script is based on arduino. If you are anything like me you don't want to learn a whole new language,
for a single project.

DON't worry I got you.....

thingESP-micropython is just a translated version of thingESP with a interrupt message function ( explained in the code ).

usage :

copy ThingESP.py file and save it as "ThingESP.py", then initialize it in main.py file with authentication key, project name and username ( explained in the code ).
and you are good to go!

tested with MicroPython v1.20.0 on 2023-04-26; ESP module (1M) with ESP8266
