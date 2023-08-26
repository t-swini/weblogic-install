#!/u01/app/oracle/may23/new_middleware/wls/oracle_common/common/bin/wlst.sh
import os, sys
readTemplate('/u01/app/oracle/may23/new_middleware/wls/wlserver/common/templates/wls/wls.jar')
cd('/Security/base_domain/User/weblogic')
cmo.setPassword('weblogic1')
cd('/Server/AdminServer')
setOption('ServerStartMode', 'prod')
cmo.setName('admin_teja')
cmo.setListenPort(7001)
cmo.setListenAddress('192.168.1.7')
writeDomain('/u01/app/oracle/may23/new_middleware/wls/user_projects/domains/jenkins_teja')
closeTemplate()
print '>>>Domain created successfully>>>'
exit()
