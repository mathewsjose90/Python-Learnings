#!/usr/bin/python
"""
Author  : Mathews Jose
Date    : 28/11/2018
History:
Version : V1.0
Details : Script to trigger the commands over SSL or nonSSL to the given ip and port
"""
 
import socket
import argparse
import sys,os
import ssl
from time import time
from multiprocessing import Pool,Lock,Manager
 
#Global Lock
lock = Lock()
manager=Manager()
time_tracker = manager.list()
 
def parse_args():
    parser = argparse.ArgumentParser()
 
    parser.add_argument("-q", "--query_file", dest="query_file", help="Provide the query file to use with each query is prefixed with a query_id and ::")
 
    parser.add_argument("-i", "--machine_ip", dest="machine_ip", help="Provide machine IP to query ")
 
    parser.add_argument("-p", "--port", dest="port", type=int, help="Provide machine port ")
    
    parser.add_argument("-n", "--poolsize", dest="poolsize", type=int, default=8,help='Number of processes to spawn for parallel querying (default: 8)')
 
    parser.add_argument("-o", "--output_path", dest="output_path", help="Provide the absoulute output path for storing the result ")
 
    parser.add_argument('-s', '--ssl', dest='is_ssl', action='store_true', default=None,
                        help='Is SSL socket enabled.(default: False)')
 
    parser.add_argument('-k', '--ssl-key', dest='ssl_key', type=str, default=None, help='SSL Key path.(default: False)')
 
    parser.add_argument('-c', '--ssl-cert', dest='ssl_cert', type=str, default=None,
                        help='SSL cert path.(default: False)')
 
    args = parser.parse_args()
 
    # Checking the mandatory arguments
    if args.query_file is None or args.machine_ip is None or args.port is None or args.output_path is None:
        parser.print_help()
        sys.exit(-1)
    # Checking for the required options if SSL is enabled
    if args.is_ssl:
        if not args.ssl_key or not args.ssl_cert:
            print "Key and Certificate locations are mandatory when using the SSL option."
            sys.exit(-1)
 
    return args
 
def track_time_for_query(output_path,query_id=None,time_in_secs=0):
    #global lock
    global time_tracker
    tracker_file=os.path.join(output_path,'time_taken_for_each_query.log')
    with open(tracker_file,'a+') as f:
       #lock.acquire()
       #f.write(query_id+':'+str(time_in_secs)+"\n")
       #lock.release()
       f.write("\n".join(time_tracker)) 
 
def run_query_and_store_result(arg):
    global time_tracker
    start = time()
    try:
        run_query_and_store_result_(*arg)
    except KeyboardInterrupt:
        raise Exception()
    time_taken = time() - start
    #track_time_for_query(os.path.dirname(arg[4]),arg[2],time_taken)
    time_tracker.append(arg[2]+':'+str(time_taken))
    return time_taken
 
def run_query_and_store_result_(ip, port, query_id, query, output_file, is_ssl=None, ssl_key=None, ssl_cert=None, timeout=2800):
    #print "Sending query ==>{0}<== to server {1} on port {2} with is_ssl={3}".format(query, ip, port, is_ssl)
    print "Sending query_id:{0} to server:{1} on port:{2} with is_ssl={3}".format(query_id, ip, port, is_ssl)
 
    try:
 
        #Appending query_id with the queries for tracking later
        #query = query.rstrip(';\n')+"  with '{" +'"query_id":"'+str(query_id)+'"}'+"';"
        query = query.rstrip('\n')
        with open(output_file, 'w') as f:
            f.write(query+"\n\n")
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            try:
                # Run the query over SSL if SSL options are provided
                if is_ssl:
                    #ssl_sock = ssl.wrap_socket(sock, keyfile=ssl_key, certfile=ssl_cert, cert_reqs=ssl.CERT_NONE)
                    ssl_sock = ssl.wrap_socket(sock, keyfile=ssl_key, certfile=ssl_cert, cert_reqs=ssl.CERT_REQUIRED,ca_certs="/home/mjose/BACKUP/SSL/ssl_certs/servercert.chain_cert")
                    ssl_sock.connect((ip, port))
                    #ssl_sock.settimeout(timeout)
                    ssl_sock.write(query+"\n")
                    while 1:
                        data = ssl_sock.read()
                        if not data:
                            break
                        f.write(data)
                    ssl_sock.close()
                # If nonSSL was requested then run the query over normal socket and store the result
                else:
                    sock.connect((ip, port))
                    #sock.settimeout(timeout)
                    sock.send(query + "\n")
                    while 1:
                        data = sock.recv(4096)
                        if not data:
                            break
                        f.write(data)
                    sock.close()
                f.write("\n")
            except Exception, e:
                print "There is some error with the socket connection as :  {0}".format(e)
    except IOError, e:
        print "Unable to open the output file {0} for storing the result . Some error occured as : {1}".format(
            output_file, e)
 
def gen_args(ip, port, query_file, output_path, is_ssl=None, ssl_key=None, ssl_cert=None):
    with open(query_file,'r') as f:
        for line in f:
            if not line.startswith('#') and line != '\n':
                query_info = line.split('::')
           #proceed only if there is a query_id and query given in the input line
                if len(query_info) == 2:
                    output_file = os.path.join(output_path,query_info[0]+'_result.log')
                    yield (ip, port, query_info[0], query_info[1], output_file, is_ssl, ssl_key, ssl_cert)   
 
def main():
    # Get the commandline arguments
    options = parse_args()
    query_file = options.query_file
    ip = options.machine_ip
    port = int(options.port)
    output_path = options.output_path
    is_ssl = options.is_ssl
    ssl_cert = options.ssl_cert
    ssl_key = options.ssl_key
    
    #Create output directory to store results
    if not os.path.exists(output_path):
        os.makedirs(output_path)
 
    pool = Pool(options.poolsize)
    time_taken = []
    start_time = time()
    try:
     # Run the query passed and store the result
        time_taken = pool.map(run_query_and_store_result,gen_args(ip, port, query_file, output_path, is_ssl, ssl_key, ssl_cert))
        pool.close()
    except Exception, e:
        print("Caught Exception, terminating workers.")
        print(e)
    pool.terminate()
    pool.join()
    track_time_for_query(output_path)
    print "Total time taken for individual queries together is : {} secs".format(sum(time_taken))
    print "Wall clock time taken is : {} secs".format(time()-start_time)
 
 
if __name__ == "__main__":
    main()
 
