MIDDLEWARE=/u01/app/oracle/may23/new_middlware
tar -zxvf  $MIDDLEWARE/jdk-8u191-linux-x64.tar.gz -C $MIDDLEWARE
mv $MIDDLEWARE/jdk1.8.0_191 $MIDDLEWARE/jdk
export JAVA_HOME=/u01/app/oracle/may23/new_middlware/jdk
$JAVA_HOME/bin/java -jar  $MIDDLEWARE/fmw_12.2.1.2.0_wls.jar  -silent -responseFile $PWD/weblogic-install/resposnse.rsp
$PWD/weblogic-install/domain.py
