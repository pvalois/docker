From python
WORKDIR /root
RUN pip3 install docker 
COPY get_containers_date.py /root/get_containers_date.py
COPY orphaned_overlays.py /root/orphaned_overlays.py
COPY pause.py /pause.py
#ENTRYPOINT ["python3", "/root/get_containers_date.py"]
#ENTRYPOINT ["python3", "/root/orphaned_overlays.py"]
ENTRYPOINT ["python3","/pause.py"]
