#THis program will check the appserver status on the server, then will present the appservers as choice to be either restarted, stopped or queried.
import os
list=os.popen("ver=102B . /usr/local/dlc/bin/dlcverset;nsman -i NS1 -port 20943 -q|awk '{print $2}'|grep -e AS -e WS").read()
listvar=[]
listvar=list.splitlines()
<<<<<<< HEAD
newlistvar=[x.split('.')[-1] for x in listvar]
#Added on 27Oct to list the appservers
for i,j in enumerate(newlistvar):
    print i,j
=======
print listvar[1]
for i, list in listvar[:]:
    appsvr[i]=list
    print appsrv[i]

printf "make the selection"
  printf [i] for appsr[i]
  exit 0
  exit 1
  exit 3
>>>>>>> origin/master
