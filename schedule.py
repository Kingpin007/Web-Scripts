import MySQLdb as mdb
import vh
def read():
        db=mdb.connect(host="localhost", user="root", passwd="icui4cu", db="verlihub")
        cur=db.cursor()
        sql="SELECT * FROM dchub_tvschedule ORDER BY date ASC"
        cur.execute(sql)
        data=cur.fetchall()
        l=len(data)
        ret=""
        for i in range(0,l):
                curdate=data[i][1]
                date=""
                temp=curdate.split("-")
                date=temp[2]+"/"+temp[1]+"/"+temp[0]
                ret=ret+"<==========="+date+"===========>\n"
                for j in range(i,l):
                        if data[j][1]==curdate:
                                ret=ret+data[i][0]+"\n"
                        else:
                                break
                i=j
        return ret
def OnUserCommand(nick,data):
        if data=="+schedule":
                schedule=read()
                vh.usermc("\nSchedule sent via pm.")
                vh.pm(schedule,nick)
        return 0
def OnOperatorCommand(nick,data):
        if data=="+schedule":
                schedule=read()
                vh.usermc("\nSchedule sent via pm.")
                vh.pm(schedule,nick)
        return 0
