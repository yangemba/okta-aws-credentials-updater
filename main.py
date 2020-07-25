import pexpect
import time
import sys

from os import environ

update_range_time = int(environ.get('UPDATE_RANGE_TIME', None)) - 200
organization = environ.get('ORGANIZATION', None)
password = environ.get('PASSWORD', None)


def validate_settings():
    """Validate the docker-compose env settings"""
    print('Enter validating settings')
    setting_list = [update_range_time, organization, password]

    for value in setting_list:
        if value is None:
            print('Error: no {} was set in the docker-compose'.format(value))
            sys.exit()
    print('Setting has been successfully validated')


if __name__ == "__main__":
    print('Running main.py')
    validate_settings()

    while True:
        time.sleep(update_range_time)
        with pexpect.spawn('okta-awscli --profile {}'.format(organization),
                           timeout=10,
                           encoding="utf-8") as child:
            try:
                child.expect('Enter password: ', timeout=None)
                child.sendline('{}'.format(password))
                time.sleep(7)
                print('AWS credentials has been successfully updated')
                continue
            except Exception as ex:
                print('Error while updating AWS credentials: {}'.format(ex))
