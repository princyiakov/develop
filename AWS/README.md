# Jump Box Set Up 

## What's a Jump Box?

An SSH Jump Box is simply a single, hardened server that you "jump" through in order to access other servers on the inner network. Sometimes called a bastion or relay host, it's simply a server that all of your users can log into and use as a relay server to connect to other servers.


# Steps to follow 

## Create VPC


![Create VPC](https://github.com/princys-lab/develop/blob/master/AWS/CreateVPC.jpg)


## Create two subnet : One for Public and One for Private
![Subnet](https://github.com/princys-lab/develop/blob/master/AWS/Subnet.png)


## Create Internet Gateway
![IGW](https://github.com/princys-lab/develop/blob/master/AWS/IGW.png)

## Attach IGW to a VPC
![IGWToVPC](https://github.com/princys-lab/develop/blob/master/AWS/IGWToVPC.png)

## Create Route table
![CreateRoute](https://github.com/princys-lab/develop/blob/master/AWS/CreateRoute.png) 

## Click on edit route table 
![EditRoute](https://github.com/princys-lab/develop/blob/master/AWS/EditRoute.png)

## Add route table for the Public Subnet
![AddRoute](https://github.com/princys-lab/develop/blob/master/AWS/AddRoute.png)


## Associate the public subnet 
![AssociatePublic](https://github.com/princys-lab/develop/blob/master/AWS/AssociatePublic.png)

## Create a security group 
![CreateSG](https://github.com/princys-lab/develop/blob/master/AWS/CreateSG.png)

## Edit Inbound rules
![CreateRules](https://github.com/princys-lab/develop/blob/master/AWS/CreateRules.png)

# Launch the NAT instance

1.	Launch an instance into your public subnet from an AMI that's been configured to run as a NAT instance. Amazon provides Amazon Linux AMIs that are configured to run as NAT instances. These AMIs include the string amzn-ami-vpc-nat in their names, so you can search for them in the Amazon EC2 console.
		a.	Open the Amazon EC2 console.
		b.	On the dashboard, choose the Launch Instance button, and complete the wizard as follows:
	i.	On the Choose an Amazon Machine Image (AMI) page, select the Community AMIs category, and search for amzn-ami-vpc-nat. In the results list, each AMI's name includes the version to enable you to select the most recent AMI, for example, 2013.09. Choose Select.
 
	ii.	On the Choose an Instance Type page, select the instance type, then choose Next: Configure Instance Details.
 
	![ChooseInstance](https://github.com/princys-lab/develop/blob/master/AWS/ChooseInstance.png)

	iii.	On the Configure Instance Details page, select the VPC you created from the Network list, and select your public subnet from the Subnet list.
 
	![ConfigureInstance](https://github.com/princys-lab/develop/blob/master/AWS/ConfigureInstance.png)

	iv.	(Optional) Select the Public IP check box to request that your NAT instance receives a public IP address. If you choose not to assign a public IP address now, you can allocate an Elastic IP address and assign it to your instance after it's launched. Choose Next: Add Storage
 
	v.	You can choose to add storage to your instance, and on the next page, you can add tags. Choose Next: Configure Security Group when you are done.
	vi.	On the Configure Security Group page, select the Select an existing security group option, and select the NATSG security group that you created. Choose Review and Launch.
 
	vii.	Review the settings that you've chosen. Make any changes that you need, and then choose Launch to choose a key pair and launch your instance.

2.	(Optional) Connect to the NAT instance, make any modifications that you need, and then create your own AMI that's configured to run as a NAT instance. You can use this AMI the next time that you need to launch a NAT instance. 

3.	Disable the SrcDestCheck attribute for the NAT instance
	To disable source/destination checking using the console 

		a.	Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.
		b.	In the navigation pane, choose Instances.
		c.	Select the NAT instance, choose Actions, Networking, Change Source/Dest. Check.
		d.	For the NAT instance, verify that this attribute is disabled. Otherwise, choose Yes, Disable.
		e.	If the NAT instance has a secondary network interface, choose it from Network interfaces on the Description tab and choose the interface ID to go to the network interfaces page. Choose Actions, Change Source/Dest. Check, disable the setting, and choose Save.

	![DisableDestCheck](https://github.com/princys-lab/develop/blob/master/AWS/DisableDestCheck.png)

4.	If you did not assign a public IP address to your NAT instance during launch (step 3), you need to associate an Elastic IP address with it.
		a.	Open the Amazon VPC console at https://console.aws.amazon.com/vpc/.
		b.	In the navigation pane, choose Elastic IPs, and then choose Allocate new address.
		c.	Choose Allocate.
		d.	Select the Elastic IP address from the list, and then choose Actions, Associate address.
		e.	Select the network interface resource, then select the network interface for the NAT instance. Select the address to associate the Elastic IP with from the Private IP list, and then choose Associate.

5.	Update the main route table to send traffic to the NAT instance. 


## Create another instance which would act as Jump Box

## Create a private instance 

## Don’t forget to update the route table for your private instance to connect the IGW using Public Instance
The private subnet in your VPC is not associated with a custom route table, therefore it uses the main route table. By default, the main route table enables the instances in your VPC to communicate with each other. You must add route that sends all other subnet traffic to the NAT instance.
To update the main route table
	1.	Open the Amazon VPC console at https://console.aws.amazon.com/vpc/.
	2.	In the navigation pane, choose Route Tables.
	3.	Select the main route table for your VPC (the Main column displays Yes) . The details pane displays tabs for working with its routes, associations, and route propagation.
	4.	On the Routes tab, choose Edit, specify 0.0.0.0/0 in the Destination box, select the instance ID of the NAT instance from the Target list, and then choose Save.
	5.	On the Subnet Associations tab, choose Edit, and then select the Associate check box for the subnet. Choose Save.

## Once all the three instances are deployed 

	1.	Copying key of private instance to your jump box using scp .(make sure you are in the directory where the key is placed )
	```
	scp -i PrincyHW.pem PrincyHW.pem ec2-user@54.167.98.214:PrincyHW.pem
	```

	2.	Connect the  jumpbox using ssh 
	```
	ssh -i Princy_KeyPair.pem ec2-user@54.167.98.214
	```
	
	3.	Connect the  private instance  using ssh 
	```
	ssh -i PrincyHW.pem ec2-user@10.1.2.185
	```

	4.	Ping Google and it works !
	![Ping](https://github.com/princys-lab/develop/blob/master/AWS/Ping.png)
 
