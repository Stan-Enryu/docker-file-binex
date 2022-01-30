FROM ${os}

RUN apt-get update 
% if type == 'xinetd':
RUN apt-get install -y xinetd 
% elif type == 'socat' :
RUN apt-get install -y socat 
% endif
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /etc/xinetd.d/*

RUN useradd -U -m -s /bin/bash ${name}

WORKDIR /home/${name}

COPY ./flag.txt .
COPY ./${file} .
% if type == 'xinetd':
COPY ./run.sh ./run
COPY ./xinetd /etc/xinetd.d/xinetd
COPY ./startchall.sh /usr/bin/startchall
% elif type == 'ynetd' :
COPY ./ynetd /usr/bin/ynetd
% elif type == 'socat' :
% endif

RUN chown -R root:${name} /home/${name}
RUN chmod -R 750 /home/${name} && chmod 440 flag.txt 
RUN mv flag.txt flag-$(md5sum flag.txt | awk '{print $1}').txt
% if type == 'xinetd':
RUN chmod 500 /etc/xinetd.d/xinetd && chmod 500 /usr/bin/startchall
% elif type == 'ynetd' :
RUN chown root:${name} /usr/bin/ynetd
RUN chmod 750 /usr/bin/ynetd
% elif type == 'socat' :
% endif

% if type != 'socat':
EXPOSE ${port}
% endif

% if type == 'xinetd':
CMD ["/usr/bin/startchall"]
% elif type == 'ynetd' :
CMD ["/usr/bin/ynetd", "-p", "${port}", "/home/${name}/${file}"]
% elif type == 'socat' :
CMD $
CMD ["socat","TCP4-LISTEN:${port},reuseaddr,fork,su=${name}","EXEC:'/home/${name}/${file}'"]
% endif
