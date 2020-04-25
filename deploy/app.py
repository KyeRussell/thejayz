#!/usr/bin/env python3

from aws_cdk import core

from thejayz.frontend import FrontendStack
from thejayz.networking import NetworkingAndDBStack

app = core.App()
FrontendStack(app, "thejayz-frontend")
NetworkingAndDBStack(app, "thejayz-networking-db")

app.synth()
