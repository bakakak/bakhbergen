import json

a = open('sample.json')
x = json.load(a)

print("""Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------""")

for i in x['imdata']:
    print(i['l1PhysIf']['attributes']['dn'], end="                              ")
    print(i['l1PhysIf']['attributes']['speed'], end="     ")
    print(i['l1PhysIf']['attributes']['mtu'])