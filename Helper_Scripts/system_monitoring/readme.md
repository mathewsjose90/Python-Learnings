# Usage

For system monitoring of a linux machine for parameters like CPU , Memory etc

## Start monitoring

Edit hosts.txt with the ip addresses to monitor

Keep each ip address in a new line in hosts.txt

```bash
./manage_system_monitoring.sh start
```

## Stop monitoring
Let the script run for as long as we want . Once the monitoring period is over run the below command to stop the monitoring .

```bash
./manage_system_monitoring.sh stop <result_dir>
#above command will generate a folder with the name <result_dir> in the current path under <reports> folder
```

## Generate reports
To generate the PDF reports from the result files in the previous step .

````bash
#For entire duration reports
<base_path>/colplot -dir <base_path>/reports/<result_dir>/collectl -filedir <base_path>/reports/ -plots mem,cpu,loadavg,disk,diskdsize,diskio,disktimes,diskque,diskutil,swap,net,netpkt -filetype pdf

Here base path is the location where we are keeping this script and the related files . 
<result_dir> is the name we gave in the previous step while stopping the monitoring script.

#For specific time duration
<base_path>/colplot -dir <base_path>/reports/<result_dir>/collectl -filedir <base_path>/reports/ -plots mem,cpu,loadavg,disk,diskdsize,diskio,disktimes,diskque,diskutil,swap,net,netpkt -filetype pdf --time `date -d @$start_time +'%H:%M:%S'`-`date -d @$end_time +'%H:%M:%S'`

#ex:
start_time=$(( 1576129839 - 3600 ))
end_time=$(( $start_time + 10800 ))

start_time=1577851200
end_time=1577908800

````

## License

