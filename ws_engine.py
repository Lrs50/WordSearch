import random 
from datetime import datetime


def generateWS(table,words,n_words,setting,dim_x,dim_y):
    possible=True
    for i in range(n_words):
        #Validating the word position
        s=random.choice(setting)
        #print(f"{words[i]}  {s}")
        valid=False
        pos_x=0
        pos_y=0
        tam=len(words[i])
        attempt=0
        while not valid:
            t=True
            attempt+=1
            s=random.choice(setting)
            pos_x=random.randint(0,dim_x-1)
            pos_y=random.randint(0,dim_y-1)
            if attempt>1000 or possible==False:
                possible=False
                break
            if table[pos_y][pos_x]!=" ":
                continue
            if s==0:
                if pos_x+tam<=dim_x:
                    for j in range(tam):
                        if table[pos_y][pos_x+j]!=" " and table[pos_y][pos_x+j]!=words[i][j]:
                            t=False
                            break
                else:
                    t=False
            elif s==1:
                if pos_y+tam<=dim_y:
                    for j in range(tam):
                        if table[pos_y+j][pos_x]!=" " and table[pos_y+j][pos_x]!=words[i][j]:
                            t=False
                            break
                else:
                    t=False
            elif s==2:
                if pos_x+tam<=dim_x and pos_y+tam<=dim_y:
                    for j in range(tam):
                        if table[pos_y+j][pos_x+j]!=" " and table[pos_y+j][pos_x+j]!=words[i][j]:
                            t=False
                            break
                else:
                    t=False
            elif s==3:
                if pos_x-tam>=-1 and pos_y+tam<=dim_y:
                    for j in range (tam):
                        if table[pos_y+j][pos_x-j]!=" " and table[pos_y+j][pos_x-j]!=words[i][j]:
                            t=False
                            break
                else:
                    t=False
            if t==True:
                valid=True
        #Putting the word in the table
        if possible==True:
            if s==0:
                for j in range(tam):
                    table[pos_y][pos_x+j]=words[i][j]
            elif s==1:
                for j in range(tam):
                    table[pos_y+j][pos_x]=words[i][j]
            elif s==2:
                for j in range(tam):
                    table[pos_y+j][pos_x+j]=words[i][j]
            elif s==3:
                for j in range(tam):
                    table[pos_y+j][pos_x-j]=words[i][j]
        else:
            #print("the WordSearch is impossible!")
            table=[[" " for i in range(dim_x)]for j in  range(dim_y)]
            return -1,table
            break
    return 1,table


def ws_engine(dim_x,dim_y,words_entry,configs_):
    error=0
    configs=[0,0,0,0,0,0,0]
    for i in range(7):
        configs[i]=int(configs_[i].get())

    output=["",""]
    if dim_x*dim_y<len(words_entry):
        output[0]="Error0"
        error=-1
        return output,error
    #setting configs
    if configs[0]==0 and configs[1]==0 and configs[2]==0 and configs[3]==0:
        error=-1
        output[0]="Error1"
        return output,error
    random.seed(datetime.now())
    random_letters="QWERTYUIOPASDFGHJKLÇZXCVBNMqwertyuiopasdfghjklçzxcvbnm"
    setting=[]
    for i in range(4):
        if configs[i]==1:
            setting.append(i)

    if configs[5]==configs[6]:
        configs[5]=1
        configs[6]=0

    if configs[5]==1:
        words_entry=words_entry.upper()
    elif configs[6]==1:
        words_entry=words_entry.lower()


    words=words_entry.split(",")
    for word in words:
        if len(word)>dim_x and len(word)>dim_y:
            output[0]="Error2"
            error=-1
            return output,error
    
    n_words=len(words)
    if configs[4]==1:
        for i in range(n_words):
            random.seed(datetime.now())
            rev=random.randint(0,1)
            if rev==1:
                word_len=len(words[i])
                words[i]=words[i][word_len::-1]


    table=[[" " for i in range(dim_x)]for j in  range(dim_y)]

    valid=0
    for i in range(1000):
        j,table=generateWS(table,words,n_words,setting,dim_x,dim_y)
        if j==1:
            valid=1
            break
    if valid==0:
        output[0]="Error3"
        error=-1
        return output,error

    #printing the table
    for j in range(dim_y):
        for i in range(dim_x):
            if table[j][i]!=" ":
                output[1]+=table[j][i]+" "
            else:
                output[1]+="  "
        output[1]+="\n"

    for j in range(dim_y):
        for i in range(dim_x):
            if table[j][i]!=" ":
                output[0]+=table[j][i]+" "
            else:
                if configs[5]==1:
                    output[0]+=random_letters[random.randint(0,26)]+" "
                else:
                    output[0]+=random_letters[random.randint(27,53)]+" "
        output[0]+="\n"
    error=0
    return output,error



def main():

    dim_x=0
    dim_y=0
    words_entry="lOvE,lovi"
    configs=[1,1,1,1,0,1,0]
    output=ws_engine(dim_x,dim_y,words_entry,configs)
    print(output[0])
    print(output[1])

if __name__=="__main__":
    main()