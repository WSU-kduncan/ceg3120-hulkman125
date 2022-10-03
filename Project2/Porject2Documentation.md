Part 1 Step 1: Create a VPC 

I simply typed in the Search for Services text box “VPC” and pressed the VPC option and then on the list on the left I clicked “Your VPCs”. Afterward I clicked on the “Create VPC button and I gave it the name” Harvey-VPC” and gave it the IP address 10.0.0.0/24 with a 24 bit subnet.

A VPC, or Virtual Private Cloud is a digital cloud that lets an owner or group of people such as a corporation create ther own computing environment on shared cloud infrastructure. This give the owner(s) the power to control the virtual network such as the path of data to where it can and cannot go, including what kind of data can go inside there network. 

Part 1 Step 2: Create a Subnet

I then clicked on the “Subnet” tab on the left and I then clicked the “Create Subnet” button. On the new page I got sent to I typed down the VPC ID I got when I made the VPC. I then typed down the a 28 bit subnet address range of 10.0.0.0/28. Afterwards I then named my new subnet to "Harvey-Subnet".

A subnet is a range of IP addresses that certain level of departments in an organization could share, such as in a school the math department can have many Ip addresses that follow within their Subnet address, while the Science department can have multiple IP addresses within their own Subnet address.

Part 1 Step 3: Create a Internet Gateway

On the left I clicked the “Internet gateway” tab and clicked the “Create Internet Gateway” button where I got sent to another page. I then gave it the name “Harvey-gw” before I pressed the “Create Internet Gateway” button. Afterwards I got sent to another page where I clicked the “Attach to a VPC” button right before I typed down my VPC address like before.

An Internet gateway is a node that is capable of connecting multiple networks for communicating. This is specifically used when the two nodes being connected together use completely different protocols for communicating with each other. An internet gateway is basically where the data temporarily stops between networks.

Part 1 Step 4: Create a Route Table

On the left I pressed the “route table” tab before I pressed the “Create Route Table” button. Afterwards I gave it the name “Harvey-routetable”, then I assigned it my VPC ID before I clicked on the “Create route table” button. Instantly clicked on the “Subnet Associations” tab near the bottom of the screen before pressing the “Edit Subnet Associations” button. Afterwards I then typed down my Subnet ID that I got when I created the Subnet. I then clicked on the “Save associations”. I then clicked on the “routes” tab before clicking the “Edit routes” before I clicked the “Add Route” button. On the new area I could edit I typed down in the destination column “0.0.0.0/0” and then typed down “Internet Gateway” to declare that traffic to all destinations to my internet gateway.

A route table is a group of rules that are more commonly known as route that decide where specifically the data in the network traffic that can be found in the subnet can e sent to. 

Part 1 Step 5: Create a Security Group

On the left I clicked the “Security Group” tab and clicked on the “Create Security Group” button where I was sent to a different page. On the “inbound rules” box I clicked on the “Add Rule” button before I set the Type to “SSH”. Afterwards I then set the destination to “My IP” so that it would be set to my computer’s IP address to make the data be available to my computer. I then clicked on “Add Rule” to create a new Inbound rule I again set the Type to SSH right before I typed down the IP address range of 130.108.0.0/24 to give Wright State University access to inbound traffic. I then added a new Inbound rule and typed down the IP addres range for my VPC which is 10.0.0.0/24. Afterwards I then gave my security group name of “Harvey-sg” before I attached it to my VPC ID.

A security group acts as a firewall virtually, which has the ability to control the traffic of data and can give nodes the ability to access the data or even deny them.

Part 2 :

On the Search box up top I typed in “EC2” and clicked on the option of itself where I was redirected to a new page. On the left I clicked on the “Instances” tab before I clecked on the “Create Instances” button. I was sent to a new page where I gave my Instance a name of “ Harvey-Instance” before I clicked on the “Windows OS” option in the “Application and OS Images” box. I the left the Instance type where it is currently is at t2.micro. On the “network Settings” section I clicked the “Edit” button where I was given the opportunity to attach my instance with my VPC.

I personally believe that it would be wise to use a privte IPv4 address because only a my computer, the Wright State University, and anyone who will be using my VPC will have access to my data meaning not everyone should be using them.

I left the volume to where it was already to 8 Giga Bytes. If I wanted to change this I could just type in a new number either increasing or decreasing the data it can store in the Instance.

I then associated my security group called “Harvey-sg”, before I clicked on the “ Launch Instance” button where I was taken back to the earlier “Instance” Page. I then clicked on the “Elastic Ips” tab on the left and clicked on the “Allocate Elastic IP address” button where I was redirected to a new page. I then, in the “Value- Optional” textField, entered the name of my Elastic IP address of “Harvey-EIP”. I then clicked on the “Allocate” button.

Afterwards I was given a choice to associate the Elastic IP with my instance and I clicked on the button on the top where I was redirected to do so. In the “Instance” textfield I then typed down my Instance name of “Harvey-Instance”. I then clicked on the “Associate” button.