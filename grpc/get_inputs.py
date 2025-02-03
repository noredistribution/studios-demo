#!/usr/bin/python3

# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the COPYING file.

import argparse
import grpc
import json

from arista.studio.v1 import services as studio_services

from fmp import wrappers_pb2 as fmp_wrappers
from google.protobuf import wrappers_pb2 as wrappers
from google.protobuf.json_format import Parse

RPC_TIMEOUT = 30  # in seconds
CC_EXECUTION_TIMEOUT = 60  # in seconds
MAINLINE_ID = ""  # ID to reference merged workspace data
STUDIO_ID = "studio-evpn-services"


def main(args):

    # Get connection credentials.
    token = args.token_file.read().strip()
    callCreds = grpc.access_token_call_credentials(token)
    if args.cert_file:
        cert = args.cert_file.read()
        channelCreds = grpc.ssl_channel_credentials(root_certificates=cert)
    else:
        channelCreds = grpc.ssl_channel_credentials()
    connCreds = grpc.composite_channel_credentials(channelCreds, callCreds)

    with grpc.secure_channel(args.server, connCreds) as channel:

        if args.wsid:
            workspace_id = args.wsid
        else:
            workspace_id = ""
        request = get_studio_inputs(channel, STUDIO_ID, workspace_id)
        print(list(request))

def get_studio_inputs(channel, studio_id, workspace_id):
    '''
    Returns the inputs for a given studio in a workspace.
    '''

    json_request = json.dumps({"partialEqFilter":[{"key":{"studioId":studio_id,"workspaceId":workspace_id}}]})
    request = Parse(json_request, studio_services.InputsStreamRequest(), False)
    stub = studio_services.InputsServiceStub(channel)
    res = stub.GetAll(request, timeout=RPC_TIMEOUT)
    return res


if __name__ == '__main__':
    desc = (
        "Configure interfaces on devices using a YAML file which populates and"
        "submits the built-in Interface Configuration studio.\n"
        "Example:\n"
        "python3 get_inputs.py --server 192.0.2.79:443 --token-file token.txt"
        "--cert-file cvp.crt"
    )
    parser = argparse.ArgumentParser(
        description=desc,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--server', required=True,
                        help="CloudVision server to connect to in <host>:<port> format")
    parser.add_argument("--token-file", required=True, type=argparse.FileType('r'),
                        help="file with access token")
    parser.add_argument("--cert-file", type=argparse.FileType('rb'),
                        help="file with certificate to use as root CA")
    parser.add_argument("--wsid", type=str, default=False,
                        help="existing wsid")
    args = parser.parse_args()
    main(args)
