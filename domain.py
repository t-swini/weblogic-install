#!/u01/app/oracle/may23/new_middlware/wls/oracle_common/common/bin/wlst.sh
import os, sys
readTemplate('/u01/app/oracle/may23/new_middlware/wls/wlserver/common/templates/wls/wls.jar')
cd('/Security/base_domain/User/weblogic')
cmo.setPassword('weblogic1')
cd('/Server/AdminServer')
setOption('ServerStartMode', 'prod')
cmo.setName('admin_test')
cmo.setListenPort(7001)
cmo.setListenAddress('192.168.0.152')
writeDomain('/u01/app/oracle/may23/new_middlware/wls/user_projects/domains/jenkins_test')
closeTemplate()
print '>>>Domain created successfully>>>'
exit()
