#!/usr/bin/env python3

import socket, datetime 
import docker
import json
import os
import sys

client = docker.DockerClient(base_url='unix://var/run/docker.sock')
overlays = {}

for container in client.containers.list():
  #print (json.dumps(container.attrs,indent=2))
  gddata=container.attrs["GraphDriver"]["Data"]
  paths=[]
  for value in gddata:
    paths=paths+[os.path.dirname(x) for x in gddata[value].split(":")]
    overlays[container.attrs["Id"][:8]]=paths

os.system("echo List of orphans")
for files in os.listdir("/var/lib/docker/overlay2"):
  if (files != "l"):  
    owner=[x for x in overlays if (os.path.join("/var/lib/docker/overlay2",files) in overlays[x])]
    if (len(owner)==0):
      os.system ("du -sh "+os.path.join("/var/lib/docker/overlay2",files))
    
