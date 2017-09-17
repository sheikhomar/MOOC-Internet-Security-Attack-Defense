yaf --in capture.pcap --out results.yaf --active-timeout 120 --idle-timeout 60 --uniflow
yafscii --in results.yaf --out text-result.txt --tabular --print-header
less text-result.txt 
