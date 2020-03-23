#!/usr/bin/python
"""
Author  : mjose
Date    : 28/11/2018
History:
Version : V1.0
Details : Script to trigger the commands over SSL or nonSSL to the given ip and port
"""

import socket
import argparse
import sys
import ssl


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("-q", "--query", dest="query", help="Provide the query to run")

    parser.add_argument("-i", "--machine_ip", dest="machine_ip", help="Provide machine IP to query ")

    parser.add_argument("-p", "--port", dest="port", type=int, help="Provide machine port ")

    parser.add_argument("-o", "--output", dest="output_file", help="Provide the output file for storing the result ")

    parser.add_argument('-s', '--ssl', dest='is_ssl', action='store_true', default=None,
                        help='Is SSL socket enabled.(default: False)')

    parser.add_argument('-k', '--ssl-key', dest='ssl_key', type=str, default=None, help='SSL Key path.(default: False)')

    parser.add_argument('-c', '--ssl-cert', dest='ssl_cert', type=str, default=None,
                        help='SSL cert path.(default: False)')

    args = parser.parse_args()

    # Checking the mandatory arguments
    if args.query is None or args.machine_ip is None or args.port is None or args.output_file is None:
        parser.print_help()
        sys.exit(-1)
    # Checking for the required options if SSL is enabled
    if args.is_ssl:
        if not args.ssl_key or not args.ssl_cert:
            print "Key and Certificate locations are mandatory when using the SSL option."
            sys.exit(-1)

    return args


def run_query_and_store_result(ip, port, query, output_file, is_ssl=None, ssl_key=None, ssl_cert=None, timeout=600):
    print "Sending query {0} to server {1} on port {2} with is_ssl={3}".format(query, ip, port, is_ssl)

    try:

        with open(output_file, 'w') as f:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                # Run the query over SSL if SSL options are provided
                if is_ssl:
                    ssl_sock = ssl.wrap_socket(sock, keyfile=ssl_key, certfile=ssl_cert, cert_reqs=ssl.CERT_NONE)
                    ssl_sock.connect((ip, port))
                    ssl_sock.write(query)
                    while 1:
                        data = ssl_sock.read()
                        if not data:
                            break
                        f.write(data)
                    ssl_sock.close()
                # If nonSSL was requested then run the query over normal socket and store the result
                else:
                    sock.connect((ip, port))
                    sock.settimeout(timeout)
                    sock.send(query + "\n")
                    while 1:
                        data = sock.recv(1024)
                        if not data:
                            break
                        f.write(data)
                    sock.close()
                f.write("\n")
            except Exception, e:
                print "There is some error with the socket connection {0}".format(e)
    except IOError, e:
        print "Unable to open the output file {0} for storing the result . Some error occured as {1}".format(
            output_file, e)


def main():
    # Get the commandline arguments
    options = parse_args()
    query = options.query
    ip = options.machine_ip
    port = int(options.port)
    output_file = options.output_file
    is_ssl = options.is_ssl
    ssl_cert = options.ssl_cert
    ssl_key = options.ssl_key

    # Run the query passed and store the result
    run_query_and_store_result(ip, port, query, output_file, is_ssl, ssl_key, ssl_cert)


if __name__ == "__main__":
    main()
