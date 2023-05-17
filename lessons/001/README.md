# Autoscaling with Custom metrics

Autoscaling in K8s can be done using [Horizontal Pod Autoscaler](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/). Autoscaling can be done on metrics provided by the kubernetes. This was the older case where we were able to autoscale only on cpu usage, but later updates included much more metrics where we can apply `hpa`.

The `hpa` is purely based on the `cpu` utilization. The `hpa` can use the resource metrics api or the custom metrics api. HPA fetches metrics from series of aggregated API (`metrics.k8s.io`, `custom.metrics.k8s.io` and `external.metrics.k8s.io`). The `metrics.k8s.io` API is usually provided by [metrics-server](https://kubernetes.io/docs/tasks/debug-application-cluster/resource-metrics-pipeline/#metrics-server), which needs to be launched separately. See metrics-server for instructions.


## Prerequsites
- EKS Cluster
- Application with `/metrics` endpoint

## Prometheus 
> The entire manifests files will be inside autoscale directory

### **1. Custom resource definitions**
The entire resource will be created under the `monitoring` namespace

`kubectl create -f 0-setup/`

### **2. Components**
Create the essential components like prometheus-operator, prometheus-adapter, grafana, prometheus, rules etc. 
> *prometheusAdapter-configMap.yaml* add the custom metrics name that matches the application metrics, here it *random_number_total* in both fastapi app and configmap

`kubectl create -f 1-components/`

Once components are created and starts running expose the prometheus-operated svc to access the prometheus from localhost

`kube -n monitoring port-forward svc/prometheus-operated 9090` -> Prometheus

`kube -n monitoring port-forward svc/grafana 3000` -> Grafana

### **3. Pod metrics**
To get the top pods create the cadvisor to scrape the CPU and Memory

`kubectl create -f components.yaml`

> After setting all sometimes the custom metrics doesn't work please verify that servicemonitor for the svc is up (eg; servicemonitor for server, worker)

## Resource refered: 
<!-- ***Youtube*** -->


***Docs***
- [HPA using Custom Metrics by IBM](https://www.ibm.com/docs/en/cloud-private/3.1.2?topic=tp-horizontal-pod-auto-scaling-by-using-custom-metrics)
- [Kubernetes HPA with Custom Metrics from Prometheus](https://towardsdatascience.com/kubernetes-hpa-with-custom-metrics-from-prometheus-9ffc201991e)
- [Monitoring Prometheus Operator](https://sysdig.com/blog/kubernetes-monitoring-prometheus-operator-part3/)