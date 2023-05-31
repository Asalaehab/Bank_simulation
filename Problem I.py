import random
import numpy as np
from matplotlib import pyplot as plt

numberOfCustomerOrdinary=int(input("Enter the number of customer ordinary: "))
arrive_between_time_ordinary=[]
arrival_time_ordinary=[]
random_digits_ForArrival_ordiary=[]
service_time_ordinary=[]
service_start_ord=[]
service_end_ord=[]
service_wait_ord=[]
inSystem_ord=[]
Idle_ord=[]
index_ord=0
so=0
sd=0
for i in range(numberOfCustomerOrdinary):
    #For the customer ordianry
    #Genetra the random variable 
   r1=random.randint(1, 100)
   random_digits_ForArrival_ordiary.append(r1)
   #print(r1)
   if (r1 >= 1 and r1<= 9):
       arrive_between_time_ordinary.append(0)
   elif (r1 >=10 and r1<=26):
       arrive_between_time_ordinary.append(1)
   elif(r1>=27 and r1<=53):
       arrive_between_time_ordinary.append(2)
   elif(r1>=54 and r1<=73):
       arrive_between_time_ordinary.append(3)
   elif(r1>=74 and r1<=88):
        arrive_between_time_ordinary.append(4)
   elif(r1>=89 and r1<=100):
        arrive_between_time_ordinary.append(5)
  #Generate the arrival time
   if(i==0):
      arrival_time_ordinary.append(0)
   elif i==1:
       arrival_time_ordinary.append(arrive_between_time_ordinary[i])
   elif i>1:
       arrival_time_ordinary.append(arrival_time_ordinary[i-1]+arrive_between_time_ordinary[i])
   #Genarate service time
   if r1>=1 and r1<=20:
       service_time_ordinary.append(1)
   elif r1>=21 and r1<=60:
       service_time_ordinary.append(2)
   elif r1>=61 and r1<=88:
       service_time_ordinary.append(3)
   elif r1>=89 and r1<=100:
       service_time_ordinary.append(4)
   
#for the distingushed
#distingushed
numberOfCustomerdistingushed=int(input("Enter the number of customer distingushed: "))
arrive_between_time_distingush=[]
arrive_distingush=[]
random2=[]
service_time_dis=[]
service_start_dis=[]
service_end_dis=[]
service_wait_dis=[]
inSystem_dis=[]
Idle_dis=[]
index_Dis=0

for j in range(numberOfCustomerdistingushed):
   r2=random.randint(1, 100)
   random2.append(r2)
   if (r2>=1)and (r2<=10):
       arrive_between_time_distingush.append(1)
   elif r2>=11 and r2<=30:
      arrive_between_time_distingush.append(2)
   elif r2>=31 and r2<=60:
       arrive_between_time_distingush.append(3)
   elif r2>=61 and r2<=100:
       arrive_between_time_distingush.append(4)
    #arrive time for distingushed
   if j==0:
       arrive_distingush.append(0)
   elif j==1:
       arrive_distingush.append(arrive_between_time_distingush[j])
   else:
       arrive_distingush.append(arrive_distingush[j-1]+arrive_between_time_distingush[j])
    #service time destingushed:
   if r2>=1 and r2<=10:
       service_time_dis.append(1)
   elif r2>=11 and r2<=40:
       service_time_dis.append(2)
   elif r2>=40 and r2<=78:
       service_time_dis.append(3)
   elif r2>=79 and r2<=100:
      service_time_dis.append(4)
   
