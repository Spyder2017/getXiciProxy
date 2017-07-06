#coding=utf-8
import MySQLdb

conn= MySQLdb.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='root',
    db='openioc'
    )
cur = conn.cursor()


sql = "insert into proxy (date,ip,port) values ('2017-07-06','192.168.0.1',3306)"

sqli = "select * from proxy where ip = '192.168.0.115'"

# cur.execute(sql)

test_ip = cur.execute(sqli)

# print cur.fetchmany(test_ip)

print test_ip

for row in cur.fetchmany(test_ip):
    print row[0],row[1],row[2]

# proxy_list = cur.fetchmany(proxy_num)
#
# for proxy_ifo in proxy_list:
#     print proxy_ifo
# 创建数据表
#cur.execute("create table student(id int ,name varchar(20),class varchar(30),age varchar(10))")

#插入一条数据
#cur.execute("insert into student values('2','Tom','3 year 2 class','9')")


#修改查询条件的数据
#cur.execute("update student set class='3 year 1 class' where name = 'Tom'")

#删除查询条件的数据
#cur.execute("delete from student where age='9'")

cur.close()
conn.commit()
conn.close()