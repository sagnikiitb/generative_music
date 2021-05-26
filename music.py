import numpy as np
from midiutil.MidiFile import MIDIFile
import random
# create your MIDI object
mf = MIDIFile(1)     # only 1 track
track = 0   # the only track

time = 0    # start at the beginning
source = input("Enter file path and file name. Eg like C:/music/music1.mid \n ")
tempo = int(input("Enter bpm: \n"))
scale = int(input("Choose from the following modes \n 0.Ionian \n 1.Dorian \n 2.Phrygian \n 3.Lydian \n 4.Mixolydian \n 5.Aeolian \n 6.Locrian \n"))
intervals_plus = np.array([[2,2,1,2,2,2,1],
                      [2,1,2,2,2,1,2],
                      [1,2,2,2,1,2,2],
                      [2,2,2,1,2,2,1],
                      [2,2,1,2,2,1,2],
                      [2,1,2,2,1,2,2],
                      [1,2,2,1,2,2,2]
                       ])
intervals_minus = np.array([[1,2,2,1,2,2,2],
                      [2,2,1,2,2,2,1],
                      [2,1,2,2,2,1,2],
                      [1,2,2,2,1,2,2],
                      [2,2,2,1,2,2,1],
                      [2,2,1,2,2,1,2],
                      [2,1,2,2,1,2,2]
                       ])
position = np.array([[0, 2, 4, 5, 7, 9, 11], [0, 2, 3, 5, 7, 9, 10], [0, 1, 3, 5, 7, 8, 10], [0, 2, 4, 6, 7, 9, 11], [0, 2, 4, 5, 7, 9, 10], [0, 2, 3, 5, 7, 8, 10], [0, 1, 3, 5, 6, 8, 10]])

