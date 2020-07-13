# Demonstrate how to customize logging output

import logging

extradata={
    'user':'Mathews Jose'
}

# TODO: add another function to log from
def testlogging():
    logging.debug('Test logging from another function',extra=extradata)

def main():
    # set the output file and debug level, and
    # TODO: use a custom formatting specification
    fmtstr="User:%(user)s %(asctime)s: %(levelname)s: %(funcName)s: Line %(lineno)d : %(message)s "
    datestr="%d/%m/%Y %I:%M:%S %p"
    logging.basicConfig(filename="output.log",
                        level=logging.DEBUG,filemode='w',format=fmtstr,datefmt=datestr)

    logging.info("This is an info-level log message",extra=extradata)
    logging.warning("This is a warning-level message",extra=extradata)
    testlogging()


if __name__ == "__main__":
    main()
