import boto

from boto.ec2.regioninfo import RegionInfo
from boto.ec2.connection import EC2Connection

import config


def establish():

    my_region = RegionInfo(name=config.region(), endpoint=config.endpoint())

    conn = boto.connect_ec2(
        aws_access_key_id=config.aws_access_key_id(),
        aws_secret_access_key=config.aws_secret_access_key(),
        is_secure=True, region=my_region, port=config.port(),
        path=config.endpoint_path(), validate_certs=False)

    return conn


def main():
    conn = establish()
    print(conn)
    print(conn.region)
    #print(conn.get_region)
    #create_instances(conn)


def create_instances(conn, count=1):
    # ami-000022b3 NeCTAR Ubuntu 14.04 (Trusty) amd64
    instance_list = []
    for c in range(count):
        instance_list.append(
            conn.run_instances('ami-000022b3',
                               key_name='Default-cloud',
                               instance_type='m1.small',
                               security_groups=['default'],
                               placement='melbourne-np')
        )


if __name__ == '__main__':
    main()
