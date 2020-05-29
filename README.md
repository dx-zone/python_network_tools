## Python Network Tools

### Description

This is a collection of tools scripted in Python for network/system automation and troubleshooting. These are intended for to speed up automation (such as configure multiple network/system devices), automate repetitive task and/or to speed up network troubleshooting processes.  Ideally for those who works with Cisco/Juniper networks, *Nix systems, datacenter techs, IT, etc.

## Tools

**dnsResolver_ns.py**

This script will read the "domains.txt" file to perform a DNS lookup in order to resolve the Name Server record for each domain listed in "domains.txt" file.

The **"domains.txt"** is a text file which must exist in the same directory where the script will be executed and the file must contain a domain or a list of domains to be read and processed by this script (one domain per line).

### Requirements

* Python 3
* dnspython module
* A text file named "domains.txt" in within the same script directory with domain names listed in the "domains.txt" text file (one domain per line).

### Installation

* Python 3 (refer to [Python.org](Python.org) for installation instructions)
* pip (refer to [Python.org](Python.org) for installation instructions)
* dnspython module (refer to this [link](https://pypi.org/project/dnspython/) for more details)
   * Install dnspython
      ```pip install dnspython```

### To Run The Program

To run the program execute:
`python3 dnsResolver_ns.py`

The **dnsResolver_ns.py** programm will look for the **domains.txt** file and will execute a DNS querie to resolve the Name Server per each domain listed in the "domains.txt" file.

### Author

* Daniel Cruz - [dx-zone](https://github.com/dx-zone)