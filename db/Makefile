apply-service:
	kubectl apply -f service.yaml
	kubectl get service

exec-mongo:
	kubectl exec -it mongo-server-pod mongo

delete-service:
	kubectl delete -f service.yaml

image-rm:
	docker image rm mongo:4.2.0
