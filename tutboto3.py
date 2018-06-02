#configure aws in and let instance be 'shotty'
import boto3
import sys

if __name__=='__main__':    #doesn't work when imported into another module
    #creates a session on the aws instance shotty
    session=boto3.Session(profile_name='shotty')

    #get the resource for each type of service
    ec2=session.resource('ec2')

    #add permissions to users in aws, manage policy

    for i in ec2.instances.all():
        print i

    #get commandline arguements
    print sys.argv
