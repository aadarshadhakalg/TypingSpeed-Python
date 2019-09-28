from tkinter import *
import datetime
import pytz
import requests
import json

#windows_setup
root = Tk()
root.title("Typing Speed Test")
root.geometry("600x500")

payload={'type':'all-meat','sentences':'1','format':'json'}
url="https://baconipsum.com/api/"
gText=requests.get(url,params=payload)
list=json.loads(gText.content)
Text=list[0]

total_it=1

def start():
    Message(text_frame,text=Text,width='600').place(rely='0.2',relx='0.015',relwidth='0.97')
    x=datetime.datetime.now()
    isec=x.strftime("%S")
    imin=x.strftime("%M")
    total_it=int(imin)*60+int(isec)
    displaytext1="Start:",x
    Label(text_frame,text=displaytext1).place(rely='0.8',relx='0.015')


def stop():
    y=datetime.datetime.now()
    fsec=y.strftime("%S")
    fmin=y.strftime("%M")
    total_ft=int(fmin)*60+int(fsec)
    displaytext2="End: ", y
    Label(text_frame,text=displaytext2).place(rely='0.8',relx='0.6')

    Text1=entry_box.get()
   # file=open("temp.txt","wb")
    #chars=file.write(Text1)
    tdiff=total_ft-total_it
    time_taken="Your taken time: ", tdiff
    Label(result,text=time_taken).place()
    total_char=len(Text1)
    tspeed=float(total_char/tdiff)
    speed_res="Your typing speed is: ", tspeed, "charecters per second"
    Message(result,text=speed_res,width='600').place(rely='0.2',relx='0.015',relwidth='0.97')

#error calculations

    if len(Text)<=len(Text1):
        counter=0
        error=0
        while counter < len(Text):
            if Text[counter]==Text1[counter]:
                error=error+0
            else:
                error=error+1
                counter=counter+1
    elif len(Text1)<=len(Text):
        counter=0
        error=0
        while counter < len(Text1):
            if Text[counter]==Text1[counter]:
                error=error+0
            else:
                error=error+1
                counter=counter+1
    error_res="Errors: ", error,"characters"
    Message(result,text=error_res,width='600').place(rely='0.5',relx='0.015',relwidth='0.97')
    
    
#Frames
text_frame= Frame(root)
text_frame.place(relwidth="0.97",relheight="0.3",relx="0.015")
start_button=Button(root,text="start",command=start)
start_button.place(relwidth="0.35",relheight="0.1",relx="0.15",rely="0.35")

end_button=Button(root,text="stop",command=stop)
end_button.place(relwidth="0.35",relheight="0.1",relx="0.50",rely="0.35")


entry_box= Entry(root,bg="grey")
entry_box.place(relwidth="0.97",relheight="0.3",relx="0.015",rely="0.5")

result=Frame(root)
result.place(rely='0.8',relx='0.015',relwidth="0.97",relheight='0.15')

credit=Label(root,text="Created by Aadarsha Dhakal",bg="black",fg='white').place(relheight="0.05",rely='0.95',relwidth='1')

root.mainloop()
