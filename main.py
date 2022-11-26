from collections import defaultdict
import streamlit as st
import pandas as pd
import numpy as np


memory = defaultdict(list)
tags = defaultdict(int)
registers = {
    "zero" : 0,
    "ra" : 0,
    "sp" : 0, 
    "gp" : 0, 
    "tp" : 0,
    "t0" : 0,
    "t1" : 0, 
    "t2" : 0,
    "s0" : 0,
    "s1" : 0, 
    "a0" : 0,
    "a1" : 0,
    "a2" : 0,
    "a3" : 0, 
    "a4" : 0,
    "a5" : 0,
    "a6" : 0,
    "a7" : 0, 
    "s2" : 0,
    "s3" : 0,
    "s4" : 0,
    "s5" : 0, 
    "s6" : 0,
    "s7" : 0,
    "s8" : 0,
    "s9" : 0, 
    "s10" : 0,
    "s11" : 0,
    "t3" : 0,
    "t4" : 0, 
    "t5" : 0,
    "t6": 0
}
def add(dest, s1, s2): 
    registers[dest] = registers[s1] + registers[s2]

def addi(dest, s1, val): 
    registers[dest] = registers[s1] + int(val)

def sub(dest, s1, s2): 
    registers[dest] = registers[s1] - registers[s2]

def mv(dest, s1): 
    registers[dest] = registers[s1]

def slli(dest, s1, s2): 
    registers[dest] = registers[s1]*pow(2, int(s2) )

def srli(dest, s1, s2):
    registers[dest] = int(registers[s1]/pow(2, int(s2) ))

def sll(dest, s1, s2): 
    registers[dest] = registers[s1]*pow(2, registers[s2] )

def srl(dest, s1, s2):
    registers[dest] = int(registers[s1]/pow(2, registers[s2] ))


def li(dest, val): 
    if val in registers.keys() or val in memory.keys(): 
        print("error")
    else: 
        registers[dest] = int(val)

def sd(val, to): 
    regfind = to.split('(')
    
    if(int(regfind[0])>32 or int(regfind[0])<0):
        print("error mem location not found")
    else:
        reg = regfind[1].replace(')', '')
        if reg in registers.keys(): 
            memory[to].append(registers[val])

def ld(to ,From): 
    regfind = From.split('(')
    
    if(int(regfind[0])>32 or int(regfind[0])<0):
        print("error mem location not found")
    else:
        reg = regfind[1].replace(')', '')
        if reg in registers.keys(): 
            registers[to] = memory[From]

def AND(dest, s1, s2): 
    s1 = format(registers[s1],'b')
    s2 = format(registers[s2],'b')
    len1 = len(s1)
    len2 = len(s2)
    res = ''
    if len1>len2: 
        s2 = s2.rjust(len1, '0')
    else:  
        s2 = s2.rjust(len1, '0')

    for i in range(max(s1, s2)): 
        if(s1[i]=='1'and s2[i]=='1'): 
            res += '1'
        else: 
            res +='0'
    registers[dest]= int(res, 2)


def OR(dest, s1, s2): 
    s1 = format(registers[s1],'b')
    s2 = format(registers[s2],'b')
    len1 = len(s1)
    len2 = len(s2)
    res = ''
    if len1>len2: 
        s2 = s2.rjust(len1, '0')
    else:  
        s2 = s2.rjust(len1, '0')

    for i in range(max(s1, s2)): 
        if(s1[i]=='1'or s2[i]=='1'): 
            res += '1'
        else: 
            res +='0'
    registers[dest]= int(res, 2)

def XOR(dest, s1, s2): 
    s1 = format(registers[s1],'b')
    s2 = format(registers[s2],'b')
    len1 = len(s1)
    len2 = len(s2)
    res = ''
    if len1>len2: 
        s2 = s2.rjust(len1, '0')
    else:  
        s2 = s2.rjust(len1, '0')

    for i in range(max(s1, s2)): 
        if((s1[i]=='1'and s2[i]=='0')or(s1[i]=='0'and s2[i]=='1')): 
            res += '1'
        else: 
            res +='0'
    registers[dest]= int(res, 2)

def XORI(dest, s1, s2): 
    s1 = format(registers[s1],'b')
    s2 = format(s2,'b')
    len1 = len(s1)
    len2 = len(s2)
    res = ''
    if len1>len2: 
        s2 = s2.rjust(len1, '0')
    else:  
        s2 = s2.rjust(len1, '0')

    for i in range(max(s1, s2)): 
        if((s1[i]=='1'and s2[i]=='0')or(s1[i]=='0'and s2[i]=='1')): 
            res += '1'
        else: 
            res +='0'
    registers[dest]= int(res, 2)

