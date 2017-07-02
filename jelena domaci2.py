rečnik = {"brzo":{"sinonimi":["žurno", "hitro"], "antonimi":["polako", "sporo"]},"sreća":{"sinonimi":["radost", "veselje"], "antonimi":[ "tuga", "depresija"]}, "beba":{"sinonimi":["novorođenče", "čedo"], "antonimi":["baka", "deka"]}}
print(rečnik["brzo"]["sinonimi"]) 
print(rečnik["toplo"]["antonimi"]) 
print(rečnik["beba"]["sinonimi"][0]) 
print(rečnik["brzo"]["antonimi"][1]) 

for reč in rečnik.keys():
    
    print("Reč: ", reč) 
    sin = "Sinonimi: "
    ant = "Antonimi: "

    for sinonim in rečnik[reč]["sinonimi"]:
        sin += sinonim + ", "
    print(sin[:-2])

    for antonim in rečnik[reč]["antonimi"]:
        ant += antonim + ", "    
    print(ant[:-2] + "\n") 

   


   