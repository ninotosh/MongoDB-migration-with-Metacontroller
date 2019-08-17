import json
import requests
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class Controller(BaseHTTPRequestHandler):
  def sync(self, parent, children):
    # Compute status based on observed state.
    desired_status = {
      "configmaps": len(children["ConfigMap.v1"]),
      "pods": len(children["Pod.v1"]),
    }

    url = parent["spec"]["url"]
    response = requests.get(url)
    response.raise_for_status()
    content = response.text

    name = parent["metadata"]["name"]
    namespace = parent["metadata"]["namespace"]
    configmap_name = "configmap-" + name

    desired_children = [
      {
        "apiVersion": "v1",
        "kind": "ConfigMap",
        "metadata": {
          "name": configmap_name,
          "namespace": namespace,
          "labels": {
            "for": "mongomigration",
          },
        },
        "data": {
          "url": url,
          "migration.js": content,
        }
      },
      {
        "apiVersion": "v1",
        "kind": "Pod",
        "metadata": {
          "name": "pod-" + name,
          "labels": {
            "for": "mongomigration",
          },
        },
        "spec": {
          "restartPolicy": "Never",
          "containers": [
            {
              "name": "container-" + name,
              "image": "mongo",
              "command": ["mongo", "--host", "mongo-service.default", "/mnt/migration.js"],
              "volumeMounts": [
                {"name": "configmap-volume", "mountPath": "/mnt"},
              ],
            },
          ],
          "volumes": [
            {
              "name": "configmap-volume",
              "configMap": {
                "name": configmap_name,
              },
            },
          ]
        }
      }
    ]

    return {"status": desired_status, "children": desired_children}

  def do_POST(self):
    # Serve the sync() function as a JSON webhook.
    observed = json.loads(self.rfile.read(int(self.headers.getheader("content-length"))))

    import pprint as pp
    pp.pprint(observed)

    desired = self.sync(observed["parent"], observed["children"])

    self.send_response(200)
    self.send_header("Content-type", "application/json")
    self.end_headers()
    self.wfile.write(json.dumps(desired))

HTTPServer(("", 80), Controller).serve_forever()
