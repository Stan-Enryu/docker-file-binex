FROM ${os}

RUN apt-get update 
% if type == 'xinetd':
RUN apt-get install -y xinetd 
% elif type == 'socat' :
RUN apt-get install -y socat 
% endif
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN useradd -U -m -s /bin/sh ${name}

WORKDIR /home/${name}

COPY ./${file} .
% if type == 'ynetd':
COPY ./ynetd /usr/bin/ynetd
% endif

% if type == 'xinetd':
RUN echo 'service ${name}\n\
{\n\
  type = UNLISTED\n\
  disable = no\n\
  socket_type = stream\n\
  protocol = tcp\n\
  wait = no\n\
  user = ${name}\n\
  bind = 0.0.0.0\n\
  port = ${port}\n\
  server = /home/${name}/chall\n\
}' > /etc/xinetd.d/pwn
RUN echo '#!/bin/bash\n\
service xinetd restart && /bin/sleep infinity' > /etc/init.sh
RUN echo '#!/bin/bash\n\
cd /home/${name}/ && ./${file}' > ./run.sh
RUN chmod 444 /etc/xinetd.d/pwn && chmod 500 /etc/init.sh
% elif type == 'ynetd' :
RUN chown root:${name} /usr/bin/ynetd
RUN chmod 750 /usr/bin/ynetd
% elif type == 'socat' :
% endif

RUN chmod -R 750 /home/${name}
RUN echo "${flag}" > ./flag.txt
RUN chmod 440 flag.txt
RUN mv flag.txt flag-$(md5sum flag.txt | awk '{print $1}').txt
RUN chown -R root:${name} /home/${name}

% if type != 'socat':
EXPOSE ${port}
% endif

% if type == 'xinetd':
RUN service xinetd restart
% elif type == 'ynetd' :
CMD ["/usr/bin/ynetd", "-u","${name}", "-p", "${port}", "/home/${name}/${file}"]
% elif type == 'socat' :
CMD $
CMD ["socat","TCP4-LISTEN:${port},reuseaddr,fork,su=${name}","EXEC:'/home/${name}/${file}'"]
% endif
