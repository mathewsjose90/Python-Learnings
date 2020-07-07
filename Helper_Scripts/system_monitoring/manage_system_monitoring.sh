#!/bin/sh
#Author : Mathews Jose
#Date   : 03/12/2018
#Use    : To capture sytem utilization parameters for the systems mentioned in hosts.txt

if [ $# -lt 1 ]
then
	echo "Usage is : `basename $0` start/stop [report_folder_name]"
	exit 1
fi

if [ ! -f hosts.txt ]
then
	echo "Please create the file hosts.txt with the remote ip addresses to monitor"
	exit 1
fi

action=$1
result_dir=reports/${2:-`date '+%d%m%Y%H%M'`}
remote_monitoring_base_dir="$HOME/system_monitoring/"
collectl_package="collectl-4.3.1.src.tar.gz"

if [[ $action == start ]]
then
	echo "starting the monitoring"
	parallel-ssh -h hosts.txt -l root -o ./ssh_out/ -t 600 "mkdir -p ${remote_monitoring_base_dir}; rm -rf ${remote_monitoring_base_dir}/*.sh; rm -rf ${remote_monitoring_base_dir}/*.gz ;rm -rf ${remote_monitoring_base_dir}/col* ; rm -rf ${remote_monitoring_base_dir}/gnu* ;rm -rf ${remote_monitoring_base_dir}/reports/; rm -f ${remote_monitoring_base_dir}/*.log"
	parallel-scp -h hosts.txt -o ./ssh_out/ -l root monitor_system.sh ${remote_monitoring_base_dir}.
	parallel-scp -h hosts.txt -o ./ssh_out/ -l root ${collectl_package} ${remote_monitoring_base_dir}.
	parallel-scp -h hosts.txt -o ./ssh_out/ -l root start_command ${remote_monitoring_base_dir}.
	parallel-scp -h hosts.txt -o ./ssh_out/ -l root stop_command ${remote_monitoring_base_dir}.
	#parallel-ssh -h hosts.txt -l root -o ./ssh_out/ -t 600 "cd ${remote_monitoring_base_dir} ; nohup sh ${remote_monitoring_base_dir}monitor_system.sh &"
	parallel-ssh -h hosts.txt -l root -o ./ssh_out/ -t 600 "cd ${remote_monitoring_base_dir};setsid sh start_command &"
	
elif [[ $action == stop ]]
then
	echo "stopping the monitoring"
	parallel-ssh -h hosts.txt -l root -o ./ssh_out/ -t 60 "/etc/init.d/collectl stop"
	parallel-ssh -h hosts.txt -l root -o ./ssh_out/ -t 60 "cd ${remote_monitoring_base_dir};sh stop_command "
	rm -rf ${result_dir}
	mkdir -p ${result_dir}
	#Wait till results are processed in the target machines
	echo "Sleeping for 60 secs for the results to get processed in the target machines"
	sleep 60
	echo "Starting the download of result files(if any)"
	while read ip
	do
		scp -r root@${ip}:/var/log/collectl/ ${result_dir}/
	done < hosts.txt
fi

