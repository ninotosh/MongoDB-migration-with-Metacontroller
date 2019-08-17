NAMESPACE=webhook

apply-migration:
	kubectl -n ${NAMESPACE} apply -f migration.yaml
	kubectl get -n ${NAMESPACE} mongomigration
	kubectl get -n ${NAMESPACE} pod

delete-migration:
	kubectl delete -n ${NAMESPACE} -l resource=mongomigration mongomigration
