#THis program will check the appserver status on the server, then will present the appservers as choice to be either restarted, stopped or queried.

ver=102B . /usr/local/dlc/bin/dlcverset;nsman -i NS1 -port 20943 -q | grep -e AS -e WS |awk '{print $2}'|sort | tr -s '\n' '\n' > listas.txt
for word in `cat listas.txt`;do word=${word:3};echo $word >> listgbpone.txt;done

list=os.popen("ver=102B . /usr/local/dlc/bin/dlcverset;nsman -i NS1 -port 20943 -q|awk '{print $2}'|grep -e AS -e WS").read()
listvar=[]
listvar=list.splitlines()
print listvar[1]
for i, list in listvar[:]:
    appsvr[i]=list
    print appsrv[i]

printf "make the selection"
  printf [i] for appsr[i]
  exit 0
