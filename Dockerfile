FROM 	debian:buster-slim



RUN		apt-get update; apt-get -y upgrade; \
		apt-get -y install openssh-server net-tools \
		procps dnsutils htop sudo 



COPY 	files/ns-start /usr/bin/
COPY	files/nstools /opt/nstools

#Add Docker Client
ADD 	https://download.docker.com/linux/debian/dists/buster/pool/stable/amd64/docker-ce-cli_20.10.7~3-0~debian-buster_amd64.deb /tmp/docker-ce-cli.deb

RUN     chmod +x /usr/bin/ns-start; \
		chmod +x /opt/nstools/bin/*; \
		dpkg -i /tmp/docker-ce-cli.deb; \
		rm -f /tmp/docker-ce-cli.deb


#Admin user
RUN		useradd --no-create-home --shell /bin/bash --comment "Nsoporte Admin Default User" admin; \
		echo "admin:admin" |chpasswd; \
		groupadd nstools; \
		adduser admin nstools; \
		echo "sudo /opt/nstools/bin/nstools_start" >> /etc/bash.bashrc; \
		echo "%nstools ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/nstools 



CMD 	[ "/usr/bin/ns-start" ]