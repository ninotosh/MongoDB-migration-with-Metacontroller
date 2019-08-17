install:
	kubectl create namespace metacontroller
	kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/metacontroller/5cd8f46/manifests/metacontroller-rbac.yaml
	kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/metacontroller/eacb75b/manifests/metacontroller.yaml

uninstall:
	kubectl delete -f https://raw.githubusercontent.com/GoogleCloudPlatform/metacontroller/eacb75b/manifests/metacontroller.yaml
	kubectl delete -f https://raw.githubusercontent.com/GoogleCloudPlatform/metacontroller/5cd8f46/manifests/metacontroller-rbac.yaml
	kubectl delete namespace metacontroller

image-rm:
	docker image rm metacontroller/metacontroller:v0.4.0
