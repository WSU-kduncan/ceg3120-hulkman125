So far I see nothing wrong with this file, it compiles perfectly.

As for how I created it, I started with altering the description of the file up on the top.

Afterwards I Adjusted the Mapping to allow the AMI to be "ami-0b0ea68c435eb488d".

When that was finished I then atlered the resources of the file by changing the VPC to be within the range of /24. Meaning the first three octets of the subnet mask would be set to "1"'s before I set them set it's value to "TylerHarvey-CF-VPC" which is the given name of my VPC. I then made similar modifications to the Subnet Resource by setting its Subnet range to /28, which means the first 3 octets followed by the next four digits in the subnet mask would be set to "1"'s also. I then changed it's value also to "TylerHarvey-CF-VPC". 

After wards i then began working to the Security Group Settings. I changed the IpProtocol to "tcp" before I changed the FromPort and ToPort to '22'. I then changed the CidrIp to 208.38.225.197/32 to make it equal to my own personel IP address. I then began working on the next group of settings by also making th IpProtocol to "tcp" and again making the FromPort and ToPort to '22'. I then changed to CidrIp to make it's subnet range  to 130.108.0.0/16 to make it available for WSU. I then went to the next group of settings by making the IpProtocol also "tcp" and also made both the FromPort and ToPort become '22'. I then made the CidrIp to be the same as my VPC CidrBlock which is 10.0.0.0/24.

I then went to the instance settings and set it's value become equal to "Harvey-CF-instance" and then create a private Ip address that is within my subnet range. SoI chose 10.0.0.14. After that I then had to instal the python3 and pip 3 by typing this command within my code: "udo apt install python3-pip && \". I then had to change my host name to become equal to value of my instance, so I typed down "sudo hostnamectl set-hostname Harvey-CF-instance && \"
