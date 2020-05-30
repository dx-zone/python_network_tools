#!/usr/bin/env python
#
# This script will read the "domains.txt" to perform a DNS lookup
# in order to resolve the Name Server record for each domain listed
# in "domains.txt" file
# The "domains.txt" file must exist and must contain a domain or a list
# of domains to be read and processed by this script (one domain per line).
#
# Requirements: dnspython module
#
# Title:         dnsResolver_ns.py
# Author:        Daniel Cruz Quinones
# Version:       1.0
#
#
# check if the dnspython module is install (for dns.resolver to work),
# if the module is not present, then prompt the user and install it
# automatically (the scipt will do a "pip install" for the user)
try:
    import dns.resolver
except ModuleNotFoundError as err:
    print(f"A missing module is required: {err} was found.\n")
    input("""Press ENTER to install the missing module.
Otherwise press CTRL+C to end this program.""")
    import os
    os.system('pip install dnspython')
    import dns.resolver

# look for "domain.txt" file,read each line and store it in a domains list,
# prompt the user if file is not found
try:
    with open("domains.txt", "r") as file:
        domains = file.read().splitlines()
except FileNotFoundError:
    print('File not found. Check if the file "domains.txt" exist.')

# domains list variable for debugging purposes (disabled)
#domains = ['example.com', 'fakedomain.com']

# create an instance named resolver to be used to resolve DNS records
resolver = dns.resolver.Resolver()

# set DNS queries timeout parameters (30 seconds in this example)
resolver.timeout = 30
resolver.lifetime = 30

# iteration to lookup for each domain listed in the domains list variable,
# perform a DNS lookup, and catch any error (if any) is found.
for domain in domains:
    try:
        result = resolver.query(domain, 'NS')
        for rdata in result:
            print(f"Domain: {domain} | Name Server: {rdata}")
    except dns.resolver.NXDOMAIN as err:
        pass
        print(f"Remove this domain from the list: {err}")   
    except dns.exception.Timeout as err:
        print(f"DNS request timed out for this domain: {err}")
    except dns.resolver.NoAnswer as err:
        print(f"DNS did not answer for this domain: {err}")
    except dns.resolver.NoNameservers as err:
        print(f"Remove this domain from the list: {err}")
    except KeyError as err:
        print(f"Another exception was catched: {err}")
