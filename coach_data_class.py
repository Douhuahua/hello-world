#encoding=utf-8
import os
def sanitize(time_string):
    if '-' in time_string:
        splitter='-'
    elif ':' in time_string:
        splitter=':'
    else:
        return(time_string)
    (mins,secs)=time_string.split(splitter)
    return(mins+"."+secs)
#继承类list
class AthleteList(list):
    def __init__(self,a_name,a_bitrhday=None,a_times=[]):
        list.__init__([])
        self.name=a_name
        self.birthday=a_bitrhday
        self.extend(a_times)
    def top3(self):
        return(sorted(set([sanitize(t) for t in self]))[0:3])

os.chdir('F:\\hfpy_ch6_data\\')    
def get_coach_data(filenames):
    try:
        with open(filenames) as f:
            data=f.readline()
        templ=data.strip().split(',')
        return(AthleteList(templ.pop(0),templ.pop(0),templ))
    except IOError as err:
        print('File Error:'+str(err))
    
for timefiles in os.listdir(os.getcwd()):
    people=get_coach_data(timefiles)
    print(people.name+"'s fastest time are: "+str(people.top3()))

Vera=AthleteList('Vera Vi')
Vera.append('1.31') 
print(Vera.top3())
Vera.extend(["2.34","3.12","2.32"])
print(Vera.top3())