root_start = int(input("Choose root note \n 0.C \n 1.C# \n 2.D \n 3.D# \n 4.E \n 5.F \n 6.F# \n 7.G \n 8.G# \n 9.A \n 10.A# \n 11.B \n"))
root = 60+root_start
start_string = "F1F1F1"
def lsystem(start_string,sto):
    start = ""
    for i in range(len(start_string)):
        if(start_string[i] == "0" or start_string[i]=="1"):
            to_replace = start_string[i]
            prefix=""
            suffix=""
            for j in reversed(range(i)):
                if(start_string[j] == "0"):
                    prefix = "0"
                    break
                elif(start_string[j] == "1"):
                    prefix = "1"
                    break
            for j in range(i+1,len(start_string)):
                if (start_string[j] == "0"):
                    suffix = "0"
                    break
                elif (start_string[j] == "1"):
                    suffix = "1"
                    break
            #stochastic = random.randint(1,5)
            stochastic = sto
            if(stochastic==1):
                if(prefix=="0" and to_replace=="0"and suffix=="0"):
                    start = start + "0"
                if (prefix == "0" and to_replace == "0" and suffix == "1"):
                    start = start + "1[+F1F1]"
                if (prefix == "0" and to_replace == "1" and suffix == "0"):
                    start = start + "1"
                if (prefix == "0" and to_replace == "1" and suffix == "1"):
                    start = start + "1"
                if (prefix == "1" and to_replace == "0" and suffix == "0"):
                    start = start + "0"
                if (prefix == "1" and to_replace == "0" and suffix == "1"):
                    start = start + "1F1"
                if (prefix == "1" and to_replace == "1" and suffix == "0"):
                    start = start + "0"
                if (prefix == "1" and to_replace == "1" and suffix == "1"):
                    start = start + "0"
                if(prefix == "" or suffix == ""):
                    start = start + to_replace
            elif (stochastic == 2):
                if (prefix == "0" and to_replace == "0" and suffix == "0"):
                    start = start + "1"
                if (prefix == "0" and to_replace == "0" and suffix == "1"):
                    start = start + "1[-F1F1]"
                if (prefix == "0" and to_replace == "1" and suffix == "0"):
                    start = start + "1"
                if (prefix == "0" and to_replace == "1" and suffix == "1"):
                    start = start + "1"
                if (prefix == "1" and to_replace == "0" and suffix == "0"):
                    start = start + "0"
                if (prefix == "1" and to_replace == "0" and suffix == "1"):
                    start = start + "1F1"
                if (prefix == "1" and to_replace == "1" and suffix == "0"):
                    start = start + "1"
                if (prefix == "1" and to_replace == "1" and suffix == "1"):
                    start = start + "0"
                if(prefix == "" or suffix == ""):
                    start = start + to_replace
            elif (stochastic == 3):
                if (prefix == "0" and to_replace == "0" and suffix == "0"):
                    start = start + "0"
                if (prefix == "0" and to_replace == "0" and suffix == "1"):
                    start = start + "1"
                if (prefix == "0" and to_replace == "1" and suffix == "0"):
                    start = start + "0"
                if (prefix == "0" and to_replace == "1" and suffix == "1"):
                    start = start + "1[+F1F1]"
                if (prefix == "1" and to_replace == "0" and suffix == "0"):
                    start = start + "0"
                if (prefix == "1" and to_replace == "0" and suffix == "1"):
                    start = start + "1F1"
                if (prefix == "1" and to_replace == "1" and suffix == "0"):
                    start = start + "0"
                if (prefix == "1" and to_replace == "1" and suffix == "1"):
                    start = start + "0"
                if(prefix == "" or suffix == ""):
                    start = start + to_replace
            elif (stochastic == 4):
                if (prefix == "0" and to_replace == "0" and suffix == "0"):
                    start = start + "1"
                if (prefix == "0" and to_replace == "0" and suffix == "1"):
                    start = start + "0"
                if (prefix == "0" and to_replace == "1" and suffix == "0"):
                    start = start + "0"
                if (prefix == "0" and to_replace == "1" and suffix == "1"):
                    start = start + "1F1"
                if (prefix == "1" and to_replace == "0" and suffix == "0"):
                    start = start + "1"
                if (prefix == "1" and to_replace == "0" and suffix == "1"):
                    start = start + "1[+F1F1]"
                if (prefix == "1" and to_replace == "1" and suffix == "0"):
                    start = start + "1"
                if (prefix == "1" and to_replace == "1" and suffix == "1"):
                    start = start + "0"
                if(prefix == "" or suffix == ""):
                    start = start + to_replace
            elif (stochastic == 5):
                if (prefix == "0" and to_replace == "0" and suffix == "0"):
                    start = start + "0"
                if (prefix == "0" and to_replace == "0" and suffix == "1"):
                    start = start + "1[-F1F1]"
                if (prefix == "0" and to_replace == "1" and suffix == "0"):
                    start = start + "1"
                if (prefix == "0" and to_replace == "1" and suffix == "1"):
                    start = start + "1"
                if (prefix == "1" and to_replace == "0" and suffix == "0"):
                    start = start + "0"
                if (prefix == "1" and to_replace == "0" and suffix == "1"):
                    start = start + "1F1"
                if (prefix == "1" and to_replace == "1" and suffix == "0"):
                    start = start + "1"
                if (prefix == "1" and to_replace == "1" and suffix == "1"):
                    start = start + "0"
                if(prefix == "" or suffix == ""):
                    start = start + to_replace
        else:
            if(start_string[i]=="+"):
                start = start + "-"
            elif(start_string[i]=="-"):
                start = start + "+"
            else:
                start = start + start_string[i]
    return start
sto = random.randint(1,5)
for i in range(25):
    start_string = lsystem(start_string,sto)
    if(i%5==0):
        sto = random.randint(1, 5)

mf.addTrackName(track, time, "Sample Track")
mf.addTempo(track, time, tempo)

# add some notes
channel = 0
volume = 100

stack = [[]]
note = root
dur = 0
k = 0
time = 0
#print(start_string)
for i in range(len(start_string)):
    if(start_string[i] == "F"):
        dur = dur + 0.25
    elif(start_string[i] == "+"):
        note = note + intervals_plus[scale][k]
        k = (k+1)%7
    elif(start_string[i] == "-"):
        note = note - intervals_minus[scale][k]
        k = (k-1)%7
    elif(start_string[i] == "["):
        stack.append([note,dur])
        dur = 0
    elif(start_string[i] == "]"):
        popup = stack.pop()
        note = popup[0]
        dur = popup[1]
        position_calculate = (note-root)%12
        for loop in range(7):
            if(position[scale][loop] == position_calculate):
                k = loop

        mf.addNote(track, channel, note, time, dur, volume)
        #print(note)
        time = time + dur


# write it to disk
with open(source , 'wb') as outf:
    mf.writeFile(outf)
