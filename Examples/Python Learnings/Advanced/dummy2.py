# This Module generate Test Data
from threading import Thread
import secrets


def write_in():
    beacon_id = secrets.token_hex(8)
    session_id = secrets.token_hex(8)
    events = ['I', 'S', 'P', 'C', 'V']
    for event in events:
        with open('input_testdata.txt', "a") as f:
            f.write(
                "http://<something>?/9.gif?a=" + event + "~b=" + beacon_id + "~c=" + session_id + "~d=1da7f6a21c91495d78e0c19b0cc6f70~e=0~g=0~k=2a13ddddcb69b13348850266de8d82a~w=0~ac=%2Fdvrorigin%2F_definst_%2Fsmil%3AStar_Sports_HD_1_hs.smil%2Fplaylist.m3u8~ak=Android~al=Android~am=Android%3AL~aw=http%3A%2F%2Fhotstar.live.cdn.jio.com%2Fdvrorigin%2F_definst_%2Fsmil%3AStar_Sports_HD_1_hs.smil%2Fplaylist.m3u8%3FDVR%26hdnea%3Dst%3D1484189762*%40*exp%3D1484190362*%40*acl%3D%2F**%40*hmac%3Dcaede62f68670756f9b7494c624e09b1d89114061d0ae4cb932066ca08ecd5db~ax=L~ay=2.6.5~cg=FICTITIOUS~cn=MOBILE%3ALTE~dx=0~en=Star%20Sports%201~pd=HS-ANDROID-PLAYER~sa=hotstar-android-jio-app~sh=Star%20Sports%201~vv=1.0~xd=0a97ce1fe1d4a5f4ddccd2466489596f~az=1.4~os=Linux-Android-5.1~&cip=157.49.203.217&ct=1484276399&country=IN&regional_info=MH&city=MUMBAI&dma=&pmsa=&areacode =&county=&fips=&lat=18.98&long=72.83&zip=&continent=AS&throughput=vhi" + "\n")


for i in range(100000):
    t1 = Thread(target=write_in)
    t1.start()
    #print("Done ", i)