def ANDI(dest, s1, s2): 
    s1 = format(registers[s1],'b')
    s2 = format(s2,'b')
    len1 = len(s1)
    len2 = len(s2)
    res = ''
    if len1>len2: 
        s2 = s2.rjust(len1, '0')
    else:  
        s2 = s2.rjust(len1, '0')

    for i in range(max(s1, s2)): 
        if(s1[i]=='1'and s2[i]=='1'): 
            res += '1'
        else: 
            res +='0'
    registers[dest]= int(res, 2)

def beq(s1, s2, tag, i): 
    if(registers[s1] == registers[s2]):
        if tag in tags.keys(): 
            return (i -tags[tag])
        else: 
            return (i- int(tag, 0))
    
    else: 
        return 0

def bne(s1, s2, tag, i): 
    if(registers[s1] != registers[s2]):
        if tag in tags.keys(): 
            return (i- tags[tag])
        else: 
            return (i- int(tag, 0))
    
    else: 
        return 0

def blt(s1, s2, tag, i): 
    if(registers[s1] < registers[s2]):
        if tag in tags.keys(): 
            return (tags[tag]-i)
        else: 
            return (int(tag, 0)-i)
    
    else: 
        return 0

def bltu(s1, s2, tag, i): 
    if(registers[s1]< s2):
        if tag in tags.keys(): 
            return (tags[tag]-i)
        else: 
            return (int(tag, 0)-i)
    
    else: 
        return 0

def bge(s1, s2, tag, i): 
    if(registers[s1] >= registers[s2]):
        if tag in tags.keys(): 
            return (tags[tag]-i)
        else: 
            return (int(tag, 0)-i)
    
    else: 
        return 0

def bgeu(s1, s2, tag, i): 
    if(registers[s1] >= s2):
        if tag in tags.keys(): 
            return (tags[tag]-i)
        else: 
            return (int(tag, 0)-i)
    
    else: 
        return 0


def ORI(dest, s1, s2): 
    s1 = format(registers[s1],'b')
    s2 = format(s2,'b')
    len1 = len(s1)
    len2 = len(s2)
    res = ''
    if len1>len2: 
        s2 = s2.rjust(len1, '0')
    else:  
        s2 = s2.rjust(len1, '0')

    for i in range(max(s1, s2)): 
        if(s1[i]=='1'or s2[i]=='1'): 
            res += '1'
        else: 
            res +='0'
    registers[dest]= int(res, 2)

func_keys = {
    'add': add,
    'addi': addi,
    'sub': sub, 
    'mv' : mv,
    'sd': sd,
    'ld':ld, 
    'slli':slli,
    'srli':srli,
    'li': li, 
    
    'and':AND, 
    'or':OR,
    'xor':XOR,
    'andi':ANDI,
    'ori':ORI,
    'srl':srl,
    'sll':sll,
    'xori':XORI

}

branches = {
    'beq' : beq,
    'blt' : blt,
    'bltu' : bltu,
    'bge' : bge,
    'bgeu' : bgeu,
    'bne' : bne
}
st.title("RISC V ASSEMBLY ONLINE")
with st.form("RISC V", clear_on_submit=False):
    lines= st.text_area('Enter Assembly Code Here',  height=350)
    submit = st.form_submit_button("RUN")

lines = lines.split('\n')

def run():
    
    i = 0
    while ( i < (len(lines))): 
        
        line =lines[i]
        txt = line.replace(',', ' ')
        txt = txt.replace(':', '')
        prompt = txt.split()
        cmd = []
        print(line)
        for st in prompt: 
            if st.isupper(): 
                if st not in tags.keys():
                    tags[st] = i
 
                else:
                    cmd.append(st)

            else : 
                cmd.append(st)
        if len(cmd) > 1 : 
            if cmd[0] in branches.keys(): 
                print(tags)
                tmp = i
                
                i += branches[cmd[0]](cmd[1],cmd[2],cmd[3],tmp)
                print(branches[cmd[0]](cmd[1],cmd[2],cmd[3],tmp))
                print(i)
                
            
            else:
                if len(cmd) ==4 : 
                    
                    func_keys[cmd[0]](cmd[1],cmd[2],cmd[3])
                elif len(cmd) ==3 : 
                    func_keys[cmd[0]](cmd[1],cmd[2])
                else: 
                    func_keys[cmd[0]](cmd[1])
        else: 
            pass
        i += 1



def conv():
    hx = []
    bn=  []
    for val in registers.values(): 
        bn.append(bin(val))
        hx.append(hex(val))

    dfv = pd.DataFrame(data=np.column_stack((bn,hx)),columns=['Binary','Hexadecimal'])
    return dfv



                    
with st.form("Resgisters", clear_on_submit=False):
    run()
   
    
    df = pd.DataFrame([registers])
    df = df.T
    df.columns = ['Decimal']
    dfv =  conv()
    
    dfv.index = df.index
    df = pd.concat([df, dfv], axis=1)
    print(df)
    st.write(df)
    submit = st.form_submit_button("update") 
