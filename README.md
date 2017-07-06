# getXiciProxy
1. 通过urllib2和lxml获取西刺代理，并保存在MySQL中
2. 代理失效检测，如果代理失效，则从数据库中删除
3. 代理重复检测，如果获取的代理重复，则不写入数据库

### 运行环境
 * Ubuntu 14.04
 * Python 2.7
 * MySQL 5.5.55
