import boto3
from datetime import datetime
import argparse

def check_odd_day():
    """Check if the current day of the month is an odd number."""
    day_of_month = datetime.now().day
    return day_of_month % 2 != 0

def reboot_instance(ec2_client, instance_id):
    """Reboot the specified EC2 instance."""
    try:
        ec2_client.reboot_instances(InstanceIds=[instance_id])
        return True
    except Exception as e:
        print(f"Error rebooting instance: {e}")
        return False

def publish_message(sns_client, topic_arn, message):
    """Publish a message to the specified SNS topic."""
    try:
        response = sns_client.publish(
            TopicArn=topic_arn,
            Message=message
        )
        return response['MessageId']
    except Exception as e:
        print(f"Error publishing message to SNS: {e}")
        return None

def main(instance_id, topic_arn):
    ec2_client = boto3.client('ec2')
    sns_client = boto3.client('sns')

    if check_odd_day():
        success = reboot_instance(ec2_client, instance_id)
        message = f"Reboot of instance {instance_id} was {'successful' if success else 'unsuccessful'}."
        message_id = publish_message(sns_client, topic_arn, message)
        if message_id:
            print(f"Message published to SNS with MessageId: {message_id}")
        else:
            print("Failed to publish message to SNS.")
    else:
        print("Today is not an odd day. No action taken.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Reboot EC2 instance on odd days and publish SNS message.")
    parser.add_argument("--instance-id", type=str, required=True, help="The ID of the EC2 instance to reboot.")
    parser.add_argument("--sns-topic", type=str, required=True, help="The ARN of the SNS topic to publish the message to.")
    args = parser.parse_args()

    main(args.instance_id, args.sns_topic)
