import os, sys
from wptserve.utils import isomorphic_decode
subresource = __import__("common.security-features.subresource.subresource")

def generate_payload(server_data):
    return subresource.get_template(u"document.html.template") % server_data

def main(request, response):
    subresource.respond(request,
                        response,
                        payload_generator = generate_payload)
