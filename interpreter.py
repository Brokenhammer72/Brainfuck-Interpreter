import sys

def interpret(content):
    global memory
    global closed
    global opened
    memory=[0]
    ptr=0
    counter = 0;
    closed=0
    opened=0
    while counter < len(content):
        if  content[counter] == '+':
            memory[ptr]+=1
        elif  content[counter]  == '-':
            memory[ptr]-=1
        elif content[counter]  == '>':
            if ptr == len(memory)-1:
                memory.append(0)
            ptr+=1
        elif content[counter] == '<' and not ptr==0:
            ptr-=1
        elif content[counter] == ',':
            memory[ptr] = input(' ')
        elif content[counter] == '.':
            print(chr(memory[ptr]),end="")
        elif content[counter] == '[':
            if memory[ptr]=='0':
                counter+=1
                while counter < len(content):
                    if opened==0 and content[counter]==']':
                        break
                    elif content[counter] == '[':
                        opened+=1
                    elif content[counter]==']':
                        opened-=1
        elif content[counter] == ']':
            if memory[ptr]!=0:
                counter-=1
                while counter > 0:
                    if closed==0 and content[counter]=='[':
                        break
                    elif content[counter] == ']':
                        closed+=1
                    elif content[counter]=='[':
                        closed-=1
                    counter-=1

        counter+=1
if(not len(sys.argv) == 2):
    print("enter a file name")
else:
    try:
        Source = open(sys.argv[1])
        interpret(Source.read())
        Source.close()
    except FileNotFoundError:
        print("cannot open File")
