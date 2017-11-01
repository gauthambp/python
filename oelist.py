#!/usr/bin/python

#THis program will check the appserver status on the server, then will present the appservers as choice to be either restarted, stopped or queried.
import os
list=os.popen("ver=102B . /usr/local/dlc/bin/dlcverset;nsman -i NS1 -port 20943 -q|awk '{print $2}'|grep -e AS -e WS").read()
listvar=[]
listvar=list.splitlines()

newlistvar=[x.split('.')[-1] for x in listvar]
#Added on 27Oct to list the appservers
print "The following appservers are seen on the server"
for i,j in enumerate(newlistvar):
    print i,j
    k[i]=j
#Next step is to run the command based on selections
print "Select the appserver to be used"
#The appserver needs to be stopped started or queired"
i = input("select the appserver")
myoutput=os.popen("ver=102B . /usr/local/dlc/bin/dlcverset;nsman -i $k[i] -port 20943 -q).read()
print myoutput

#The appserver needs to be stopped started or queired"
i = input("select the appserver")
myname=k[i]
print myname
print "%s" % myname
myoutput=os.popen("ver=102B . /usr/local/dlc/bin/dlcverset;nsman -i" + ' ' + myname + "-port 2094
3 -q").read()
print myoutput

#dummy comment

#dummy comment