x=max(numberOfCustomerdistingushed, numberOfCustomerOrdinary)
dis=True
ordi=True
turn=True
turn_ord=True
while True:
    if(turn_ord==False and turn==False):
        so=service_end_ord[numberOfCustomerOrdinary-1]
        sd=service_end_dis[numberOfCustomerdistingushed-1]
        break
    
    if(index_Dis==0):
        service_start_dis.append(0)
        service_end_dis.append(service_time_dis[index_Dis]+service_start_dis[index_Dis])
        service_wait_dis.append(0)
        inSystem_dis.append(service_end_dis[index_Dis]-arrive_distingush[index_Dis])
        Idle_dis.append(0)
        index_Dis+=1
        continue
    #*********#
    elif(index_Dis>=1):
        while (turn):
           if(arrive_distingush[index_Dis]<=service_end_dis[index_Dis-1] and ordi==True and dis==True):
               service_start_dis.append(service_end_dis[index_Dis-1])#will equal to the the end time
               service_end_dis.append(service_time_dis[index_Dis]+service_start_dis[index_Dis])#serviceEnd=serviceTime+serviceStart
               service_wait_dis.append(service_start_dis[index_Dis]-arrive_distingush[index_Dis])#service start time-service arrival time
               inSystem_dis.append(service_end_dis[index_Dis]-service_start_dis[index_Dis])##service end-service start
               Idle_dis.append(service_start_dis[index_Dis]-service_end_dis[index_Dis-1])
               index_Dis+=1
               if(index_Dis==numberOfCustomerdistingushed):
                   dis=False
                   #index_Dis-=1
                   turn=False
                   break
            #***********#
           elif(ordi==False and service_end_ord[index_ord-1]>=arrive_distingush[index_Dis]):
               service_start_dis.append(service_end_ord[index_ord-1])
               service_end_dis.append(service_time_dis[index_Dis]+service_start_dis[index_Dis])
               service_wait_dis.append(service_start_dis[index_Dis]-arrive_distingush[index_Dis])
               inSystem_dis.append(service_end_dis[index_Dis]-service_start_dis[index_Dis])
               Idle_dis.append(service_start_dis[index_Dis]-service_end_ord[index_ord-1])
               index_Dis+=1
               ordi=True  
               dis=True
               if(index_Dis==numberOfCustomerdistingushed):
                   dis=False
                 #  index_Dis-=1
                   turn=False
                   break
               continue
           # ************#
           else:#arrive is greater than end time
               dis=False
               break
        #*********#
        if(turn!=False):
            if(arrive_distingush[index_Dis]>arrival_time_ordinary[index_ord]and dis==False and ordi==True ):
                #will enter the ordinary  
                        service_start_ord.append(service_end_dis[index_Dis-1])#will equal the end time for the privous index dis
                        service_end_ord.append(service_time_ordinary[index_ord]+service_start_ord[index_ord])
                        service_wait_ord.append(service_start_ord[index_ord]-arrival_time_ordinary[index_ord])
                        inSystem_ord.append(service_end_ord[index_ord]-service_start_ord[index_ord])
                        Idle_ord.append(service_start_ord[index_ord]-service_end_dis[index_Dis-1])
                        index_ord+=1
                        if (service_end_ord[index_ord-1]>=arrive_distingush[index_Dis] and turn!=False):
                            ordi=False
                            continue
                        #**********************#
                        elif(arrival_time_ordinary[index_ord-1]<arrive_distingush[index_Dis] and turn!=False):
                            #exisit in ordiary
                            while(True):
                                if(arrival_time_ordinary[index_ord]<=service_end_ord[index_ord-1]):
                                    service_start_ord.append(service_end_ord[index_ord-1])
                                else:
                                    service_start_ord.append(arrival_time_ordinary[index_ord])
                                service_end_ord.append(service_start_ord[index_ord]+service_time_ordinary[index_ord])
                                service_wait_ord.append(service_start_ord[index_ord]-arrival_time_ordinary[index_ord])
                                inSystem_ord.append(service_end_ord[index_ord]-service_start_ord[index_ord])
                                Idle_ord.append(service_start_ord[index_ord]-service_end_ord[index_ord-1])
                                index_ord+=1
                                if (service_end_ord[index_ord-1]>=arrive_distingush[index_Dis] and turn!=False):
                                    ordi=False
                                    break
                                if(index_ord==numberOfCustomerOrdinary):break
                                #***************/#                            
        elif(turn==False):
            service_start_ord.append(service_end_dis[index_Dis-1])#will equal the end time for the privous index dis
            service_end_ord.append(service_time_ordinary[index_ord]+service_start_ord[index_ord])
            service_wait_ord.append(service_start_ord[index_ord]-arrival_time_ordinary[index_ord])
            inSystem_ord.append(service_end_ord[index_ord]-service_start_ord[index_ord])
            Idle_ord.append(service_start_ord[index_ord]-service_end_dis[index_Dis-1])
            index_ord+=1
            while(turn_ord): #so our disngued was end and it still ordinary customer
                    if(index_ord==numberOfCustomerOrdinary):
                        turn_ord=False
                        break
                    #********#
                    #31
                    if(arrival_time_ordinary[index_ord]<=service_end_ord[index_ord-1]):
                        service_start_ord.append(service_end_ord[index_ord-1])
                    else:
                        service_start_ord.append(arrival_time_ordinary[index_ord])
                    service_end_ord.append(service_start_ord[index_ord]+service_time_ordinary[index_ord])
                    service_wait_ord.append(service_start_ord[index_ord]-arrival_time_ordinary[index_ord])
                    inSystem_ord.append(service_end_ord[index_ord]-service_start_ord[index_ord])
                    Idle_ord.append(service_start_ord[index_ord]-service_end_ord[index_ord-1])
                    index_ord+=1
                    if(index_ord==numberOfCustomerOrdinary):
                        turn_ord=False
                        break
                                
                        
                        
