import os
import sys

ROOT = "/Users/caitygraves/Desktop/Cowork/Client Dashboards/openbook-client-plans"
os.chdir(ROOT)

# Inject the directory so http.server's argparse default doesn't call os.getcwd()
sys.argv = ["http.server", "8123"]

import http.server
http.server.test(
    HandlerClass=http.server.SimpleHTTPRequestHandler,
    port=8123,
    bind="127.0.0.1",
)
