#configure aws in and let instance be 'shotty'
import boto3
import sys
import click

#creates a session on the aws instance shotty
session=boto3.Session(profile_name='shotty')
#get the resource for each type of service
ec2=session.resource('ec2')

def filter_instances(project):
    instances=[]

    if project:
        filters=[{'Name':'tag:Project','Values':[project]}]
        instances=ec2.instances.filter(Filters=filters)
    else:
        instances=ec2.instances.all()

    return instances
#decorators
@click.group()
def instances():
    'commands for instances'
@instances.command('list')
@instances.option('--project',default=None,help='only for this project')

def list_instances(project):
    'list instances of ec2'
    #add permissions to users in aws, manage policy
    instances=filter_instances(project)
    for i in ec2.instances.all():
        tags={t['Key']:t['Value'] for t in i.tags or []}
        print i
        print i.id
        print i.placement       #region and stuff
        print i.state       #running

    #get commandline arguements
    print sys.argv
    return

@instances.command('stop')
@instances.option('--project',default=None,help='only instances for project')

def stop_instances(project):
    'stop ec2 instances'
    instances=filter_instances(project)
    for i in instances:
        #stopping all instances
        print 'stopping instance'+str(i.id)
        i.stop()
    return

@instances.command('start')
@instances.option('--project',default=None,help='only instances for project')

def start_instances(project):
    'start ec2 instances'
    instances=filter_instances(project)
    for i in instances:
        #starting all instances
        print 'starting instance'+str(i.id)
        i.start()

    return

if __name__=='__main__':    #doesn't work when imported into another module
    instances()
#run this code
#python tuboto3.py list --project=<NAME>
#python tuboto3.py stop --project=<NAME>