#end of algorithm
#**********#
#cleander*****before edit
print("******ordinary cleander******")
print("\n \n")
for i in range(numberOfCustomerOrdinary):
    if i==0:
        print(
      "customer",i+1," ",
      "arrive time between : - ",     
      "arrive time: ",arrival_time_ordinary[i],"  ",
      "service time: ",service_time_ordinary[i]," ",
      "service time start: ",service_start_ord[i]," ",
      "service time end: ",service_end_ord[i]," ",
      "waiting: ",service_wait_ord[i]," ",
      "in system: ",inSystem_ord[i]," ",
      "idle: ", Idle_ord[i]
    )

    else:
      print(
    "customer",i+1," ",
    "arrive time between :",arrive_between_time_ordinary[i],     
    "arrive time: ",arrival_time_ordinary[i],"  ",
    "service time: ",service_time_ordinary[i]," ",
    "service time start: ",service_start_ord[i]," ",
    "service time end: ",service_end_ord[i]," ",
    "waiting: ",service_wait_ord[i]," ",
    "in system: ",inSystem_ord[i]," ",
    "idle: ", Idle_ord[i]
  )
      

#******************#
print("******distingushed cleander******")
print("\n \n")
for i in range(numberOfCustomerdistingushed):
    if i==0:
        print(
              "customer: ",i+1," ",
              "Arrive between: --"," ",
              "arrive time: ",arrive_distingush[i]," ",
              "service time: ",service_time_dis[i]," ",
              "begin time :",service_start_dis[i]," ",
              "end time : ",service_end_dis[i]," ",
              "waiting : ",service_wait_dis[i]," ",
              "in system : ",inSystem_dis[i]," ",
              "idle : ",Idle_dis[i]
              )
    else:
        print(
              "customer: ",i+1," ",
              "arrive between: ",arrive_between_time_distingush[i]," ",
              "arrive time: ",arrive_distingush[i]," ",
              "service time: ",service_time_dis[i]," ",
              "begin time :",service_start_dis[i]," ",
              "end time : ",service_end_dis[i]," ",
              "waiting : ",service_wait_dis[i]," ",
              "in system : ",inSystem_dis[i]," ",
              "idle : ",Idle_dis[i]
              )






average_service_time=0
average_service_time_ord=0
average_service_time_dis=0
average_wait_dis=0
average_wait_ord=0
wait_or=0
wait_di=0
aver_ord=0
aver_dis=0
prob_dis=0
prob_ord=0
inter_ord_avg=0
inter_dis_avg=0
average_service_time=((sum(service_time_ordinary))+(sum(service_time_dis)))/(numberOfCustomerOrdinary+numberOfCustomerdistingushed)
average_service_time_ord=np.mean(service_time_ordinary)
average_service_time_dis=np.mean(service_time_dis)
average_wait_dis=np.mean(service_wait_dis)
average_wait_ord=np.mean(service_wait_ord)
#*************#
for y in range(numberOfCustomerOrdinary):
    if (service_wait_ord[y] >0):
        wait_or+=1

