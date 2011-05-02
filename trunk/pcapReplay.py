#!/usr/bin/env python
"""
From the initial pcap file, you first need to:
    tcpprep \
      --port \
      --cachefile=linux-ids-snortbopre.cache \
      --pcap=linux-ids-snortbopre.pcap
    tcprewrite \
      --endpoints=192.168.100.48:192.168.100.45 \
      --enet-dmac=00:0c:29:0a:ce:e7 \
      --enet-smac=70:f1:a1:a7:85:95 \
      --cachefile=linux-ids-snortbopre.cache \
      --infile=linux-ids-snortbopre.pcap \
      --outfile=linux-ids-snortbopre_rw.pcap
Where
    192.168.100.45: client
    192.168.100.48: target (snort|suricata)
For more information, refer to http://tcpreplay.synfin.net/wiki/usage
    
PcapReplay testing module
    Replays traffic from pcap with tcpreplay

Syntax:
    self.payloads.append([
        "{TEST_NAME}",
        "pcap",
        "{PCAP_PATH}",
        "{EXPECTED_PATTERN}"
        ])

Parameters for writing tests:
    0: {TEST_NAME} is a string identifying the test
    1: 'pcap' is a constant
    2: {PCAP_PATH} is the path (string) of the pcap to replay
    3: {EXPECTED_PATTERN} is the pattern (string) expected in the triggered alerts
"""
import ConfigParser

class PcapReplay():
    def __init__(self, target):
        # Read configuration
        self.config = ConfigParser.RawConfigParser()
        self.config.read('config.cfg')

        self._target = target
        self.payloads = []

    def getPayloads(self):

        ### linux-ids-snortbopre.pcap
        self.payloads.append([
            "ripv2_request_rw",
            "pcap",
            "pcap/ripv2_request_rw.pcap",
            ""
            ])

        return self.payloads

if __name__ == "__main__":
    print BadTraffic("192.168.100.48").getPayloads()