
1.      The host file, located in "C:\Windows\System32\drivers\etc", is mainly a text file that is used by Windows to help directed IP addresses to host names/ domain names. In other words this file acts like a DNS service for your PC. It overrides the mappings from the DNS server that your personal computer is currently connected to. You can configure this file by going to the WSL software and by connecting to your AWS account, then typing down "sudo vim /etc/hosts".

https://search.yahoo.com/yhs/search?p=what%20is%20etc%2Fhosts&hspart=fc&hsimp=yhs-2212&type=fc_A30C76C6185_s58_g_e_d020122_n1009_c24&param1=7&param2=eJw1i8sKgzAQRX9llgoSJw9ji5%2FRVREXqaYxGI34wNKv71hahoFz7p1xvqur5nbniFIqWWfNRE52JTwrFMiFIGlJhCLw83khkXG80Cr2rZ2NFO8r4W6Ixvj2IZi8YAjJ4acuHitMG3BkWAEFWlXw0ioFM8%2FBHvYx%2BC0vZMmkhmTotzFkEPxgwdl2iCm0%2FRJHm3PUDM%2BB1TzN4v8vtnO%2FjssSWSE%2BPQk%2B9A%3D%3D

https://aws.amazon.com/premiumsupport/knowledge-center/linux-static-hostname/


2.      I typed down ssh -i v2.pem ubuntu@44.205.151.49

3.      I typed down on my wsl when I connected to my proxy instance "sudo apt install -y haproxy". I then cd'd by typing down "/etc/haproxy". I backed up the original config file, made my changes, and then attempted to restart haproxy

    (a) I modified the haproxy.cfg at "/etc/haproxy"
    (b)     following the configurations:
            frontend index.srv1.html
                bind *:80
                mode http
                
                default_backend webservers

            backend webservers
                balance roundrobin
                server server1 10.0.1.101:80
                server server2 10.0.1.102:80

        

    (c) the command for restarting haproxy is "systemctl restart haproxy"
    (d) https://www.digitalocean.com/community/tutorials/how-to-troubleshoot-common-haproxy-errors

    https://www.digitalocean.com/community/tutorials/an-introduction-to-haproxy-and-load-balancing-concepts
    


    

4.   I unfortunalty was not able to get any further than that, Im sorry but I left images on Github to show what I got so far.