for z in range(numberOfCustomerdistingushed):
    if (service_wait_dis[z] > 0):
        wait_di+=1

               
#*********#
prob_ord=wait_or/(numberOfCustomerOrdinary)
prob_dis=wait_di/(numberOfCustomerdistingushed)
print("\n")
#*************#

print("the average service time distingushed: ",average_service_time_dis)  
if(average_service_time_dis>=2 and average_service_time_dis<=3 ):
    print("it Approximately match the theoritcal distingushed service time ")
else:   
    print("it doesnot match the theoritcal distingushed service time")

print("\n")
print("the average service time for ordinary :",average_service_time_ord)
if (average_service_time_ord>=2  and average_service_time_ord<=3):
    print("and theoretical average service time of the service time distribution Approximately match the experimental ordinary ")
else:
    print("it doesnot match with the  theoretical average service")
print("\n")
#*************#

print("average time wait for ordinary: ",average_wait_ord)
print("average time wait for distingued: ",average_wait_dis)
print("\n")

print("the maximum wait for ordinary",wait_or)
print("the maximum wait for distingushed: ",wait_di)
print("\n")  
                  
print("probability for waiting for ordinary: ",prob_ord)
print("probability for waiting for distingushed:",prob_dis)
print("\n")

#propotion
po=0
pd=0
po=sum(Idle_ord)/so
pd=sum(Idle_dis)/sd

print("the portion for ordinary: ",po)
print("the portion for distinguished: ",pd)
print("\n")

#***************#

inter_dis_avg=np.mean(arrive_between_time_distingush)
inter_ord_avg=np.mean(arrive_between_time_ordinary)
if(inter_ord_avg>=2 and inter_ord_avg<=3):
    print("the inter arrive ordinary time does  Approximately match because it is",inter_ord_avg)
else:
    print("the inter arrive ordinary time does not  match because it is",inter_ord_avg)
    
if(inter_dis_avg>=2 and inter_dis_avg<=3):
    print("the inter arrive distinguished time does Approximately  match because it is",inter_dis_avg)
else:
    print("the inter arrive distinguished time does not  match because it is",inter_dis_avg) 
print("\n")

#*******************#


#*Two teller*******#
#************#   
#distinguished
begin_dis=[]
end_dis=[]
wait_dis=[]
system_dis=[]
idle_d=[]
D=0
while (D<numberOfCustomerdistingushed):
    if D==0:
        begin_dis.append(0)
        end_dis.append(service_time_dis[D]+begin_dis[D])
        wait_dis.append(begin_dis[D]-0)
        system_dis.append(end_dis[D]-begin_dis[D])
        idle_d.append(0)
    elif D>=1:
        if(end_dis[D-1]<=arrive_distingush[D]):
            begin_dis.append(arrive_distingush[D])
        else:
            begin_dis.append(end_dis[D-1])
        end_dis.append(service_time_dis[D]+begin_dis[D])
        wait_dis.append(begin_dis[D]-arrive_distingush[D])
        system_dis.append(end_dis[D]-begin_dis[D])
        idle_d.append(abs(begin_dis[D]-end_dis[D-1]))
    D+=1
        
    
#*************#
#ordinary
begin_ord=[]
end_ord=[]
wait_ord=[]
system_ord=[]
index=0
idle_o=[]
while  index<numberOfCustomerOrdinary:
    if index==0:
        begin_ord.append(0)
        end_ord.append(begin_ord[index]+service_time_ordinary[index])
        wait_ord.append(0)
        system_ord.append(end_ord[index]-begin_ord[index])
        idle_o.append(0)
    elif index>=1:
        if(arrival_time_ordinary[index]>=end_ord[index-1]):
            begin_ord.append(arrival_time_ordinary[index])
        else:
            begin_ord.append(end_ord[index-1])
        end_ord.append(begin_ord[index]+service_time_ordinary[index])
        wait_ord.append(begin_ord[index]-arrival_time_ordinary[index])
        system_ord.append(end_ord[index]-begin_ord[index])
        idle_o.append(abs(begin_ord[index]-end_ord[index-1]))
    index+=1    

