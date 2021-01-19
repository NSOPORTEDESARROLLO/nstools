FROM 	debian:buster-slim



RUN		apt-get update; apt-get -y upgrade; \
		apt-get -y install openssh-server net-tools \
		procps dnsutils




EXPOSE 	22

COPY 	files/ns-start /usr/bin/
RUN     chmod +x /usr/bin/ns-start


CMD 	[ "/usr/bin/ns-start" ]