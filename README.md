# RUN
Help
```
└─$ make-docker -h                                                                    
usage: make-docker [-h] [-n NAME] [-p PORT] [-f FILE] [-o OS] [-fl FLAG] {xinetd,ynetd,socat,pwnred}

positional arguments:
  {xinetd,ynetd,socat,pwnred}
                        For type

options:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  Default : ctf
  -p PORT, --port PORT  Default : 11100
  -f FILE, --file FILE  Default : chall
  -o OS, --os OS        Default : ubuntu:latest
  -fl FLAG, --flag FLAG
                        Default : FLAG{test}
```

For ynetd
```
make-docker ynetd -n pwnuser -p 11101 -fl 'FLAG{Fake_Flag}' -o 'ubuntu:24.04'
```