print("*************")
print("we add the teller two the system")     
#****************

print("\n")
print("*****teller distingushed***** ")
print("\n \n")
for i in range (numberOfCustomerdistingushed):
    if i==0:
        print(
              "customer : ",i+1," ",
              "arrive between: --",
              "arrive time: ",arrive_distingush[i]," ",
              "service time:",service_time_dis[i]," ",
              "begin_time: ",begin_dis[i]," ",
              "end_time:",end_dis[i]," ",
              "waiting :",wait_dis[i]," ",
              "in system:",system_dis[i]," ",
              "idle",idle_d[i]," ",
               )
    else:
        print(
             " customer : ",i+1," ",
              "arrive between: ",arrive_between_time_distingush[i]," ",
              "arrive time: ",arrive_distingush[i]," ",
              "service time:",service_time_dis[i]," ",
              "begin_time: ",begin_dis[i]," ",
              "end_time:",end_dis[i]," ",
              "waiting :",wait_dis[i]," ",
              "in system:",system_dis[i]," ",
              "idle",idle_d[i]," ",
               
              )

print("\n")
print("*****teller ordinary***** ")
print("\n \n")
for i in range (numberOfCustomerOrdinary):
    if i==0:
        print(
              " customer : ",i+1," ",
              "arrive between: --"," ",
              "arrive time: ",arrival_time_ordinary[i],
              "service time:",service_time_ordinary[i]," ",
              "begin_time: ",begin_ord[i]," ",
              "end_time:",end_ord[i]," ",
              "waiting :",wait_ord[i]," ",
              "in system:",system_ord[i]," ",
              "idle",idle_o[i],
              )
    else:
        print(           
              " customer : ",i+1," ",
              "arrive between: ",arrive_between_time_ordinary[i]," ",
              "arrive time: ",arrival_time_ordinary[i]," ",
              "service time:",service_time_ordinary[i]," ",
              "begin_time: ",begin_ord[i]," ",
              "end_time:",end_ord[i]," ",
              "waiting :",wait_ord[i]," ",
              "in system:",system_ord[i]," ",
              "idle",idle_o[i],
              )
              
print("\n \n")
print("and the new update is:")         
average_service_time=0
average_service_time_ord=0
average_service_time_dis=0
average_wait_dis=0
average_wait_ord=0
wait_or=0
wait_di=0
aver_ord=0
aver_dis=0
prob_dis=0
prob_ord=0
inter_ord_avg=0
inter_dis_avg=0
                   
#******************
average_wait_dis=np.mean(wait_dis)
average_wait_ord=np.mean(wait_ord)
#******************
for y in range(numberOfCustomerOrdinary):
    if (wait_ord[y] >0):
        wait_or+=1

for z in range(numberOfCustomerdistingushed):
    if (wait_dis[z] > 0):
        wait_di+=1

               
#*********#
prob_ord=wait_or/(numberOfCustomerOrdinary)
prob_dis=wait_di/(numberOfCustomerdistingushed)      
                   
print("\n")
#*************#

print("average time wait for ordinary: ",average_wait_ord)
print("average time wait for distingued: ",average_wait_dis)
print("\n")

print("the maximum wait for ordinary",wait_or)
print("the maximum wait for distingushed: ",wait_di)
print("\n")  
                  
print("probability for waiting for ordinary: ",prob_ord)
print("probability for waiting for distingushed:",prob_dis)
print("\n")

#***************#    
print("So we fix the average wait for the ordinary and it better with two teller")

print("histogram before update")


print("the wait for ordinary customer ")
plt.hist(service_wait_ord,bins=10)
plt.show()

print("the wait for distingushed customer ")
plt.hist(service_wait_dis,bins=10)
plt.show()


print("histogram after edit:")

print("the wait for ordinary customer ")
plt.hist(wait_ord, bins=10)
plt.show()


print("the wait for distingushed customer ")
plt.hist(wait_dis, bins=10)
plt.show()