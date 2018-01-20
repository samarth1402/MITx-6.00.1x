#code snipet for video 2 of of 8-exceptions

#code to extract data from a file

data = []
file_name = input("enter name of your file")

try:
    fh = open(file_name,'r')
except IOError:
    print("cannot open file",file_name)
else:
    for new in fh:
        if new != '\n':
            addIt = new[:-1].split(',')     #remove trailing \n
            data.append(addIt)
finally:
    fh.close()  #close file even if fails

gradesData=[]
if data:
    for student in data:
        try:
            name = student[:-1]
            grades = int(student[-1])
            gradesData.append([name, [grades] ])
        except ValueError:
            gradesData.append([student[:], [] ])