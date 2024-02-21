import json

f = open("/Users/datkha/Desktop/sample-data.json")

x = json.load(f)

print("Interface Status")
print("============================================================================================")
print("DN                                                 Description           Speed        MTU  ")
print("-------------------------------------------------- --------------------  -------      ------")

for i in range(len(x["imdata"])):
    print(x["imdata"][i]["l1PhysIf"]["attributes"]["dn"], "\t\t\t\t", x["imdata"][i]["l1PhysIf"]["attributes"]["speed"],"     ",x["imdata"][i]["l1PhysIf"]["attributes"]["mtu"])
    
f.close()