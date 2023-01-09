from aws_cdk import (
    # Duration,
    Stack,
    aws_ec2 as ec2,
    aws_elasticache as elasticache,
    CfnOutput
)

from constructs import Construct


class ElasticacheAppStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # VPC
        vpc = ec2.Vpc(self, "VPC",
                      nat_gateways=1,
                      cidr="192.168.0.0/16",
                      subnet_configuration=[
                          ec2.SubnetConfiguration(name="public", subnet_type=ec2.SubnetType.PUBLIC, cidr_mask=24),
                          ec2.SubnetConfiguration(name="private", subnet_type=ec2.SubnetType.PRIVATE_WITH_NAT,
                                                  cidr_mask=24)
                      ]
                      )

        # Security Groups
        vpc_sec_group = ec2.SecurityGroup(
            self, "vpc_sec_group",security_group_name="vpc_sec_group", vpc=vpc, allow_all_outbound=True,
        )
        redis_sec_group = ec2.SecurityGroup(
            self, "redis-sec-group", security_group_name="redis-sec-group", vpc=vpc, allow_all_outbound=True,
        )

        private_subnets_ids = [ps.subnet_id for ps in vpc.private_subnets]

        redis_subnet_group = elasticache.CfnSubnetGroup(
            scope=self,
            id="redis_subnet_group",
            subnet_ids=private_subnets_ids,
            description="subnet group for redis"
        )

        redis_sec_group.add_ingress_rule(
            peer=vpc_sec_group,
            description="Allow Redis connection",
            connection=ec2.Port.tcp(6379),
        )

        # Elasticache for Redis cluster
        redis_cluster = elasticache.CfnCacheCluster(
            scope=self,
            id="redis_cluster",
            engine="redis",
            cache_node_type="cache.t3.small",
            num_cache_nodes=1,
            cache_subnet_group_name=redis_subnet_group.ref,
            vpc_security_group_ids=[redis_sec_group.security_group_id],
        )

        # Generate CloudFormation Outputs
        CfnOutput(scope=self, id="redis_endpoint", value=redis_cluster.attr_redis_endpoint_address)