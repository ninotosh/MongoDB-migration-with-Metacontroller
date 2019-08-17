image-build:
	docker image build -t migration-webhook --label migration-webhook .
	docker image tag migration-webhook:latest migration-webhook:`date +%s`
	# docker image rm migration-webhook:latest
	docker image ls --filter label=migration-webhook

test-run:
	docker container run -it --rm -p 8000:80 migration-webhook

NAMESPACE=webhook

create-namespace:
	kubectl create namespace ${NAMESPACE}

apply-service:
	kubectl apply -n ${NAMESPACE} -f service.yaml
	kubectl get -n ${NAMESPACE} service
	kubectl get -n ${NAMESPACE} deployment
	kubectl get -n ${NAMESPACE} pod
	sleep 5

delete-service:
	kubectl delete -n ${NAMESPACE} -f service.yaml

delete-namespace:
	kubectl delete namespace ${NAMESPACE}

image-rm:
	docker image rm -f `docker image ls --filter label=migration-webhook -q`
	docker image prune -f
	docker image rm python:2.7-alpine
