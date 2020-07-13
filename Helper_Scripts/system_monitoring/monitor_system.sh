#!/bin/bash
#Author : Mathews Jose
#Date   : 29/12/2018
#Detail : To perform system monitoring using collectl utility

base_path="$HOME/system_monitoring"
time_stamp=`date  '+%d%m%Y%H%M%S'`
log_file="${base_path}/system_monitoring_${time_stamp}.log"
collectl_package="${base_path}/collectl-4.3.1.src.tar.gz"
pid_file="${base_path}/monitor_system_run.pid"

log_info()
{
	echo "`date` : INFO : $1" >> ${log_file}

}

stop_monitoring()
{
	log_info "stopping the monitoring"
	/etc/init.d/collectl stop
	log_info "---------------STOP---------------"
	rm -f ${pid_file}
	exit 0
}

trap stop_monitoring 1 2 3 6 14 15


start_monitoring()
{
	log_info "---------------START---------------"
	cd ${base_path}
	echo "$$" > ${pid_file}

	if [ -f /etc/init.d/collectl ]
	then
		log_info "collectl is already present in the system."
	else
		log_info "collectl is not present in the system already. Installing the same"
		if [ -f ${collectl_package} ]
		then
			tar -zxf ${collectl_package} 
			collectl_dir=`basename -s ".src.tar.gz" "${collectl_package}"`
			chown -R root:root ${base_path} ; chmod -R 755 ${base_path}
			cd ${base_path}/${collectl_dir}
			log_info "CWD:`pwd` and install command is ${base_path}/${collectl_dir}/INSTALL"
			${base_path}/${collectl_dir}/INSTALL
		else
			log_info "${collectl_package} is not present .Can not continue with monitoring"
			exit 1
		fi
	fi
	
	if [ ! -f /etc/init.d/collectl ]
	then
		log_info "collectl installation failed .Can not continue"
		exit 1
	fi
	#cleaning the log directory
	/etc/init.d/collectl stop
	rm -rf /var/log/collectl/*
	log_info "Starting the system monitoring"
	/etc/init.d/collectl start '-i 5 -P'

	while true
	do
		#Add any actions that is needed during the monitoring here 
		if [ `pgrep collectl| wc -l` -gt 0 ] 
		then 
			log_info "monitoring is active"
		else
			log_info "monitoring was not running .restarting the same"
			/etc/init.d/collectl start '-i 5 -P'
		fi
		
		sleep 10
	done

}

start_monitoring



