
#!bin/bash


touch /root/Dockerfile

echo "FROM ubuntu

MAINTAINER Selva Karthik

RUN apt-get update
RUN apt-get install -y python

COPY /root/server.py">>/root/Dockerfile

i=0

while [ $i -lt 154 ]
do
echo "COPY /root/client.py /root/client$i.py">>/root/Dockerfile
i=$[$i+1]
done

echo "CMD ["/root/server.py"]
ENTRYPOINT ["python"]">>/root/Dockerfile

$i = 0
while [ $i -lt 154 ]
do
echo "CMD ["/root/client$i.py"]
ENTRYPOINT ["python"]">>/root/Dockerfile
i=$[$i+1]
done


docker build -t Chat_application /root/Dockerfile

docker run --name MyContainer -it Chat_application