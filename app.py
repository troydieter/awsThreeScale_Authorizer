#!/usr/bin/env python3

from aws_cdk import App

from api_gw.api_gw_stack import APIGWStack
from elasticache.elasticache_app_stack import ElasticacheAppStack

app = App()
APIGWStack(app, "ApiGateway3ScaleAuth")
ElasticacheAppStack(app, "ElasticacheAppStack")

app.synth()
