This is an example Kubernetes Operator implemented with [Metacontroller](https://github.com/GoogleCloudPlatform/metacontroller) to run a MongoDB migration.

### before you begin

Make these commands available.
- `docker`
- `kubectl`

### edit a migration

1. `cd operation`
1. Edit `spec.url` in `migration.yaml`.
The content of `url` will be executed in MongoDB.

### to run a migration

1. `cd db`
  1. `make apply-service`
1. `cd metacontroller`
  1. `make install`
1. `cd custom`
  1. `make apply-crd`
  1. `make apply-controller`
1. `cd webhook`
  1. `make image-build`
  1. `make create-namespace`
  1. `make apply-service`
1. `cd operation`
  1. `make apply-migration`

### to confirm

1. `cd db`
  1. `make exec-mongo`

### to clean up
1. `cd operation`
  1. `make delete-migration`
1. `cd webhook`
  1. `make delete-service`
  1. `make delete-namespace`
  1. `make image-rm`
1. `cd custom`
  1. `make delete-controller`
  1. `make delete-crd`
1. `cd metacontroller`
  1. `make uninstall`
  1. `make image-rm`
1. `db`
  1. `make delete-service`
  1. `make image-rm`
