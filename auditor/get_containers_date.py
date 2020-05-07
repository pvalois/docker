#!/usr/bin/env python3

import socket, datetime
import docker
import json

client = docker.DockerClient(base_url='unix://var/run/docker.sock')

for container in client.containers.list():
  #print (json.dumps(container.attrs,indent=2))
  print ("%s %-40s" %(container.attrs["Id"][:8],container.attrs["Config"]["Image"]), end=" -> ")
  response=container.exec_run("date",tty=True,stdin=True)

  if (response.exit_code==0):
    print (response.output.decode("utf8").strip())
  else:
    print ("exit_code :",response.exit_code)

print (" =============================================== ")

