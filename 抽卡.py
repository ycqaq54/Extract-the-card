import random
pool=[]
my_bag=[]
my_n=0
my_r=0
my_sr=0
my_ssr=0
n=0
r=0
sr=0
ssr=0
def Set_Up_CARDPOOL(card_pool,n_number,r_number,sr_number,ssr_number):
    for i in range(1,1+n_number):
        card_pool.append('n')
    for i in range(1,1+r_number):
        card_pool.append('r')
    for i in range(1,1+sr_number):
        card_pool.append('sr')
    for i in range(1,1+ssr_number):
        card_pool.append('ssr')
    random.shuffle(card_pool)
def Extract_Card(card_pool,bag):
    if card_pool:
        pop_card=random.choice(card_pool)
        popped_card=card_pool.pop()
        bag.append(popped_card)
        print('恭喜你抽中了一张'+popped_card)
    else:
        pass

Set_Up_CARDPOOL(pool,50000,2000,100,10)

while pool:
    extracr=input('a,单抽\nb,五连\nc,十连\nd,背包\ne,卡池\n')
    
    if extracr=='a':
        Extract_Card(pool,my_bag)
        
    if extracr=='b':
        for i in range(1,6):
            Extract_Card(pool,my_bag)
            
    if extracr=='c':
        for i in range(1,10):
            Extract_Card(pool,my_bag)
            
    if extracr=='d':
        for i in my_bag:
            if i=='n':
                my_n+=1
            if i=='r':
                my_r+=1
            if i=='sr':
                my_sr+=1
            if i=='ssr':
                my_ssr+=1
        print('你有'+str(my_n)+'张n\n'+'你有'+str(my_r)+'张r\n'+'你有'\
                      +str(my_sr)+'张sr\n'+'你有'+str(my_ssr)+'张ssr\n')
        my_n=0
        my_r=0
        my_sr=0
        my_ssr=0

    if extracr=='e':
                for i in pool:
                    if i=='n':
                        n+=1
                    if i=='r':
                        r+=1
                    if i=='sr':
                        sr+=1
                    if i=='ssr':
                        ssr+=1
                print('卡池有'+str(n)+'张n\n有'+str(r)+'张r\n有'+str(sr)+'张sr\n有'+str(ssr)+'张ssr\n')
                n=0
                r=0
                sr=0
                ssr=0


print('卡被你抽完了，你有'+str(my_n)+'张n\n'+'你有'+str(my_r)+'张r\n''你有'\
                      +str(my_sr)+'张sr\n''你有'+str(my_ssr)+'张ssr\n')
input()
