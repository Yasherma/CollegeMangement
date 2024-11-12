new=("vivek collage of bijnor")
print(new)
Department=["there are Department in the collage"]
while (True):
    press=int(input("1 for depatment name's"))
    if press==1:
        print("vivek collage of Edcuation \n",
                    "vivek collage of management \n",
                    "vivek collage of ayurvaida\n",
                     "vivek collage of scince")
        print("if you want collage of Edcuation details 11 \n"
              " if you want collage of management details 12\n"
              'if you want collage of ayurvaida details 13\n'
              "if you want collage of scince\n")
        continue
    elif press==11:
        print("In the Edcuation depatment there are course \n"
              "Bca,B.ed,basic homesince,LLB,BaLLb")
        break
    elif press==12:
        print("In the management depatment there are course \n"
              "BBa,B.com,B.com(honers),Mba,")
        break

    elif press==13:
        print("In the ayurvaida depatment there are course \n"
              "B.farma,D.farma,basic.nurssing,genome,Bms")
        break
    elif press==14:
        print("In the scince depatment there are course \n"
              "basic.math,basic. bio,basic.computer-scince")
        break

course={"Bca":"Bca, fees 25000+exam fees 2200+dress fees 3000 include all fees",
       "B.ed":"B.ed,fees 75000+exam fees 2500+dress 3000 include allfess",
       "basic homescince":"basic homescince fees 15000+exam fees 2500+fress 3000 include allfees",
       "LLb":"LLb fees 15000+exam fees +dress fees include aalfees",
       "BaLLb":"BaLLb fees 20000+exam fees 2500+dress fess 3000  include fees",
       "BBa":"BBa fees 60000+exam fees 2500+dress fees 3000 include fees",
        "B.com":"B.com 25000+Exam fees 2500+dress fees 3000 include fees",
        "B.com,honers":"B.com(honers) 35000+Exam fees 2500+dress fees 3000 include fees",
        "Mba":"Mba 25000+Exam fees 90000+dress fees 3000 include fees",
       " B.farma":"B.farme 75000+Exam fees 2500+dress fees 3000 include fees",
        "D.farma":"D.farma 70000+Exam fees 2500+dress fees 3000 include fees",
        "basic.nurssing":"basic.nurssing 30000+Exam fees 2500+dress fees 3000 include fees",
        "genome":"genome 35000+Exam fees 2500+dress fees 3000 include fees",
        "Bms":"Bms 25000+Exam fees 2500+dress fees 3000 include fees",
        "basic.math":"basic.math 25000+Exam fees 2500+dress fees 3000 include fees",
        "Basic.bio":"Basic.bio 30000+Exam fees 2500+dress fees 3000 include fees",
        "computer-scince":"compu=scince 30000+Exam fees 2500+dress fees 3000 include fees",
        }
couress=input("enter the name of courese")
print(course[couress])


