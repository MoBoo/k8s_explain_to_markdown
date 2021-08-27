# Deployment

---



## Description
Deployment enables declarative updates for Pods and ReplicaSets.




## Fields

<details>
<summary>apiVersion: string</summary>

# Deployment.apiVersion

---

**Type**: string

## Description
APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources





---

</details>

<details>
<summary>kind: string</summary>

# Deployment.kind

---

**Type**: string

## Description
Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds





---

</details>

<details>
<summary>metadata: Object</summary>

# Deployment.metadata

---

**Type**: Object

## Description
Standard object metadata.




## Fields

<details>
<summary>annotations: map[string]string</summary>

# Deployment.metadata.annotations

---

**Type**: map[string]string

## Description
Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects. More info: http://kubernetes.io/docs/user-guide/annotations





---

</details>

<details>
<summary>clusterName: string</summary>

# Deployment.metadata.clusterName

---

**Type**: string

## Description
The name of the cluster which the object belongs to. This is used to distinguish resources with same name and namespace in different clusters. This field is not set anywhere right now and apiserver is going to ignore it if set in create or update request.





---

</details>

<details>
<summary>creationTimestamp: string</summary>

# Deployment.metadata.creationTimestamp

---

**Type**: string

## Description
CreationTimestamp is a timestamp representing the server time when this object was created. It is not guaranteed to be set in happens-before order across separate operations. Clients may not set this value. It is represented in RFC3339 form and is in UTC.      Populated by the system. Read-only. Null for lists. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata





---

</details>

<details>
<summary>deletionGracePeriodSeconds: integer</summary>

# Deployment.metadata.deletionGracePeriodSeconds

---

**Type**: integer

## Description
Number of seconds allowed for this object to gracefully terminate before it will be removed from the system. Only set when deletionTimestamp is also set. May only be shortened. Read-only.





---

</details>

<details>
<summary>deletionTimestamp: string</summary>

# Deployment.metadata.deletionTimestamp

---

**Type**: string

## Description
DeletionTimestamp is RFC 3339 date and time at which this resource will be deleted. This field is set by the server when a graceful deletion is requested by the user, and is not directly settable by a client. The resource is expected to be deleted (no longer visible from resource lists, and not reachable by name) after the time in this field, once the finalizers list is empty. As long as the finalizers list contains items, deletion is blocked. Once the deletionTimestamp is set, this value may not be unset or be set further into the future, although it may be shortened or the resource may be deleted prior to this time. For example, a user may request that a pod is deleted in 30 seconds. The Kubelet will react by sending a graceful termination signal to the containers in the pod. After that 30 seconds, the Kubelet will send a hard termination signal (SIGKILL) to the container and after cleanup, remove the pod from the API. In the presence of network partitions, this object may still exist after this timestamp, until an administrator or automated process can determine the resource is fully terminated. If not set, graceful deletion of the object has not been requested.      Populated by the system when a graceful deletion is requested. Read-only. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata





---

</details>

<details>
<summary>finalizers: []string</summary>

# Deployment.metadata.finalizers

---

**Type**: []string

## Description
Must be empty before the object is deleted from the registry. Each entry is an identifier for the responsible component that will remove the entry from the list. If the deletionTimestamp of the object is non-nil, entries in this list can only be removed. Finalizers may be processed and removed in any order. Order is NOT enforced because it introduces significant risk of stuck finalizers. finalizers is a shared field, any actor with permission can reorder it. If the finalizer list is processed in order, then this can lead to a situation in which the component responsible for the first finalizer in the list is waiting for a signal (field value, external system, or other) produced by a component responsible for a finalizer later in the list, resulting in a deadlock. Without enforced ordering finalizers are free to order amongst themselves and are not vulnerable to ordering changes in the list.





---

</details>

<details>
<summary>generateName: string</summary>

# Deployment.metadata.generateName

---

**Type**: string

## Description
GenerateName is an optional prefix, used by the server, to generate a unique name ONLY IF the Name field has not been provided. If this field is used, the name returned to the client will be different than the name passed. This value will also be combined with a unique suffix. The provided value has the same validation rules as the Name field, and may be truncated by the length of the suffix required to make the value unique on the server.      If this field is specified and the generated name exists, the server will NOT return a 409 - instead, it will either return 201 Created or 500 with Reason ServerTimeout indicating a unique name could not be found in the time allotted, and the client should retry (optionally after the time indicated in the Retry-After header).      Applied only if Name is not specified. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#idempotency





---

</details>

<details>
<summary>generation: integer</summary>

# Deployment.metadata.generation

---

**Type**: integer

## Description
A sequence number representing a specific generation of the desired state. Populated by the system. Read-only.





---

</details>

<details>
<summary>labels: map[string]string</summary>

# Deployment.metadata.labels

---

**Type**: map[string]string

## Description
Map of string keys and values that can be used to organize and categorize (scope and select) objects. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels





---

</details>

<details>
<summary>managedFields: []Object</summary>

# Deployment.metadata.managedFields

---

**Type**: []Object

## Description
ManagedFields maps workflow-id and version to the set of fields that are managed by that workflow. This is mostly for internal housekeeping, and users typically shouldn't need to set or understand this field. A workflow can be the user's name, a controller's name, or the name of a specific apply path like "ci-cd". The set of fields is always in the version that the workflow used when modifying the object.




## Fields

<details>
<summary>apiVersion: string</summary>

# Deployment.metadata.managedFields.apiVersion

---

**Type**: string

## Description
APIVersion defines the version of this resource that this field set applies to. The format is "group/version" just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted.





---

</details>

<details>
<summary>fieldsType: string</summary>

# Deployment.metadata.managedFields.fieldsType

---

**Type**: string

## Description
FieldsType is the discriminator for the different fields format and version. There is currently only one possible value: "FieldsV1"





---

</details>

<details>
<summary>fieldsV1: map[string]</summary>

# Deployment.metadata.managedFields.fieldsV1

---

**Type**: map[string]

## Description
FieldsV1 holds the first JSON version format as described in the "FieldsV1" type.





---

</details>

<details>
<summary>manager: string</summary>

# Deployment.metadata.managedFields.manager

---

**Type**: string

## Description
Manager is an identifier of the workflow managing these fields.





---

</details>

<details>
<summary>operation: string</summary>

# Deployment.metadata.managedFields.operation

---

**Type**: string

## Description
Operation is the type of operation which lead to this ManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'.





---

</details>

<details>
<summary>time: string</summary>

# Deployment.metadata.managedFields.time

---

**Type**: string

## Description
Time is timestamp of when these fields were set. It should always be empty if Operation is 'Apply'





---

</details>



---

</details>

<details>
<summary>name: string</summary>

# Deployment.metadata.name

---

**Type**: string

## Description
Name must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names





---

</details>

<details>
<summary>namespace: string</summary>

# Deployment.metadata.namespace

---

**Type**: string

## Description
Namespace defines the space within which each name must be unique. An empty namespace is equivalent to the "default" namespace, but "default" is the canonical representation. Not all objects are required to be scoped to a namespace - the value of this field for those objects will be empty.      Must be a DNS_LABEL. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/namespaces





---

</details>

<details>
<summary>ownerReferences: []Object</summary>

# Deployment.metadata.ownerReferences

---

**Type**: []Object

## Description
List of objects depended by this object. If ALL objects in the list have been deleted, this object will be garbage collected. If this object is managed by a controller, then an entry in this list will point to this controller, with the controller field set to true. There cannot be more than one managing controller.




## Fields

<details>
<summary>apiVersion: string required!</summary>

# Deployment.metadata.ownerReferences.apiVersion

---

**Type**: string (required)

## Description
API version of the referent.





---

</details>

<details>
<summary>blockOwnerDeletion: boolean</summary>

# Deployment.metadata.ownerReferences.blockOwnerDeletion

---

**Type**: boolean

## Description
If true, AND if the owner has the "foregroundDeletion" finalizer, then the owner cannot be deleted from the key-value store until this reference is removed. Defaults to false. To set this field, a user needs "delete" permission of the owner, otherwise 422 (Unprocessable Entity) will be returned.





---

</details>

<details>
<summary>controller: boolean</summary>

# Deployment.metadata.ownerReferences.controller

---

**Type**: boolean

## Description
If true, this reference points to the managing controller.





---

</details>

<details>
<summary>kind: string required!</summary>

# Deployment.metadata.ownerReferences.kind

---

**Type**: string (required)

## Description
Kind of the referent. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds





---

</details>

<details>
<summary>name: string required!</summary>

# Deployment.metadata.ownerReferences.name

---

**Type**: string (required)

## Description
Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names





---

</details>

<details>
<summary>uid: string required!</summary>

# Deployment.metadata.ownerReferences.uid

---

**Type**: string (required)

## Description
UID of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#uids





---

</details>



---

</details>

<details>
<summary>resourceVersion: string</summary>

# Deployment.metadata.resourceVersion

---

**Type**: string

## Description
An opaque value that represents the internal version of this object that can be used by clients to determine when objects have changed. May be used for optimistic concurrency, change detection, and the watch operation on a resource or set of resources. Clients must treat these values as opaque and passed unmodified back to the server. They may only be valid for a particular resource or set of resources.      Populated by the system. Read-only. Value must be treated as opaque by clients and . More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency





---

</details>

<details>
<summary>selfLink: string</summary>

# Deployment.metadata.selfLink

---

**Type**: string

## Description
SelfLink is a URL representing this object. Populated by the system. Read-only.      DEPRECATED Kubernetes will stop propagating this field in 1.20 release and the field is planned to be removed in 1.21 release.





---

</details>

<details>
<summary>uid: string</summary>

# Deployment.metadata.uid

---

**Type**: string

## Description
UID is the unique in time and space value for this object. It is typically generated by the server on successful creation of a resource and is not allowed to change on PUT operations.      Populated by the system. Read-only. More info: http://kubernetes.io/docs/user-guide/identifiers#uids





---

</details>



---

</details>

<details>
<summary>spec: Object</summary>

# Deployment.spec

---

**Type**: Object

## Description
Specification of the desired behavior of the Deployment.




## Fields

<details>
<summary>minReadySeconds: integer</summary>

# Deployment.spec.minReadySeconds

---

**Type**: integer

## Description
Minimum number of seconds for which a newly created pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready)





---

</details>

<details>
<summary>paused: boolean</summary>

# Deployment.spec.paused

---

**Type**: boolean

## Description
Indicates that the deployment is paused.





---

</details>

<details>
<summary>progressDeadlineSeconds: integer</summary>

# Deployment.spec.progressDeadlineSeconds

---

**Type**: integer

## Description
The maximum time in seconds for a deployment to make progress before it is considered to be failed. The deployment controller will continue to process failed deployments and a condition with a ProgressDeadlineExceeded reason will be surfaced in the deployment status. Note that progress will not be estimated during the time a deployment is paused. Defaults to 600s.





---

</details>

<details>
<summary>replicas: integer</summary>

# Deployment.spec.replicas

---

**Type**: integer

## Description
Number of desired pods. This is a pointer to distinguish between explicit zero and not specified. Defaults to 1.





---

</details>

<details>
<summary>revisionHistoryLimit: integer</summary>

# Deployment.spec.revisionHistoryLimit

---

**Type**: integer

## Description
The number of old ReplicaSets to retain to allow rollback. This is a pointer to distinguish between explicit zero and not specified. Defaults to 10.





---

</details>

<details>
<summary>selector: Object required!</summary>

# Deployment.spec.selector

---

**Type**: Object (required)

## Description
Label selector for pods. Existing ReplicaSets whose pods are selected by this will be the ones affected by this deployment. It must match the pod template's labels.




## Fields

<details>
<summary>matchExpressions: []Object</summary>

# Deployment.spec.selector.matchExpressions

---

**Type**: []Object

## Description
matchExpressions is a list of label selector requirements. The requirements are ANDed.




## Fields

<details>
<summary>key: string required!</summary>

# Deployment.spec.selector.matchExpressions.key

---

**Type**: string (required)

## Description
key is the label key that the selector applies to.





---

</details>

<details>
<summary>operator: string required!</summary>

# Deployment.spec.selector.matchExpressions.operator

---

**Type**: string (required)

## Description
operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.





---

</details>

<details>
<summary>values: []string</summary>

# Deployment.spec.selector.matchExpressions.values

---

**Type**: []string

## Description
values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.





---

</details>



---

</details>

<details>
<summary>matchLabels: map[string]string</summary>

# Deployment.spec.selector.matchLabels

---

**Type**: map[string]string

## Description
matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.





---

</details>



---

</details>

<details>
<summary>strategy: Object</summary>

# Deployment.spec.strategy

---

**Type**: Object

## Description
The deployment strategy to use to replace existing pods with new ones.




## Fields

<details>
<summary>rollingUpdate: Object</summary>

# Deployment.spec.strategy.rollingUpdate

---

**Type**: Object

## Description
Rolling update config params. Present only if DeploymentStrategyType = RollingUpdate.




## Fields

<details>
<summary>maxSurge: string</summary>

# Deployment.spec.strategy.rollingUpdate.maxSurge

---

**Type**: string

## Description
The maximum number of pods that can be scheduled above the desired number of pods. Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). This can not be 0 if MaxUnavailable is 0. Absolute number is calculated from percentage by rounding up. Defaults to 25%. Example: when this is set to 30%, the new ReplicaSet can be scaled up immediately when the rolling update starts, such that the total number of old and new pods do not exceed 130% of desired pods. Once old pods have been killed, new ReplicaSet can be scaled up further, ensuring that total number of pods running at any time during the update is at most 130% of desired pods.





---

</details>

<details>
<summary>maxUnavailable: string</summary>

# Deployment.spec.strategy.rollingUpdate.maxUnavailable

---

**Type**: string

## Description
The maximum number of pods that can be unavailable during the update. Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). Absolute number is calculated from percentage by rounding down. This can not be 0 if MaxSurge is 0. Defaults to 25%. Example: when this is set to 30%, the old ReplicaSet can be scaled down to 70% of desired pods immediately when the rolling update starts. Once new pods are ready, old ReplicaSet can be scaled down further, followed by scaling up the new ReplicaSet, ensuring that the total number of pods available at all times during the update is at least 70% of desired pods.





---

</details>



---

</details>

<details>
<summary>type: string</summary>

# Deployment.spec.strategy.type

---

**Type**: string

## Description
Type of deployment. Can be "Recreate" or "RollingUpdate". Default is RollingUpdate.





---

</details>



---

</details>

<details>
<summary>template: Object required!</summary>

# Deployment.spec.template

---

**Type**: Object (required)

## Description
Template describes the pods that will be created.




## Fields

<details>
<summary>metadata: Object</summary>

# Deployment.spec.template.metadata

---

**Type**: Object

## Description
Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata




## Fields

<details>
<summary>annotations: map[string]string</summary>

# Deployment.spec.template.metadata.annotations

---

**Type**: map[string]string

## Description
Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects. More info: http://kubernetes.io/docs/user-guide/annotations





---

</details>

<details>
<summary>clusterName: string</summary>

# Deployment.spec.template.metadata.clusterName

---

**Type**: string

## Description
The name of the cluster which the object belongs to. This is used to distinguish resources with same name and namespace in different clusters. This field is not set anywhere right now and apiserver is going to ignore it if set in create or update request.





---

</details>

<details>
<summary>creationTimestamp: string</summary>

# Deployment.spec.template.metadata.creationTimestamp

---

**Type**: string

## Description
CreationTimestamp is a timestamp representing the server time when this object was created. It is not guaranteed to be set in happens-before order across separate operations. Clients may not set this value. It is represented in RFC3339 form and is in UTC.      Populated by the system. Read-only. Null for lists. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata





---

</details>

<details>
<summary>deletionGracePeriodSeconds: integer</summary>

# Deployment.spec.template.metadata.deletionGracePeriodSeconds

---

**Type**: integer

## Description
Number of seconds allowed for this object to gracefully terminate before it will be removed from the system. Only set when deletionTimestamp is also set. May only be shortened. Read-only.





---

</details>

<details>
<summary>deletionTimestamp: string</summary>

# Deployment.spec.template.metadata.deletionTimestamp

---

**Type**: string

## Description
DeletionTimestamp is RFC 3339 date and time at which this resource will be deleted. This field is set by the server when a graceful deletion is requested by the user, and is not directly settable by a client. The resource is expected to be deleted (no longer visible from resource lists, and not reachable by name) after the time in this field, once the finalizers list is empty. As long as the finalizers list contains items, deletion is blocked. Once the deletionTimestamp is set, this value may not be unset or be set further into the future, although it may be shortened or the resource may be deleted prior to this time. For example, a user may request that a pod is deleted in 30 seconds. The Kubelet will react by sending a graceful termination signal to the containers in the pod. After that 30 seconds, the Kubelet will send a hard termination signal (SIGKILL) to the container and after cleanup, remove the pod from the API. In the presence of network partitions, this object may still exist after this timestamp, until an administrator or automated process can determine the resource is fully terminated. If not set, graceful deletion of the object has not been requested.      Populated by the system when a graceful deletion is requested. Read-only. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata





---

</details>

<details>
<summary>finalizers: []string</summary>

# Deployment.spec.template.metadata.finalizers

---

**Type**: []string

## Description
Must be empty before the object is deleted from the registry. Each entry is an identifier for the responsible component that will remove the entry from the list. If the deletionTimestamp of the object is non-nil, entries in this list can only be removed. Finalizers may be processed and removed in any order. Order is NOT enforced because it introduces significant risk of stuck finalizers. finalizers is a shared field, any actor with permission can reorder it. If the finalizer list is processed in order, then this can lead to a situation in which the component responsible for the first finalizer in the list is waiting for a signal (field value, external system, or other) produced by a component responsible for a finalizer later in the list, resulting in a deadlock. Without enforced ordering finalizers are free to order amongst themselves and are not vulnerable to ordering changes in the list.





---

</details>

<details>
<summary>generateName: string</summary>

# Deployment.spec.template.metadata.generateName

---

**Type**: string

## Description
GenerateName is an optional prefix, used by the server, to generate a unique name ONLY IF the Name field has not been provided. If this field is used, the name returned to the client will be different than the name passed. This value will also be combined with a unique suffix. The provided value has the same validation rules as the Name field, and may be truncated by the length of the suffix required to make the value unique on the server.      If this field is specified and the generated name exists, the server will NOT return a 409 - instead, it will either return 201 Created or 500 with Reason ServerTimeout indicating a unique name could not be found in the time allotted, and the client should retry (optionally after the time indicated in the Retry-After header).      Applied only if Name is not specified. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#idempotency





---

</details>

<details>
<summary>generation: integer</summary>

# Deployment.spec.template.metadata.generation

---

**Type**: integer

## Description
A sequence number representing a specific generation of the desired state. Populated by the system. Read-only.





---

</details>

<details>
<summary>labels: map[string]string</summary>

# Deployment.spec.template.metadata.labels

---

**Type**: map[string]string

## Description
Map of string keys and values that can be used to organize and categorize (scope and select) objects. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels





---

</details>

<details>
<summary>managedFields: []Object</summary>

# Deployment.spec.template.metadata.managedFields

---

**Type**: []Object

## Description
ManagedFields maps workflow-id and version to the set of fields that are managed by that workflow. This is mostly for internal housekeeping, and users typically shouldn't need to set or understand this field. A workflow can be the user's name, a controller's name, or the name of a specific apply path like "ci-cd". The set of fields is always in the version that the workflow used when modifying the object.




## Fields

<details>
<summary>apiVersion: string</summary>

# Deployment.spec.template.metadata.managedFields.apiVersion

---

**Type**: string

## Description
APIVersion defines the version of this resource that this field set applies to. The format is "group/version" just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted.





---

</details>

<details>
<summary>fieldsType: string</summary>

# Deployment.spec.template.metadata.managedFields.fieldsType

---

**Type**: string

## Description
FieldsType is the discriminator for the different fields format and version. There is currently only one possible value: "FieldsV1"





---

</details>

<details>
<summary>fieldsV1: map[string]</summary>

# Deployment.spec.template.metadata.managedFields.fieldsV1

---

**Type**: map[string]

## Description
FieldsV1 holds the first JSON version format as described in the "FieldsV1" type.





---

</details>

<details>
<summary>manager: string</summary>

# Deployment.spec.template.metadata.managedFields.manager

---

**Type**: string

## Description
Manager is an identifier of the workflow managing these fields.





---

</details>

<details>
<summary>operation: string</summary>

# Deployment.spec.template.metadata.managedFields.operation

---

**Type**: string

## Description
Operation is the type of operation which lead to this ManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'.





---

</details>

<details>
<summary>time: string</summary>

# Deployment.spec.template.metadata.managedFields.time

---

**Type**: string

## Description
Time is timestamp of when these fields were set. It should always be empty if Operation is 'Apply'





---

</details>



---

</details>

<details>
<summary>name: string</summary>

# Deployment.spec.template.metadata.name

---

**Type**: string

## Description
Name must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names





---

</details>

<details>
<summary>namespace: string</summary>

# Deployment.spec.template.metadata.namespace

---

**Type**: string

## Description
Namespace defines the space within which each name must be unique. An empty namespace is equivalent to the "default" namespace, but "default" is the canonical representation. Not all objects are required to be scoped to a namespace - the value of this field for those objects will be empty.      Must be a DNS_LABEL. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/namespaces





---

</details>

<details>
<summary>ownerReferences: []Object</summary>

# Deployment.spec.template.metadata.ownerReferences

---

**Type**: []Object

## Description
List of objects depended by this object. If ALL objects in the list have been deleted, this object will be garbage collected. If this object is managed by a controller, then an entry in this list will point to this controller, with the controller field set to true. There cannot be more than one managing controller.




## Fields

<details>
<summary>apiVersion: string required!</summary>

# Deployment.spec.template.metadata.ownerReferences.apiVersion

---

**Type**: string (required)

## Description
API version of the referent.





---

</details>

<details>
<summary>blockOwnerDeletion: boolean</summary>

# Deployment.spec.template.metadata.ownerReferences.blockOwnerDeletion

---

**Type**: boolean

## Description
If true, AND if the owner has the "foregroundDeletion" finalizer, then the owner cannot be deleted from the key-value store until this reference is removed. Defaults to false. To set this field, a user needs "delete" permission of the owner, otherwise 422 (Unprocessable Entity) will be returned.





---

</details>

<details>
<summary>controller: boolean</summary>

# Deployment.spec.template.metadata.ownerReferences.controller

---

**Type**: boolean

## Description
If true, this reference points to the managing controller.





---

</details>

<details>
<summary>kind: string required!</summary>

# Deployment.spec.template.metadata.ownerReferences.kind

---

**Type**: string (required)

## Description
Kind of the referent. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds





---

</details>

<details>
<summary>name: string required!</summary>

# Deployment.spec.template.metadata.ownerReferences.name

---

**Type**: string (required)

## Description
Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names





---

</details>

<details>
<summary>uid: string required!</summary>

# Deployment.spec.template.metadata.ownerReferences.uid

---

**Type**: string (required)

## Description
UID of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#uids





---

</details>



---

</details>

<details>
<summary>resourceVersion: string</summary>

# Deployment.spec.template.metadata.resourceVersion

---

**Type**: string

## Description
An opaque value that represents the internal version of this object that can be used by clients to determine when objects have changed. May be used for optimistic concurrency, change detection, and the watch operation on a resource or set of resources. Clients must treat these values as opaque and passed unmodified back to the server. They may only be valid for a particular resource or set of resources.      Populated by the system. Read-only. Value must be treated as opaque by clients and . More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency





---

</details>

<details>
<summary>selfLink: string</summary>

# Deployment.spec.template.metadata.selfLink

---

**Type**: string

## Description
SelfLink is a URL representing this object. Populated by the system. Read-only.      DEPRECATED Kubernetes will stop propagating this field in 1.20 release and the field is planned to be removed in 1.21 release.





---

</details>

<details>
<summary>uid: string</summary>

# Deployment.spec.template.metadata.uid

---

**Type**: string

## Description
UID is the unique in time and space value for this object. It is typically generated by the server on successful creation of a resource and is not allowed to change on PUT operations.      Populated by the system. Read-only. More info: http://kubernetes.io/docs/user-guide/identifiers#uids





---

</details>



---

</details>

<details>
<summary>spec: Object</summary>

# Deployment.spec.template.spec

---

**Type**: Object

## Description
Specification of the desired behavior of the pod. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status




## Fields

<details>
<summary>activeDeadlineSeconds: integer</summary>

# Deployment.spec.template.spec.activeDeadlineSeconds

---

**Type**: integer

## Description
Optional duration in seconds the pod may be active on the node relative to StartTime before the system will actively try to mark it failed and kill associated containers. Value must be a positive integer.





---

</details>

<details>
<summary>affinity: Object</summary>

# Deployment.spec.template.spec.affinity

---

**Type**: Object

## Description
If specified, the pod's scheduling constraints




## Fields

<details>
<summary>nodeAffinity: Object</summary>

# Deployment.spec.template.spec.affinity.nodeAffinity

---

**Type**: Object

## Description
Describes node affinity scheduling rules for the pod.




## Fields

<details>
<summary>preferredDuringSchedulingIgnoredDuringExecution: []Object</summary>

# Deployment.spec.template.spec.affinity.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution

---

**Type**: []Object

## Description
The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node matches the corresponding matchExpressions; the node(s) with the highest sum are the most preferred.




## Fields

<details>
<summary>preference: Object required!</summary>

# Deployment.spec.template.spec.affinity.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution.preference

---

**Type**: Object (required)

## Description
A node selector term, associated with the corresponding weight.




## Fields

<details>
<summary>matchExpressions: []Object</summary>

# Deployment.spec.template.spec.affinity.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution.preference.matchExpressions

---

**Type**: []Object

## Description
A list of node selector requirements by node's labels.




## Fields

<details>
<summary>key: string required!</summary>

# Deployment.spec.template.spec.affinity.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution.preference.matchExpressions.key

---

**Type**: string (required)

## Description
The label key that the selector applies to.





---

</details>

<details>
<summary>operator: string required!</summary>

# Deployment.spec.template.spec.affinity.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution.preference.matchExpressions.operator

---

**Type**: string (required)

## Description
Represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.





---

</details>

<details>
<summary>values: []string</summary>

# Deployment.spec.template.spec.affinity.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution.preference.matchExpressions.values

---

**Type**: []string

## Description
An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which will be interpreted as an integer. This array is replaced during a strategic merge patch.





---

</details>



---

</details>

<details>
<summary>matchFields: []Object</summary>

# Deployment.spec.template.spec.affinity.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution.preference.matchFields

---

**Type**: []Object

## Description
A list of node selector requirements by node's fields.




## Fields

<details>
<summary>key: string required!</summary>

# Deployment.spec.template.spec.affinity.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution.preference.matchFields.key

---

**Type**: string (required)

## Description
The label key that the selector applies to.





---

</details>

<details>
<summary>operator: string required!</summary>

# Deployment.spec.template.spec.affinity.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution.preference.matchFields.operator

---

**Type**: string (required)

## Description
Represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.





---

</details>

<details>
<summary>values: []string</summary>

# Deployment.spec.template.spec.affinity.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution.preference.matchFields.values

---

**Type**: []string

## Description
An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which will be interpreted as an integer. This array is replaced during a strategic merge patch.





---

</details>



---

</details>



---

</details>

<details>
<summary>weight: integer required!</summary>

# Deployment.spec.template.spec.affinity.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution.weight

---

**Type**: integer (required)

## Description
Weight associated with matching the corresponding nodeSelectorTerm, in the range 1-100.





---

</details>



---

</details>

<details>
<summary>requiredDuringSchedulingIgnoredDuringExecution: Object</summary>

# Deployment.spec.template.spec.affinity.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution

---

**Type**: Object

## Description
If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to an update), the system may or may not try to eventually evict the pod from its node.




## Fields

<details>
<summary>nodeSelectorTerms: []Object required!</summary>

# Deployment.spec.template.spec.affinity.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms

---

**Type**: []Object (required)

## Description
Required. A list of node selector terms. The terms are ORed.




## Fields

<details>
<summary>matchExpressions: []Object</summary>

# Deployment.spec.template.spec.affinity.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms.matchExpressions

---

**Type**: []Object

## Description
A list of node selector requirements by node's labels.




## Fields

<details>
<summary>key: string required!</summary>

# Deployment.spec.template.spec.affinity.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms.matchExpressions.key

---

**Type**: string (required)

## Description
The label key that the selector applies to.





---

</details>

<details>
<summary>operator: string required!</summary>

# Deployment.spec.template.spec.affinity.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms.matchExpressions.operator

---

**Type**: string (required)

## Description
Represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.





---

</details>

<details>
<summary>values: []string</summary>

# Deployment.spec.template.spec.affinity.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms.matchExpressions.values

---

**Type**: []string

## Description
An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which will be interpreted as an integer. This array is replaced during a strategic merge patch.





---

</details>



---

</details>

<details>
<summary>matchFields: []Object</summary>

# Deployment.spec.template.spec.affinity.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms.matchFields

---

**Type**: []Object

## Description
A list of node selector requirements by node's fields.




## Fields

<details>
<summary>key: string required!</summary>

# Deployment.spec.template.spec.affinity.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms.matchFields.key

---

**Type**: string (required)

## Description
The label key that the selector applies to.





---

</details>

<details>
<summary>operator: string required!</summary>

# Deployment.spec.template.spec.affinity.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms.matchFields.operator

---

**Type**: string (required)

## Description
Represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.





---

</details>

<details>
<summary>values: []string</summary>

# Deployment.spec.template.spec.affinity.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms.matchFields.values

---

**Type**: []string

## Description
An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which will be interpreted as an integer. This array is replaced during a strategic merge patch.





---

</details>



---

</details>



---

</details>



---

</details>



---

</details>

<details>
<summary>podAffinity: Object</summary>

# Deployment.spec.template.spec.affinity.podAffinity

---

**Type**: Object

## Description
Describes pod affinity scheduling rules (e.g. co-locate this pod in the same node, zone, etc. as some other pod(s)).




## Fields

<details>
<summary>preferredDuringSchedulingIgnoredDuringExecution: []Object</summary>

# Deployment.spec.template.spec.affinity.podAffinity.preferredDuringSchedulingIgnoredDuringExecution

---

**Type**: []Object

## Description
The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node has pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most preferred.




## Fields

<details>
<summary>podAffinityTerm: Object required!</summary>

# Deployment.spec.template.spec.affinity.podAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm

---

**Type**: Object (required)

## Description
Required. A pod affinity term, associated with the corresponding weight.




## Fields

<details>
<summary>labelSelector: Object</summary>

# Deployment.spec.template.spec.affinity.podAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.labelSelector

---

**Type**: Object

## Description
A label query over a set of resources, in this case pods.




## Fields

<details>
<summary>matchExpressions: []Object</summary>

# Deployment.spec.template.spec.affinity.podAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.labelSelector.matchExpressions

---

**Type**: []Object

## Description
matchExpressions is a list of label selector requirements. The requirements are ANDed.




## Fields

<details>
<summary>key: string required!</summary>

# Deployment.spec.template.spec.affinity.podAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.labelSelector.matchExpressions.key

---

**Type**: string (required)

## Description
key is the label key that the selector applies to.





---

</details>

<details>
<summary>operator: string required!</summary>

# Deployment.spec.template.spec.affinity.podAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.labelSelector.matchExpressions.operator

---

**Type**: string (required)

## Description
operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.





---

</details>

<details>
<summary>values: []string</summary>

# Deployment.spec.template.spec.affinity.podAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.labelSelector.matchExpressions.values

---

**Type**: []string

## Description
values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.





---

</details>



---

</details>

<details>
<summary>matchLabels: map[string]string</summary>

# Deployment.spec.template.spec.affinity.podAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.labelSelector.matchLabels

---

**Type**: map[string]string

## Description
matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.





---

</details>



---

</details>

<details>
<summary>namespaceSelector: Object</summary>

# Deployment.spec.template.spec.affinity.podAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.namespaceSelector

---

**Type**: Object

## Description
A label query over the set of namespaces that the term applies to. The term is applied to the union of the namespaces selected by this field and the ones listed in the namespaces field. null selector and null or empty namespaces list means "this pod's namespace". An empty selector ({}) matches all namespaces. This field is alpha-level and is only honored when PodAffinityNamespaceSelector feature is enabled.




## Fields

<details>
<summary>matchExpressions: []Object</summary>

# Deployment.spec.template.spec.affinity.podAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.namespaceSelector.matchExpressions

---

**Type**: []Object

## Description
matchExpressions is a list of label selector requirements. The requirements are ANDed.




## Fields

<details>
<summary>key: string required!</summary>

# Deployment.spec.template.spec.affinity.podAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.namespaceSelector.matchExpressions.key

---

**Type**: string (required)

## Description
key is the label key that the selector applies to.





---

</details>

<details>
<summary>operator: string required!</summary>

# Deployment.spec.template.spec.affinity.podAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.namespaceSelector.matchExpressions.operator

---

**Type**: string (required)

## Description
operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.





---

</details>

<details>
<summary>values: []string</summary>

# Deployment.spec.template.spec.affinity.podAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.namespaceSelector.matchExpressions.values

---

**Type**: []string

## Description
values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.





---

</details>



---

</details>

<details>
<summary>matchLabels: map[string]string</summary>

# Deployment.spec.template.spec.affinity.podAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.namespaceSelector.matchLabels

---

**Type**: map[string]string

## Description
matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.





---

</details>



---

</details>

<details>
<summary>namespaces: []string</summary>

# Deployment.spec.template.spec.affinity.podAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.namespaces

---

**Type**: []string

## Description
namespaces specifies a static list of namespace names that the term applies to. The term is applied to the union of the namespaces listed in this field and the ones selected by namespaceSelector. null or empty namespaces list and null namespaceSelector means "this pod's namespace"





---

</details>

<details>
<summary>topologyKey: string required!</summary>

# Deployment.spec.template.spec.affinity.podAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.topologyKey

---

**Type**: string (required)

## Description
This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.





---

</details>



---

</details>

<details>
<summary>weight: integer required!</summary>

# Deployment.spec.template.spec.affinity.podAffinity.preferredDuringSchedulingIgnoredDuringExecution.weight

---

**Type**: integer (required)

## Description
weight associated with matching the corresponding podAffinityTerm, in the range 1-100.





---

</details>



---

</details>

<details>
<summary>requiredDuringSchedulingIgnoredDuringExecution: []Object</summary>

# Deployment.spec.template.spec.affinity.podAffinity.requiredDuringSchedulingIgnoredDuringExecution

---

**Type**: []Object

## Description
If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, i.e. all terms must be satisfied.




## Fields

<details>
<summary>labelSelector: Object</summary>

# Deployment.spec.template.spec.affinity.podAffinity.requiredDuringSchedulingIgnoredDuringExecution.labelSelector

---

**Type**: Object

## Description
A label query over a set of resources, in this case pods.




## Fields

<details>
<summary>matchExpressions: []Object</summary>

# Deployment.spec.template.spec.affinity.podAffinity.requiredDuringSchedulingIgnoredDuringExecution.labelSelector.matchExpressions

---

**Type**: []Object

## Description
matchExpressions is a list of label selector requirements. The requirements are ANDed.




## Fields

<details>
<summary>key: string required!</summary>

# Deployment.spec.template.spec.affinity.podAffinity.requiredDuringSchedulingIgnoredDuringExecution.labelSelector.matchExpressions.key

---

**Type**: string (required)

## Description
key is the label key that the selector applies to.





---

</details>

<details>
<summary>operator: string required!</summary>

# Deployment.spec.template.spec.affinity.podAffinity.requiredDuringSchedulingIgnoredDuringExecution.labelSelector.matchExpressions.operator

---

**Type**: string (required)

## Description
operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.





---

</details>

<details>
<summary>values: []string</summary>

# Deployment.spec.template.spec.affinity.podAffinity.requiredDuringSchedulingIgnoredDuringExecution.labelSelector.matchExpressions.values

---

**Type**: []string

## Description
values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.





---

</details>



---

</details>

<details>
<summary>matchLabels: map[string]string</summary>

# Deployment.spec.template.spec.affinity.podAffinity.requiredDuringSchedulingIgnoredDuringExecution.labelSelector.matchLabels

---

**Type**: map[string]string

## Description
matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.





---

</details>



---

</details>

<details>
<summary>namespaceSelector: Object</summary>

# Deployment.spec.template.spec.affinity.podAffinity.requiredDuringSchedulingIgnoredDuringExecution.namespaceSelector

---

**Type**: Object

## Description
A label query over the set of namespaces that the term applies to. The term is applied to the union of the namespaces selected by this field and the ones listed in the namespaces field. null selector and null or empty namespaces list means "this pod's namespace". An empty selector ({}) matches all namespaces. This field is alpha-level and is only honored when PodAffinityNamespaceSelector feature is enabled.




## Fields

<details>
<summary>matchExpressions: []Object</summary>

# Deployment.spec.template.spec.affinity.podAffinity.requiredDuringSchedulingIgnoredDuringExecution.namespaceSelector.matchExpressions

---

**Type**: []Object

## Description
matchExpressions is a list of label selector requirements. The requirements are ANDed.




## Fields

<details>
<summary>key: string required!</summary>

# Deployment.spec.template.spec.affinity.podAffinity.requiredDuringSchedulingIgnoredDuringExecution.namespaceSelector.matchExpressions.key

---

**Type**: string (required)

## Description
key is the label key that the selector applies to.





---

</details>

<details>
<summary>operator: string required!</summary>

# Deployment.spec.template.spec.affinity.podAffinity.requiredDuringSchedulingIgnoredDuringExecution.namespaceSelector.matchExpressions.operator

---

**Type**: string (required)

## Description
operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.





---

</details>

<details>
<summary>values: []string</summary>

# Deployment.spec.template.spec.affinity.podAffinity.requiredDuringSchedulingIgnoredDuringExecution.namespaceSelector.matchExpressions.values

---

**Type**: []string

## Description
values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.





---

</details>



---

</details>

<details>
<summary>matchLabels: map[string]string</summary>

# Deployment.spec.template.spec.affinity.podAffinity.requiredDuringSchedulingIgnoredDuringExecution.namespaceSelector.matchLabels

---

**Type**: map[string]string

## Description
matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.





---

</details>



---

</details>

<details>
<summary>namespaces: []string</summary>

# Deployment.spec.template.spec.affinity.podAffinity.requiredDuringSchedulingIgnoredDuringExecution.namespaces

---

**Type**: []string

## Description
namespaces specifies a static list of namespace names that the term applies to. The term is applied to the union of the namespaces listed in this field and the ones selected by namespaceSelector. null or empty namespaces list and null namespaceSelector means "this pod's namespace"





---

</details>

<details>
<summary>topologyKey: string required!</summary>

# Deployment.spec.template.spec.affinity.podAffinity.requiredDuringSchedulingIgnoredDuringExecution.topologyKey

---

**Type**: string (required)

## Description
This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.





---

</details>



---

</details>



---

</details>

<details>
<summary>podAntiAffinity: Object</summary>

# Deployment.spec.template.spec.affinity.podAntiAffinity

---

**Type**: Object

## Description
Describes pod anti-affinity scheduling rules (e.g. avoid putting this pod in the same node, zone, etc. as some other pod(s)).




## Fields

<details>
<summary>preferredDuringSchedulingIgnoredDuringExecution: []Object</summary>

# Deployment.spec.template.spec.affinity.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution

---

**Type**: []Object

## Description
The scheduler will prefer to schedule pods to nodes that satisfy the anti-affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling anti-affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node has pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most preferred.




## Fields

<details>
<summary>podAffinityTerm: Object required!</summary>

# Deployment.spec.template.spec.affinity.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm

---

**Type**: Object (required)

## Description
Required. A pod affinity term, associated with the corresponding weight.




## Fields

<details>
<summary>labelSelector: Object</summary>

# Deployment.spec.template.spec.affinity.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.labelSelector

---

**Type**: Object

## Description
A label query over a set of resources, in this case pods.




## Fields

<details>
<summary>matchExpressions: []Object</summary>

# Deployment.spec.template.spec.affinity.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.labelSelector.matchExpressions

---

**Type**: []Object

## Description
matchExpressions is a list of label selector requirements. The requirements are ANDed.




## Fields

<details>
<summary>key: string required!</summary>

# Deployment.spec.template.spec.affinity.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.labelSelector.matchExpressions.key

---

**Type**: string (required)

## Description
key is the label key that the selector applies to.





---

</details>

<details>
<summary>operator: string required!</summary>

# Deployment.spec.template.spec.affinity.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.labelSelector.matchExpressions.operator

---

**Type**: string (required)

## Description
operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.





---

</details>

<details>
<summary>values: []string</summary>

# Deployment.spec.template.spec.affinity.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.labelSelector.matchExpressions.values

---

**Type**: []string

## Description
values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.





---

</details>



---

</details>

<details>
<summary>matchLabels: map[string]string</summary>

# Deployment.spec.template.spec.affinity.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.labelSelector.matchLabels

---

**Type**: map[string]string

## Description
matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.





---

</details>



---

</details>

<details>
<summary>namespaceSelector: Object</summary>

# Deployment.spec.template.spec.affinity.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.namespaceSelector

---

**Type**: Object

## Description
A label query over the set of namespaces that the term applies to. The term is applied to the union of the namespaces selected by this field and the ones listed in the namespaces field. null selector and null or empty namespaces list means "this pod's namespace". An empty selector ({}) matches all namespaces. This field is alpha-level and is only honored when PodAffinityNamespaceSelector feature is enabled.




## Fields

<details>
<summary>matchExpressions: []Object</summary>

# Deployment.spec.template.spec.affinity.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.namespaceSelector.matchExpressions

---

**Type**: []Object

## Description
matchExpressions is a list of label selector requirements. The requirements are ANDed.




## Fields

<details>
<summary>key: string required!</summary>

# Deployment.spec.template.spec.affinity.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.namespaceSelector.matchExpressions.key

---

**Type**: string (required)

## Description
key is the label key that the selector applies to.





---

</details>

<details>
<summary>operator: string required!</summary>

# Deployment.spec.template.spec.affinity.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.namespaceSelector.matchExpressions.operator

---

**Type**: string (required)

## Description
operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.





---

</details>

<details>
<summary>values: []string</summary>

# Deployment.spec.template.spec.affinity.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.namespaceSelector.matchExpressions.values

---

**Type**: []string

## Description
values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.





---

</details>



---

</details>

<details>
<summary>matchLabels: map[string]string</summary>

# Deployment.spec.template.spec.affinity.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.namespaceSelector.matchLabels

---

**Type**: map[string]string

## Description
matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.





---

</details>



---

</details>

<details>
<summary>namespaces: []string</summary>

# Deployment.spec.template.spec.affinity.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.namespaces

---

**Type**: []string

## Description
namespaces specifies a static list of namespace names that the term applies to. The term is applied to the union of the namespaces listed in this field and the ones selected by namespaceSelector. null or empty namespaces list and null namespaceSelector means "this pod's namespace"





---

</details>

<details>
<summary>topologyKey: string required!</summary>

# Deployment.spec.template.spec.affinity.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.topologyKey

---

**Type**: string (required)

## Description
This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.





---

</details>



---

</details>

<details>
<summary>weight: integer required!</summary>

# Deployment.spec.template.spec.affinity.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.weight

---

**Type**: integer (required)

## Description
weight associated with matching the corresponding podAffinityTerm, in the range 1-100.





---

</details>



---

</details>

<details>
<summary>requiredDuringSchedulingIgnoredDuringExecution: []Object</summary>

# Deployment.spec.template.spec.affinity.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution

---

**Type**: []Object

## Description
If the anti-affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the anti-affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, i.e. all terms must be satisfied.




## Fields

<details>
<summary>labelSelector: Object</summary>

# Deployment.spec.template.spec.affinity.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.labelSelector

---

**Type**: Object

## Description
A label query over a set of resources, in this case pods.




## Fields

<details>
<summary>matchExpressions: []Object</summary>

# Deployment.spec.template.spec.affinity.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.labelSelector.matchExpressions

---

**Type**: []Object

## Description
matchExpressions is a list of label selector requirements. The requirements are ANDed.




## Fields

<details>
<summary>key: string required!</summary>

# Deployment.spec.template.spec.affinity.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.labelSelector.matchExpressions.key

---

**Type**: string (required)

## Description
key is the label key that the selector applies to.





---

</details>

<details>
<summary>operator: string required!</summary>

# Deployment.spec.template.spec.affinity.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.labelSelector.matchExpressions.operator

---

**Type**: string (required)

## Description
operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.





---

</details>

<details>
<summary>values: []string</summary>

# Deployment.spec.template.spec.affinity.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.labelSelector.matchExpressions.values

---

**Type**: []string

## Description
values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.





---

</details>



---

</details>

<details>
<summary>matchLabels: map[string]string</summary>

# Deployment.spec.template.spec.affinity.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.labelSelector.matchLabels

---

**Type**: map[string]string

## Description
matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.





---

</details>



---

</details>

<details>
<summary>namespaceSelector: Object</summary>

# Deployment.spec.template.spec.affinity.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.namespaceSelector

---

**Type**: Object

## Description
A label query over the set of namespaces that the term applies to. The term is applied to the union of the namespaces selected by this field and the ones listed in the namespaces field. null selector and null or empty namespaces list means "this pod's namespace". An empty selector ({}) matches all namespaces. This field is alpha-level and is only honored when PodAffinityNamespaceSelector feature is enabled.




## Fields

<details>
<summary>matchExpressions: []Object</summary>

# Deployment.spec.template.spec.affinity.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.namespaceSelector.matchExpressions

---

**Type**: []Object

## Description
matchExpressions is a list of label selector requirements. The requirements are ANDed.




## Fields

<details>
<summary>key: string required!</summary>

# Deployment.spec.template.spec.affinity.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.namespaceSelector.matchExpressions.key

---

**Type**: string (required)

## Description
key is the label key that the selector applies to.





---

</details>

<details>
<summary>operator: string required!</summary>

# Deployment.spec.template.spec.affinity.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.namespaceSelector.matchExpressions.operator

---

**Type**: string (required)

## Description
operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.





---

</details>

<details>
<summary>values: []string</summary>

# Deployment.spec.template.spec.affinity.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.namespaceSelector.matchExpressions.values

---

**Type**: []string

## Description
values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.





---

</details>



---

</details>

<details>
<summary>matchLabels: map[string]string</summary>

# Deployment.spec.template.spec.affinity.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.namespaceSelector.matchLabels

---

**Type**: map[string]string

## Description
matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.





---

</details>



---

</details>

<details>
<summary>namespaces: []string</summary>

# Deployment.spec.template.spec.affinity.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.namespaces

---

**Type**: []string

## Description
namespaces specifies a static list of namespace names that the term applies to. The term is applied to the union of the namespaces listed in this field and the ones selected by namespaceSelector. null or empty namespaces list and null namespaceSelector means "this pod's namespace"





---

</details>

<details>
<summary>topologyKey: string required!</summary>

# Deployment.spec.template.spec.affinity.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.topologyKey

---

**Type**: string (required)

## Description
This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.





---

</details>



---

</details>



---

</details>



---

</details>

<details>
<summary>automountServiceAccountToken: boolean</summary>

# Deployment.spec.template.spec.automountServiceAccountToken

---

**Type**: boolean

## Description
AutomountServiceAccountToken indicates whether a service account token should be automatically mounted.





---

</details>

<details>
<summary>containers: []Object required!</summary>

# Deployment.spec.template.spec.containers

---

**Type**: []Object (required)

## Description
List of containers belonging to the pod. Containers cannot currently be added or removed. There must be at least one container in a Pod. Cannot be updated.




## Fields

<details>
<summary>args: []string</summary>

# Deployment.spec.template.spec.containers.args

---

**Type**: []string

## Description
Arguments to the entrypoint. The docker image's CMD is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell





---

</details>

<details>
<summary>command: []string</summary>

# Deployment.spec.template.spec.containers.command

---

**Type**: []string

## Description
Entrypoint array. Not executed within a shell. The docker image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell





---

</details>

<details>
<summary>env: []Object</summary>

# Deployment.spec.template.spec.containers.env

---

**Type**: []Object

## Description
List of environment variables to set in the container. Cannot be updated.




## Fields

<details>
<summary>name: string required!</summary>

# Deployment.spec.template.spec.containers.env.name

---

**Type**: string (required)

## Description
Name of the environment variable. Must be a C_IDENTIFIER.





---

</details>

<details>
<summary>value: string</summary>

# Deployment.spec.template.spec.containers.env.value

---

**Type**: string

## Description
Variable references $(VAR_NAME) are expanded using the previous defined environment variables in the container and any service environment variables. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Defaults to "".





---

</details>

<details>
<summary>valueFrom: Object</summary>

# Deployment.spec.template.spec.containers.env.valueFrom

---

**Type**: Object

## Description
Source for the environment variable's value. Cannot be used if value is not empty.




## Fields

<details>
<summary>configMapKeyRef: Object</summary>

# Deployment.spec.template.spec.containers.env.valueFrom.configMapKeyRef

---

**Type**: Object

## Description
Selects a key of a ConfigMap.




## Fields

<details>
<summary>key: string required!</summary>

# Deployment.spec.template.spec.containers.env.valueFrom.configMapKeyRef.key

---

**Type**: string (required)

## Description
The key to select.





---

</details>

<details>
<summary>name: string</summary>

# Deployment.spec.template.spec.containers.env.valueFrom.configMapKeyRef.name

---

**Type**: string

## Description
Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names





---

</details>

<details>
<summary>optional: boolean</summary>

# Deployment.spec.template.spec.containers.env.valueFrom.configMapKeyRef.optional

---

**Type**: boolean

## Description
Specify whether the ConfigMap or its key must be defined





---

</details>



---

</details>

<details>
<summary>fieldRef: Object</summary>

# Deployment.spec.template.spec.containers.env.valueFrom.fieldRef

---

**Type**: Object

## Description
Selects a field of the pod: supports metadata.name, metadata.namespace, `metadata.labels['<KEY>']`, `metadata.annotations['<KEY>']`, spec.nodeName, spec.serviceAccountName, status.hostIP, status.podIP, status.podIPs.




## Fields

<details>
<summary>apiVersion: string</summary>

# Deployment.spec.template.spec.containers.env.valueFrom.fieldRef.apiVersion

---

**Type**: string

## Description
Version of the schema the FieldPath is written in terms of, defaults to "v1".





---

</details>

<details>
<summary>fieldPath: string required!</summary>

# Deployment.spec.template.spec.containers.env.valueFrom.fieldRef.fieldPath

---

**Type**: string (required)

## Description
Path of the field to select in the specified API version.





---

</details>



---

</details>

<details>
<summary>resourceFieldRef: Object</summary>

# Deployment.spec.template.spec.containers.env.valueFrom.resourceFieldRef

---

**Type**: Object

## Description
Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, limits.ephemeral-storage, requests.cpu, requests.memory and requests.ephemeral-storage) are currently supported.




## Fields

<details>
<summary>containerName: string</summary>

# Deployment.spec.template.spec.containers.env.valueFrom.resourceFieldRef.containerName

---

**Type**: string

## Description
Container name: required for volumes, optional for env vars





---

</details>

<details>
<summary>divisor: string</summary>

# Deployment.spec.template.spec.containers.env.valueFrom.resourceFieldRef.divisor

---

**Type**: string

## Description
Specifies the output format of the exposed resources, defaults to "1"





---

</details>

<details>
<summary>resource: string required!</summary>

# Deployment.spec.template.spec.containers.env.valueFrom.resourceFieldRef.resource

---

**Type**: string (required)

## Description
Required: resource to select





---

</details>



---

</details>

<details>
<summary>secretKeyRef: Object</summary>

# Deployment.spec.template.spec.containers.env.valueFrom.secretKeyRef

---

**Type**: Object

## Description
Selects a key of a secret in the pod's namespace




## Fields

<details>
<summary>key: string required!</summary>

# Deployment.spec.template.spec.containers.env.valueFrom.secretKeyRef.key

---

**Type**: string (required)

## Description
The key of the secret to select from. Must be a valid secret key.





---

</details>

<details>
<summary>name: string</summary>

# Deployment.spec.template.spec.containers.env.valueFrom.secretKeyRef.name

---

**Type**: string

## Description
Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names





---

</details>

<details>
<summary>optional: boolean</summary>

# Deployment.spec.template.spec.containers.env.valueFrom.secretKeyRef.optional

---

**Type**: boolean

## Description
Specify whether the Secret or its key must be defined





---

</details>



---

</details>



---

</details>



---

</details>

<details>
<summary>envFrom: []Object</summary>

# Deployment.spec.template.spec.containers.envFrom

---

**Type**: []Object

## Description
List of sources to populate environment variables in the container. The keys defined within a source must be a C_IDENTIFIER. All invalid keys will be reported as an event when the container is starting. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated.




## Fields

<details>
<summary>configMapRef: Object</summary>

# Deployment.spec.template.spec.containers.envFrom.configMapRef

---

**Type**: Object

## Description
The ConfigMap to select from




## Fields

<details>
<summary>name: string</summary>

# Deployment.spec.template.spec.containers.envFrom.configMapRef.name

---

**Type**: string

## Description
Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names





---

</details>

<details>
<summary>optional: boolean</summary>

# Deployment.spec.template.spec.containers.envFrom.configMapRef.optional

---

**Type**: boolean

## Description
Specify whether the ConfigMap must be defined





---

</details>



---

</details>

<details>
<summary>prefix: string</summary>

# Deployment.spec.template.spec.containers.envFrom.prefix

---

**Type**: string

## Description
An optional identifier to prepend to each key in the ConfigMap. Must be a C_IDENTIFIER.





---

</details>

<details>
<summary>secretRef: Object</summary>

# Deployment.spec.template.spec.containers.envFrom.secretRef

---

**Type**: Object

## Description
The Secret to select from




## Fields

<details>
<summary>name: string</summary>

# Deployment.spec.template.spec.containers.envFrom.secretRef.name

---

**Type**: string

## Description
Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names





---

</details>

<details>
<summary>optional: boolean</summary>

# Deployment.spec.template.spec.containers.envFrom.secretRef.optional

---

**Type**: boolean

## Description
Specify whether the Secret must be defined





---

</details>



---

</details>



---

</details>

<details>
<summary>image: string</summary>

# Deployment.spec.template.spec.containers.image

---

**Type**: string

## Description
Docker image name. More info: https://kubernetes.io/docs/concepts/containers/images This field is optional to allow higher level config management to default or override container images in workload controllers like Deployments and StatefulSets.





---

</details>

<details>
<summary>imagePullPolicy: string</summary>

# Deployment.spec.template.spec.containers.imagePullPolicy

---

**Type**: string

## Description
Image pull policy. One of Always, Never, IfNotPresent. Defaults to Always if :latest tag is specified, or IfNotPresent otherwise. Cannot be updated. More info: https://kubernetes.io/docs/concepts/containers/images#updating-images





---

</details>

<details>
<summary>lifecycle: Object</summary>

# Deployment.spec.template.spec.containers.lifecycle

---

**Type**: Object

## Description
Actions that the management system should take in response to container lifecycle events. Cannot be updated.




## Fields

<details>
<summary>postStart: Object</summary>

# Deployment.spec.template.spec.containers.lifecycle.postStart

---

**Type**: Object

## Description
PostStart is called immediately after a container is created. If the handler fails, the container is terminated and restarted according to its restart policy. Other management of the container blocks until the hook completes. More info: https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks




## Fields

<details>
<summary>exec: Object</summary>

# Deployment.spec.template.spec.containers.lifecycle.postStart.exec

---

**Type**: Object

## Description
One and only one of the following should be specified. Exec specifies the action to take.




## Fields

<details>
<summary>command: []string</summary>

# Deployment.spec.template.spec.containers.lifecycle.postStart.exec.command

---

**Type**: []string

## Description
Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container's filesystem. The command is simply exec'd, it is not run inside a shell, so traditional shell instructions ('|', etc) won't work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy.





---

</details>



---

</details>

<details>
<summary>httpGet: Object</summary>

# Deployment.spec.template.spec.containers.lifecycle.postStart.httpGet

---

**Type**: Object

## Description
HTTPGet specifies the http request to perform.




## Fields

<details>
<summary>host: string</summary>

# Deployment.spec.template.spec.containers.lifecycle.postStart.httpGet.host

---

**Type**: string

## Description
Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.





---

</details>

<details>
<summary>httpHeaders: []Object</summary>

# Deployment.spec.template.spec.containers.lifecycle.postStart.httpGet.httpHeaders

---

**Type**: []Object

## Description
Custom headers to set in the request. HTTP allows repeated headers.




## Fields

<details>
<summary>name: string required!</summary>

# Deployment.spec.template.spec.containers.lifecycle.postStart.httpGet.httpHeaders.name

---

**Type**: string (required)

## Description
The header field name





---

</details>

<details>
<summary>value: string required!</summary>

# Deployment.spec.template.spec.containers.lifecycle.postStart.httpGet.httpHeaders.value

---

**Type**: string (required)

## Description
The header field value





---

</details>



---

</details>

<details>
<summary>path: string</summary>

# Deployment.spec.template.spec.containers.lifecycle.postStart.httpGet.path

---

**Type**: string

## Description
Path to access on the HTTP server.





---

</details>

<details>
<summary>port: string required!</summary>

# Deployment.spec.template.spec.containers.lifecycle.postStart.httpGet.port

---

**Type**: string (required)

## Description
Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.





---

</details>

<details>
<summary>scheme: string</summary>

# Deployment.spec.template.spec.containers.lifecycle.postStart.httpGet.scheme

---

**Type**: string

## Description
Scheme to use for connecting to the host. Defaults to HTTP.





---

</details>



---

</details>

<details>
<summary>tcpSocket: Object</summary>

# Deployment.spec.template.spec.containers.lifecycle.postStart.tcpSocket

---

**Type**: Object

## Description
TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported




## Fields

<details>
<summary>host: string</summary>

# Deployment.spec.template.spec.containers.lifecycle.postStart.tcpSocket.host

---

**Type**: string

## Description
Optional: Host name to connect to, defaults to the pod IP.





---

</details>

<details>
<summary>port: string required!</summary>

# Deployment.spec.template.spec.containers.lifecycle.postStart.tcpSocket.port

---

**Type**: string (required)

## Description
Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.





---

</details>



---

</details>



---

</details>

<details>
<summary>preStop: Object</summary>

# Deployment.spec.template.spec.containers.lifecycle.preStop

---

**Type**: Object

## Description
PreStop is called immediately before a container is terminated due to an API request or management event such as liveness/startup probe failure, preemption, resource contention, etc. The handler is not called if the container crashes or exits. The reason for termination is passed to the handler. The Pod's termination grace period countdown begins before the PreStop hooked is executed. Regardless of the outcome of the handler, the container will eventually terminate within the Pod's termination grace period. Other management of the container blocks until the hook completes or until the termination grace period is reached. More info: https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks




## Fields

<details>
<summary>exec: Object</summary>

# Deployment.spec.template.spec.containers.lifecycle.preStop.exec

---

**Type**: Object

## Description
One and only one of the following should be specified. Exec specifies the action to take.




## Fields

<details>
<summary>command: []string</summary>

# Deployment.spec.template.spec.containers.lifecycle.preStop.exec.command

---

**Type**: []string

## Description
Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container's filesystem. The command is simply exec'd, it is not run inside a shell, so traditional shell instructions ('|', etc) won't work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy.





---

</details>



---

</details>

<details>
<summary>httpGet: Object</summary>

# Deployment.spec.template.spec.containers.lifecycle.preStop.httpGet

---

**Type**: Object

## Description
HTTPGet specifies the http request to perform.




## Fields

<details>
<summary>host: string</summary>

# Deployment.spec.template.spec.containers.lifecycle.preStop.httpGet.host

---

**Type**: string

## Description
Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.





---

</details>

<details>
<summary>httpHeaders: []Object</summary>

# Deployment.spec.template.spec.containers.lifecycle.preStop.httpGet.httpHeaders

---

**Type**: []Object

## Description
Custom headers to set in the request. HTTP allows repeated headers.




## Fields

<details>
<summary>name: string required!</summary>

# Deployment.spec.template.spec.containers.lifecycle.preStop.httpGet.httpHeaders.name

---

**Type**: string (required)

## Description
The header field name





---

</details>

<details>
<summary>value: string required!</summary>

# Deployment.spec.template.spec.containers.lifecycle.preStop.httpGet.httpHeaders.value

---

**Type**: string (required)

## Description
The header field value





---

</details>



---

</details>

<details>
<summary>path: string</summary>

# Deployment.spec.template.spec.containers.lifecycle.preStop.httpGet.path

---

**Type**: string

## Description
Path to access on the HTTP server.





---

</details>

<details>
<summary>port: string required!</summary>

# Deployment.spec.template.spec.containers.lifecycle.preStop.httpGet.port

---

**Type**: string (required)

## Description
Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.





---

</details>

<details>
<summary>scheme: string</summary>

# Deployment.spec.template.spec.containers.lifecycle.preStop.httpGet.scheme

---

**Type**: string

## Description
Scheme to use for connecting to the host. Defaults to HTTP.





---

</details>



---

</details>

<details>
<summary>tcpSocket: Object</summary>

# Deployment.spec.template.spec.containers.lifecycle.preStop.tcpSocket

---

**Type**: Object

## Description
TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported




## Fields

<details>
<summary>host: string</summary>

# Deployment.spec.template.spec.containers.lifecycle.preStop.tcpSocket.host

---

**Type**: string

## Description
Optional: Host name to connect to, defaults to the pod IP.





---

</details>

<details>
<summary>port: string required!</summary>

# Deployment.spec.template.spec.containers.lifecycle.preStop.tcpSocket.port

---

**Type**: string (required)

## Description
Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.





---

</details>



---

</details>



---

</details>



---

</details>

<details>
<summary>livenessProbe: Object</summary>

# Deployment.spec.template.spec.containers.livenessProbe

---

**Type**: Object

## Description
Periodic probe of container liveness. Container will be restarted if the probe fails. Cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes




## Fields

<details>
<summary>exec: Object</summary>

# Deployment.spec.template.spec.containers.livenessProbe.exec

---

**Type**: Object

## Description
One and only one of the following should be specified. Exec specifies the action to take.




## Fields

<details>
<summary>command: []string</summary>

# Deployment.spec.template.spec.containers.livenessProbe.exec.command

---

**Type**: []string

## Description
Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container's filesystem. The command is simply exec'd, it is not run inside a shell, so traditional shell instructions ('|', etc) won't work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy.





---

</details>



---

</details>

<details>
<summary>failureThreshold: integer</summary>

# Deployment.spec.template.spec.containers.livenessProbe.failureThreshold

---

**Type**: integer

## Description
Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1.





---

</details>

<details>
<summary>httpGet: Object</summary>

# Deployment.spec.template.spec.containers.livenessProbe.httpGet

---

**Type**: Object

## Description
HTTPGet specifies the http request to perform.




## Fields

<details>
<summary>host: string</summary>

# Deployment.spec.template.spec.containers.livenessProbe.httpGet.host

---

**Type**: string

## Description
Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.





---

</details>

<details>
<summary>httpHeaders: []Object</summary>

# Deployment.spec.template.spec.containers.livenessProbe.httpGet.httpHeaders

---

**Type**: []Object

## Description
Custom headers to set in the request. HTTP allows repeated headers.




## Fields

<details>
<summary>name: string required!</summary>

# Deployment.spec.template.spec.containers.livenessProbe.httpGet.httpHeaders.name

---

**Type**: string (required)

## Description
The header field name





---

</details>

<details>
<summary>value: string required!</summary>

# Deployment.spec.template.spec.containers.livenessProbe.httpGet.httpHeaders.value

---

**Type**: string (required)

## Description
The header field value





---

</details>



---

</details>

<details>
<summary>path: string</summary>

# Deployment.spec.template.spec.containers.livenessProbe.httpGet.path

---

**Type**: string

## Description
Path to access on the HTTP server.





---

</details>

<details>
<summary>port: string required!</summary>

# Deployment.spec.template.spec.containers.livenessProbe.httpGet.port

---

**Type**: string (required)

## Description
Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.





---

</details>

<details>
<summary>scheme: string</summary>

# Deployment.spec.template.spec.containers.livenessProbe.httpGet.scheme

---

**Type**: string

## Description
Scheme to use for connecting to the host. Defaults to HTTP.





---

</details>



---

</details>

<details>
<summary>initialDelaySeconds: integer</summary>

# Deployment.spec.template.spec.containers.livenessProbe.initialDelaySeconds

---

**Type**: integer

## Description
Number of seconds after the container has started before liveness probes are initiated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes





---

</details>

<details>
<summary>periodSeconds: integer</summary>

# Deployment.spec.template.spec.containers.livenessProbe.periodSeconds

---

**Type**: integer

## Description
How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1.





---

</details>

<details>
<summary>successThreshold: integer</summary>

# Deployment.spec.template.spec.containers.livenessProbe.successThreshold

---

**Type**: integer

## Description
Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1.





---

</details>

<details>
<summary>tcpSocket: Object</summary>

# Deployment.spec.template.spec.containers.livenessProbe.tcpSocket

---

**Type**: Object

## Description
TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported




## Fields

<details>
<summary>host: string</summary>

# Deployment.spec.template.spec.containers.livenessProbe.tcpSocket.host

---

**Type**: string

## Description
Optional: Host name to connect to, defaults to the pod IP.





---

</details>

<details>
<summary>port: string required!</summary>

# Deployment.spec.template.spec.containers.livenessProbe.tcpSocket.port

---

**Type**: string (required)

## Description
Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.





---

</details>



---

</details>

<details>
<summary>terminationGracePeriodSeconds: integer</summary>

# Deployment.spec.template.spec.containers.livenessProbe.terminationGracePeriodSeconds

---

**Type**: integer

## Description
Optional duration in seconds the pod needs to terminate gracefully upon probe failure. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. If this value is nil, the pod's terminationGracePeriodSeconds will be used. Otherwise, this value overrides the value provided by the pod spec. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). This is an alpha field and requires enabling ProbeTerminationGracePeriod feature gate.





---

</details>

<details>
<summary>timeoutSeconds: integer</summary>

# Deployment.spec.template.spec.containers.livenessProbe.timeoutSeconds

---

**Type**: integer

## Description
Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes





---

</details>



---

</details>

<details>
<summary>name: string required!</summary>

# Deployment.spec.template.spec.containers.name

---

**Type**: string (required)

## Description
Name of the container specified as a DNS_LABEL. Each container in a pod must have a unique name (DNS_LABEL). Cannot be updated.





---

</details>

<details>
<summary>ports: []Object</summary>

# Deployment.spec.template.spec.containers.ports

---

**Type**: []Object

## Description
List of ports to expose from the container. Exposing a port here gives the system additional information about the network connections a container uses, but is primarily informational. Not specifying a port here DOES NOT prevent that port from being exposed. Any port which is listening on the default "0.0.0.0" address inside a container will be accessible from the network. Cannot be updated.




## Fields

<details>
<summary>containerPort: integer required!</summary>

# Deployment.spec.template.spec.containers.ports.containerPort

---

**Type**: integer (required)

## Description
Number of port to expose on the pod's IP address. This must be a valid port number, 0 < x < 65536.





---

</details>

<details>
<summary>hostIP: string</summary>

# Deployment.spec.template.spec.containers.ports.hostIP

---

**Type**: string

## Description
What host IP to bind the external port to.





---

</details>

<details>
<summary>hostPort: integer</summary>

# Deployment.spec.template.spec.containers.ports.hostPort

---

**Type**: integer

## Description
Number of port to expose on the host. If specified, this must be a valid port number, 0 < x < 65536. If HostNetwork is specified, this must match ContainerPort. Most containers do not need this.





---

</details>

<details>
<summary>name: string</summary>

# Deployment.spec.template.spec.containers.ports.name

---

**Type**: string

## Description
If specified, this must be an IANA_SVC_NAME and unique within the pod. Each named port in a pod must have a unique name. Name for the port that can be referred to by services.





---

</details>

<details>
<summary>protocol: string</summary>

# Deployment.spec.template.spec.containers.ports.protocol

---

**Type**: string

## Description
Protocol for port. Must be UDP, TCP, or SCTP. Defaults to "TCP".





---

</details>



---

</details>

<details>
<summary>readinessProbe: Object</summary>

# Deployment.spec.template.spec.containers.readinessProbe

---

**Type**: Object

## Description
Periodic probe of container service readiness. Container will be removed from service endpoints if the probe fails. Cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes




## Fields

<details>
<summary>exec: Object</summary>

# Deployment.spec.template.spec.containers.readinessProbe.exec

---

**Type**: Object

## Description
One and only one of the following should be specified. Exec specifies the action to take.




## Fields

<details>
<summary>command: []string</summary>

# Deployment.spec.template.spec.containers.readinessProbe.exec.command

---

**Type**: []string

## Description
Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container's filesystem. The command is simply exec'd, it is not run inside a shell, so traditional shell instructions ('|', etc) won't work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy.





---

</details>



---

</details>

<details>
<summary>failureThreshold: integer</summary>

# Deployment.spec.template.spec.containers.readinessProbe.failureThreshold

---

**Type**: integer

## Description
Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1.





---

</details>

<details>
<summary>httpGet: Object</summary>

# Deployment.spec.template.spec.containers.readinessProbe.httpGet

---

**Type**: Object

## Description
HTTPGet specifies the http request to perform.




## Fields

<details>
<summary>host: string</summary>

# Deployment.spec.template.spec.containers.readinessProbe.httpGet.host

---

**Type**: string

## Description
Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.





---

</details>

<details>
<summary>httpHeaders: []Object</summary>

# Deployment.spec.template.spec.containers.readinessProbe.httpGet.httpHeaders

---

**Type**: []Object

## Description
Custom headers to set in the request. HTTP allows repeated headers.




## Fields

<details>
<summary>name: string required!</summary>

# Deployment.spec.template.spec.containers.readinessProbe.httpGet.httpHeaders.name

---

**Type**: string (required)

## Description
The header field name





---

</details>

<details>
<summary>value: string required!</summary>

# Deployment.spec.template.spec.containers.readinessProbe.httpGet.httpHeaders.value

---

**Type**: string (required)

## Description
The header field value





---

</details>



---

</details>

<details>
<summary>path: string</summary>

# Deployment.spec.template.spec.containers.readinessProbe.httpGet.path

---

**Type**: string

## Description
Path to access on the HTTP server.





---

</details>

<details>
<summary>port: string required!</summary>

# Deployment.spec.template.spec.containers.readinessProbe.httpGet.port

---

**Type**: string (required)

## Description
Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.





---

</details>

<details>
<summary>scheme: string</summary>

# Deployment.spec.template.spec.containers.readinessProbe.httpGet.scheme

---

**Type**: string

## Description
Scheme to use for connecting to the host. Defaults to HTTP.





---

</details>



---

</details>

<details>
<summary>initialDelaySeconds: integer</summary>

# Deployment.spec.template.spec.containers.readinessProbe.initialDelaySeconds

---

**Type**: integer

## Description
Number of seconds after the container has started before liveness probes are initiated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes





---

</details>

<details>
<summary>periodSeconds: integer</summary>

# Deployment.spec.template.spec.containers.readinessProbe.periodSeconds

---

**Type**: integer

## Description
How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1.





---

</details>

<details>
<summary>successThreshold: integer</summary>

# Deployment.spec.template.spec.containers.readinessProbe.successThreshold

---

**Type**: integer

## Description
Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1.





---

</details>

<details>
<summary>tcpSocket: Object</summary>

# Deployment.spec.template.spec.containers.readinessProbe.tcpSocket

---

**Type**: Object

## Description
TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported




## Fields

<details>
<summary>host: string</summary>

# Deployment.spec.template.spec.containers.readinessProbe.tcpSocket.host

---

**Type**: string

## Description
Optional: Host name to connect to, defaults to the pod IP.





---

</details>

<details>
<summary>port: string required!</summary>

# Deployment.spec.template.spec.containers.readinessProbe.tcpSocket.port

---

**Type**: string (required)

## Description
Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.





---

</details>



---

</details>

<details>
<summary>terminationGracePeriodSeconds: integer</summary>

# Deployment.spec.template.spec.containers.readinessProbe.terminationGracePeriodSeconds

---

**Type**: integer

## Description
Optional duration in seconds the pod needs to terminate gracefully upon probe failure. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. If this value is nil, the pod's terminationGracePeriodSeconds will be used. Otherwise, this value overrides the value provided by the pod spec. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). This is an alpha field and requires enabling ProbeTerminationGracePeriod feature gate.





---

</details>

<details>
<summary>timeoutSeconds: integer</summary>

# Deployment.spec.template.spec.containers.readinessProbe.timeoutSeconds

---

**Type**: integer

## Description
Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes





---

</details>



---

</details>

<details>
<summary>resources: Object</summary>

# Deployment.spec.template.spec.containers.resources

---

**Type**: Object

## Description
Compute Resources required by this container. Cannot be updated. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/




## Fields

<details>
<summary>limits: map[string]string</summary>

# Deployment.spec.template.spec.containers.resources.limits

---

**Type**: map[string]string

## Description
Limits describes the maximum amount of compute resources allowed. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/





---

</details>

<details>
<summary>requests: map[string]string</summary>

# Deployment.spec.template.spec.containers.resources.requests

---

**Type**: map[string]string

## Description
Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/





---

</details>



---

</details>

<details>
<summary>securityContext: Object</summary>

# Deployment.spec.template.spec.containers.securityContext

---

**Type**: Object

## Description
Security options the pod should run with. More info: https://kubernetes.io/docs/concepts/policy/security-context/ More info: https://kubernetes.io/docs/tasks/configure-pod-container/security-context/




## Fields

<details>
<summary>allowPrivilegeEscalation: boolean</summary>

# Deployment.spec.template.spec.containers.securityContext.allowPrivilegeEscalation

---

**Type**: boolean

## Description
AllowPrivilegeEscalation controls whether a process can gain more privileges than its parent process. This bool directly controls if the no_new_privs flag will be set on the container process. AllowPrivilegeEscalation is true always when the container is: 1) run as Privileged 2) has CAP_SYS_ADMIN





---

</details>

<details>
<summary>capabilities: Object</summary>

# Deployment.spec.template.spec.containers.securityContext.capabilities

---

**Type**: Object

## Description
The capabilities to add/drop when running containers. Defaults to the default set of capabilities granted by the container runtime.




## Fields

<details>
<summary>add: []string</summary>

# Deployment.spec.template.spec.containers.securityContext.capabilities.add

---

**Type**: []string

## Description
Added capabilities





---

</details>

<details>
<summary>drop: []string</summary>

# Deployment.spec.template.spec.containers.securityContext.capabilities.drop

---

**Type**: []string

## Description
Removed capabilities





---

</details>



---

</details>

<details>
<summary>privileged: boolean</summary>

# Deployment.spec.template.spec.containers.securityContext.privileged

---

**Type**: boolean

## Description
Run container in privileged mode. Processes in privileged containers are essentially equivalent to root on the host. Defaults to false.





---

</details>

<details>
<summary>procMount: string</summary>

# Deployment.spec.template.spec.containers.securityContext.procMount

---

**Type**: string

## Description
procMount denotes the type of proc mount to use for the containers. The default is DefaultProcMount which uses the container runtime defaults for readonly paths and masked paths. This requires the ProcMountType feature flag to be enabled.





---

</details>

<details>
<summary>readOnlyRootFilesystem: boolean</summary>

# Deployment.spec.template.spec.containers.securityContext.readOnlyRootFilesystem

---

**Type**: boolean

## Description
Whether this container has a read-only root filesystem. Default is false.





---

</details>

<details>
<summary>runAsGroup: integer</summary>

# Deployment.spec.template.spec.containers.securityContext.runAsGroup

---

**Type**: integer

## Description
The GID to run the entrypoint of the container process. Uses runtime default if unset. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.





---

</details>

<details>
<summary>runAsNonRoot: boolean</summary>

# Deployment.spec.template.spec.containers.securityContext.runAsNonRoot

---

**Type**: boolean

## Description
Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.





---

</details>

<details>
<summary>runAsUser: integer</summary>

# Deployment.spec.template.spec.containers.securityContext.runAsUser

---

**Type**: integer

## Description
The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.





---

</details>

<details>
<summary>seLinuxOptions: Object</summary>

# Deployment.spec.template.spec.containers.securityContext.seLinuxOptions

---

**Type**: Object

## Description
The SELinux context to be applied to the container. If unspecified, the container runtime will allocate a random SELinux context for each container. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.




## Fields

<details>
<summary>level: string</summary>

# Deployment.spec.template.spec.containers.securityContext.seLinuxOptions.level

---

**Type**: string

## Description
Level is SELinux level label that applies to the container.





---

</details>

<details>
<summary>role: string</summary>

# Deployment.spec.template.spec.containers.securityContext.seLinuxOptions.role

---

**Type**: string

## Description
Role is a SELinux role label that applies to the container.





---

</details>

<details>
<summary>type: string</summary>

# Deployment.spec.template.spec.containers.securityContext.seLinuxOptions.type

---

**Type**: string

## Description
Type is a SELinux type label that applies to the container.





---

</details>

<details>
<summary>user: string</summary>

# Deployment.spec.template.spec.containers.securityContext.seLinuxOptions.user

---

**Type**: string

## Description
User is a SELinux user label that applies to the container.





---

</details>



---

</details>

<details>
<summary>seccompProfile: Object</summary>

# Deployment.spec.template.spec.containers.securityContext.seccompProfile

---

**Type**: Object

## Description
The seccomp options to use by this container. If seccomp options are provided at both the pod & container level, the container options override the pod options.




## Fields

<details>
<summary>localhostProfile: string</summary>

# Deployment.spec.template.spec.containers.securityContext.seccompProfile.localhostProfile

---

**Type**: string

## Description
localhostProfile indicates a profile defined in a file on the node should be used. The profile must be preconfigured on the node to work. Must be a descending path, relative to the kubelet's configured seccomp profile location. Must only be set if type is "Localhost".





---

</details>

<details>
<summary>type: string required!</summary>

# Deployment.spec.template.spec.containers.securityContext.seccompProfile.type

---

**Type**: string (required)

## Description
type indicates which kind of seccomp profile will be applied. Valid options are:      Localhost - a profile defined in a file on the node should be used. RuntimeDefault - the container runtime default profile should be used. Unconfined - no profile should be applied.





---

</details>



---

</details>

<details>
<summary>windowsOptions: Object</summary>

# Deployment.spec.template.spec.containers.securityContext.windowsOptions

---

**Type**: Object

## Description
The Windows specific settings applied to all containers. If unspecified, the options from the PodSecurityContext will be used. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.




## Fields

<details>
<summary>gmsaCredentialSpec: string</summary>

# Deployment.spec.template.spec.containers.securityContext.windowsOptions.gmsaCredentialSpec

---

**Type**: string

## Description
GMSACredentialSpec is where the GMSA admission webhook (https://github.com/kubernetes-sigs/windows-gmsa) inlines the contents of the GMSA credential spec named by the GMSACredentialSpecName field.





---

</details>

<details>
<summary>gmsaCredentialSpecName: string</summary>

# Deployment.spec.template.spec.containers.securityContext.windowsOptions.gmsaCredentialSpecName

---

**Type**: string

## Description
GMSACredentialSpecName is the name of the GMSA credential spec to use.





---

</details>

<details>
<summary>runAsUserName: string</summary>

# Deployment.spec.template.spec.containers.securityContext.windowsOptions.runAsUserName

---

**Type**: string

## Description
The UserName in Windows to run the entrypoint of the container process. Defaults to the user specified in image metadata if unspecified. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.





---

</details>



---

</details>



---

</details>

<details>
<summary>startupProbe: Object</summary>

# Deployment.spec.template.spec.containers.startupProbe

---

**Type**: Object

## Description
StartupProbe indicates that the Pod has successfully initialized. If specified, no other probes are executed until this completes successfully. If this probe fails, the Pod will be restarted, just as if the livenessProbe failed. This can be used to provide different probe parameters at the beginning of a Pod's lifecycle, when it might take a long time to load data or warm a cache, than during steady-state operation. This cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes




## Fields

<details>
<summary>exec: Object</summary>

# Deployment.spec.template.spec.containers.startupProbe.exec

---

**Type**: Object

## Description
One and only one of the following should be specified. Exec specifies the action to take.




## Fields

<details>
<summary>command: []string</summary>

# Deployment.spec.template.spec.containers.startupProbe.exec.command

---

**Type**: []string

## Description
Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container's filesystem. The command is simply exec'd, it is not run inside a shell, so traditional shell instructions ('|', etc) won't work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy.





---

</details>



---

</details>

<details>
<summary>failureThreshold: integer</summary>

# Deployment.spec.template.spec.containers.startupProbe.failureThreshold

---

**Type**: integer

## Description
Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1.





---

</details>

<details>
<summary>httpGet: Object</summary>

# Deployment.spec.template.spec.containers.startupProbe.httpGet

---

**Type**: Object

## Description
HTTPGet specifies the http request to perform.




## Fields

<details>
<summary>host: string</summary>

# Deployment.spec.template.spec.containers.startupProbe.httpGet.host

---

**Type**: string

## Description
Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.





---

</details>

<details>
<summary>httpHeaders: []Object</summary>

# Deployment.spec.template.spec.containers.startupProbe.httpGet.httpHeaders

---

**Type**: []Object

## Description
Custom headers to set in the request. HTTP allows repeated headers.




## Fields

<details>
<summary>name: string required!</summary>

# Deployment.spec.template.spec.containers.startupProbe.httpGet.httpHeaders.name

---

**Type**: string (required)

## Description
The header field name





---

</details>

<details>
<summary>value: string required!</summary>

# Deployment.spec.template.spec.containers.startupProbe.httpGet.httpHeaders.value

---

**Type**: string (required)

## Description
The header field value





---

</details>



---

</details>

<details>
<summary>path: string</summary>

# Deployment.spec.template.spec.containers.startupProbe.httpGet.path

---

**Type**: string

## Description
Path to access on the HTTP server.





---

</details>

<details>
<summary>port: string required!</summary>

# Deployment.spec.template.spec.containers.startupProbe.httpGet.port

---

**Type**: string (required)

## Description
Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.





---

</details>

<details>
<summary>scheme: string</summary>

# Deployment.spec.template.spec.containers.startupProbe.httpGet.scheme

---

**Type**: string

## Description
Scheme to use for connecting to the host. Defaults to HTTP.





---

</details>



---

</details>

<details>
<summary>initialDelaySeconds: integer</summary>

# Deployment.spec.template.spec.containers.startupProbe.initialDelaySeconds

---

**Type**: integer

## Description
Number of seconds after the container has started before liveness probes are initiated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes





---

</details>

<details>
<summary>periodSeconds: integer</summary>

# Deployment.spec.template.spec.containers.startupProbe.periodSeconds

---

**Type**: integer

## Description
How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1.





---

</details>

<details>
<summary>successThreshold: integer</summary>

# Deployment.spec.template.spec.containers.startupProbe.successThreshold

---

**Type**: integer

## Description
Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1.





---

</details>

<details>
<summary>tcpSocket: Object</summary>

# Deployment.spec.template.spec.containers.startupProbe.tcpSocket

---

**Type**: Object

## Description
TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported




## Fields

<details>
<summary>host: string</summary>

# Deployment.spec.template.spec.containers.startupProbe.tcpSocket.host

---

**Type**: string

## Description
Optional: Host name to connect to, defaults to the pod IP.





---

</details>

<details>
<summary>port: string required!</summary>

# Deployment.spec.template.spec.containers.startupProbe.tcpSocket.port

---

**Type**: string (required)

## Description
Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.





---

</details>



---

</details>

<details>
<summary>terminationGracePeriodSeconds: integer</summary>

# Deployment.spec.template.spec.containers.startupProbe.terminationGracePeriodSeconds

---

**Type**: integer

## Description
Optional duration in seconds the pod needs to terminate gracefully upon probe failure. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. If this value is nil, the pod's terminationGracePeriodSeconds will be used. Otherwise, this value overrides the value provided by the pod spec. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). This is an alpha field and requires enabling ProbeTerminationGracePeriod feature gate.





---

</details>

<details>
<summary>timeoutSeconds: integer</summary>

# Deployment.spec.template.spec.containers.startupProbe.timeoutSeconds

---

**Type**: integer

## Description
Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes





---

</details>



---

</details>

<details>
<summary>stdin: boolean</summary>

# Deployment.spec.template.spec.containers.stdin

---

**Type**: boolean

## Description
Whether this container should allocate a buffer for stdin in the container runtime. If this is not set, reads from stdin in the container will always result in EOF. Default is false.





---

</details>

<details>
<summary>stdinOnce: boolean</summary>

# Deployment.spec.template.spec.containers.stdinOnce

---

**Type**: boolean

## Description
Whether the container runtime should close the stdin channel after it has been opened by a single attach. When stdin is true the stdin stream will remain open across multiple attach sessions. If stdinOnce is set to true, stdin is opened on container start, is empty until the first client attaches to stdin, and then remains open and accepts data until the client disconnects, at which time stdin is closed and remains closed until the container is restarted. If this flag is false, a container processes that reads from stdin will never receive an EOF. Default is false





---

</details>

<details>
<summary>terminationMessagePath: string</summary>

# Deployment.spec.template.spec.containers.terminationMessagePath

---

**Type**: string

## Description
Optional: Path at which the file to which the container's termination message will be written is mounted into the container's filesystem. Message written is intended to be brief final status, such as an assertion failure message. Will be truncated by the node if greater than 4096 bytes. The total message length across all containers will be limited to 12kb. Defaults to /dev/termination-log. Cannot be updated.





---

</details>

<details>
<summary>terminationMessagePolicy: string</summary>

# Deployment.spec.template.spec.containers.terminationMessagePolicy

---

**Type**: string

## Description
Indicate how the termination message should be populated. File will use the contents of terminationMessagePath to populate the container status message on both success and failure. FallbackToLogsOnError will use the last chunk of container log output if the termination message file is empty and the container exited with an error. The log output is limited to 2048 bytes or 80 lines, whichever is smaller. Defaults to File. Cannot be updated.





---

</details>

<details>
<summary>tty: boolean</summary>

# Deployment.spec.template.spec.containers.tty

---

**Type**: boolean

## Description
Whether this container should allocate a TTY for itself, also requires 'stdin' to be true. Default is false.





---

</details>

<details>
<summary>volumeDevices: []Object</summary>

# Deployment.spec.template.spec.containers.volumeDevices

---

**Type**: []Object

## Description
volumeDevices is the list of block devices to be used by the container.




## Fields

<details>
<summary>devicePath: string required!</summary>

# Deployment.spec.template.spec.containers.volumeDevices.devicePath

---

**Type**: string (required)

## Description
devicePath is the path inside of the container that the device will be mapped to.





---

</details>

<details>
<summary>name: string required!</summary>

# Deployment.spec.template.spec.containers.volumeDevices.name

---

**Type**: string (required)

## Description
name must match the name of a persistentVolumeClaim in the pod





---

</details>



---

</details>

<details>
<summary>volumeMounts: []Object</summary>

# Deployment.spec.template.spec.containers.volumeMounts

---

**Type**: []Object

## Description
Pod volumes to mount into the container's filesystem. Cannot be updated.




## Fields

<details>
<summary>mountPath: string required!</summary>

# Deployment.spec.template.spec.containers.volumeMounts.mountPath

---

**Type**: string (required)

## Description
Path within the container at which the volume should be mounted. Must not contain ':'.





---

</details>

<details>
<summary>mountPropagation: string</summary>

# Deployment.spec.template.spec.containers.volumeMounts.mountPropagation

---

**Type**: string

## Description
mountPropagation determines how mounts are propagated from the host to container and the other way around. When not set, MountPropagationNone is used. This field is beta in 1.10.





---

</details>

<details>
<summary>name: string required!</summary>

# Deployment.spec.template.spec.containers.volumeMounts.name

---

**Type**: string (required)

## Description
This must match the Name of a Volume.





---

</details>

<details>
<summary>readOnly: boolean</summary>

# Deployment.spec.template.spec.containers.volumeMounts.readOnly

---

**Type**: boolean

## Description
Mounted read-only if true, read-write otherwise (false or unspecified). Defaults to false.





---

</details>

<details>
<summary>subPath: string</summary>

# Deployment.spec.template.spec.containers.volumeMounts.subPath

---

**Type**: string

## Description
Path within the volume from which the container's volume should be mounted. Defaults to "" (volume's root).





---

</details>

<details>
<summary>subPathExpr: string</summary>

# Deployment.spec.template.spec.containers.volumeMounts.subPathExpr

---

**Type**: string

## Description
Expanded path within the volume from which the container's volume should be mounted. Behaves similarly to SubPath but environment variable references $(VAR_NAME) are expanded using the container's environment. Defaults to "" (volume's root). SubPathExpr and SubPath are mutually exclusive.





---

</details>



---

</details>

<details>
<summary>workingDir: string</summary>

# Deployment.spec.template.spec.containers.workingDir

---

**Type**: string

## Description
Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated.





---

</details>



---

</details>

<details>
<summary>dnsConfig: Object</summary>

# Deployment.spec.template.spec.dnsConfig

---

**Type**: Object

## Description
Specifies the DNS parameters of a pod. Parameters specified here will be merged to the generated DNS configuration based on DNSPolicy.




## Fields

<details>
<summary>nameservers: []string</summary>

# Deployment.spec.template.spec.dnsConfig.nameservers

---

**Type**: []string

## Description
A list of DNS name server IP addresses. This will be appended to the base nameservers generated from DNSPolicy. Duplicated nameservers will be removed.





---

</details>

<details>
<summary>options: []Object</summary>

# Deployment.spec.template.spec.dnsConfig.options

---

**Type**: []Object

## Description
A list of DNS resolver options. This will be merged with the base options generated from DNSPolicy. Duplicated entries will be removed. Resolution options given in Options will override those that appear in the base DNSPolicy.




## Fields

<details>
<summary>name: string</summary>

# Deployment.spec.template.spec.dnsConfig.options.name

---

**Type**: string

## Description
Required.





---

</details>

<details>
<summary>value: string</summary>

# Deployment.spec.template.spec.dnsConfig.options.value

---

**Type**: string

## Description
None





---

</details>



---

</details>

<details>
<summary>searches: []string</summary>

# Deployment.spec.template.spec.dnsConfig.searches

---

**Type**: []string

## Description
A list of DNS search domains for host-name lookup. This will be appended to the base search paths generated from DNSPolicy. Duplicated search paths will be removed.





---

</details>



---

</details>

<details>
<summary>dnsPolicy: string</summary>

# Deployment.spec.template.spec.dnsPolicy

---

**Type**: string

## Description
Set DNS policy for the pod. Defaults to "ClusterFirst". Valid values are 'ClusterFirstWithHostNet', 'ClusterFirst', 'Default' or 'None'. DNS parameters given in DNSConfig will be merged with the policy selected with DNSPolicy. To have DNS options set along with hostNetwork, you have to specify DNS policy explicitly to 'ClusterFirstWithHostNet'.





---

</details>

<details>
<summary>enableServiceLinks: boolean</summary>

# Deployment.spec.template.spec.enableServiceLinks

---

**Type**: boolean

## Description
EnableServiceLinks indicates whether information about services should be injected into pod's environment variables, matching the syntax of Docker links. Optional: Defaults to true.





---

</details>

<details>
<summary>ephemeralContainers: []Object</summary>

# Deployment.spec.template.spec.ephemeralContainers

---

**Type**: []Object

## Description
List of ephemeral containers run in this pod. Ephemeral containers may be run in an existing pod to perform user-initiated actions such as debugging. This list cannot be specified when creating a pod, and it cannot be modified by updating the pod spec. In order to add an ephemeral container to an existing pod, use the pod's ephemeralcontainers subresource. This field is alpha-level and is only honored by servers that enable the EphemeralContainers feature.




## Fields

<details>
<summary>args: []string</summary>

# Deployment.spec.template.spec.ephemeralContainers.args

---

**Type**: []string

## Description
Arguments to the entrypoint. The docker image's CMD is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell





---

</details>

<details>
<summary>command: []string</summary>

# Deployment.spec.template.spec.ephemeralContainers.command

---

**Type**: []string

## Description
Entrypoint array. Not executed within a shell. The docker image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell





---

</details>

<details>
<summary>env: []Object</summary>

# Deployment.spec.template.spec.ephemeralContainers.env

---

**Type**: []Object

## Description
List of environment variables to set in the container. Cannot be updated.




## Fields

<details>
<summary>name: string required!</summary>

# Deployment.spec.template.spec.ephemeralContainers.env.name

---

**Type**: string (required)

## Description
Name of the environment variable. Must be a C_IDENTIFIER.





---

</details>

<details>
<summary>value: string</summary>

# Deployment.spec.template.spec.ephemeralContainers.env.value

---

**Type**: string

## Description
Variable references $(VAR_NAME) are expanded using the previous defined environment variables in the container and any service environment variables. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Defaults to "".





---

</details>

<details>
<summary>valueFrom: Object</summary>

# Deployment.spec.template.spec.ephemeralContainers.env.valueFrom

---

**Type**: Object

## Description
Source for the environment variable's value. Cannot be used if value is not empty.




## Fields

<details>
<summary>configMapKeyRef: Object</summary>

# Deployment.spec.template.spec.ephemeralContainers.env.valueFrom.configMapKeyRef

---

**Type**: Object

## Description
Selects a key of a ConfigMap.




## Fields

<details>
<summary>key: string required!</summary>

# Deployment.spec.template.spec.ephemeralContainers.env.valueFrom.configMapKeyRef.key

---

**Type**: string (required)

## Description
The key to select.





---

</details>

<details>
<summary>name: string</summary>

# Deployment.spec.template.spec.ephemeralContainers.env.valueFrom.configMapKeyRef.name

---

**Type**: string

## Description
Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names





---

</details>

<details>
<summary>optional: boolean</summary>

# Deployment.spec.template.spec.ephemeralContainers.env.valueFrom.configMapKeyRef.optional

---

**Type**: boolean

## Description
Specify whether the ConfigMap or its key must be defined





---

</details>



---

</details>

<details>
<summary>fieldRef: Object</summary>

# Deployment.spec.template.spec.ephemeralContainers.env.valueFrom.fieldRef

---

**Type**: Object

## Description
Selects a field of the pod: supports metadata.name, metadata.namespace, `metadata.labels['<KEY>']`, `metadata.annotations['<KEY>']`, spec.nodeName, spec.serviceAccountName, status.hostIP, status.podIP, status.podIPs.




## Fields

<details>
<summary>apiVersion: string</summary>

# Deployment.spec.template.spec.ephemeralContainers.env.valueFrom.fieldRef.apiVersion

---

**Type**: string

## Description
Version of the schema the FieldPath is written in terms of, defaults to "v1".





---

</details>

<details>
<summary>fieldPath: string required!</summary>

# Deployment.spec.template.spec.ephemeralContainers.env.valueFrom.fieldRef.fieldPath

---

**Type**: string (required)

## Description
Path of the field to select in the specified API version.





---

</details>



---

</details>

<details>
<summary>resourceFieldRef: Object</summary>

# Deployment.spec.template.spec.ephemeralContainers.env.valueFrom.resourceFieldRef

---

**Type**: Object

## Description
Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, limits.ephemeral-storage, requests.cpu, requests.memory and requests.ephemeral-storage) are currently supported.




## Fields

<details>
<summary>containerName: string</summary>

# Deployment.spec.template.spec.ephemeralContainers.env.valueFrom.resourceFieldRef.containerName

---

**Type**: string

## Description
Container name: required for volumes, optional for env vars





---

</details>

<details>
<summary>divisor: string</summary>

# Deployment.spec.template.spec.ephemeralContainers.env.valueFrom.resourceFieldRef.divisor

---

**Type**: string

## Description
Specifies the output format of the exposed resources, defaults to "1"





---

</details>

<details>
<summary>resource: string required!</summary>

# Deployment.spec.template.spec.ephemeralContainers.env.valueFrom.resourceFieldRef.resource

---

**Type**: string (required)

## Description
Required: resource to select





---

</details>



---

</details>

<details>
<summary>secretKeyRef: Object</summary>

# Deployment.spec.template.spec.ephemeralContainers.env.valueFrom.secretKeyRef

---

**Type**: Object

## Description
Selects a key of a secret in the pod's namespace




## Fields

<details>
<summary>key: string required!</summary>

# Deployment.spec.template.spec.ephemeralContainers.env.valueFrom.secretKeyRef.key

---

**Type**: string (required)

## Description
The key of the secret to select from. Must be a valid secret key.





---

</details>

<details>
<summary>name: string</summary>

# Deployment.spec.template.spec.ephemeralContainers.env.valueFrom.secretKeyRef.name

---

**Type**: string

## Description
Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names





---

</details>

<details>
<summary>optional: boolean</summary>

# Deployment.spec.template.spec.ephemeralContainers.env.valueFrom.secretKeyRef.optional

---

**Type**: boolean

## Description
Specify whether the Secret or its key must be defined





---

</details>



---

</details>



---

</details>



---

</details>

<details>
<summary>envFrom: []Object</summary>

# Deployment.spec.template.spec.ephemeralContainers.envFrom

---

**Type**: []Object

## Description
List of sources to populate environment variables in the container. The keys defined within a source must be a C_IDENTIFIER. All invalid keys will be reported as an event when the container is starting. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated.




## Fields

<details>
<summary>configMapRef: Object</summary>

# Deployment.spec.template.spec.ephemeralContainers.envFrom.configMapRef

---

**Type**: Object

## Description
The ConfigMap to select from




## Fields

<details>
<summary>name: string</summary>

# Deployment.spec.template.spec.ephemeralContainers.envFrom.configMapRef.name

---

**Type**: string

## Description
Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names





---

</details>

<details>
<summary>optional: boolean</summary>

# Deployment.spec.template.spec.ephemeralContainers.envFrom.configMapRef.optional

---

**Type**: boolean

## Description
Specify whether the ConfigMap must be defined





---

</details>



---

</details>

<details>
<summary>prefix: string</summary>

# Deployment.spec.template.spec.ephemeralContainers.envFrom.prefix

---

**Type**: string

## Description
An optional identifier to prepend to each key in the ConfigMap. Must be a C_IDENTIFIER.





---

</details>

<details>
<summary>secretRef: Object</summary>

# Deployment.spec.template.spec.ephemeralContainers.envFrom.secretRef

---

**Type**: Object

## Description
The Secret to select from




## Fields

<details>
<summary>name: string</summary>

# Deployment.spec.template.spec.ephemeralContainers.envFrom.secretRef.name

---

**Type**: string

## Description
Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names





---

</details>

<details>
<summary>optional: boolean</summary>

# Deployment.spec.template.spec.ephemeralContainers.envFrom.secretRef.optional

---

**Type**: boolean

## Description
Specify whether the Secret must be defined





---

</details>



---

</details>



---

</details>

<details>
<summary>image: string</summary>

# Deployment.spec.template.spec.ephemeralContainers.image

---

**Type**: string

## Description
Docker image name. More info: https://kubernetes.io/docs/concepts/containers/images





---

</details>

<details>
<summary>imagePullPolicy: string</summary>

# Deployment.spec.template.spec.ephemeralContainers.imagePullPolicy

---

**Type**: string

## Description
Image pull policy. One of Always, Never, IfNotPresent. Defaults to Always if :latest tag is specified, or IfNotPresent otherwise. Cannot be updated. More info: https://kubernetes.io/docs/concepts/containers/images#updating-images





---

</details>

<details>
<summary>lifecycle: Object</summary>

# Deployment.spec.template.spec.ephemeralContainers.lifecycle

---

**Type**: Object

## Description
Lifecycle is not allowed for ephemeral containers.




## Fields

<details>
<summary>postStart: Object</summary>

# Deployment.spec.template.spec.ephemeralContainers.lifecycle.postStart

---

**Type**: Object

## Description
PostStart is called immediately after a container is created. If the handler fails, the container is terminated and restarted according to its restart policy. Other management of the container blocks until the hook completes. More info: https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks




## Fields

<details>
<summary>exec: Object</summary>

# Deployment.spec.template.spec.ephemeralContainers.lifecycle.postStart.exec

---

**Type**: Object

## Description
One and only one of the following should be specified. Exec specifies the action to take.




## Fields

<details>
<summary>command: []string</summary>

# Deployment.spec.template.spec.ephemeralContainers.lifecycle.postStart.exec.command

---

**Type**: []string

## Description
Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container's filesystem. The command is simply exec'd, it is not run inside a shell, so traditional shell instructions ('|', etc) won't work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy.





---

</details>



---

</details>

<details>
<summary>httpGet: Object</summary>

# Deployment.spec.template.spec.ephemeralContainers.lifecycle.postStart.httpGet

---

**Type**: Object

## Description
HTTPGet specifies the http request to perform.




## Fields

<details>
<summary>host: string</summary>

# Deployment.spec.template.spec.ephemeralContainers.lifecycle.postStart.httpGet.host

---

**Type**: string

## Description
Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.





---

</details>

<details>
<summary>httpHeaders: []Object</summary>

# Deployment.spec.template.spec.ephemeralContainers.lifecycle.postStart.httpGet.httpHeaders

---

**Type**: []Object

## Description
Custom headers to set in the request. HTTP allows repeated headers.




## Fields

<details>
<summary>name: string required!</summary>

# Deployment.spec.template.spec.ephemeralContainers.lifecycle.postStart.httpGet.httpHeaders.name

---

**Type**: string (required)

## Description
The header field name





---

</details>

<details>
<summary>value: string required!</summary>

# Deployment.spec.template.spec.ephemeralContainers.lifecycle.postStart.httpGet.httpHeaders.value

---

**Type**: string (required)

## Description
The header field value





---

</details>



---

</details>

<details>
<summary>path: string</summary>

# Deployment.spec.template.spec.ephemeralContainers.lifecycle.postStart.httpGet.path

---

**Type**: string

## Description
Path to access on the HTTP server.





---

</details>

<details>
<summary>port: string required!</summary>

# Deployment.spec.template.spec.ephemeralContainers.lifecycle.postStart.httpGet.port

---

**Type**: string (required)

## Description
Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.





---

</details>

<details>
<summary>scheme: string</summary>

# Deployment.spec.template.spec.ephemeralContainers.lifecycle.postStart.httpGet.scheme

---

**Type**: string

## Description
Scheme to use for connecting to the host. Defaults to HTTP.





---

</details>



---

</details>

<details>
<summary>tcpSocket: Object</summary>

# Deployment.spec.template.spec.ephemeralContainers.lifecycle.postStart.tcpSocket

---

**Type**: Object

## Description
TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported




## Fields

<details>
<summary>host: string</summary>

# Deployment.spec.template.spec.ephemeralContainers.lifecycle.postStart.tcpSocket.host

---

**Type**: string

## Description
Optional: Host name to connect to, defaults to the pod IP.





---

</details>

<details>
<summary>port: string required!</summary>

# Deployment.spec.template.spec.ephemeralContainers.lifecycle.postStart.tcpSocket.port

---

**Type**: string (required)

## Description
Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.





---

</details>



---

</details>



---

</details>

<details>
<summary>preStop: Object</summary>

# Deployment.spec.template.spec.ephemeralContainers.lifecycle.preStop

---

**Type**: Object

## Description
PreStop is called immediately before a container is terminated due to an API request or management event such as liveness/startup probe failure, preemption, resource contention, etc. The handler is not called if the container crashes or exits. The reason for termination is passed to the handler. The Pod's termination grace period countdown begins before the PreStop hooked is executed. Regardless of the outcome of the handler, the container will eventually terminate within the Pod's termination grace period. Other management of the container blocks until the hook completes or until the termination grace period is reached. More info: https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks




## Fields

<details>
<summary>exec: Object</summary>

# Deployment.spec.template.spec.ephemeralContainers.lifecycle.preStop.exec

---

**Type**: Object

## Description
One and only one of the following should be specified. Exec specifies the action to take.




## Fields

<details>
<summary>command: []string</summary>

# Deployment.spec.template.spec.ephemeralContainers.lifecycle.preStop.exec.command

---

**Type**: []string

## Description
Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container's filesystem. The command is simply exec'd, it is not run inside a shell, so traditional shell instructions ('|', etc) won't work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy.





---

</details>



---

</details>

<details>
<summary>httpGet: Object</summary>

# Deployment.spec.template.spec.ephemeralContainers.lifecycle.preStop.httpGet

---

**Type**: Object

## Description
HTTPGet specifies the http request to perform.




## Fields

<details>
<summary>host: string</summary>

# Deployment.spec.template.spec.ephemeralContainers.lifecycle.preStop.httpGet.host

---

**Type**: string

## Description
Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.





---

</details>

<details>
<summary>httpHeaders: []Object</summary>

# Deployment.spec.template.spec.ephemeralContainers.lifecycle.preStop.httpGet.httpHeaders

---

**Type**: []Object

## Description
Custom headers to set in the request. HTTP allows repeated headers.




## Fields

<details>
<summary>name: string required!</summary>

# Deployment.spec.template.spec.ephemeralContainers.lifecycle.preStop.httpGet.httpHeaders.name

---

**Type**: string (required)

## Description
The header field name





---

</details>

<details>
<summary>value: string required!</summary>

# Deployment.spec.template.spec.ephemeralContainers.lifecycle.preStop.httpGet.httpHeaders.value

---

**Type**: string (required)

## Description
The header field value





---

</details>



---

</details>

<details>
<summary>path: string</summary>

# Deployment.spec.template.spec.ephemeralContainers.lifecycle.preStop.httpGet.path

---

**Type**: string

## Description
Path to access on the HTTP server.





---

</details>

<details>
<summary>port: string required!</summary>

# Deployment.spec.template.spec.ephemeralContainers.lifecycle.preStop.httpGet.port

---

**Type**: string (required)

## Description
Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.





---

</details>

<details>
<summary>scheme: string</summary>

# Deployment.spec.template.spec.ephemeralContainers.lifecycle.preStop.httpGet.scheme

---

**Type**: string

## Description
Scheme to use for connecting to the host. Defaults to HTTP.





---

</details>



---

</details>

<details>
<summary>tcpSocket: Object</summary>

# Deployment.spec.template.spec.ephemeralContainers.lifecycle.preStop.tcpSocket

---

**Type**: Object

## Description
TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported




## Fields

<details>
<summary>host: string</summary>

# Deployment.spec.template.spec.ephemeralContainers.lifecycle.preStop.tcpSocket.host

---

**Type**: string

## Description
Optional: Host name to connect to, defaults to the pod IP.





---

</details>

<details>
<summary>port: string required!</summary>

# Deployment.spec.template.spec.ephemeralContainers.lifecycle.preStop.tcpSocket.port

---

**Type**: string (required)

## Description
Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.





---

</details>



---

</details>



---

</details>



---

</details>

<details>
<summary>livenessProbe: Object</summary>

# Deployment.spec.template.spec.ephemeralContainers.livenessProbe

---

**Type**: Object

## Description
Probes are not allowed for ephemeral containers.




## Fields

<details>
<summary>exec: Object</summary>

# Deployment.spec.template.spec.ephemeralContainers.livenessProbe.exec

---

**Type**: Object

## Description
One and only one of the following should be specified. Exec specifies the action to take.




## Fields

<details>
<summary>command: []string</summary>

# Deployment.spec.template.spec.ephemeralContainers.livenessProbe.exec.command

---

**Type**: []string

## Description
Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container's filesystem. The command is simply exec'd, it is not run inside a shell, so traditional shell instructions ('|', etc) won't work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy.





---

</details>



---

</details>

<details>
<summary>failureThreshold: integer</summary>

# Deployment.spec.template.spec.ephemeralContainers.livenessProbe.failureThreshold

---

**Type**: integer

## Description
Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1.





---

</details>

<details>
<summary>httpGet: Object</summary>

# Deployment.spec.template.spec.ephemeralContainers.livenessProbe.httpGet

---

**Type**: Object

## Description
HTTPGet specifies the http request to perform.




## Fields

<details>
<summary>host: string</summary>

# Deployment.spec.template.spec.ephemeralContainers.livenessProbe.httpGet.host

---

**Type**: string

## Description
Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.





---

</details>

<details>
<summary>httpHeaders: []Object</summary>

# Deployment.spec.template.spec.ephemeralContainers.livenessProbe.httpGet.httpHeaders

---

**Type**: []Object

## Description
Custom headers to set in the request. HTTP allows repeated headers.




## Fields

<details>
<summary>name: string required!</summary>

# Deployment.spec.template.spec.ephemeralContainers.livenessProbe.httpGet.httpHeaders.name

---

**Type**: string (required)

## Description
The header field name





---

</details>

<details>
<summary>value: string required!</summary>

# Deployment.spec.template.spec.ephemeralContainers.livenessProbe.httpGet.httpHeaders.value

---

**Type**: string (required)

## Description
The header field value





---

</details>



---

</details>

<details>
<summary>path: string</summary>

# Deployment.spec.template.spec.ephemeralContainers.livenessProbe.httpGet.path

---

**Type**: string

## Description
Path to access on the HTTP server.





---

</details>

<details>
<summary>port: string required!</summary>

# Deployment.spec.template.spec.ephemeralContainers.livenessProbe.httpGet.port

---

**Type**: string (required)

## Description
Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.





---

</details>

<details>
<summary>scheme: string</summary>

# Deployment.spec.template.spec.ephemeralContainers.livenessProbe.httpGet.scheme

---

**Type**: string

## Description
Scheme to use for connecting to the host. Defaults to HTTP.





---

</details>



---

</details>

<details>
<summary>initialDelaySeconds: integer</summary>

# Deployment.spec.template.spec.ephemeralContainers.livenessProbe.initialDelaySeconds

---

**Type**: integer

## Description
Number of seconds after the container has started before liveness probes are initiated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes





---

</details>

<details>
<summary>periodSeconds: integer</summary>

# Deployment.spec.template.spec.ephemeralContainers.livenessProbe.periodSeconds

---

**Type**: integer

## Description
How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1.





---

</details>

<details>
<summary>successThreshold: integer</summary>

# Deployment.spec.template.spec.ephemeralContainers.livenessProbe.successThreshold

---

**Type**: integer

## Description
Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1.





---

</details>

<details>
<summary>tcpSocket: Object</summary>

# Deployment.spec.template.spec.ephemeralContainers.livenessProbe.tcpSocket

---

**Type**: Object

## Description
TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported




## Fields

<details>
<summary>host: string</summary>

# Deployment.spec.template.spec.ephemeralContainers.livenessProbe.tcpSocket.host

---

**Type**: string

## Description
Optional: Host name to connect to, defaults to the pod IP.





---

</details>

<details>
<summary>port: string required!</summary>

# Deployment.spec.template.spec.ephemeralContainers.livenessProbe.tcpSocket.port

---

**Type**: string (required)

## Description
Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.





---

</details>



---

</details>

<details>
<summary>terminationGracePeriodSeconds: integer</summary>

# Deployment.spec.template.spec.ephemeralContainers.livenessProbe.terminationGracePeriodSeconds

---

**Type**: integer

## Description
Optional duration in seconds the pod needs to terminate gracefully upon probe failure. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. If this value is nil, the pod's terminationGracePeriodSeconds will be used. Otherwise, this value overrides the value provided by the pod spec. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). This is an alpha field and requires enabling ProbeTerminationGracePeriod feature gate.





---

</details>

<details>
<summary>timeoutSeconds: integer</summary>

# Deployment.spec.template.spec.ephemeralContainers.livenessProbe.timeoutSeconds

---

**Type**: integer

## Description
Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes





---

</details>



---

</details>

<details>
<summary>name: string required!</summary>

# Deployment.spec.template.spec.ephemeralContainers.name

---

**Type**: string (required)

## Description
Name of the ephemeral container specified as a DNS_LABEL. This name must be unique among all containers, init containers and ephemeral containers.





---

</details>

<details>
<summary>ports: []Object</summary>

# Deployment.spec.template.spec.ephemeralContainers.ports

---

**Type**: []Object

## Description
Ports are not allowed for ephemeral containers.




## Fields

<details>
<summary>containerPort: integer required!</summary>

# Deployment.spec.template.spec.ephemeralContainers.ports.containerPort

---

**Type**: integer (required)

## Description
Number of port to expose on the pod's IP address. This must be a valid port number, 0 < x < 65536.





---

</details>

<details>
<summary>hostIP: string</summary>

# Deployment.spec.template.spec.ephemeralContainers.ports.hostIP

---

**Type**: string

## Description
What host IP to bind the external port to.





---

</details>

<details>
<summary>hostPort: integer</summary>

# Deployment.spec.template.spec.ephemeralContainers.ports.hostPort

---

**Type**: integer

## Description
Number of port to expose on the host. If specified, this must be a valid port number, 0 < x < 65536. If HostNetwork is specified, this must match ContainerPort. Most containers do not need this.





---

</details>

<details>
<summary>name: string</summary>

# Deployment.spec.template.spec.ephemeralContainers.ports.name

---

**Type**: string

## Description
If specified, this must be an IANA_SVC_NAME and unique within the pod. Each named port in a pod must have a unique name. Name for the port that can be referred to by services.





---

</details>

<details>
<summary>protocol: string</summary>

# Deployment.spec.template.spec.ephemeralContainers.ports.protocol

---

**Type**: string

## Description
Protocol for port. Must be UDP, TCP, or SCTP. Defaults to "TCP".





---

</details>



---

</details>

<details>
<summary>readinessProbe: Object</summary>

# Deployment.spec.template.spec.ephemeralContainers.readinessProbe

---

**Type**: Object

## Description
Probes are not allowed for ephemeral containers.




## Fields

<details>
<summary>exec: Object</summary>

# Deployment.spec.template.spec.ephemeralContainers.readinessProbe.exec

---

**Type**: Object

## Description
One and only one of the following should be specified. Exec specifies the action to take.




## Fields

<details>
<summary>command: []string</summary>

# Deployment.spec.template.spec.ephemeralContainers.readinessProbe.exec.command

---

**Type**: []string

## Description
Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container's filesystem. The command is simply exec'd, it is not run inside a shell, so traditional shell instructions ('|', etc) won't work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy.





---

</details>



---

</details>

<details>
<summary>failureThreshold: integer</summary>

# Deployment.spec.template.spec.ephemeralContainers.readinessProbe.failureThreshold

---

**Type**: integer

## Description
Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1.





---

</details>

<details>
<summary>httpGet: Object</summary>

# Deployment.spec.template.spec.ephemeralContainers.readinessProbe.httpGet

---

**Type**: Object

## Description
HTTPGet specifies the http request to perform.




## Fields

<details>
<summary>host: string</summary>

# Deployment.spec.template.spec.ephemeralContainers.readinessProbe.httpGet.host

---

**Type**: string

## Description
Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.





---

</details>

<details>
<summary>httpHeaders: []Object</summary>

# Deployment.spec.template.spec.ephemeralContainers.readinessProbe.httpGet.httpHeaders

---

**Type**: []Object

## Description
Custom headers to set in the request. HTTP allows repeated headers.




## Fields

<details>
<summary>name: string required!</summary>

# Deployment.spec.template.spec.ephemeralContainers.readinessProbe.httpGet.httpHeaders.name

---

**Type**: string (required)

## Description
The header field name





---

</details>

<details>
<summary>value: string required!</summary>

# Deployment.spec.template.spec.ephemeralContainers.readinessProbe.httpGet.httpHeaders.value

---

**Type**: string (required)

## Description
The header field value





---

</details>



---

</details>

<details>
<summary>path: string</summary>

# Deployment.spec.template.spec.ephemeralContainers.readinessProbe.httpGet.path

---

**Type**: string

## Description
Path to access on the HTTP server.





---

</details>

<details>
<summary>port: string required!</summary>

# Deployment.spec.template.spec.ephemeralContainers.readinessProbe.httpGet.port

---

**Type**: string (required)

## Description
Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.





---

</details>

<details>
<summary>scheme: string</summary>

# Deployment.spec.template.spec.ephemeralContainers.readinessProbe.httpGet.scheme

---

**Type**: string

## Description
Scheme to use for connecting to the host. Defaults to HTTP.





---

</details>



---

</details>

<details>
<summary>initialDelaySeconds: integer</summary>

# Deployment.spec.template.spec.ephemeralContainers.readinessProbe.initialDelaySeconds

---

**Type**: integer

## Description
Number of seconds after the container has started before liveness probes are initiated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes





---

</details>

<details>
<summary>periodSeconds: integer</summary>

# Deployment.spec.template.spec.ephemeralContainers.readinessProbe.periodSeconds

---

**Type**: integer

## Description
How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1.





---

</details>

<details>
<summary>successThreshold: integer</summary>

# Deployment.spec.template.spec.ephemeralContainers.readinessProbe.successThreshold

---

**Type**: integer

## Description
Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1.





---

</details>

<details>
<summary>tcpSocket: Object</summary>

# Deployment.spec.template.spec.ephemeralContainers.readinessProbe.tcpSocket

---

**Type**: Object

## Description
TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported




## Fields

<details>
<summary>host: string</summary>

# Deployment.spec.template.spec.ephemeralContainers.readinessProbe.tcpSocket.host

---

**Type**: string

## Description
Optional: Host name to connect to, defaults to the pod IP.





---

</details>

<details>
<summary>port: string required!</summary>

# Deployment.spec.template.spec.ephemeralContainers.readinessProbe.tcpSocket.port

---

**Type**: string (required)

## Description
Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.





---

</details>



---

</details>

<details>
<summary>terminationGracePeriodSeconds: integer</summary>

# Deployment.spec.template.spec.ephemeralContainers.readinessProbe.terminationGracePeriodSeconds

---

**Type**: integer

## Description
Optional duration in seconds the pod needs to terminate gracefully upon probe failure. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. If this value is nil, the pod's terminationGracePeriodSeconds will be used. Otherwise, this value overrides the value provided by the pod spec. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). This is an alpha field and requires enabling ProbeTerminationGracePeriod feature gate.





---

</details>

<details>
<summary>timeoutSeconds: integer</summary>

# Deployment.spec.template.spec.ephemeralContainers.readinessProbe.timeoutSeconds

---

**Type**: integer

## Description
Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes





---

</details>



---

</details>

<details>
<summary>resources: Object</summary>

# Deployment.spec.template.spec.ephemeralContainers.resources

---

**Type**: Object

## Description
Resources are not allowed for ephemeral containers. Ephemeral containers use spare resources already allocated to the pod.




## Fields

<details>
<summary>limits: map[string]string</summary>

# Deployment.spec.template.spec.ephemeralContainers.resources.limits

---

**Type**: map[string]string

## Description
Limits describes the maximum amount of compute resources allowed. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/





---

</details>

<details>
<summary>requests: map[string]string</summary>

# Deployment.spec.template.spec.ephemeralContainers.resources.requests

---

**Type**: map[string]string

## Description
Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/





---

</details>



---

</details>

<details>
<summary>securityContext: Object</summary>

# Deployment.spec.template.spec.ephemeralContainers.securityContext

---

**Type**: Object

## Description
SecurityContext is not allowed for ephemeral containers.




## Fields

<details>
<summary>allowPrivilegeEscalation: boolean</summary>

# Deployment.spec.template.spec.ephemeralContainers.securityContext.allowPrivilegeEscalation

---

**Type**: boolean

## Description
AllowPrivilegeEscalation controls whether a process can gain more privileges than its parent process. This bool directly controls if the no_new_privs flag will be set on the container process. AllowPrivilegeEscalation is true always when the container is: 1) run as Privileged 2) has CAP_SYS_ADMIN





---

</details>

<details>
<summary>capabilities: Object</summary>

# Deployment.spec.template.spec.ephemeralContainers.securityContext.capabilities

---

**Type**: Object

## Description
The capabilities to add/drop when running containers. Defaults to the default set of capabilities granted by the container runtime.




## Fields

<details>
<summary>add: []string</summary>

# Deployment.spec.template.spec.ephemeralContainers.securityContext.capabilities.add

---

**Type**: []string

## Description
Added capabilities





---

</details>

<details>
<summary>drop: []string</summary>

# Deployment.spec.template.spec.ephemeralContainers.securityContext.capabilities.drop

---

**Type**: []string

## Description
Removed capabilities





---

</details>



---

</details>

<details>
<summary>privileged: boolean</summary>

# Deployment.spec.template.spec.ephemeralContainers.securityContext.privileged

---

**Type**: boolean

## Description
Run container in privileged mode. Processes in privileged containers are essentially equivalent to root on the host. Defaults to false.





---

</details>

<details>
<summary>procMount: string</summary>

# Deployment.spec.template.spec.ephemeralContainers.securityContext.procMount

---

**Type**: string

## Description
procMount denotes the type of proc mount to use for the containers. The default is DefaultProcMount which uses the container runtime defaults for readonly paths and masked paths. This requires the ProcMountType feature flag to be enabled.





---

</details>

<details>
<summary>readOnlyRootFilesystem: boolean</summary>

# Deployment.spec.template.spec.ephemeralContainers.securityContext.readOnlyRootFilesystem

---

**Type**: boolean

## Description
Whether this container has a read-only root filesystem. Default is false.





---

</details>

<details>
<summary>runAsGroup: integer</summary>

# Deployment.spec.template.spec.ephemeralContainers.securityContext.runAsGroup

---

**Type**: integer

## Description
The GID to run the entrypoint of the container process. Uses runtime default if unset. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.





---

</details>

<details>
<summary>runAsNonRoot: boolean</summary>

# Deployment.spec.template.spec.ephemeralContainers.securityContext.runAsNonRoot

---

**Type**: boolean

## Description
Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.





---

</details>

<details>
<summary>runAsUser: integer</summary>

# Deployment.spec.template.spec.ephemeralContainers.securityContext.runAsUser

---

**Type**: integer

## Description
The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.





---

</details>

<details>
<summary>seLinuxOptions: Object</summary>

# Deployment.spec.template.spec.ephemeralContainers.securityContext.seLinuxOptions

---

**Type**: Object

## Description
The SELinux context to be applied to the container. If unspecified, the container runtime will allocate a random SELinux context for each container. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.




## Fields

<details>
<summary>level: string</summary>

# Deployment.spec.template.spec.ephemeralContainers.securityContext.seLinuxOptions.level

---

**Type**: string

## Description
Level is SELinux level label that applies to the container.





---

</details>

<details>
<summary>role: string</summary>

# Deployment.spec.template.spec.ephemeralContainers.securityContext.seLinuxOptions.role

---

**Type**: string

## Description
Role is a SELinux role label that applies to the container.





---

</details>

<details>
<summary>type: string</summary>

# Deployment.spec.template.spec.ephemeralContainers.securityContext.seLinuxOptions.type

---

**Type**: string

## Description
Type is a SELinux type label that applies to the container.





---

</details>

<details>
<summary>user: string</summary>

# Deployment.spec.template.spec.ephemeralContainers.securityContext.seLinuxOptions.user

---

**Type**: string

## Description
User is a SELinux user label that applies to the container.





---

</details>



---

</details>

<details>
<summary>seccompProfile: Object</summary>

# Deployment.spec.template.spec.ephemeralContainers.securityContext.seccompProfile

---

**Type**: Object

## Description
The seccomp options to use by this container. If seccomp options are provided at both the pod & container level, the container options override the pod options.




## Fields

<details>
<summary>localhostProfile: string</summary>

# Deployment.spec.template.spec.ephemeralContainers.securityContext.seccompProfile.localhostProfile

---

**Type**: string

## Description
localhostProfile indicates a profile defined in a file on the node should be used. The profile must be preconfigured on the node to work. Must be a descending path, relative to the kubelet's configured seccomp profile location. Must only be set if type is "Localhost".





---

</details>

<details>
<summary>type: string required!</summary>

# Deployment.spec.template.spec.ephemeralContainers.securityContext.seccompProfile.type

---

**Type**: string (required)

## Description
type indicates which kind of seccomp profile will be applied. Valid options are:      Localhost - a profile defined in a file on the node should be used. RuntimeDefault - the container runtime default profile should be used. Unconfined - no profile should be applied.





---

</details>



---

</details>

<details>
<summary>windowsOptions: Object</summary>

# Deployment.spec.template.spec.ephemeralContainers.securityContext.windowsOptions

---

**Type**: Object

## Description
The Windows specific settings applied to all containers. If unspecified, the options from the PodSecurityContext will be used. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.




## Fields

<details>
<summary>gmsaCredentialSpec: string</summary>

# Deployment.spec.template.spec.ephemeralContainers.securityContext.windowsOptions.gmsaCredentialSpec

---

**Type**: string

## Description
GMSACredentialSpec is where the GMSA admission webhook (https://github.com/kubernetes-sigs/windows-gmsa) inlines the contents of the GMSA credential spec named by the GMSACredentialSpecName field.





---

</details>

<details>
<summary>gmsaCredentialSpecName: string</summary>

# Deployment.spec.template.spec.ephemeralContainers.securityContext.windowsOptions.gmsaCredentialSpecName

---

**Type**: string

## Description
GMSACredentialSpecName is the name of the GMSA credential spec to use.





---

</details>

<details>
<summary>runAsUserName: string</summary>

# Deployment.spec.template.spec.ephemeralContainers.securityContext.windowsOptions.runAsUserName

---

**Type**: string

## Description
The UserName in Windows to run the entrypoint of the container process. Defaults to the user specified in image metadata if unspecified. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.





---

</details>



---

</details>



---

</details>

<details>
<summary>startupProbe: Object</summary>

# Deployment.spec.template.spec.ephemeralContainers.startupProbe

---

**Type**: Object

## Description
Probes are not allowed for ephemeral containers.




## Fields

<details>
<summary>exec: Object</summary>

# Deployment.spec.template.spec.ephemeralContainers.startupProbe.exec

---

**Type**: Object

## Description
One and only one of the following should be specified. Exec specifies the action to take.




## Fields

<details>
<summary>command: []string</summary>

# Deployment.spec.template.spec.ephemeralContainers.startupProbe.exec.command

---

**Type**: []string

## Description
Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container's filesystem. The command is simply exec'd, it is not run inside a shell, so traditional shell instructions ('|', etc) won't work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy.





---

</details>



---

</details>

<details>
<summary>failureThreshold: integer</summary>

# Deployment.spec.template.spec.ephemeralContainers.startupProbe.failureThreshold

---

**Type**: integer

## Description
Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1.





---

</details>

<details>
<summary>httpGet: Object</summary>

# Deployment.spec.template.spec.ephemeralContainers.startupProbe.httpGet

---

**Type**: Object

## Description
HTTPGet specifies the http request to perform.




## Fields

<details>
<summary>host: string</summary>

# Deployment.spec.template.spec.ephemeralContainers.startupProbe.httpGet.host

---

**Type**: string

## Description
Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.





---

</details>

<details>
<summary>httpHeaders: []Object</summary>

# Deployment.spec.template.spec.ephemeralContainers.startupProbe.httpGet.httpHeaders

---

**Type**: []Object

## Description
Custom headers to set in the request. HTTP allows repeated headers.




## Fields

<details>
<summary>name: string required!</summary>

# Deployment.spec.template.spec.ephemeralContainers.startupProbe.httpGet.httpHeaders.name

---

**Type**: string (required)

## Description
The header field name





---

</details>

<details>
<summary>value: string required!</summary>

# Deployment.spec.template.spec.ephemeralContainers.startupProbe.httpGet.httpHeaders.value

---

**Type**: string (required)

## Description
The header field value





---

</details>



---

</details>

<details>
<summary>path: string</summary>

# Deployment.spec.template.spec.ephemeralContainers.startupProbe.httpGet.path

---

**Type**: string

## Description
Path to access on the HTTP server.





---

</details>

<details>
<summary>port: string required!</summary>

# Deployment.spec.template.spec.ephemeralContainers.startupProbe.httpGet.port

---

**Type**: string (required)

## Description
Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.





---

</details>

<details>
<summary>scheme: string</summary>

# Deployment.spec.template.spec.ephemeralContainers.startupProbe.httpGet.scheme

---

**Type**: string

## Description
Scheme to use for connecting to the host. Defaults to HTTP.





---

</details>



---

</details>

<details>
<summary>initialDelaySeconds: integer</summary>

# Deployment.spec.template.spec.ephemeralContainers.startupProbe.initialDelaySeconds

---

**Type**: integer

## Description
Number of seconds after the container has started before liveness probes are initiated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes





---

</details>

<details>
<summary>periodSeconds: integer</summary>

# Deployment.spec.template.spec.ephemeralContainers.startupProbe.periodSeconds

---

**Type**: integer

## Description
How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1.





---

</details>

<details>
<summary>successThreshold: integer</summary>

# Deployment.spec.template.spec.ephemeralContainers.startupProbe.successThreshold

---

**Type**: integer

## Description
Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1.





---

</details>

<details>
<summary>tcpSocket: Object</summary>

# Deployment.spec.template.spec.ephemeralContainers.startupProbe.tcpSocket

---

**Type**: Object

## Description
TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported




## Fields

<details>
<summary>host: string</summary>

# Deployment.spec.template.spec.ephemeralContainers.startupProbe.tcpSocket.host

---

**Type**: string

## Description
Optional: Host name to connect to, defaults to the pod IP.





---

</details>

<details>
<summary>port: string required!</summary>

# Deployment.spec.template.spec.ephemeralContainers.startupProbe.tcpSocket.port

---

**Type**: string (required)

## Description
Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.





---

</details>



---

</details>

<details>
<summary>terminationGracePeriodSeconds: integer</summary>

# Deployment.spec.template.spec.ephemeralContainers.startupProbe.terminationGracePeriodSeconds

---

**Type**: integer

## Description
Optional duration in seconds the pod needs to terminate gracefully upon probe failure. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. If this value is nil, the pod's terminationGracePeriodSeconds will be used. Otherwise, this value overrides the value provided by the pod spec. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). This is an alpha field and requires enabling ProbeTerminationGracePeriod feature gate.





---

</details>

<details>
<summary>timeoutSeconds: integer</summary>

# Deployment.spec.template.spec.ephemeralContainers.startupProbe.timeoutSeconds

---

**Type**: integer

## Description
Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes





---

</details>



---

</details>

<details>
<summary>stdin: boolean</summary>

# Deployment.spec.template.spec.ephemeralContainers.stdin

---

**Type**: boolean

## Description
Whether this container should allocate a buffer for stdin in the container runtime. If this is not set, reads from stdin in the container will always result in EOF. Default is false.





---

</details>

<details>
<summary>stdinOnce: boolean</summary>

# Deployment.spec.template.spec.ephemeralContainers.stdinOnce

---

**Type**: boolean

## Description
Whether the container runtime should close the stdin channel after it has been opened by a single attach. When stdin is true the stdin stream will remain open across multiple attach sessions. If stdinOnce is set to true, stdin is opened on container start, is empty until the first client attaches to stdin, and then remains open and accepts data until the client disconnects, at which time stdin is closed and remains closed until the container is restarted. If this flag is false, a container processes that reads from stdin will never receive an EOF. Default is false





---

</details>

<details>
<summary>targetContainerName: string</summary>

# Deployment.spec.template.spec.ephemeralContainers.targetContainerName

---

**Type**: string

## Description
If set, the name of the container from PodSpec that this ephemeral container targets. The ephemeral container will be run in the namespaces (IPC, PID, etc) of this container. If not set then the ephemeral container is run in whatever namespaces are shared for the pod. Note that the container runtime must support this feature.





---

</details>

<details>
<summary>terminationMessagePath: string</summary>

# Deployment.spec.template.spec.ephemeralContainers.terminationMessagePath

---

**Type**: string

## Description
Optional: Path at which the file to which the container's termination message will be written is mounted into the container's filesystem. Message written is intended to be brief final status, such as an assertion failure message. Will be truncated by the node if greater than 4096 bytes. The total message length across all containers will be limited to 12kb. Defaults to /dev/termination-log. Cannot be updated.





---

</details>

<details>
<summary>terminationMessagePolicy: string</summary>

# Deployment.spec.template.spec.ephemeralContainers.terminationMessagePolicy

---

**Type**: string

## Description
Indicate how the termination message should be populated. File will use the contents of terminationMessagePath to populate the container status message on both success and failure. FallbackToLogsOnError will use the last chunk of container log output if the termination message file is empty and the container exited with an error. The log output is limited to 2048 bytes or 80 lines, whichever is smaller. Defaults to File. Cannot be updated.





---

</details>

<details>
<summary>tty: boolean</summary>

# Deployment.spec.template.spec.ephemeralContainers.tty

---

**Type**: boolean

## Description
Whether this container should allocate a TTY for itself, also requires 'stdin' to be true. Default is false.





---

</details>

<details>
<summary>volumeDevices: []Object</summary>

# Deployment.spec.template.spec.ephemeralContainers.volumeDevices

---

**Type**: []Object

## Description
volumeDevices is the list of block devices to be used by the container.




## Fields

<details>
<summary>devicePath: string required!</summary>

# Deployment.spec.template.spec.ephemeralContainers.volumeDevices.devicePath

---

**Type**: string (required)

## Description
devicePath is the path inside of the container that the device will be mapped to.





---

</details>

<details>
<summary>name: string required!</summary>

# Deployment.spec.template.spec.ephemeralContainers.volumeDevices.name

---

**Type**: string (required)

## Description
name must match the name of a persistentVolumeClaim in the pod





---

</details>



---

</details>

<details>
<summary>volumeMounts: []Object</summary>

# Deployment.spec.template.spec.ephemeralContainers.volumeMounts

---

**Type**: []Object

## Description
Pod volumes to mount into the container's filesystem. Cannot be updated.




## Fields

<details>
<summary>mountPath: string required!</summary>

# Deployment.spec.template.spec.ephemeralContainers.volumeMounts.mountPath

---

**Type**: string (required)

## Description
Path within the container at which the volume should be mounted. Must not contain ':'.





---

</details>

<details>
<summary>mountPropagation: string</summary>

# Deployment.spec.template.spec.ephemeralContainers.volumeMounts.mountPropagation

---

**Type**: string

## Description
mountPropagation determines how mounts are propagated from the host to container and the other way around. When not set, MountPropagationNone is used. This field is beta in 1.10.





---

</details>

<details>
<summary>name: string required!</summary>

# Deployment.spec.template.spec.ephemeralContainers.volumeMounts.name

---

**Type**: string (required)

## Description
This must match the Name of a Volume.





---

</details>

<details>
<summary>readOnly: boolean</summary>

# Deployment.spec.template.spec.ephemeralContainers.volumeMounts.readOnly

---

**Type**: boolean

## Description
Mounted read-only if true, read-write otherwise (false or unspecified). Defaults to false.





---

</details>

<details>
<summary>subPath: string</summary>

# Deployment.spec.template.spec.ephemeralContainers.volumeMounts.subPath

---

**Type**: string

## Description
Path within the volume from which the container's volume should be mounted. Defaults to "" (volume's root).





---

</details>

<details>
<summary>subPathExpr: string</summary>

# Deployment.spec.template.spec.ephemeralContainers.volumeMounts.subPathExpr

---

**Type**: string

## Description
Expanded path within the volume from which the container's volume should be mounted. Behaves similarly to SubPath but environment variable references $(VAR_NAME) are expanded using the container's environment. Defaults to "" (volume's root). SubPathExpr and SubPath are mutually exclusive.





---

</details>



---

</details>

<details>
<summary>workingDir: string</summary>

# Deployment.spec.template.spec.ephemeralContainers.workingDir

---

**Type**: string

## Description
Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated.





---

</details>



---

</details>

<details>
<summary>hostAliases: []Object</summary>

# Deployment.spec.template.spec.hostAliases

---

**Type**: []Object

## Description
HostAliases is an optional list of hosts and IPs that will be injected into the pod's hosts file if specified. This is only valid for non-hostNetwork pods.




## Fields

<details>
<summary>hostnames: []string</summary>

# Deployment.spec.template.spec.hostAliases.hostnames

---

**Type**: []string

## Description
Hostnames for the above IP address.





---

</details>

<details>
<summary>ip: string</summary>

# Deployment.spec.template.spec.hostAliases.ip

---

**Type**: string

## Description
IP address of the host file entry.





---

</details>



---

</details>

<details>
<summary>hostIPC: boolean</summary>

# Deployment.spec.template.spec.hostIPC

---

**Type**: boolean

## Description
Use the host's ipc namespace. Optional: Default to false.





---

</details>

<details>
<summary>hostNetwork: boolean</summary>

# Deployment.spec.template.spec.hostNetwork

---

**Type**: boolean

## Description
Host networking requested for this pod. Use the host's network namespace. If this option is set, the ports that will be used must be specified. Default to false.





---

</details>

<details>
<summary>hostPID: boolean</summary>

# Deployment.spec.template.spec.hostPID

---

**Type**: boolean

## Description
Use the host's pid namespace. Optional: Default to false.





---

</details>

<details>
<summary>hostname: string</summary>

# Deployment.spec.template.spec.hostname

---

**Type**: string

## Description
Specifies the hostname of the Pod If not specified, the pod's hostname will be set to a system-defined value.





---

</details>

<details>
<summary>imagePullSecrets: []Object</summary>

# Deployment.spec.template.spec.imagePullSecrets

---

**Type**: []Object

## Description
ImagePullSecrets is an optional list of references to secrets in the same namespace to use for pulling any of the images used by this PodSpec. If specified, these secrets will be passed to individual puller implementations for them to use. For example, in the case of docker, only DockerConfig type secrets are honored. More info: https://kubernetes.io/docs/concepts/containers/images#specifying-imagepullsecrets-on-a-pod




## Fields

<details>
<summary>name: string</summary>

# Deployment.spec.template.spec.imagePullSecrets.name

---

**Type**: string

## Description
Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names





---

</details>



---

</details>

<details>
<summary>initContainers: []Object</summary>

# Deployment.spec.template.spec.initContainers

---

**Type**: []Object

## Description
List of initialization containers belonging to the pod. Init containers are executed in order prior to containers being started. If any init container fails, the pod is considered to have failed and is handled according to its restartPolicy. The name for an init container or normal container must be unique among all containers. Init containers may not have Lifecycle actions, Readiness probes, Liveness probes, or Startup probes. The resourceRequirements of an init container are taken into account during scheduling by finding the highest request/limit for each resource type, and then using the max of of that value or the sum of the normal containers. Limits are applied to init containers in a similar fashion. Init containers cannot currently be added or removed. Cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/init-containers/




## Fields

<details>
<summary>args: []string</summary>

# Deployment.spec.template.spec.initContainers.args

---

**Type**: []string

## Description
Arguments to the entrypoint. The docker image's CMD is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell





---

</details>

<details>
<summary>command: []string</summary>

# Deployment.spec.template.spec.initContainers.command

---

**Type**: []string

## Description
Entrypoint array. Not executed within a shell. The docker image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell





---

</details>

<details>
<summary>env: []Object</summary>

# Deployment.spec.template.spec.initContainers.env

---

**Type**: []Object

## Description
List of environment variables to set in the container. Cannot be updated.




## Fields

<details>
<summary>name: string required!</summary>

# Deployment.spec.template.spec.initContainers.env.name

---

**Type**: string (required)

## Description
Name of the environment variable. Must be a C_IDENTIFIER.





---

</details>

<details>
<summary>value: string</summary>

# Deployment.spec.template.spec.initContainers.env.value

---

**Type**: string

## Description
Variable references $(VAR_NAME) are expanded using the previous defined environment variables in the container and any service environment variables. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not. Defaults to "".





---

</details>

<details>
<summary>valueFrom: Object</summary>

# Deployment.spec.template.spec.initContainers.env.valueFrom

---

**Type**: Object

## Description
Source for the environment variable's value. Cannot be used if value is not empty.




## Fields

<details>
<summary>configMapKeyRef: Object</summary>

# Deployment.spec.template.spec.initContainers.env.valueFrom.configMapKeyRef

---

**Type**: Object

## Description
Selects a key of a ConfigMap.




## Fields

<details>
<summary>key: string required!</summary>

# Deployment.spec.template.spec.initContainers.env.valueFrom.configMapKeyRef.key

---

**Type**: string (required)

## Description
The key to select.





---

</details>

<details>
<summary>name: string</summary>

# Deployment.spec.template.spec.initContainers.env.valueFrom.configMapKeyRef.name

---

**Type**: string

## Description
Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names





---

</details>

<details>
<summary>optional: boolean</summary>

# Deployment.spec.template.spec.initContainers.env.valueFrom.configMapKeyRef.optional

---

**Type**: boolean

## Description
Specify whether the ConfigMap or its key must be defined





---

</details>



---

</details>

<details>
<summary>fieldRef: Object</summary>

# Deployment.spec.template.spec.initContainers.env.valueFrom.fieldRef

---

**Type**: Object

## Description
Selects a field of the pod: supports metadata.name, metadata.namespace, `metadata.labels['<KEY>']`, `metadata.annotations['<KEY>']`, spec.nodeName, spec.serviceAccountName, status.hostIP, status.podIP, status.podIPs.




## Fields

<details>
<summary>apiVersion: string</summary>

# Deployment.spec.template.spec.initContainers.env.valueFrom.fieldRef.apiVersion

---

**Type**: string

## Description
Version of the schema the FieldPath is written in terms of, defaults to "v1".





---

</details>

<details>
<summary>fieldPath: string required!</summary>

# Deployment.spec.template.spec.initContainers.env.valueFrom.fieldRef.fieldPath

---

**Type**: string (required)

## Description
Path of the field to select in the specified API version.





---

</details>



---

</details>

<details>
<summary>resourceFieldRef: Object</summary>

# Deployment.spec.template.spec.initContainers.env.valueFrom.resourceFieldRef

---

**Type**: Object

## Description
Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, limits.ephemeral-storage, requests.cpu, requests.memory and requests.ephemeral-storage) are currently supported.




## Fields

<details>
<summary>containerName: string</summary>

# Deployment.spec.template.spec.initContainers.env.valueFrom.resourceFieldRef.containerName

---

**Type**: string

## Description
Container name: required for volumes, optional for env vars





---

</details>

<details>
<summary>divisor: string</summary>

# Deployment.spec.template.spec.initContainers.env.valueFrom.resourceFieldRef.divisor

---

**Type**: string

## Description
Specifies the output format of the exposed resources, defaults to "1"





---

</details>

<details>
<summary>resource: string required!</summary>

# Deployment.spec.template.spec.initContainers.env.valueFrom.resourceFieldRef.resource

---

**Type**: string (required)

## Description
Required: resource to select





---

</details>



---

</details>

<details>
<summary>secretKeyRef: Object</summary>

# Deployment.spec.template.spec.initContainers.env.valueFrom.secretKeyRef

---

**Type**: Object

## Description
Selects a key of a secret in the pod's namespace




## Fields

<details>
<summary>key: string required!</summary>

# Deployment.spec.template.spec.initContainers.env.valueFrom.secretKeyRef.key

---

**Type**: string (required)

## Description
The key of the secret to select from. Must be a valid secret key.





---

</details>

<details>
<summary>name: string</summary>

# Deployment.spec.template.spec.initContainers.env.valueFrom.secretKeyRef.name

---

**Type**: string

## Description
Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names





---

</details>

<details>
<summary>optional: boolean</summary>

# Deployment.spec.template.spec.initContainers.env.valueFrom.secretKeyRef.optional

---

**Type**: boolean

## Description
Specify whether the Secret or its key must be defined





---

</details>



---

</details>



---

</details>



---

</details>

<details>
<summary>envFrom: []Object</summary>

# Deployment.spec.template.spec.initContainers.envFrom

---

**Type**: []Object

## Description
List of sources to populate environment variables in the container. The keys defined within a source must be a C_IDENTIFIER. All invalid keys will be reported as an event when the container is starting. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated.




## Fields

<details>
<summary>configMapRef: Object</summary>

# Deployment.spec.template.spec.initContainers.envFrom.configMapRef

---

**Type**: Object

## Description
The ConfigMap to select from




## Fields

<details>
<summary>name: string</summary>

# Deployment.spec.template.spec.initContainers.envFrom.configMapRef.name

---

**Type**: string

## Description
Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names





---

</details>

<details>
<summary>optional: boolean</summary>

# Deployment.spec.template.spec.initContainers.envFrom.configMapRef.optional

---

**Type**: boolean

## Description
Specify whether the ConfigMap must be defined





---

</details>



---

</details>

<details>
<summary>prefix: string</summary>

# Deployment.spec.template.spec.initContainers.envFrom.prefix

---

**Type**: string

## Description
An optional identifier to prepend to each key in the ConfigMap. Must be a C_IDENTIFIER.





---

</details>

<details>
<summary>secretRef: Object</summary>

# Deployment.spec.template.spec.initContainers.envFrom.secretRef

---

**Type**: Object

## Description
The Secret to select from




## Fields

<details>
<summary>name: string</summary>

# Deployment.spec.template.spec.initContainers.envFrom.secretRef.name

---

**Type**: string

## Description
Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names





---

</details>

<details>
<summary>optional: boolean</summary>

# Deployment.spec.template.spec.initContainers.envFrom.secretRef.optional

---

**Type**: boolean

## Description
Specify whether the Secret must be defined





---

</details>



---

</details>



---

</details>

<details>
<summary>image: string</summary>

# Deployment.spec.template.spec.initContainers.image

---

**Type**: string

## Description
Docker image name. More info: https://kubernetes.io/docs/concepts/containers/images This field is optional to allow higher level config management to default or override container images in workload controllers like Deployments and StatefulSets.





---

</details>

<details>
<summary>imagePullPolicy: string</summary>

# Deployment.spec.template.spec.initContainers.imagePullPolicy

---

**Type**: string

## Description
Image pull policy. One of Always, Never, IfNotPresent. Defaults to Always if :latest tag is specified, or IfNotPresent otherwise. Cannot be updated. More info: https://kubernetes.io/docs/concepts/containers/images#updating-images





---

</details>

<details>
<summary>lifecycle: Object</summary>

# Deployment.spec.template.spec.initContainers.lifecycle

---

**Type**: Object

## Description
Actions that the management system should take in response to container lifecycle events. Cannot be updated.




## Fields

<details>
<summary>postStart: Object</summary>

# Deployment.spec.template.spec.initContainers.lifecycle.postStart

---

**Type**: Object

## Description
PostStart is called immediately after a container is created. If the handler fails, the container is terminated and restarted according to its restart policy. Other management of the container blocks until the hook completes. More info: https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks




## Fields

<details>
<summary>exec: Object</summary>

# Deployment.spec.template.spec.initContainers.lifecycle.postStart.exec

---

**Type**: Object

## Description
One and only one of the following should be specified. Exec specifies the action to take.




## Fields

<details>
<summary>command: []string</summary>

# Deployment.spec.template.spec.initContainers.lifecycle.postStart.exec.command

---

**Type**: []string

## Description
Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container's filesystem. The command is simply exec'd, it is not run inside a shell, so traditional shell instructions ('|', etc) won't work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy.





---

</details>



---

</details>

<details>
<summary>httpGet: Object</summary>

# Deployment.spec.template.spec.initContainers.lifecycle.postStart.httpGet

---

**Type**: Object

## Description
HTTPGet specifies the http request to perform.




## Fields

<details>
<summary>host: string</summary>

# Deployment.spec.template.spec.initContainers.lifecycle.postStart.httpGet.host

---

**Type**: string

## Description
Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.





---

</details>

<details>
<summary>httpHeaders: []Object</summary>

# Deployment.spec.template.spec.initContainers.lifecycle.postStart.httpGet.httpHeaders

---

**Type**: []Object

## Description
Custom headers to set in the request. HTTP allows repeated headers.




## Fields

<details>
<summary>name: string required!</summary>

# Deployment.spec.template.spec.initContainers.lifecycle.postStart.httpGet.httpHeaders.name

---

**Type**: string (required)

## Description
The header field name





---

</details>

<details>
<summary>value: string required!</summary>

# Deployment.spec.template.spec.initContainers.lifecycle.postStart.httpGet.httpHeaders.value

---

**Type**: string (required)

## Description
The header field value





---

</details>



---

</details>

<details>
<summary>path: string</summary>

# Deployment.spec.template.spec.initContainers.lifecycle.postStart.httpGet.path

---

**Type**: string

## Description
Path to access on the HTTP server.





---

</details>

<details>
<summary>port: string required!</summary>

# Deployment.spec.template.spec.initContainers.lifecycle.postStart.httpGet.port

---

**Type**: string (required)

## Description
Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.





---

</details>

<details>
<summary>scheme: string</summary>

# Deployment.spec.template.spec.initContainers.lifecycle.postStart.httpGet.scheme

---

**Type**: string

## Description
Scheme to use for connecting to the host. Defaults to HTTP.





---

</details>



---

</details>

<details>
<summary>tcpSocket: Object</summary>

# Deployment.spec.template.spec.initContainers.lifecycle.postStart.tcpSocket

---

**Type**: Object

## Description
TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported




## Fields

<details>
<summary>host: string</summary>

# Deployment.spec.template.spec.initContainers.lifecycle.postStart.tcpSocket.host

---

**Type**: string

## Description
Optional: Host name to connect to, defaults to the pod IP.





---

</details>

<details>
<summary>port: string required!</summary>

# Deployment.spec.template.spec.initContainers.lifecycle.postStart.tcpSocket.port

---

**Type**: string (required)

## Description
Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.





---

</details>



---

</details>



---

</details>

<details>
<summary>preStop: Object</summary>

# Deployment.spec.template.spec.initContainers.lifecycle.preStop

---

**Type**: Object

## Description
PreStop is called immediately before a container is terminated due to an API request or management event such as liveness/startup probe failure, preemption, resource contention, etc. The handler is not called if the container crashes or exits. The reason for termination is passed to the handler. The Pod's termination grace period countdown begins before the PreStop hooked is executed. Regardless of the outcome of the handler, the container will eventually terminate within the Pod's termination grace period. Other management of the container blocks until the hook completes or until the termination grace period is reached. More info: https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks




## Fields

<details>
<summary>exec: Object</summary>

# Deployment.spec.template.spec.initContainers.lifecycle.preStop.exec

---

**Type**: Object

## Description
One and only one of the following should be specified. Exec specifies the action to take.




## Fields

<details>
<summary>command: []string</summary>

# Deployment.spec.template.spec.initContainers.lifecycle.preStop.exec.command

---

**Type**: []string

## Description
Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container's filesystem. The command is simply exec'd, it is not run inside a shell, so traditional shell instructions ('|', etc) won't work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy.





---

</details>



---

</details>

<details>
<summary>httpGet: Object</summary>

# Deployment.spec.template.spec.initContainers.lifecycle.preStop.httpGet

---

**Type**: Object

## Description
HTTPGet specifies the http request to perform.




## Fields

<details>
<summary>host: string</summary>

# Deployment.spec.template.spec.initContainers.lifecycle.preStop.httpGet.host

---

**Type**: string

## Description
Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.





---

</details>

<details>
<summary>httpHeaders: []Object</summary>

# Deployment.spec.template.spec.initContainers.lifecycle.preStop.httpGet.httpHeaders

---

**Type**: []Object

## Description
Custom headers to set in the request. HTTP allows repeated headers.




## Fields

<details>
<summary>name: string required!</summary>

# Deployment.spec.template.spec.initContainers.lifecycle.preStop.httpGet.httpHeaders.name

---

**Type**: string (required)

## Description
The header field name





---

</details>

<details>
<summary>value: string required!</summary>

# Deployment.spec.template.spec.initContainers.lifecycle.preStop.httpGet.httpHeaders.value

---

**Type**: string (required)

## Description
The header field value





---

</details>



---

</details>

<details>
<summary>path: string</summary>

# Deployment.spec.template.spec.initContainers.lifecycle.preStop.httpGet.path

---

**Type**: string

## Description
Path to access on the HTTP server.





---

</details>

<details>
<summary>port: string required!</summary>

# Deployment.spec.template.spec.initContainers.lifecycle.preStop.httpGet.port

---

**Type**: string (required)

## Description
Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.





---

</details>

<details>
<summary>scheme: string</summary>

# Deployment.spec.template.spec.initContainers.lifecycle.preStop.httpGet.scheme

---

**Type**: string

## Description
Scheme to use for connecting to the host. Defaults to HTTP.





---

</details>



---

</details>

<details>
<summary>tcpSocket: Object</summary>

# Deployment.spec.template.spec.initContainers.lifecycle.preStop.tcpSocket

---

**Type**: Object

## Description
TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported




## Fields

<details>
<summary>host: string</summary>

# Deployment.spec.template.spec.initContainers.lifecycle.preStop.tcpSocket.host

---

**Type**: string

## Description
Optional: Host name to connect to, defaults to the pod IP.





---

</details>

<details>
<summary>port: string required!</summary>

# Deployment.spec.template.spec.initContainers.lifecycle.preStop.tcpSocket.port

---

**Type**: string (required)

## Description
Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.





---

</details>



---

</details>



---

</details>



---

</details>

<details>
<summary>livenessProbe: Object</summary>

# Deployment.spec.template.spec.initContainers.livenessProbe

---

**Type**: Object

## Description
Periodic probe of container liveness. Container will be restarted if the probe fails. Cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes




## Fields

<details>
<summary>exec: Object</summary>

# Deployment.spec.template.spec.initContainers.livenessProbe.exec

---

**Type**: Object

## Description
One and only one of the following should be specified. Exec specifies the action to take.




## Fields

<details>
<summary>command: []string</summary>

# Deployment.spec.template.spec.initContainers.livenessProbe.exec.command

---

**Type**: []string

## Description
Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container's filesystem. The command is simply exec'd, it is not run inside a shell, so traditional shell instructions ('|', etc) won't work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy.





---

</details>



---

</details>

<details>
<summary>failureThreshold: integer</summary>

# Deployment.spec.template.spec.initContainers.livenessProbe.failureThreshold

---

**Type**: integer

## Description
Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1.





---

</details>

<details>
<summary>httpGet: Object</summary>

# Deployment.spec.template.spec.initContainers.livenessProbe.httpGet

---

**Type**: Object

## Description
HTTPGet specifies the http request to perform.




## Fields

<details>
<summary>host: string</summary>

# Deployment.spec.template.spec.initContainers.livenessProbe.httpGet.host

---

**Type**: string

## Description
Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.





---

</details>

<details>
<summary>httpHeaders: []Object</summary>

# Deployment.spec.template.spec.initContainers.livenessProbe.httpGet.httpHeaders

---

**Type**: []Object

## Description
Custom headers to set in the request. HTTP allows repeated headers.




## Fields

<details>
<summary>name: string required!</summary>

# Deployment.spec.template.spec.initContainers.livenessProbe.httpGet.httpHeaders.name

---

**Type**: string (required)

## Description
The header field name





---

</details>

<details>
<summary>value: string required!</summary>

# Deployment.spec.template.spec.initContainers.livenessProbe.httpGet.httpHeaders.value

---

**Type**: string (required)

## Description
The header field value





---

</details>



---

</details>

<details>
<summary>path: string</summary>

# Deployment.spec.template.spec.initContainers.livenessProbe.httpGet.path

---

**Type**: string

## Description
Path to access on the HTTP server.





---

</details>

<details>
<summary>port: string required!</summary>

# Deployment.spec.template.spec.initContainers.livenessProbe.httpGet.port

---

**Type**: string (required)

## Description
Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.





---

</details>

<details>
<summary>scheme: string</summary>

# Deployment.spec.template.spec.initContainers.livenessProbe.httpGet.scheme

---

**Type**: string

## Description
Scheme to use for connecting to the host. Defaults to HTTP.





---

</details>



---

</details>

<details>
<summary>initialDelaySeconds: integer</summary>

# Deployment.spec.template.spec.initContainers.livenessProbe.initialDelaySeconds

---

**Type**: integer

## Description
Number of seconds after the container has started before liveness probes are initiated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes





---

</details>

<details>
<summary>periodSeconds: integer</summary>

# Deployment.spec.template.spec.initContainers.livenessProbe.periodSeconds

---

**Type**: integer

## Description
How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1.





---

</details>

<details>
<summary>successThreshold: integer</summary>

# Deployment.spec.template.spec.initContainers.livenessProbe.successThreshold

---

**Type**: integer

## Description
Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1.





---

</details>

<details>
<summary>tcpSocket: Object</summary>

# Deployment.spec.template.spec.initContainers.livenessProbe.tcpSocket

---

**Type**: Object

## Description
TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported




## Fields

<details>
<summary>host: string</summary>

# Deployment.spec.template.spec.initContainers.livenessProbe.tcpSocket.host

---

**Type**: string

## Description
Optional: Host name to connect to, defaults to the pod IP.





---

</details>

<details>
<summary>port: string required!</summary>

# Deployment.spec.template.spec.initContainers.livenessProbe.tcpSocket.port

---

**Type**: string (required)

## Description
Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.





---

</details>



---

</details>

<details>
<summary>terminationGracePeriodSeconds: integer</summary>

# Deployment.spec.template.spec.initContainers.livenessProbe.terminationGracePeriodSeconds

---

**Type**: integer

## Description
Optional duration in seconds the pod needs to terminate gracefully upon probe failure. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. If this value is nil, the pod's terminationGracePeriodSeconds will be used. Otherwise, this value overrides the value provided by the pod spec. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). This is an alpha field and requires enabling ProbeTerminationGracePeriod feature gate.





---

</details>

<details>
<summary>timeoutSeconds: integer</summary>

# Deployment.spec.template.spec.initContainers.livenessProbe.timeoutSeconds

---

**Type**: integer

## Description
Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes





---

</details>



---

</details>

<details>
<summary>name: string required!</summary>

# Deployment.spec.template.spec.initContainers.name

---

**Type**: string (required)

## Description
Name of the container specified as a DNS_LABEL. Each container in a pod must have a unique name (DNS_LABEL). Cannot be updated.





---

</details>

<details>
<summary>ports: []Object</summary>

# Deployment.spec.template.spec.initContainers.ports

---

**Type**: []Object

## Description
List of ports to expose from the container. Exposing a port here gives the system additional information about the network connections a container uses, but is primarily informational. Not specifying a port here DOES NOT prevent that port from being exposed. Any port which is listening on the default "0.0.0.0" address inside a container will be accessible from the network. Cannot be updated.




## Fields

<details>
<summary>containerPort: integer required!</summary>

# Deployment.spec.template.spec.initContainers.ports.containerPort

---

**Type**: integer (required)

## Description
Number of port to expose on the pod's IP address. This must be a valid port number, 0 < x < 65536.





---

</details>

<details>
<summary>hostIP: string</summary>

# Deployment.spec.template.spec.initContainers.ports.hostIP

---

**Type**: string

## Description
What host IP to bind the external port to.





---

</details>

<details>
<summary>hostPort: integer</summary>

# Deployment.spec.template.spec.initContainers.ports.hostPort

---

**Type**: integer

## Description
Number of port to expose on the host. If specified, this must be a valid port number, 0 < x < 65536. If HostNetwork is specified, this must match ContainerPort. Most containers do not need this.





---

</details>

<details>
<summary>name: string</summary>

# Deployment.spec.template.spec.initContainers.ports.name

---

**Type**: string

## Description
If specified, this must be an IANA_SVC_NAME and unique within the pod. Each named port in a pod must have a unique name. Name for the port that can be referred to by services.





---

</details>

<details>
<summary>protocol: string</summary>

# Deployment.spec.template.spec.initContainers.ports.protocol

---

**Type**: string

## Description
Protocol for port. Must be UDP, TCP, or SCTP. Defaults to "TCP".





---

</details>



---

</details>

<details>
<summary>readinessProbe: Object</summary>

# Deployment.spec.template.spec.initContainers.readinessProbe

---

**Type**: Object

## Description
Periodic probe of container service readiness. Container will be removed from service endpoints if the probe fails. Cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes




## Fields

<details>
<summary>exec: Object</summary>

# Deployment.spec.template.spec.initContainers.readinessProbe.exec

---

**Type**: Object

## Description
One and only one of the following should be specified. Exec specifies the action to take.




## Fields

<details>
<summary>command: []string</summary>

# Deployment.spec.template.spec.initContainers.readinessProbe.exec.command

---

**Type**: []string

## Description
Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container's filesystem. The command is simply exec'd, it is not run inside a shell, so traditional shell instructions ('|', etc) won't work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy.





---

</details>



---

</details>

<details>
<summary>failureThreshold: integer</summary>

# Deployment.spec.template.spec.initContainers.readinessProbe.failureThreshold

---

**Type**: integer

## Description
Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1.





---

</details>

<details>
<summary>httpGet: Object</summary>

# Deployment.spec.template.spec.initContainers.readinessProbe.httpGet

---

**Type**: Object

## Description
HTTPGet specifies the http request to perform.




## Fields

<details>
<summary>host: string</summary>

# Deployment.spec.template.spec.initContainers.readinessProbe.httpGet.host

---

**Type**: string

## Description
Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.





---

</details>

<details>
<summary>httpHeaders: []Object</summary>

# Deployment.spec.template.spec.initContainers.readinessProbe.httpGet.httpHeaders

---

**Type**: []Object

## Description
Custom headers to set in the request. HTTP allows repeated headers.




## Fields

<details>
<summary>name: string required!</summary>

# Deployment.spec.template.spec.initContainers.readinessProbe.httpGet.httpHeaders.name

---

**Type**: string (required)

## Description
The header field name





---

</details>

<details>
<summary>value: string required!</summary>

# Deployment.spec.template.spec.initContainers.readinessProbe.httpGet.httpHeaders.value

---

**Type**: string (required)

## Description
The header field value





---

</details>



---

</details>

<details>
<summary>path: string</summary>

# Deployment.spec.template.spec.initContainers.readinessProbe.httpGet.path

---

**Type**: string

## Description
Path to access on the HTTP server.





---

</details>

<details>
<summary>port: string required!</summary>

# Deployment.spec.template.spec.initContainers.readinessProbe.httpGet.port

---

**Type**: string (required)

## Description
Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.





---

</details>

<details>
<summary>scheme: string</summary>

# Deployment.spec.template.spec.initContainers.readinessProbe.httpGet.scheme

---

**Type**: string

## Description
Scheme to use for connecting to the host. Defaults to HTTP.





---

</details>



---

</details>

<details>
<summary>initialDelaySeconds: integer</summary>

# Deployment.spec.template.spec.initContainers.readinessProbe.initialDelaySeconds

---

**Type**: integer

## Description
Number of seconds after the container has started before liveness probes are initiated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes





---

</details>

<details>
<summary>periodSeconds: integer</summary>

# Deployment.spec.template.spec.initContainers.readinessProbe.periodSeconds

---

**Type**: integer

## Description
How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1.





---

</details>

<details>
<summary>successThreshold: integer</summary>

# Deployment.spec.template.spec.initContainers.readinessProbe.successThreshold

---

**Type**: integer

## Description
Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1.





---

</details>

<details>
<summary>tcpSocket: Object</summary>

# Deployment.spec.template.spec.initContainers.readinessProbe.tcpSocket

---

**Type**: Object

## Description
TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported




## Fields

<details>
<summary>host: string</summary>

# Deployment.spec.template.spec.initContainers.readinessProbe.tcpSocket.host

---

**Type**: string

## Description
Optional: Host name to connect to, defaults to the pod IP.





---

</details>

<details>
<summary>port: string required!</summary>

# Deployment.spec.template.spec.initContainers.readinessProbe.tcpSocket.port

---

**Type**: string (required)

## Description
Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.





---

</details>



---

</details>

<details>
<summary>terminationGracePeriodSeconds: integer</summary>

# Deployment.spec.template.spec.initContainers.readinessProbe.terminationGracePeriodSeconds

---

**Type**: integer

## Description
Optional duration in seconds the pod needs to terminate gracefully upon probe failure. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. If this value is nil, the pod's terminationGracePeriodSeconds will be used. Otherwise, this value overrides the value provided by the pod spec. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). This is an alpha field and requires enabling ProbeTerminationGracePeriod feature gate.





---

</details>

<details>
<summary>timeoutSeconds: integer</summary>

# Deployment.spec.template.spec.initContainers.readinessProbe.timeoutSeconds

---

**Type**: integer

## Description
Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes





---

</details>



---

</details>

<details>
<summary>resources: Object</summary>

# Deployment.spec.template.spec.initContainers.resources

---

**Type**: Object

## Description
Compute Resources required by this container. Cannot be updated. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/




## Fields

<details>
<summary>limits: map[string]string</summary>

# Deployment.spec.template.spec.initContainers.resources.limits

---

**Type**: map[string]string

## Description
Limits describes the maximum amount of compute resources allowed. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/





---

</details>

<details>
<summary>requests: map[string]string</summary>

# Deployment.spec.template.spec.initContainers.resources.requests

---

**Type**: map[string]string

## Description
Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/





---

</details>



---

</details>

<details>
<summary>securityContext: Object</summary>

# Deployment.spec.template.spec.initContainers.securityContext

---

**Type**: Object

## Description
Security options the pod should run with. More info: https://kubernetes.io/docs/concepts/policy/security-context/ More info: https://kubernetes.io/docs/tasks/configure-pod-container/security-context/




## Fields

<details>
<summary>allowPrivilegeEscalation: boolean</summary>

# Deployment.spec.template.spec.initContainers.securityContext.allowPrivilegeEscalation

---

**Type**: boolean

## Description
AllowPrivilegeEscalation controls whether a process can gain more privileges than its parent process. This bool directly controls if the no_new_privs flag will be set on the container process. AllowPrivilegeEscalation is true always when the container is: 1) run as Privileged 2) has CAP_SYS_ADMIN





---

</details>

<details>
<summary>capabilities: Object</summary>

# Deployment.spec.template.spec.initContainers.securityContext.capabilities

---

**Type**: Object

## Description
The capabilities to add/drop when running containers. Defaults to the default set of capabilities granted by the container runtime.




## Fields

<details>
<summary>add: []string</summary>

# Deployment.spec.template.spec.initContainers.securityContext.capabilities.add

---

**Type**: []string

## Description
Added capabilities





---

</details>

<details>
<summary>drop: []string</summary>

# Deployment.spec.template.spec.initContainers.securityContext.capabilities.drop

---

**Type**: []string

## Description
Removed capabilities





---

</details>



---

</details>

<details>
<summary>privileged: boolean</summary>

# Deployment.spec.template.spec.initContainers.securityContext.privileged

---

**Type**: boolean

## Description
Run container in privileged mode. Processes in privileged containers are essentially equivalent to root on the host. Defaults to false.





---

</details>

<details>
<summary>procMount: string</summary>

# Deployment.spec.template.spec.initContainers.securityContext.procMount

---

**Type**: string

## Description
procMount denotes the type of proc mount to use for the containers. The default is DefaultProcMount which uses the container runtime defaults for readonly paths and masked paths. This requires the ProcMountType feature flag to be enabled.





---

</details>

<details>
<summary>readOnlyRootFilesystem: boolean</summary>

# Deployment.spec.template.spec.initContainers.securityContext.readOnlyRootFilesystem

---

**Type**: boolean

## Description
Whether this container has a read-only root filesystem. Default is false.





---

</details>

<details>
<summary>runAsGroup: integer</summary>

# Deployment.spec.template.spec.initContainers.securityContext.runAsGroup

---

**Type**: integer

## Description
The GID to run the entrypoint of the container process. Uses runtime default if unset. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.





---

</details>

<details>
<summary>runAsNonRoot: boolean</summary>

# Deployment.spec.template.spec.initContainers.securityContext.runAsNonRoot

---

**Type**: boolean

## Description
Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.





---

</details>

<details>
<summary>runAsUser: integer</summary>

# Deployment.spec.template.spec.initContainers.securityContext.runAsUser

---

**Type**: integer

## Description
The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.





---

</details>

<details>
<summary>seLinuxOptions: Object</summary>

# Deployment.spec.template.spec.initContainers.securityContext.seLinuxOptions

---

**Type**: Object

## Description
The SELinux context to be applied to the container. If unspecified, the container runtime will allocate a random SELinux context for each container. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.




## Fields

<details>
<summary>level: string</summary>

# Deployment.spec.template.spec.initContainers.securityContext.seLinuxOptions.level

---

**Type**: string

## Description
Level is SELinux level label that applies to the container.





---

</details>

<details>
<summary>role: string</summary>

# Deployment.spec.template.spec.initContainers.securityContext.seLinuxOptions.role

---

**Type**: string

## Description
Role is a SELinux role label that applies to the container.





---

</details>

<details>
<summary>type: string</summary>

# Deployment.spec.template.spec.initContainers.securityContext.seLinuxOptions.type

---

**Type**: string

## Description
Type is a SELinux type label that applies to the container.





---

</details>

<details>
<summary>user: string</summary>

# Deployment.spec.template.spec.initContainers.securityContext.seLinuxOptions.user

---

**Type**: string

## Description
User is a SELinux user label that applies to the container.





---

</details>



---

</details>

<details>
<summary>seccompProfile: Object</summary>

# Deployment.spec.template.spec.initContainers.securityContext.seccompProfile

---

**Type**: Object

## Description
The seccomp options to use by this container. If seccomp options are provided at both the pod & container level, the container options override the pod options.




## Fields

<details>
<summary>localhostProfile: string</summary>

# Deployment.spec.template.spec.initContainers.securityContext.seccompProfile.localhostProfile

---

**Type**: string

## Description
localhostProfile indicates a profile defined in a file on the node should be used. The profile must be preconfigured on the node to work. Must be a descending path, relative to the kubelet's configured seccomp profile location. Must only be set if type is "Localhost".





---

</details>

<details>
<summary>type: string required!</summary>

# Deployment.spec.template.spec.initContainers.securityContext.seccompProfile.type

---

**Type**: string (required)

## Description
type indicates which kind of seccomp profile will be applied. Valid options are:      Localhost - a profile defined in a file on the node should be used. RuntimeDefault - the container runtime default profile should be used. Unconfined - no profile should be applied.





---

</details>



---

</details>

<details>
<summary>windowsOptions: Object</summary>

# Deployment.spec.template.spec.initContainers.securityContext.windowsOptions

---

**Type**: Object

## Description
The Windows specific settings applied to all containers. If unspecified, the options from the PodSecurityContext will be used. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.




## Fields

<details>
<summary>gmsaCredentialSpec: string</summary>

# Deployment.spec.template.spec.initContainers.securityContext.windowsOptions.gmsaCredentialSpec

---

**Type**: string

## Description
GMSACredentialSpec is where the GMSA admission webhook (https://github.com/kubernetes-sigs/windows-gmsa) inlines the contents of the GMSA credential spec named by the GMSACredentialSpecName field.





---

</details>

<details>
<summary>gmsaCredentialSpecName: string</summary>

# Deployment.spec.template.spec.initContainers.securityContext.windowsOptions.gmsaCredentialSpecName

---

**Type**: string

## Description
GMSACredentialSpecName is the name of the GMSA credential spec to use.





---

</details>

<details>
<summary>runAsUserName: string</summary>

# Deployment.spec.template.spec.initContainers.securityContext.windowsOptions.runAsUserName

---

**Type**: string

## Description
The UserName in Windows to run the entrypoint of the container process. Defaults to the user specified in image metadata if unspecified. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.





---

</details>



---

</details>



---

</details>

<details>
<summary>startupProbe: Object</summary>

# Deployment.spec.template.spec.initContainers.startupProbe

---

**Type**: Object

## Description
StartupProbe indicates that the Pod has successfully initialized. If specified, no other probes are executed until this completes successfully. If this probe fails, the Pod will be restarted, just as if the livenessProbe failed. This can be used to provide different probe parameters at the beginning of a Pod's lifecycle, when it might take a long time to load data or warm a cache, than during steady-state operation. This cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes




## Fields

<details>
<summary>exec: Object</summary>

# Deployment.spec.template.spec.initContainers.startupProbe.exec

---

**Type**: Object

## Description
One and only one of the following should be specified. Exec specifies the action to take.




## Fields

<details>
<summary>command: []string</summary>

# Deployment.spec.template.spec.initContainers.startupProbe.exec.command

---

**Type**: []string

## Description
Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container's filesystem. The command is simply exec'd, it is not run inside a shell, so traditional shell instructions ('|', etc) won't work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy.





---

</details>



---

</details>

<details>
<summary>failureThreshold: integer</summary>

# Deployment.spec.template.spec.initContainers.startupProbe.failureThreshold

---

**Type**: integer

## Description
Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1.





---

</details>

<details>
<summary>httpGet: Object</summary>

# Deployment.spec.template.spec.initContainers.startupProbe.httpGet

---

**Type**: Object

## Description
HTTPGet specifies the http request to perform.




## Fields

<details>
<summary>host: string</summary>

# Deployment.spec.template.spec.initContainers.startupProbe.httpGet.host

---

**Type**: string

## Description
Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.





---

</details>

<details>
<summary>httpHeaders: []Object</summary>

# Deployment.spec.template.spec.initContainers.startupProbe.httpGet.httpHeaders

---

**Type**: []Object

## Description
Custom headers to set in the request. HTTP allows repeated headers.




## Fields

<details>
<summary>name: string required!</summary>

# Deployment.spec.template.spec.initContainers.startupProbe.httpGet.httpHeaders.name

---

**Type**: string (required)

## Description
The header field name





---

</details>

<details>
<summary>value: string required!</summary>

# Deployment.spec.template.spec.initContainers.startupProbe.httpGet.httpHeaders.value

---

**Type**: string (required)

## Description
The header field value





---

</details>



---

</details>

<details>
<summary>path: string</summary>

# Deployment.spec.template.spec.initContainers.startupProbe.httpGet.path

---

**Type**: string

## Description
Path to access on the HTTP server.





---

</details>

<details>
<summary>port: string required!</summary>

# Deployment.spec.template.spec.initContainers.startupProbe.httpGet.port

---

**Type**: string (required)

## Description
Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.





---

</details>

<details>
<summary>scheme: string</summary>

# Deployment.spec.template.spec.initContainers.startupProbe.httpGet.scheme

---

**Type**: string

## Description
Scheme to use for connecting to the host. Defaults to HTTP.





---

</details>



---

</details>

<details>
<summary>initialDelaySeconds: integer</summary>

# Deployment.spec.template.spec.initContainers.startupProbe.initialDelaySeconds

---

**Type**: integer

## Description
Number of seconds after the container has started before liveness probes are initiated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes





---

</details>

<details>
<summary>periodSeconds: integer</summary>

# Deployment.spec.template.spec.initContainers.startupProbe.periodSeconds

---

**Type**: integer

## Description
How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1.





---

</details>

<details>
<summary>successThreshold: integer</summary>

# Deployment.spec.template.spec.initContainers.startupProbe.successThreshold

---

**Type**: integer

## Description
Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1.





---

</details>

<details>
<summary>tcpSocket: Object</summary>

# Deployment.spec.template.spec.initContainers.startupProbe.tcpSocket

---

**Type**: Object

## Description
TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported




## Fields

<details>
<summary>host: string</summary>

# Deployment.spec.template.spec.initContainers.startupProbe.tcpSocket.host

---

**Type**: string

## Description
Optional: Host name to connect to, defaults to the pod IP.





---

</details>

<details>
<summary>port: string required!</summary>

# Deployment.spec.template.spec.initContainers.startupProbe.tcpSocket.port

---

**Type**: string (required)

## Description
Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.





---

</details>



---

</details>

<details>
<summary>terminationGracePeriodSeconds: integer</summary>

# Deployment.spec.template.spec.initContainers.startupProbe.terminationGracePeriodSeconds

---

**Type**: integer

## Description
Optional duration in seconds the pod needs to terminate gracefully upon probe failure. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. If this value is nil, the pod's terminationGracePeriodSeconds will be used. Otherwise, this value overrides the value provided by the pod spec. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). This is an alpha field and requires enabling ProbeTerminationGracePeriod feature gate.





---

</details>

<details>
<summary>timeoutSeconds: integer</summary>

# Deployment.spec.template.spec.initContainers.startupProbe.timeoutSeconds

---

**Type**: integer

## Description
Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes





---

</details>



---

</details>

<details>
<summary>stdin: boolean</summary>

# Deployment.spec.template.spec.initContainers.stdin

---

**Type**: boolean

## Description
Whether this container should allocate a buffer for stdin in the container runtime. If this is not set, reads from stdin in the container will always result in EOF. Default is false.





---

</details>

<details>
<summary>stdinOnce: boolean</summary>

# Deployment.spec.template.spec.initContainers.stdinOnce

---

**Type**: boolean

## Description
Whether the container runtime should close the stdin channel after it has been opened by a single attach. When stdin is true the stdin stream will remain open across multiple attach sessions. If stdinOnce is set to true, stdin is opened on container start, is empty until the first client attaches to stdin, and then remains open and accepts data until the client disconnects, at which time stdin is closed and remains closed until the container is restarted. If this flag is false, a container processes that reads from stdin will never receive an EOF. Default is false





---

</details>

<details>
<summary>terminationMessagePath: string</summary>

# Deployment.spec.template.spec.initContainers.terminationMessagePath

---

**Type**: string

## Description
Optional: Path at which the file to which the container's termination message will be written is mounted into the container's filesystem. Message written is intended to be brief final status, such as an assertion failure message. Will be truncated by the node if greater than 4096 bytes. The total message length across all containers will be limited to 12kb. Defaults to /dev/termination-log. Cannot be updated.





---

</details>

<details>
<summary>terminationMessagePolicy: string</summary>

# Deployment.spec.template.spec.initContainers.terminationMessagePolicy

---

**Type**: string

## Description
Indicate how the termination message should be populated. File will use the contents of terminationMessagePath to populate the container status message on both success and failure. FallbackToLogsOnError will use the last chunk of container log output if the termination message file is empty and the container exited with an error. The log output is limited to 2048 bytes or 80 lines, whichever is smaller. Defaults to File. Cannot be updated.





---

</details>

<details>
<summary>tty: boolean</summary>

# Deployment.spec.template.spec.initContainers.tty

---

**Type**: boolean

## Description
Whether this container should allocate a TTY for itself, also requires 'stdin' to be true. Default is false.





---

</details>

<details>
<summary>volumeDevices: []Object</summary>

# Deployment.spec.template.spec.initContainers.volumeDevices

---

**Type**: []Object

## Description
volumeDevices is the list of block devices to be used by the container.




## Fields

<details>
<summary>devicePath: string required!</summary>

# Deployment.spec.template.spec.initContainers.volumeDevices.devicePath

---

**Type**: string (required)

## Description
devicePath is the path inside of the container that the device will be mapped to.





---

</details>

<details>
<summary>name: string required!</summary>

# Deployment.spec.template.spec.initContainers.volumeDevices.name

---

**Type**: string (required)

## Description
name must match the name of a persistentVolumeClaim in the pod





---

</details>



---

</details>

<details>
<summary>volumeMounts: []Object</summary>

# Deployment.spec.template.spec.initContainers.volumeMounts

---

**Type**: []Object

## Description
Pod volumes to mount into the container's filesystem. Cannot be updated.




## Fields

<details>
<summary>mountPath: string required!</summary>

# Deployment.spec.template.spec.initContainers.volumeMounts.mountPath

---

**Type**: string (required)

## Description
Path within the container at which the volume should be mounted. Must not contain ':'.





---

</details>

<details>
<summary>mountPropagation: string</summary>

# Deployment.spec.template.spec.initContainers.volumeMounts.mountPropagation

---

**Type**: string

## Description
mountPropagation determines how mounts are propagated from the host to container and the other way around. When not set, MountPropagationNone is used. This field is beta in 1.10.





---

</details>

<details>
<summary>name: string required!</summary>

# Deployment.spec.template.spec.initContainers.volumeMounts.name

---

**Type**: string (required)

## Description
This must match the Name of a Volume.





---

</details>

<details>
<summary>readOnly: boolean</summary>

# Deployment.spec.template.spec.initContainers.volumeMounts.readOnly

---

**Type**: boolean

## Description
Mounted read-only if true, read-write otherwise (false or unspecified). Defaults to false.





---

</details>

<details>
<summary>subPath: string</summary>

# Deployment.spec.template.spec.initContainers.volumeMounts.subPath

---

**Type**: string

## Description
Path within the volume from which the container's volume should be mounted. Defaults to "" (volume's root).





---

</details>

<details>
<summary>subPathExpr: string</summary>

# Deployment.spec.template.spec.initContainers.volumeMounts.subPathExpr

---

**Type**: string

## Description
Expanded path within the volume from which the container's volume should be mounted. Behaves similarly to SubPath but environment variable references $(VAR_NAME) are expanded using the container's environment. Defaults to "" (volume's root). SubPathExpr and SubPath are mutually exclusive.





---

</details>



---

</details>

<details>
<summary>workingDir: string</summary>

# Deployment.spec.template.spec.initContainers.workingDir

---

**Type**: string

## Description
Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image. Cannot be updated.





---

</details>



---

</details>

<details>
<summary>nodeName: string</summary>

# Deployment.spec.template.spec.nodeName

---

**Type**: string

## Description
NodeName is a request to schedule this pod onto a specific node. If it is non-empty, the scheduler simply schedules this pod onto that node, assuming that it fits resource requirements.





---

</details>

<details>
<summary>nodeSelector: map[string]string</summary>

# Deployment.spec.template.spec.nodeSelector

---

**Type**: map[string]string

## Description
NodeSelector is a selector which must be true for the pod to fit on a node. Selector which must match a node's labels for the pod to be scheduled on that node. More info: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/





---

</details>

<details>
<summary>overhead: map[string]string</summary>

# Deployment.spec.template.spec.overhead

---

**Type**: map[string]string

## Description
Overhead represents the resource overhead associated with running a pod for a given RuntimeClass. This field will be autopopulated at admission time by the RuntimeClass admission controller. If the RuntimeClass admission controller is enabled, overhead must not be set in Pod create requests. The RuntimeClass admission controller will reject Pod create requests which have the overhead already set. If RuntimeClass is configured and selected in the PodSpec, Overhead will be set to the value defined in the corresponding RuntimeClass, otherwise it will remain unset and treated as zero. More info: https://git.k8s.io/enhancements/keps/sig-node/20190226-pod-overhead.md This field is alpha-level as of Kubernetes v1.16, and is only honored by servers that enable the PodOverhead feature.





---

</details>

<details>
<summary>preemptionPolicy: string</summary>

# Deployment.spec.template.spec.preemptionPolicy

---

**Type**: string

## Description
PreemptionPolicy is the Policy for preempting pods with lower priority. One of Never, PreemptLowerPriority. Defaults to PreemptLowerPriority if unset. This field is beta-level, gated by the NonPreemptingPriority feature-gate.





---

</details>

<details>
<summary>priority: integer</summary>

# Deployment.spec.template.spec.priority

---

**Type**: integer

## Description
The priority value. Various system components use this field to find the priority of the pod. When Priority Admission Controller is enabled, it prevents users from setting this field. The admission controller populates this field from PriorityClassName. The higher the value, the higher the priority.





---

</details>

<details>
<summary>priorityClassName: string</summary>

# Deployment.spec.template.spec.priorityClassName

---

**Type**: string

## Description
If specified, indicates the pod's priority. "system-node-critical" and "system-cluster-critical" are two special keywords which indicate the highest priorities with the former being the highest priority. Any other name must be defined by creating a PriorityClass object with that name. If not specified, the pod priority will be default or zero if there is no default.





---

</details>

<details>
<summary>readinessGates: []Object</summary>

# Deployment.spec.template.spec.readinessGates

---

**Type**: []Object

## Description
If specified, all readiness gates will be evaluated for pod readiness. A pod is ready when all its containers are ready AND all conditions specified in the readiness gates have status equal to "True" More info: https://git.k8s.io/enhancements/keps/sig-network/0007-pod-ready%2B%2B.md




## Fields

<details>
<summary>conditionType: string required!</summary>

# Deployment.spec.template.spec.readinessGates.conditionType

---

**Type**: string (required)

## Description
ConditionType refers to a condition in the pod's condition list with matching type.





---

</details>



---

</details>

<details>
<summary>restartPolicy: string</summary>

# Deployment.spec.template.spec.restartPolicy

---

**Type**: string

## Description
Restart policy for all containers within the pod. One of Always, OnFailure, Never. Default to Always. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy





---

</details>

<details>
<summary>runtimeClassName: string</summary>

# Deployment.spec.template.spec.runtimeClassName

---

**Type**: string

## Description
RuntimeClassName refers to a RuntimeClass object in the node.k8s.io group, which should be used to run this pod. If no RuntimeClass resource matches the named class, the pod will not be run. If unset or empty, the "legacy" RuntimeClass will be used, which is an implicit class with an empty definition that uses the default runtime handler. More info: https://git.k8s.io/enhancements/keps/sig-node/runtime-class.md This is a beta feature as of Kubernetes v1.14.





---

</details>

<details>
<summary>schedulerName: string</summary>

# Deployment.spec.template.spec.schedulerName

---

**Type**: string

## Description
If specified, the pod will be dispatched by specified scheduler. If not specified, the pod will be dispatched by default scheduler.





---

</details>

<details>
<summary>securityContext: Object</summary>

# Deployment.spec.template.spec.securityContext

---

**Type**: Object

## Description
SecurityContext holds pod-level security attributes and common container settings. Optional: Defaults to empty. See type description for default values of each field.




## Fields

<details>
<summary>fsGroup: integer</summary>

# Deployment.spec.template.spec.securityContext.fsGroup

---

**Type**: integer

## Description
A special supplemental group that applies to all containers in a pod. Some volume types allow the Kubelet to change the ownership of that volume to be owned by the pod:      1. The owning GID will be the FSGroup 2. The setgid bit is set (new files created in the volume will be owned by FSGroup) 3. The permission bits are OR'd with rw-rw----      If unset, the Kubelet will not modify the ownership and permissions of any volume.





---

</details>

<details>
<summary>fsGroupChangePolicy: string</summary>

# Deployment.spec.template.spec.securityContext.fsGroupChangePolicy

---

**Type**: string

## Description
fsGroupChangePolicy defines behavior of changing ownership and permission of the volume before being exposed inside Pod. This field will only apply to volume types which support fsGroup based ownership(and permissions). It will have no effect on ephemeral volume types such as: secret, configmaps and emptydir. Valid values are "OnRootMismatch" and "Always". If not specified, "Always" is used.





---

</details>

<details>
<summary>runAsGroup: integer</summary>

# Deployment.spec.template.spec.securityContext.runAsGroup

---

**Type**: integer

## Description
The GID to run the entrypoint of the container process. Uses runtime default if unset. May also be set in SecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container.





---

</details>

<details>
<summary>runAsNonRoot: boolean</summary>

# Deployment.spec.template.spec.securityContext.runAsNonRoot

---

**Type**: boolean

## Description
Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in SecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.





---

</details>

<details>
<summary>runAsUser: integer</summary>

# Deployment.spec.template.spec.securityContext.runAsUser

---

**Type**: integer

## Description
The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in SecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container.





---

</details>

<details>
<summary>seLinuxOptions: Object</summary>

# Deployment.spec.template.spec.securityContext.seLinuxOptions

---

**Type**: Object

## Description
The SELinux context to be applied to all containers. If unspecified, the container runtime will allocate a random SELinux context for each container. May also be set in SecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container.




## Fields

<details>
<summary>level: string</summary>

# Deployment.spec.template.spec.securityContext.seLinuxOptions.level

---

**Type**: string

## Description
Level is SELinux level label that applies to the container.





---

</details>

<details>
<summary>role: string</summary>

# Deployment.spec.template.spec.securityContext.seLinuxOptions.role

---

**Type**: string

## Description
Role is a SELinux role label that applies to the container.





---

</details>

<details>
<summary>type: string</summary>

# Deployment.spec.template.spec.securityContext.seLinuxOptions.type

---

**Type**: string

## Description
Type is a SELinux type label that applies to the container.





---

</details>

<details>
<summary>user: string</summary>

# Deployment.spec.template.spec.securityContext.seLinuxOptions.user

---

**Type**: string

## Description
User is a SELinux user label that applies to the container.





---

</details>



---

</details>

<details>
<summary>seccompProfile: Object</summary>

# Deployment.spec.template.spec.securityContext.seccompProfile

---

**Type**: Object

## Description
The seccomp options to use by the containers in this pod.




## Fields

<details>
<summary>localhostProfile: string</summary>

# Deployment.spec.template.spec.securityContext.seccompProfile.localhostProfile

---

**Type**: string

## Description
localhostProfile indicates a profile defined in a file on the node should be used. The profile must be preconfigured on the node to work. Must be a descending path, relative to the kubelet's configured seccomp profile location. Must only be set if type is "Localhost".





---

</details>

<details>
<summary>type: string required!</summary>

# Deployment.spec.template.spec.securityContext.seccompProfile.type

---

**Type**: string (required)

## Description
type indicates which kind of seccomp profile will be applied. Valid options are:      Localhost - a profile defined in a file on the node should be used. RuntimeDefault - the container runtime default profile should be used. Unconfined - no profile should be applied.





---

</details>



---

</details>

<details>
<summary>supplementalGroups: []integer</summary>

# Deployment.spec.template.spec.securityContext.supplementalGroups

---

**Type**: []integer

## Description
A list of groups applied to the first process run in each container, in addition to the container's primary GID. If unspecified, no groups will be added to any container.





---

</details>

<details>
<summary>sysctls: []Object</summary>

# Deployment.spec.template.spec.securityContext.sysctls

---

**Type**: []Object

## Description
Sysctls hold a list of namespaced sysctls used for the pod. Pods with unsupported sysctls (by the container runtime) might fail to launch.




## Fields

<details>
<summary>name: string required!</summary>

# Deployment.spec.template.spec.securityContext.sysctls.name

---

**Type**: string (required)

## Description
Name of a property to set





---

</details>

<details>
<summary>value: string required!</summary>

# Deployment.spec.template.spec.securityContext.sysctls.value

---

**Type**: string (required)

## Description
Value of a property to set





---

</details>



---

</details>

<details>
<summary>windowsOptions: Object</summary>

# Deployment.spec.template.spec.securityContext.windowsOptions

---

**Type**: Object

## Description
The Windows specific settings applied to all containers. If unspecified, the options within a container's SecurityContext will be used. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.




## Fields

<details>
<summary>gmsaCredentialSpec: string</summary>

# Deployment.spec.template.spec.securityContext.windowsOptions.gmsaCredentialSpec

---

**Type**: string

## Description
GMSACredentialSpec is where the GMSA admission webhook (https://github.com/kubernetes-sigs/windows-gmsa) inlines the contents of the GMSA credential spec named by the GMSACredentialSpecName field.





---

</details>

<details>
<summary>gmsaCredentialSpecName: string</summary>

# Deployment.spec.template.spec.securityContext.windowsOptions.gmsaCredentialSpecName

---

**Type**: string

## Description
GMSACredentialSpecName is the name of the GMSA credential spec to use.





---

</details>

<details>
<summary>runAsUserName: string</summary>

# Deployment.spec.template.spec.securityContext.windowsOptions.runAsUserName

---

**Type**: string

## Description
The UserName in Windows to run the entrypoint of the container process. Defaults to the user specified in image metadata if unspecified. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.





---

</details>



---

</details>



---

</details>

<details>
<summary>serviceAccount: string</summary>

# Deployment.spec.template.spec.serviceAccount

---

**Type**: string

## Description
DeprecatedServiceAccount is a depreciated alias for ServiceAccountName. Deprecated: Use serviceAccountName instead.





---

</details>

<details>
<summary>serviceAccountName: string</summary>

# Deployment.spec.template.spec.serviceAccountName

---

**Type**: string

## Description
ServiceAccountName is the name of the ServiceAccount to use to run this pod. More info: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/





---

</details>

<details>
<summary>setHostnameAsFQDN: boolean</summary>

# Deployment.spec.template.spec.setHostnameAsFQDN

---

**Type**: boolean

## Description
If true the pod's hostname will be configured as the pod's FQDN, rather than the leaf name (the default). In Linux containers, this means setting the FQDN in the hostname field of the kernel (the nodename field of struct utsname). In Windows containers, this means setting the registry value of hostname for the registry key HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters to FQDN. If a pod does not have FQDN, this has no effect. Default to false.





---

</details>

<details>
<summary>shareProcessNamespace: boolean</summary>

# Deployment.spec.template.spec.shareProcessNamespace

---

**Type**: boolean

## Description
Share a single process namespace between all of the containers in a pod. When this is set containers will be able to view and signal processes from other containers in the same pod, and the first process in each container will not be assigned PID 1. HostPID and ShareProcessNamespace cannot both be set. Optional: Default to false.





---

</details>

<details>
<summary>subdomain: string</summary>

# Deployment.spec.template.spec.subdomain

---

**Type**: string

## Description
If specified, the fully qualified Pod hostname will be "<hostname>.<subdomain>.<pod namespace>.svc.<cluster domain>". If not specified, the pod will not have a domainname at all.





---

</details>

<details>
<summary>terminationGracePeriodSeconds: integer</summary>

# Deployment.spec.template.spec.terminationGracePeriodSeconds

---

**Type**: integer

## Description
Optional duration in seconds the pod needs to terminate gracefully. May be decreased in delete request. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). If this value is nil, the default grace period will be used instead. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. Defaults to 30 seconds.





---

</details>

<details>
<summary>tolerations: []Object</summary>

# Deployment.spec.template.spec.tolerations

---

**Type**: []Object

## Description
If specified, the pod's tolerations.




## Fields

<details>
<summary>effect: string</summary>

# Deployment.spec.template.spec.tolerations.effect

---

**Type**: string

## Description
Effect indicates the taint effect to match. Empty means match all taint effects. When specified, allowed values are NoSchedule, PreferNoSchedule and NoExecute.





---

</details>

<details>
<summary>key: string</summary>

# Deployment.spec.template.spec.tolerations.key

---

**Type**: string

## Description
Key is the taint key that the toleration applies to. Empty means match all taint keys. If the key is empty, operator must be Exists; this combination means to match all values and all keys.





---

</details>

<details>
<summary>operator: string</summary>

# Deployment.spec.template.spec.tolerations.operator

---

**Type**: string

## Description
Operator represents a key's relationship to the value. Valid operators are Exists and Equal. Defaults to Equal. Exists is equivalent to wildcard for value, so that a pod can tolerate all taints of a particular category.





---

</details>

<details>
<summary>tolerationSeconds: integer</summary>

# Deployment.spec.template.spec.tolerations.tolerationSeconds

---

**Type**: integer

## Description
TolerationSeconds represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, it is not set, which means tolerate the taint forever (do not evict). Zero and negative values will be treated as 0 (evict immediately) by the system.





---

</details>

<details>
<summary>value: string</summary>

# Deployment.spec.template.spec.tolerations.value

---

**Type**: string

## Description
Value is the taint value the toleration matches to. If the operator is Exists, the value should be empty, otherwise just a regular string.





---

</details>



---

</details>

<details>
<summary>topologySpreadConstraints: []Object</summary>

# Deployment.spec.template.spec.topologySpreadConstraints

---

**Type**: []Object

## Description
TopologySpreadConstraints describes how a group of pods ought to spread across topology domains. Scheduler will schedule pods in a way which abides by the constraints. All topologySpreadConstraints are ANDed.




## Fields

<details>
<summary>labelSelector: Object</summary>

# Deployment.spec.template.spec.topologySpreadConstraints.labelSelector

---

**Type**: Object

## Description
LabelSelector is used to find matching pods. Pods that match this label selector are counted to determine the number of pods in their corresponding topology domain.




## Fields

<details>
<summary>matchExpressions: []Object</summary>

# Deployment.spec.template.spec.topologySpreadConstraints.labelSelector.matchExpressions

---

**Type**: []Object

## Description
matchExpressions is a list of label selector requirements. The requirements are ANDed.




## Fields

<details>
<summary>key: string required!</summary>

# Deployment.spec.template.spec.topologySpreadConstraints.labelSelector.matchExpressions.key

---

**Type**: string (required)

## Description
key is the label key that the selector applies to.





---

</details>

<details>
<summary>operator: string required!</summary>

# Deployment.spec.template.spec.topologySpreadConstraints.labelSelector.matchExpressions.operator

---

**Type**: string (required)

## Description
operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.





---

</details>

<details>
<summary>values: []string</summary>

# Deployment.spec.template.spec.topologySpreadConstraints.labelSelector.matchExpressions.values

---

**Type**: []string

## Description
values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.





---

</details>



---

</details>

<details>
<summary>matchLabels: map[string]string</summary>

# Deployment.spec.template.spec.topologySpreadConstraints.labelSelector.matchLabels

---

**Type**: map[string]string

## Description
matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.





---

</details>



---

</details>

<details>
<summary>maxSkew: integer required!</summary>

# Deployment.spec.template.spec.topologySpreadConstraints.maxSkew

---

**Type**: integer (required)

## Description
MaxSkew describes the degree to which pods may be unevenly distributed. When `whenUnsatisfiable=DoNotSchedule`, it is the maximum permitted difference between the number of matching pods in the target topology and the global minimum. For example, in a 3-zone cluster, MaxSkew is set to 1, and pods with the same labelSelector spread as 1/1/0: | zone1 | zone2 | zone3 | | P | P | | - if MaxSkew is 1, incoming pod can only be scheduled to zone3 to become 1/1/1; scheduling it onto zone1(zone2) would make the ActualSkew(2-0) on zone1(zone2) violate MaxSkew(1). - if MaxSkew is 2, incoming pod can be scheduled onto any zone. When `whenUnsatisfiable=ScheduleAnyway`, it is used to give higher precedence to topologies that satisfy it. It's a required field. Default value is 1 and 0 is not allowed.





---

</details>

<details>
<summary>topologyKey: string required!</summary>

# Deployment.spec.template.spec.topologySpreadConstraints.topologyKey

---

**Type**: string (required)

## Description
TopologyKey is the key of node labels. Nodes that have a label with this key and identical values are considered to be in the same topology. We consider each <key, value> as a "bucket", and try to put balanced number of pods into each bucket. It's a required field.





---

</details>

<details>
<summary>whenUnsatisfiable: string required!</summary>

# Deployment.spec.template.spec.topologySpreadConstraints.whenUnsatisfiable

---

**Type**: string (required)

## Description
WhenUnsatisfiable indicates how to deal with a pod if it doesn't satisfy the spread constraint. - DoNotSchedule (default) tells the scheduler not to schedule it. - ScheduleAnyway tells the scheduler to schedule the pod in any location, but giving higher precedence to topologies that would help reduce the skew. A constraint is considered "Unsatisfiable" for an incoming pod if and only if every possible node assigment for that pod would violate "MaxSkew" on some topology. For example, in a 3-zone cluster, MaxSkew is set to 1, and pods with the same labelSelector spread as 3/1/1: | zone1 | zone2 | zone3 | | P P P | P | P | If WhenUnsatisfiable is set to DoNotSchedule, incoming pod can only be scheduled to zone2(zone3) to become 3/2/1(3/1/2) as ActualSkew(2-1) on zone2(zone3) satisfies MaxSkew(1). In other words, the cluster can still be imbalanced, but scheduler won't make it *more* imbalanced. It's a required field.





---

</details>



---

</details>

<details>
<summary>volumes: []Object</summary>

# Deployment.spec.template.spec.volumes

---

**Type**: []Object

## Description
List of volumes that can be mounted by containers belonging to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes




## Fields

<details>
<summary>awsElasticBlockStore: Object</summary>

# Deployment.spec.template.spec.volumes.awsElasticBlockStore

---

**Type**: Object

## Description
AWSElasticBlockStore represents an AWS Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore




## Fields

<details>
<summary>fsType: string</summary>

# Deployment.spec.template.spec.volumes.awsElasticBlockStore.fsType

---

**Type**: string

## Description
Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore





---

</details>

<details>
<summary>partition: integer</summary>

# Deployment.spec.template.spec.volumes.awsElasticBlockStore.partition

---

**Type**: integer

## Description
The partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty).





---

</details>

<details>
<summary>readOnly: boolean</summary>

# Deployment.spec.template.spec.volumes.awsElasticBlockStore.readOnly

---

**Type**: boolean

## Description
Specify "true" to force and set the ReadOnly property in VolumeMounts to "true". If omitted, the default is "false". More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore





---

</details>

<details>
<summary>volumeID: string required!</summary>

# Deployment.spec.template.spec.volumes.awsElasticBlockStore.volumeID

---

**Type**: string (required)

## Description
Unique ID of the persistent disk resource in AWS (Amazon EBS volume). More info: https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore





---

</details>



---

</details>

<details>
<summary>azureDisk: Object</summary>

# Deployment.spec.template.spec.volumes.azureDisk

---

**Type**: Object

## Description
AzureDisk represents an Azure Data Disk mount on the host and bind mount to the pod.




## Fields

<details>
<summary>cachingMode: string</summary>

# Deployment.spec.template.spec.volumes.azureDisk.cachingMode

---

**Type**: string

## Description
Host Caching mode: None, Read Only, Read Write.





---

</details>

<details>
<summary>diskName: string required!</summary>

# Deployment.spec.template.spec.volumes.azureDisk.diskName

---

**Type**: string (required)

## Description
The Name of the data disk in the blob storage





---

</details>

<details>
<summary>diskURI: string required!</summary>

# Deployment.spec.template.spec.volumes.azureDisk.diskURI

---

**Type**: string (required)

## Description
The URI the data disk in the blob storage





---

</details>

<details>
<summary>fsType: string</summary>

# Deployment.spec.template.spec.volumes.azureDisk.fsType

---

**Type**: string

## Description
Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.





---

</details>

<details>
<summary>kind: string</summary>

# Deployment.spec.template.spec.volumes.azureDisk.kind

---

**Type**: string

## Description
Expected values Shared: multiple blob disks per storage account Dedicated: single blob disk per storage account Managed: azure managed data disk (only in managed availability set). defaults to shared





---

</details>

<details>
<summary>readOnly: boolean</summary>

# Deployment.spec.template.spec.volumes.azureDisk.readOnly

---

**Type**: boolean

## Description
Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.





---

</details>



---

</details>

<details>
<summary>azureFile: Object</summary>

# Deployment.spec.template.spec.volumes.azureFile

---

**Type**: Object

## Description
AzureFile represents an Azure File Service mount on the host and bind mount to the pod.




## Fields

<details>
<summary>readOnly: boolean</summary>

# Deployment.spec.template.spec.volumes.azureFile.readOnly

---

**Type**: boolean

## Description
Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.





---

</details>

<details>
<summary>secretName: string required!</summary>

# Deployment.spec.template.spec.volumes.azureFile.secretName

---

**Type**: string (required)

## Description
the name of secret that contains Azure Storage Account Name and Key





---

</details>

<details>
<summary>shareName: string required!</summary>

# Deployment.spec.template.spec.volumes.azureFile.shareName

---

**Type**: string (required)

## Description
Share Name





---

</details>



---

</details>

<details>
<summary>cephfs: Object</summary>

# Deployment.spec.template.spec.volumes.cephfs

---

**Type**: Object

## Description
CephFS represents a Ceph FS mount on the host that shares a pod's lifetime




## Fields

<details>
<summary>monitors: []string required!</summary>

# Deployment.spec.template.spec.volumes.cephfs.monitors

---

**Type**: []string (required)

## Description
Required: Monitors is a collection of Ceph monitors More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it





---

</details>

<details>
<summary>path: string</summary>

# Deployment.spec.template.spec.volumes.cephfs.path

---

**Type**: string

## Description
Optional: Used as the mounted root, rather than the full Ceph tree, default is /





---

</details>

<details>
<summary>readOnly: boolean</summary>

# Deployment.spec.template.spec.volumes.cephfs.readOnly

---

**Type**: boolean

## Description
Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it





---

</details>

<details>
<summary>secretFile: string</summary>

# Deployment.spec.template.spec.volumes.cephfs.secretFile

---

**Type**: string

## Description
Optional: SecretFile is the path to key ring for User, default is /etc/ceph/user.secret More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it





---

</details>

<details>
<summary>secretRef: Object</summary>

# Deployment.spec.template.spec.volumes.cephfs.secretRef

---

**Type**: Object

## Description
Optional: SecretRef is reference to the authentication secret for User, default is empty. More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it




## Fields

<details>
<summary>name: string</summary>

# Deployment.spec.template.spec.volumes.cephfs.secretRef.name

---

**Type**: string

## Description
Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names





---

</details>



---

</details>

<details>
<summary>user: string</summary>

# Deployment.spec.template.spec.volumes.cephfs.user

---

**Type**: string

## Description
Optional: User is the rados user name, default is admin More info: https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it





---

</details>



---

</details>

<details>
<summary>cinder: Object</summary>

# Deployment.spec.template.spec.volumes.cinder

---

**Type**: Object

## Description
Cinder represents a cinder volume attached and mounted on kubelets host machine. More info: https://examples.k8s.io/mysql-cinder-pd/README.md




## Fields

<details>
<summary>fsType: string</summary>

# Deployment.spec.template.spec.volumes.cinder.fsType

---

**Type**: string

## Description
Filesystem type to mount. Must be a filesystem type supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://examples.k8s.io/mysql-cinder-pd/README.md





---

</details>

<details>
<summary>readOnly: boolean</summary>

# Deployment.spec.template.spec.volumes.cinder.readOnly

---

**Type**: boolean

## Description
Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: https://examples.k8s.io/mysql-cinder-pd/README.md





---

</details>

<details>
<summary>secretRef: Object</summary>

# Deployment.spec.template.spec.volumes.cinder.secretRef

---

**Type**: Object

## Description
Optional: points to a secret object containing parameters used to connect to OpenStack.




## Fields

<details>
<summary>name: string</summary>

# Deployment.spec.template.spec.volumes.cinder.secretRef.name

---

**Type**: string

## Description
Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names





---

</details>



---

</details>

<details>
<summary>volumeID: string required!</summary>

# Deployment.spec.template.spec.volumes.cinder.volumeID

---

**Type**: string (required)

## Description
volume id used to identify the volume in cinder. More info: https://examples.k8s.io/mysql-cinder-pd/README.md





---

</details>



---

</details>

<details>
<summary>configMap: Object</summary>

# Deployment.spec.template.spec.volumes.configMap

---

**Type**: Object

## Description
ConfigMap represents a configMap that should populate this volume




## Fields

<details>
<summary>defaultMode: integer</summary>

# Deployment.spec.template.spec.volumes.configMap.defaultMode

---

**Type**: integer

## Description
Optional: mode bits used to set permissions on created files by default. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.





---

</details>

<details>
<summary>items: []Object</summary>

# Deployment.spec.template.spec.volumes.configMap.items

---

**Type**: []Object

## Description
If unspecified, each key-value pair in the Data field of the referenced ConfigMap will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the ConfigMap, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.




## Fields

<details>
<summary>key: string required!</summary>

# Deployment.spec.template.spec.volumes.configMap.items.key

---

**Type**: string (required)

## Description
The key to project.





---

</details>

<details>
<summary>mode: integer</summary>

# Deployment.spec.template.spec.volumes.configMap.items.mode

---

**Type**: integer

## Description
Optional: mode bits used to set permissions on this file. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.





---

</details>

<details>
<summary>path: string required!</summary>

# Deployment.spec.template.spec.volumes.configMap.items.path

---

**Type**: string (required)

## Description
The relative path of the file to map the key to. May not be an absolute path. May not contain the path element '..'. May not start with the string '..'.





---

</details>



---

</details>

<details>
<summary>name: string</summary>

# Deployment.spec.template.spec.volumes.configMap.name

---

**Type**: string

## Description
Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names





---

</details>

<details>
<summary>optional: boolean</summary>

# Deployment.spec.template.spec.volumes.configMap.optional

---

**Type**: boolean

## Description
Specify whether the ConfigMap or its keys must be defined





---

</details>



---

</details>

<details>
<summary>csi: Object</summary>

# Deployment.spec.template.spec.volumes.csi

---

**Type**: Object

## Description
CSI (Container Storage Interface) represents ephemeral storage that is handled by certain external CSI drivers (Beta feature).




## Fields

<details>
<summary>driver: string required!</summary>

# Deployment.spec.template.spec.volumes.csi.driver

---

**Type**: string (required)

## Description
Driver is the name of the CSI driver that handles this volume. Consult with your admin for the correct name as registered in the cluster.





---

</details>

<details>
<summary>fsType: string</summary>

# Deployment.spec.template.spec.volumes.csi.fsType

---

**Type**: string

## Description
Filesystem type to mount. Ex. "ext4", "xfs", "ntfs". If not provided, the empty value is passed to the associated CSI driver which will determine the default filesystem to apply.





---

</details>

<details>
<summary>nodePublishSecretRef: Object</summary>

# Deployment.spec.template.spec.volumes.csi.nodePublishSecretRef

---

**Type**: Object

## Description
NodePublishSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodePublishVolume and NodeUnpublishVolume calls. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secret references are passed.




## Fields

<details>
<summary>name: string</summary>

# Deployment.spec.template.spec.volumes.csi.nodePublishSecretRef.name

---

**Type**: string

## Description
Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names





---

</details>



---

</details>

<details>
<summary>readOnly: boolean</summary>

# Deployment.spec.template.spec.volumes.csi.readOnly

---

**Type**: boolean

## Description
Specifies a read-only configuration for the volume. Defaults to false (read/write).





---

</details>

<details>
<summary>volumeAttributes: map[string]string</summary>

# Deployment.spec.template.spec.volumes.csi.volumeAttributes

---

**Type**: map[string]string

## Description
VolumeAttributes stores driver-specific properties that are passed to the CSI driver. Consult your driver's documentation for supported values.





---

</details>



---

</details>

<details>
<summary>downwardAPI: Object</summary>

# Deployment.spec.template.spec.volumes.downwardAPI

---

**Type**: Object

## Description
DownwardAPI represents downward API about the pod that should populate this volume




## Fields

<details>
<summary>defaultMode: integer</summary>

# Deployment.spec.template.spec.volumes.downwardAPI.defaultMode

---

**Type**: integer

## Description
Optional: mode bits to use on created files by default. Must be a Optional: mode bits used to set permissions on created files by default. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.





---

</details>

<details>
<summary>items: []Object</summary>

# Deployment.spec.template.spec.volumes.downwardAPI.items

---

**Type**: []Object

## Description
Items is a list of downward API volume file




## Fields

<details>
<summary>fieldRef: Object</summary>

# Deployment.spec.template.spec.volumes.downwardAPI.items.fieldRef

---

**Type**: Object

## Description
Required: Selects a field of the pod: only annotations, labels, name and namespace are supported.




## Fields

<details>
<summary>apiVersion: string</summary>

# Deployment.spec.template.spec.volumes.downwardAPI.items.fieldRef.apiVersion

---

**Type**: string

## Description
Version of the schema the FieldPath is written in terms of, defaults to "v1".





---

</details>

<details>
<summary>fieldPath: string required!</summary>

# Deployment.spec.template.spec.volumes.downwardAPI.items.fieldRef.fieldPath

---

**Type**: string (required)

## Description
Path of the field to select in the specified API version.





---

</details>



---

</details>

<details>
<summary>mode: integer</summary>

# Deployment.spec.template.spec.volumes.downwardAPI.items.mode

---

**Type**: integer

## Description
Optional: mode bits used to set permissions on this file, must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.





---

</details>

<details>
<summary>path: string required!</summary>

# Deployment.spec.template.spec.volumes.downwardAPI.items.path

---

**Type**: string (required)

## Description
Required: Path is the relative path name of the file to be created. Must not be absolute or contain the '..' path. Must be utf-8 encoded. The first item of the relative path must not start with '..'





---

</details>

<details>
<summary>resourceFieldRef: Object</summary>

# Deployment.spec.template.spec.volumes.downwardAPI.items.resourceFieldRef

---

**Type**: Object

## Description
Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, requests.cpu and requests.memory) are currently supported.




## Fields

<details>
<summary>containerName: string</summary>

# Deployment.spec.template.spec.volumes.downwardAPI.items.resourceFieldRef.containerName

---

**Type**: string

## Description
Container name: required for volumes, optional for env vars





---

</details>

<details>
<summary>divisor: string</summary>

# Deployment.spec.template.spec.volumes.downwardAPI.items.resourceFieldRef.divisor

---

**Type**: string

## Description
Specifies the output format of the exposed resources, defaults to "1"





---

</details>

<details>
<summary>resource: string required!</summary>

# Deployment.spec.template.spec.volumes.downwardAPI.items.resourceFieldRef.resource

---

**Type**: string (required)

## Description
Required: resource to select





---

</details>



---

</details>



---

</details>



---

</details>

<details>
<summary>emptyDir: Object</summary>

# Deployment.spec.template.spec.volumes.emptyDir

---

**Type**: Object

## Description
EmptyDir represents a temporary directory that shares a pod's lifetime. More info: https://kubernetes.io/docs/concepts/storage/volumes#emptydir




## Fields

<details>
<summary>medium: string</summary>

# Deployment.spec.template.spec.volumes.emptyDir.medium

---

**Type**: string

## Description
What type of storage medium should back this directory. The default is "" which means to use the node's default medium. Must be an empty string (default) or Memory. More info: https://kubernetes.io/docs/concepts/storage/volumes#emptydir





---

</details>

<details>
<summary>sizeLimit: string</summary>

# Deployment.spec.template.spec.volumes.emptyDir.sizeLimit

---

**Type**: string

## Description
Total amount of local storage required for this EmptyDir volume. The size limit is also applicable for memory medium. The maximum usage on memory medium EmptyDir would be the minimum value between the SizeLimit specified here and the sum of memory limits of all containers in a pod. The default is nil which means that the limit is undefined. More info: http://kubernetes.io/docs/user-guide/volumes#emptydir





---

</details>



---

</details>

<details>
<summary>ephemeral: Object</summary>

# Deployment.spec.template.spec.volumes.ephemeral

---

**Type**: Object

## Description
Ephemeral represents a volume that is handled by a cluster storage driver. The volume's lifecycle is tied to the pod that defines it - it will be created before the pod starts, and deleted when the pod is removed.      Use this if: a) the volume is only needed while the pod runs, b) features of normal volumes like restoring from snapshot or capacity tracking are needed, c) the storage driver is specified through a storage class, and d) the storage driver supports dynamic volume provisioning through a PersistentVolumeClaim (see EphemeralVolumeSource for more information on the connection between this volume type and PersistentVolumeClaim).      Use PersistentVolumeClaim or one of the vendor-specific APIs for volumes that persist for longer than the lifecycle of an individual pod.      Use CSI for light-weight local ephemeral volumes if the CSI driver is meant to be used that way - see the documentation of the driver for more information.      A pod can use both types of ephemeral volumes and persistent volumes at the same time.      This is a beta feature and only available when the GenericEphemeralVolume feature gate is enabled.




## Fields

<details>
<summary>volumeClaimTemplate: Object</summary>

# Deployment.spec.template.spec.volumes.ephemeral.volumeClaimTemplate

---

**Type**: Object

## Description
Will be used to create a stand-alone PVC to provision the volume. The pod in which this EphemeralVolumeSource is embedded will be the owner of the PVC, i.e. the PVC will be deleted together with the pod. The name of the PVC will be `<pod name>-<volume name>` where `<volume name>` is the name from the `PodSpec.Volumes` array entry. Pod validation will reject the pod if the concatenated name is not valid for a PVC (for example, too long).      An existing PVC with that name that is not owned by the pod will *not* be used for the pod to avoid using an unrelated volume by mistake. Starting the pod is then blocked until the unrelated PVC is removed. If such a pre-created PVC is meant to be used by the pod, the PVC has to updated with an owner reference to the pod once the pod exists. Normally this should not be necessary, but it may be useful when manually reconstructing a broken cluster.      This field is read-only and no changes will be made by Kubernetes to the PVC after it has been created.      Required, must not be nil.




## Fields

<details>
<summary>metadata: Object</summary>

# Deployment.spec.template.spec.volumes.ephemeral.volumeClaimTemplate.metadata

---

**Type**: Object

## Description
May contain labels and annotations that will be copied into the PVC when creating it. No other fields are allowed and will be rejected during validation.




## Fields

<details>
<summary>annotations: map[string]string</summary>

# Deployment.spec.template.spec.volumes.ephemeral.volumeClaimTemplate.metadata.annotations

---

**Type**: map[string]string

## Description
Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects. More info: http://kubernetes.io/docs/user-guide/annotations





---

</details>

<details>
<summary>clusterName: string</summary>

# Deployment.spec.template.spec.volumes.ephemeral.volumeClaimTemplate.metadata.clusterName

---

**Type**: string

## Description
The name of the cluster which the object belongs to. This is used to distinguish resources with same name and namespace in different clusters. This field is not set anywhere right now and apiserver is going to ignore it if set in create or update request.





---

</details>

<details>
<summary>creationTimestamp: string</summary>

# Deployment.spec.template.spec.volumes.ephemeral.volumeClaimTemplate.metadata.creationTimestamp

---

**Type**: string

## Description
CreationTimestamp is a timestamp representing the server time when this object was created. It is not guaranteed to be set in happens-before order across separate operations. Clients may not set this value. It is represented in RFC3339 form and is in UTC.      Populated by the system. Read-only. Null for lists. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata





---

</details>

<details>
<summary>deletionGracePeriodSeconds: integer</summary>

# Deployment.spec.template.spec.volumes.ephemeral.volumeClaimTemplate.metadata.deletionGracePeriodSeconds

---

**Type**: integer

## Description
Number of seconds allowed for this object to gracefully terminate before it will be removed from the system. Only set when deletionTimestamp is also set. May only be shortened. Read-only.





---

</details>

<details>
<summary>deletionTimestamp: string</summary>

# Deployment.spec.template.spec.volumes.ephemeral.volumeClaimTemplate.metadata.deletionTimestamp

---

**Type**: string

## Description
DeletionTimestamp is RFC 3339 date and time at which this resource will be deleted. This field is set by the server when a graceful deletion is requested by the user, and is not directly settable by a client. The resource is expected to be deleted (no longer visible from resource lists, and not reachable by name) after the time in this field, once the finalizers list is empty. As long as the finalizers list contains items, deletion is blocked. Once the deletionTimestamp is set, this value may not be unset or be set further into the future, although it may be shortened or the resource may be deleted prior to this time. For example, a user may request that a pod is deleted in 30 seconds. The Kubelet will react by sending a graceful termination signal to the containers in the pod. After that 30 seconds, the Kubelet will send a hard termination signal (SIGKILL) to the container and after cleanup, remove the pod from the API. In the presence of network partitions, this object may still exist after this timestamp, until an administrator or automated process can determine the resource is fully terminated. If not set, graceful deletion of the object has not been requested.      Populated by the system when a graceful deletion is requested. Read-only. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata





---

</details>

<details>
<summary>finalizers: []string</summary>

# Deployment.spec.template.spec.volumes.ephemeral.volumeClaimTemplate.metadata.finalizers

---

**Type**: []string

## Description
Must be empty before the object is deleted from the registry. Each entry is an identifier for the responsible component that will remove the entry from the list. If the deletionTimestamp of the object is non-nil, entries in this list can only be removed. Finalizers may be processed and removed in any order. Order is NOT enforced because it introduces significant risk of stuck finalizers. finalizers is a shared field, any actor with permission can reorder it. If the finalizer list is processed in order, then this can lead to a situation in which the component responsible for the first finalizer in the list is waiting for a signal (field value, external system, or other) produced by a component responsible for a finalizer later in the list, resulting in a deadlock. Without enforced ordering finalizers are free to order amongst themselves and are not vulnerable to ordering changes in the list.





---

</details>

<details>
<summary>generateName: string</summary>

# Deployment.spec.template.spec.volumes.ephemeral.volumeClaimTemplate.metadata.generateName

---

**Type**: string

## Description
GenerateName is an optional prefix, used by the server, to generate a unique name ONLY IF the Name field has not been provided. If this field is used, the name returned to the client will be different than the name passed. This value will also be combined with a unique suffix. The provided value has the same validation rules as the Name field, and may be truncated by the length of the suffix required to make the value unique on the server.      If this field is specified and the generated name exists, the server will NOT return a 409 - instead, it will either return 201 Created or 500 with Reason ServerTimeout indicating a unique name could not be found in the time allotted, and the client should retry (optionally after the time indicated in the Retry-After header).      Applied only if Name is not specified. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#idempotency





---

</details>

<details>
<summary>generation: integer</summary>

# Deployment.spec.template.spec.volumes.ephemeral.volumeClaimTemplate.metadata.generation

---

**Type**: integer

## Description
A sequence number representing a specific generation of the desired state. Populated by the system. Read-only.





---

</details>

<details>
<summary>labels: map[string]string</summary>

# Deployment.spec.template.spec.volumes.ephemeral.volumeClaimTemplate.metadata.labels

---

**Type**: map[string]string

## Description
Map of string keys and values that can be used to organize and categorize (scope and select) objects. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels





---

</details>

<details>
<summary>managedFields: []Object</summary>

# Deployment.spec.template.spec.volumes.ephemeral.volumeClaimTemplate.metadata.managedFields

---

**Type**: []Object

## Description
ManagedFields maps workflow-id and version to the set of fields that are managed by that workflow. This is mostly for internal housekeeping, and users typically shouldn't need to set or understand this field. A workflow can be the user's name, a controller's name, or the name of a specific apply path like "ci-cd". The set of fields is always in the version that the workflow used when modifying the object.




## Fields

<details>
<summary>apiVersion: string</summary>

# Deployment.spec.template.spec.volumes.ephemeral.volumeClaimTemplate.metadata.managedFields.apiVersion

---

**Type**: string

## Description
APIVersion defines the version of this resource that this field set applies to. The format is "group/version" just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted.





---

</details>

<details>
<summary>fieldsType: string</summary>

# Deployment.spec.template.spec.volumes.ephemeral.volumeClaimTemplate.metadata.managedFields.fieldsType

---

**Type**: string

## Description
FieldsType is the discriminator for the different fields format and version. There is currently only one possible value: "FieldsV1"





---

</details>

<details>
<summary>fieldsV1: map[string]</summary>

# Deployment.spec.template.spec.volumes.ephemeral.volumeClaimTemplate.metadata.managedFields.fieldsV1

---

**Type**: map[string]

## Description
FieldsV1 holds the first JSON version format as described in the "FieldsV1" type.





---

</details>

<details>
<summary>manager: string</summary>

# Deployment.spec.template.spec.volumes.ephemeral.volumeClaimTemplate.metadata.managedFields.manager

---

**Type**: string

## Description
Manager is an identifier of the workflow managing these fields.





---

</details>

<details>
<summary>operation: string</summary>

# Deployment.spec.template.spec.volumes.ephemeral.volumeClaimTemplate.metadata.managedFields.operation

---

**Type**: string

## Description
Operation is the type of operation which lead to this ManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'.





---

</details>

<details>
<summary>time: string</summary>

# Deployment.spec.template.spec.volumes.ephemeral.volumeClaimTemplate.metadata.managedFields.time

---

**Type**: string

## Description
Time is timestamp of when these fields were set. It should always be empty if Operation is 'Apply'





---

</details>



---

</details>

<details>
<summary>name: string</summary>

# Deployment.spec.template.spec.volumes.ephemeral.volumeClaimTemplate.metadata.name

---

**Type**: string

## Description
Name must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names





---

</details>

<details>
<summary>namespace: string</summary>

# Deployment.spec.template.spec.volumes.ephemeral.volumeClaimTemplate.metadata.namespace

---

**Type**: string

## Description
Namespace defines the space within which each name must be unique. An empty namespace is equivalent to the "default" namespace, but "default" is the canonical representation. Not all objects are required to be scoped to a namespace - the value of this field for those objects will be empty.      Must be a DNS_LABEL. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/namespaces





---

</details>

<details>
<summary>ownerReferences: []Object</summary>

# Deployment.spec.template.spec.volumes.ephemeral.volumeClaimTemplate.metadata.ownerReferences

---

**Type**: []Object

## Description
List of objects depended by this object. If ALL objects in the list have been deleted, this object will be garbage collected. If this object is managed by a controller, then an entry in this list will point to this controller, with the controller field set to true. There cannot be more than one managing controller.




## Fields

<details>
<summary>apiVersion: string required!</summary>

# Deployment.spec.template.spec.volumes.ephemeral.volumeClaimTemplate.metadata.ownerReferences.apiVersion

---

**Type**: string (required)

## Description
API version of the referent.





---

</details>

<details>
<summary>blockOwnerDeletion: boolean</summary>

# Deployment.spec.template.spec.volumes.ephemeral.volumeClaimTemplate.metadata.ownerReferences.blockOwnerDeletion

---

**Type**: boolean

## Description
If true, AND if the owner has the "foregroundDeletion" finalizer, then the owner cannot be deleted from the key-value store until this reference is removed. Defaults to false. To set this field, a user needs "delete" permission of the owner, otherwise 422 (Unprocessable Entity) will be returned.





---

</details>

<details>
<summary>controller: boolean</summary>

# Deployment.spec.template.spec.volumes.ephemeral.volumeClaimTemplate.metadata.ownerReferences.controller

---

**Type**: boolean

## Description
If true, this reference points to the managing controller.





---

</details>

<details>
<summary>kind: string required!</summary>

# Deployment.spec.template.spec.volumes.ephemeral.volumeClaimTemplate.metadata.ownerReferences.kind

---

**Type**: string (required)

## Description
Kind of the referent. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds





---

</details>

<details>
<summary>name: string required!</summary>

# Deployment.spec.template.spec.volumes.ephemeral.volumeClaimTemplate.metadata.ownerReferences.name

---

**Type**: string (required)

## Description
Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names





---

</details>

<details>
<summary>uid: string required!</summary>

# Deployment.spec.template.spec.volumes.ephemeral.volumeClaimTemplate.metadata.ownerReferences.uid

---

**Type**: string (required)

## Description
UID of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#uids





---

</details>



---

</details>

<details>
<summary>resourceVersion: string</summary>

# Deployment.spec.template.spec.volumes.ephemeral.volumeClaimTemplate.metadata.resourceVersion

---

**Type**: string

## Description
An opaque value that represents the internal version of this object that can be used by clients to determine when objects have changed. May be used for optimistic concurrency, change detection, and the watch operation on a resource or set of resources. Clients must treat these values as opaque and passed unmodified back to the server. They may only be valid for a particular resource or set of resources.      Populated by the system. Read-only. Value must be treated as opaque by clients and . More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency





---

</details>

<details>
<summary>selfLink: string</summary>

# Deployment.spec.template.spec.volumes.ephemeral.volumeClaimTemplate.metadata.selfLink

---

**Type**: string

## Description
SelfLink is a URL representing this object. Populated by the system. Read-only.      DEPRECATED Kubernetes will stop propagating this field in 1.20 release and the field is planned to be removed in 1.21 release.





---

</details>

<details>
<summary>uid: string</summary>

# Deployment.spec.template.spec.volumes.ephemeral.volumeClaimTemplate.metadata.uid

---

**Type**: string

## Description
UID is the unique in time and space value for this object. It is typically generated by the server on successful creation of a resource and is not allowed to change on PUT operations.      Populated by the system. Read-only. More info: http://kubernetes.io/docs/user-guide/identifiers#uids





---

</details>



---

</details>

<details>
<summary>spec: Object required!</summary>

# Deployment.spec.template.spec.volumes.ephemeral.volumeClaimTemplate.spec

---

**Type**: Object (required)

## Description
The specification for the PersistentVolumeClaim. The entire content is copied unchanged into the PVC that gets created from this template. The same fields as in a PersistentVolumeClaim are also valid here.




## Fields

<details>
<summary>accessModes: []string</summary>

# Deployment.spec.template.spec.volumes.ephemeral.volumeClaimTemplate.spec.accessModes

---

**Type**: []string

## Description
AccessModes contains the desired access modes the volume should have. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1





---

</details>

<details>
<summary>dataSource: Object</summary>

# Deployment.spec.template.spec.volumes.ephemeral.volumeClaimTemplate.spec.dataSource

---

**Type**: Object

## Description
This field can be used to specify either: * An existing VolumeSnapshot object (snapshot.storage.k8s.io/VolumeSnapshot) * An existing PVC (PersistentVolumeClaim) * An existing custom resource that implements data population (Alpha) In order to use custom resource types that implement data population, the AnyVolumeDataSource feature gate must be enabled. If the provisioner or an external controller can support the specified data source, it will create a new volume based on the contents of the specified data source.




## Fields

<details>
<summary>apiGroup: string</summary>

# Deployment.spec.template.spec.volumes.ephemeral.volumeClaimTemplate.spec.dataSource.apiGroup

---

**Type**: string

## Description
APIGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required.





---

</details>

<details>
<summary>kind: string required!</summary>

# Deployment.spec.template.spec.volumes.ephemeral.volumeClaimTemplate.spec.dataSource.kind

---

**Type**: string (required)

## Description
Kind is the type of resource being referenced





---

</details>

<details>
<summary>name: string required!</summary>

# Deployment.spec.template.spec.volumes.ephemeral.volumeClaimTemplate.spec.dataSource.name

---

**Type**: string (required)

## Description
Name is the name of resource being referenced





---

</details>



---

</details>

<details>
<summary>resources: Object</summary>

# Deployment.spec.template.spec.volumes.ephemeral.volumeClaimTemplate.spec.resources

---

**Type**: Object

## Description
Resources represents the minimum resources the volume should have. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#resources




## Fields

<details>
<summary>limits: map[string]string</summary>

# Deployment.spec.template.spec.volumes.ephemeral.volumeClaimTemplate.spec.resources.limits

---

**Type**: map[string]string

## Description
Limits describes the maximum amount of compute resources allowed. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/





---

</details>

<details>
<summary>requests: map[string]string</summary>

# Deployment.spec.template.spec.volumes.ephemeral.volumeClaimTemplate.spec.resources.requests

---

**Type**: map[string]string

## Description
Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/





---

</details>



---

</details>

<details>
<summary>selector: Object</summary>

# Deployment.spec.template.spec.volumes.ephemeral.volumeClaimTemplate.spec.selector

---

**Type**: Object

## Description
A label query over volumes to consider for binding.




## Fields

<details>
<summary>matchExpressions: []Object</summary>

# Deployment.spec.template.spec.volumes.ephemeral.volumeClaimTemplate.spec.selector.matchExpressions

---

**Type**: []Object

## Description
matchExpressions is a list of label selector requirements. The requirements are ANDed.




## Fields

<details>
<summary>key: string required!</summary>

# Deployment.spec.template.spec.volumes.ephemeral.volumeClaimTemplate.spec.selector.matchExpressions.key

---

**Type**: string (required)

## Description
key is the label key that the selector applies to.





---

</details>

<details>
<summary>operator: string required!</summary>

# Deployment.spec.template.spec.volumes.ephemeral.volumeClaimTemplate.spec.selector.matchExpressions.operator

---

**Type**: string (required)

## Description
operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.





---

</details>

<details>
<summary>values: []string</summary>

# Deployment.spec.template.spec.volumes.ephemeral.volumeClaimTemplate.spec.selector.matchExpressions.values

---

**Type**: []string

## Description
values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.





---

</details>



---

</details>

<details>
<summary>matchLabels: map[string]string</summary>

# Deployment.spec.template.spec.volumes.ephemeral.volumeClaimTemplate.spec.selector.matchLabels

---

**Type**: map[string]string

## Description
matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.





---

</details>



---

</details>

<details>
<summary>storageClassName: string</summary>

# Deployment.spec.template.spec.volumes.ephemeral.volumeClaimTemplate.spec.storageClassName

---

**Type**: string

## Description
Name of the StorageClass required by the claim. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#class-1





---

</details>

<details>
<summary>volumeMode: string</summary>

# Deployment.spec.template.spec.volumes.ephemeral.volumeClaimTemplate.spec.volumeMode

---

**Type**: string

## Description
volumeMode defines what type of volume is required by the claim. Value of Filesystem is implied when not included in claim spec.





---

</details>

<details>
<summary>volumeName: string</summary>

# Deployment.spec.template.spec.volumes.ephemeral.volumeClaimTemplate.spec.volumeName

---

**Type**: string

## Description
VolumeName is the binding reference to the PersistentVolume backing this claim.





---

</details>



---

</details>



---

</details>



---

</details>

<details>
<summary>fc: Object</summary>

# Deployment.spec.template.spec.volumes.fc

---

**Type**: Object

## Description
FC represents a Fibre Channel resource that is attached to a kubelet's host machine and then exposed to the pod.




## Fields

<details>
<summary>fsType: string</summary>

# Deployment.spec.template.spec.volumes.fc.fsType

---

**Type**: string

## Description
Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.





---

</details>

<details>
<summary>lun: integer</summary>

# Deployment.spec.template.spec.volumes.fc.lun

---

**Type**: integer

## Description
Optional: FC target lun number





---

</details>

<details>
<summary>readOnly: boolean</summary>

# Deployment.spec.template.spec.volumes.fc.readOnly

---

**Type**: boolean

## Description
Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.





---

</details>

<details>
<summary>targetWWNs: []string</summary>

# Deployment.spec.template.spec.volumes.fc.targetWWNs

---

**Type**: []string

## Description
Optional: FC target worldwide names (WWNs)





---

</details>

<details>
<summary>wwids: []string</summary>

# Deployment.spec.template.spec.volumes.fc.wwids

---

**Type**: []string

## Description
Optional: FC volume world wide identifiers (wwids) Either wwids or combination of targetWWNs and lun must be set, but not both simultaneously.





---

</details>



---

</details>

<details>
<summary>flexVolume: Object</summary>

# Deployment.spec.template.spec.volumes.flexVolume

---

**Type**: Object

## Description
FlexVolume represents a generic volume resource that is provisioned/attached using an exec based plugin.




## Fields

<details>
<summary>driver: string required!</summary>

# Deployment.spec.template.spec.volumes.flexVolume.driver

---

**Type**: string (required)

## Description
Driver is the name of the driver to use for this volume.





---

</details>

<details>
<summary>fsType: string</summary>

# Deployment.spec.template.spec.volumes.flexVolume.fsType

---

**Type**: string

## Description
Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". The default filesystem depends on FlexVolume script.





---

</details>

<details>
<summary>options: map[string]string</summary>

# Deployment.spec.template.spec.volumes.flexVolume.options

---

**Type**: map[string]string

## Description
Optional: Extra command options if any.





---

</details>

<details>
<summary>readOnly: boolean</summary>

# Deployment.spec.template.spec.volumes.flexVolume.readOnly

---

**Type**: boolean

## Description
Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.





---

</details>

<details>
<summary>secretRef: Object</summary>

# Deployment.spec.template.spec.volumes.flexVolume.secretRef

---

**Type**: Object

## Description
Optional: SecretRef is reference to the secret object containing sensitive information to pass to the plugin scripts. This may be empty if no secret object is specified. If the secret object contains more than one secret, all secrets are passed to the plugin scripts.




## Fields

<details>
<summary>name: string</summary>

# Deployment.spec.template.spec.volumes.flexVolume.secretRef.name

---

**Type**: string

## Description
Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names





---

</details>



---

</details>



---

</details>

<details>
<summary>flocker: Object</summary>

# Deployment.spec.template.spec.volumes.flocker

---

**Type**: Object

## Description
Flocker represents a Flocker volume attached to a kubelet's host machine. This depends on the Flocker control service being running




## Fields

<details>
<summary>datasetName: string</summary>

# Deployment.spec.template.spec.volumes.flocker.datasetName

---

**Type**: string

## Description
Name of the dataset stored as metadata -> name on the dataset for Flocker should be considered as deprecated





---

</details>

<details>
<summary>datasetUUID: string</summary>

# Deployment.spec.template.spec.volumes.flocker.datasetUUID

---

**Type**: string

## Description
UUID of the dataset. This is unique identifier of a Flocker dataset





---

</details>



---

</details>

<details>
<summary>gcePersistentDisk: Object</summary>

# Deployment.spec.template.spec.volumes.gcePersistentDisk

---

**Type**: Object

## Description
GCEPersistentDisk represents a GCE Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk




## Fields

<details>
<summary>fsType: string</summary>

# Deployment.spec.template.spec.volumes.gcePersistentDisk.fsType

---

**Type**: string

## Description
Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk





---

</details>

<details>
<summary>partition: integer</summary>

# Deployment.spec.template.spec.volumes.gcePersistentDisk.partition

---

**Type**: integer

## Description
The partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty). More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk





---

</details>

<details>
<summary>pdName: string required!</summary>

# Deployment.spec.template.spec.volumes.gcePersistentDisk.pdName

---

**Type**: string (required)

## Description
Unique name of the PD resource in GCE. Used to identify the disk in GCE. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk





---

</details>

<details>
<summary>readOnly: boolean</summary>

# Deployment.spec.template.spec.volumes.gcePersistentDisk.readOnly

---

**Type**: boolean

## Description
ReadOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk





---

</details>



---

</details>

<details>
<summary>gitRepo: Object</summary>

# Deployment.spec.template.spec.volumes.gitRepo

---

**Type**: Object

## Description
GitRepo represents a git repository at a particular revision. DEPRECATED: GitRepo is deprecated. To provision a container with a git repo, mount an EmptyDir into an InitContainer that clones the repo using git, then mount the EmptyDir into the Pod's container.




## Fields

<details>
<summary>directory: string</summary>

# Deployment.spec.template.spec.volumes.gitRepo.directory

---

**Type**: string

## Description
Target directory name. Must not contain or start with '..'. If '.' is supplied, the volume directory will be the git repository. Otherwise, if specified, the volume will contain the git repository in the subdirectory with the given name.





---

</details>

<details>
<summary>repository: string required!</summary>

# Deployment.spec.template.spec.volumes.gitRepo.repository

---

**Type**: string (required)

## Description
Repository URL





---

</details>

<details>
<summary>revision: string</summary>

# Deployment.spec.template.spec.volumes.gitRepo.revision

---

**Type**: string

## Description
Commit hash for the specified revision.





---

</details>



---

</details>

<details>
<summary>glusterfs: Object</summary>

# Deployment.spec.template.spec.volumes.glusterfs

---

**Type**: Object

## Description
Glusterfs represents a Glusterfs mount on the host that shares a pod's lifetime. More info: https://examples.k8s.io/volumes/glusterfs/README.md




## Fields

<details>
<summary>endpoints: string required!</summary>

# Deployment.spec.template.spec.volumes.glusterfs.endpoints

---

**Type**: string (required)

## Description
EndpointsName is the endpoint name that details Glusterfs topology. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod





---

</details>

<details>
<summary>path: string required!</summary>

# Deployment.spec.template.spec.volumes.glusterfs.path

---

**Type**: string (required)

## Description
Path is the Glusterfs volume path. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod





---

</details>

<details>
<summary>readOnly: boolean</summary>

# Deployment.spec.template.spec.volumes.glusterfs.readOnly

---

**Type**: boolean

## Description
ReadOnly here will force the Glusterfs volume to be mounted with read-only permissions. Defaults to false. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod





---

</details>



---

</details>

<details>
<summary>hostPath: Object</summary>

# Deployment.spec.template.spec.volumes.hostPath

---

**Type**: Object

## Description
HostPath represents a pre-existing file or directory on the host machine that is directly exposed to the container. This is generally used for system agents or other privileged things that are allowed to see the host machine. Most containers will NOT need this. More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath




## Fields

<details>
<summary>path: string required!</summary>

# Deployment.spec.template.spec.volumes.hostPath.path

---

**Type**: string (required)

## Description
Path of the directory on the host. If the path is a symlink, it will follow the link to the real path. More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath





---

</details>

<details>
<summary>type: string</summary>

# Deployment.spec.template.spec.volumes.hostPath.type

---

**Type**: string

## Description
Type for HostPath Volume Defaults to "" More info: https://kubernetes.io/docs/concepts/storage/volumes#hostpath





---

</details>



---

</details>

<details>
<summary>iscsi: Object</summary>

# Deployment.spec.template.spec.volumes.iscsi

---

**Type**: Object

## Description
ISCSI represents an ISCSI Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: https://examples.k8s.io/volumes/iscsi/README.md




## Fields

<details>
<summary>chapAuthDiscovery: boolean</summary>

# Deployment.spec.template.spec.volumes.iscsi.chapAuthDiscovery

---

**Type**: boolean

## Description
whether support iSCSI Discovery CHAP authentication





---

</details>

<details>
<summary>chapAuthSession: boolean</summary>

# Deployment.spec.template.spec.volumes.iscsi.chapAuthSession

---

**Type**: boolean

## Description
whether support iSCSI Session CHAP authentication





---

</details>

<details>
<summary>fsType: string</summary>

# Deployment.spec.template.spec.volumes.iscsi.fsType

---

**Type**: string

## Description
Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#iscsi





---

</details>

<details>
<summary>initiatorName: string</summary>

# Deployment.spec.template.spec.volumes.iscsi.initiatorName

---

**Type**: string

## Description
Custom iSCSI Initiator Name. If initiatorName is specified with iscsiInterface simultaneously, new iSCSI interface <target portal>:<volume name> will be created for the connection.





---

</details>

<details>
<summary>iqn: string required!</summary>

# Deployment.spec.template.spec.volumes.iscsi.iqn

---

**Type**: string (required)

## Description
Target iSCSI Qualified Name.





---

</details>

<details>
<summary>iscsiInterface: string</summary>

# Deployment.spec.template.spec.volumes.iscsi.iscsiInterface

---

**Type**: string

## Description
iSCSI Interface Name that uses an iSCSI transport. Defaults to 'default' (tcp).





---

</details>

<details>
<summary>lun: integer required!</summary>

# Deployment.spec.template.spec.volumes.iscsi.lun

---

**Type**: integer (required)

## Description
iSCSI Target Lun number.





---

</details>

<details>
<summary>portals: []string</summary>

# Deployment.spec.template.spec.volumes.iscsi.portals

---

**Type**: []string

## Description
iSCSI Target Portal List. The portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260).





---

</details>

<details>
<summary>readOnly: boolean</summary>

# Deployment.spec.template.spec.volumes.iscsi.readOnly

---

**Type**: boolean

## Description
ReadOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false.





---

</details>

<details>
<summary>secretRef: Object</summary>

# Deployment.spec.template.spec.volumes.iscsi.secretRef

---

**Type**: Object

## Description
CHAP Secret for iSCSI target and initiator authentication




## Fields

<details>
<summary>name: string</summary>

# Deployment.spec.template.spec.volumes.iscsi.secretRef.name

---

**Type**: string

## Description
Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names





---

</details>



---

</details>

<details>
<summary>targetPortal: string required!</summary>

# Deployment.spec.template.spec.volumes.iscsi.targetPortal

---

**Type**: string (required)

## Description
iSCSI Target Portal. The Portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260).





---

</details>



---

</details>

<details>
<summary>name: string required!</summary>

# Deployment.spec.template.spec.volumes.name

---

**Type**: string (required)

## Description
Volume's name. Must be a DNS_LABEL and unique within the pod. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names





---

</details>

<details>
<summary>nfs: Object</summary>

# Deployment.spec.template.spec.volumes.nfs

---

**Type**: Object

## Description
NFS represents an NFS mount on the host that shares a pod's lifetime More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs




## Fields

<details>
<summary>path: string required!</summary>

# Deployment.spec.template.spec.volumes.nfs.path

---

**Type**: string (required)

## Description
Path that is exported by the NFS server. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs





---

</details>

<details>
<summary>readOnly: boolean</summary>

# Deployment.spec.template.spec.volumes.nfs.readOnly

---

**Type**: boolean

## Description
ReadOnly here will force the NFS export to be mounted with read-only permissions. Defaults to false. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs





---

</details>

<details>
<summary>server: string required!</summary>

# Deployment.spec.template.spec.volumes.nfs.server

---

**Type**: string (required)

## Description
Server is the hostname or IP address of the NFS server. More info: https://kubernetes.io/docs/concepts/storage/volumes#nfs





---

</details>



---

</details>

<details>
<summary>persistentVolumeClaim: Object</summary>

# Deployment.spec.template.spec.volumes.persistentVolumeClaim

---

**Type**: Object

## Description
PersistentVolumeClaimVolumeSource represents a reference to a PersistentVolumeClaim in the same namespace. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims




## Fields

<details>
<summary>claimName: string required!</summary>

# Deployment.spec.template.spec.volumes.persistentVolumeClaim.claimName

---

**Type**: string (required)

## Description
ClaimName is the name of a PersistentVolumeClaim in the same namespace as the pod using this volume. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims





---

</details>

<details>
<summary>readOnly: boolean</summary>

# Deployment.spec.template.spec.volumes.persistentVolumeClaim.readOnly

---

**Type**: boolean

## Description
Will force the ReadOnly setting in VolumeMounts. Default false.





---

</details>



---

</details>

<details>
<summary>photonPersistentDisk: Object</summary>

# Deployment.spec.template.spec.volumes.photonPersistentDisk

---

**Type**: Object

## Description
PhotonPersistentDisk represents a PhotonController persistent disk attached and mounted on kubelets host machine




## Fields

<details>
<summary>fsType: string</summary>

# Deployment.spec.template.spec.volumes.photonPersistentDisk.fsType

---

**Type**: string

## Description
Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.





---

</details>

<details>
<summary>pdID: string required!</summary>

# Deployment.spec.template.spec.volumes.photonPersistentDisk.pdID

---

**Type**: string (required)

## Description
ID that identifies Photon Controller persistent disk





---

</details>



---

</details>

<details>
<summary>portworxVolume: Object</summary>

# Deployment.spec.template.spec.volumes.portworxVolume

---

**Type**: Object

## Description
PortworxVolume represents a portworx volume attached and mounted on kubelets host machine




## Fields

<details>
<summary>fsType: string</summary>

# Deployment.spec.template.spec.volumes.portworxVolume.fsType

---

**Type**: string

## Description
FSType represents the filesystem type to mount Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs". Implicitly inferred to be "ext4" if unspecified.





---

</details>

<details>
<summary>readOnly: boolean</summary>

# Deployment.spec.template.spec.volumes.portworxVolume.readOnly

---

**Type**: boolean

## Description
Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.





---

</details>

<details>
<summary>volumeID: string required!</summary>

# Deployment.spec.template.spec.volumes.portworxVolume.volumeID

---

**Type**: string (required)

## Description
VolumeID uniquely identifies a Portworx volume





---

</details>



---

</details>

<details>
<summary>projected: Object</summary>

# Deployment.spec.template.spec.volumes.projected

---

**Type**: Object

## Description
Items for all in one resources secrets, configmaps, and downward API




## Fields

<details>
<summary>defaultMode: integer</summary>

# Deployment.spec.template.spec.volumes.projected.defaultMode

---

**Type**: integer

## Description
Mode bits used to set permissions on created files by default. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.





---

</details>

<details>
<summary>sources: []Object</summary>

# Deployment.spec.template.spec.volumes.projected.sources

---

**Type**: []Object

## Description
list of volume projections




## Fields

<details>
<summary>configMap: Object</summary>

# Deployment.spec.template.spec.volumes.projected.sources.configMap

---

**Type**: Object

## Description
information about the configMap data to project




## Fields

<details>
<summary>items: []Object</summary>

# Deployment.spec.template.spec.volumes.projected.sources.configMap.items

---

**Type**: []Object

## Description
If unspecified, each key-value pair in the Data field of the referenced ConfigMap will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the ConfigMap, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.




## Fields

<details>
<summary>key: string required!</summary>

# Deployment.spec.template.spec.volumes.projected.sources.configMap.items.key

---

**Type**: string (required)

## Description
The key to project.





---

</details>

<details>
<summary>mode: integer</summary>

# Deployment.spec.template.spec.volumes.projected.sources.configMap.items.mode

---

**Type**: integer

## Description
Optional: mode bits used to set permissions on this file. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.





---

</details>

<details>
<summary>path: string required!</summary>

# Deployment.spec.template.spec.volumes.projected.sources.configMap.items.path

---

**Type**: string (required)

## Description
The relative path of the file to map the key to. May not be an absolute path. May not contain the path element '..'. May not start with the string '..'.





---

</details>



---

</details>

<details>
<summary>name: string</summary>

# Deployment.spec.template.spec.volumes.projected.sources.configMap.name

---

**Type**: string

## Description
Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names





---

</details>

<details>
<summary>optional: boolean</summary>

# Deployment.spec.template.spec.volumes.projected.sources.configMap.optional

---

**Type**: boolean

## Description
Specify whether the ConfigMap or its keys must be defined





---

</details>



---

</details>

<details>
<summary>downwardAPI: Object</summary>

# Deployment.spec.template.spec.volumes.projected.sources.downwardAPI

---

**Type**: Object

## Description
information about the downwardAPI data to project




## Fields

<details>
<summary>items: []Object</summary>

# Deployment.spec.template.spec.volumes.projected.sources.downwardAPI.items

---

**Type**: []Object

## Description
Items is a list of DownwardAPIVolume file




## Fields

<details>
<summary>fieldRef: Object</summary>

# Deployment.spec.template.spec.volumes.projected.sources.downwardAPI.items.fieldRef

---

**Type**: Object

## Description
Required: Selects a field of the pod: only annotations, labels, name and namespace are supported.




## Fields

<details>
<summary>apiVersion: string</summary>

# Deployment.spec.template.spec.volumes.projected.sources.downwardAPI.items.fieldRef.apiVersion

---

**Type**: string

## Description
Version of the schema the FieldPath is written in terms of, defaults to "v1".





---

</details>

<details>
<summary>fieldPath: string required!</summary>

# Deployment.spec.template.spec.volumes.projected.sources.downwardAPI.items.fieldRef.fieldPath

---

**Type**: string (required)

## Description
Path of the field to select in the specified API version.





---

</details>



---

</details>

<details>
<summary>mode: integer</summary>

# Deployment.spec.template.spec.volumes.projected.sources.downwardAPI.items.mode

---

**Type**: integer

## Description
Optional: mode bits used to set permissions on this file, must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.





---

</details>

<details>
<summary>path: string required!</summary>

# Deployment.spec.template.spec.volumes.projected.sources.downwardAPI.items.path

---

**Type**: string (required)

## Description
Required: Path is the relative path name of the file to be created. Must not be absolute or contain the '..' path. Must be utf-8 encoded. The first item of the relative path must not start with '..'





---

</details>

<details>
<summary>resourceFieldRef: Object</summary>

# Deployment.spec.template.spec.volumes.projected.sources.downwardAPI.items.resourceFieldRef

---

**Type**: Object

## Description
Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, requests.cpu and requests.memory) are currently supported.




## Fields

<details>
<summary>containerName: string</summary>

# Deployment.spec.template.spec.volumes.projected.sources.downwardAPI.items.resourceFieldRef.containerName

---

**Type**: string

## Description
Container name: required for volumes, optional for env vars





---

</details>

<details>
<summary>divisor: string</summary>

# Deployment.spec.template.spec.volumes.projected.sources.downwardAPI.items.resourceFieldRef.divisor

---

**Type**: string

## Description
Specifies the output format of the exposed resources, defaults to "1"





---

</details>

<details>
<summary>resource: string required!</summary>

# Deployment.spec.template.spec.volumes.projected.sources.downwardAPI.items.resourceFieldRef.resource

---

**Type**: string (required)

## Description
Required: resource to select





---

</details>



---

</details>



---

</details>



---

</details>

<details>
<summary>secret: Object</summary>

# Deployment.spec.template.spec.volumes.projected.sources.secret

---

**Type**: Object

## Description
information about the secret data to project




## Fields

<details>
<summary>items: []Object</summary>

# Deployment.spec.template.spec.volumes.projected.sources.secret.items

---

**Type**: []Object

## Description
If unspecified, each key-value pair in the Data field of the referenced Secret will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the Secret, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.




## Fields

<details>
<summary>key: string required!</summary>

# Deployment.spec.template.spec.volumes.projected.sources.secret.items.key

---

**Type**: string (required)

## Description
The key to project.





---

</details>

<details>
<summary>mode: integer</summary>

# Deployment.spec.template.spec.volumes.projected.sources.secret.items.mode

---

**Type**: integer

## Description
Optional: mode bits used to set permissions on this file. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.





---

</details>

<details>
<summary>path: string required!</summary>

# Deployment.spec.template.spec.volumes.projected.sources.secret.items.path

---

**Type**: string (required)

## Description
The relative path of the file to map the key to. May not be an absolute path. May not contain the path element '..'. May not start with the string '..'.





---

</details>



---

</details>

<details>
<summary>name: string</summary>

# Deployment.spec.template.spec.volumes.projected.sources.secret.name

---

**Type**: string

## Description
Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names





---

</details>

<details>
<summary>optional: boolean</summary>

# Deployment.spec.template.spec.volumes.projected.sources.secret.optional

---

**Type**: boolean

## Description
Specify whether the Secret or its key must be defined





---

</details>



---

</details>

<details>
<summary>serviceAccountToken: Object</summary>

# Deployment.spec.template.spec.volumes.projected.sources.serviceAccountToken

---

**Type**: Object

## Description
information about the serviceAccountToken data to project




## Fields

<details>
<summary>audience: string</summary>

# Deployment.spec.template.spec.volumes.projected.sources.serviceAccountToken.audience

---

**Type**: string

## Description
Audience is the intended audience of the token. A recipient of a token must identify itself with an identifier specified in the audience of the token, and otherwise should reject the token. The audience defaults to the identifier of the apiserver.





---

</details>

<details>
<summary>expirationSeconds: integer</summary>

# Deployment.spec.template.spec.volumes.projected.sources.serviceAccountToken.expirationSeconds

---

**Type**: integer

## Description
ExpirationSeconds is the requested duration of validity of the service account token. As the token approaches expiration, the kubelet volume plugin will proactively rotate the service account token. The kubelet will start trying to rotate the token if the token is older than 80 percent of its time to live or if the token is older than 24 hours.Defaults to 1 hour and must be at least 10 minutes.





---

</details>

<details>
<summary>path: string required!</summary>

# Deployment.spec.template.spec.volumes.projected.sources.serviceAccountToken.path

---

**Type**: string (required)

## Description
Path is the path relative to the mount point of the file to project the token into.





---

</details>



---

</details>



---

</details>



---

</details>

<details>
<summary>quobyte: Object</summary>

# Deployment.spec.template.spec.volumes.quobyte

---

**Type**: Object

## Description
Quobyte represents a Quobyte mount on the host that shares a pod's lifetime




## Fields

<details>
<summary>group: string</summary>

# Deployment.spec.template.spec.volumes.quobyte.group

---

**Type**: string

## Description
Group to map volume access to Default is no group





---

</details>

<details>
<summary>readOnly: boolean</summary>

# Deployment.spec.template.spec.volumes.quobyte.readOnly

---

**Type**: boolean

## Description
ReadOnly here will force the Quobyte volume to be mounted with read-only permissions. Defaults to false.





---

</details>

<details>
<summary>registry: string required!</summary>

# Deployment.spec.template.spec.volumes.quobyte.registry

---

**Type**: string (required)

## Description
Registry represents a single or multiple Quobyte Registry services specified as a string as host:port pair (multiple entries are separated with commas) which acts as the central registry for volumes





---

</details>

<details>
<summary>tenant: string</summary>

# Deployment.spec.template.spec.volumes.quobyte.tenant

---

**Type**: string

## Description
Tenant owning the given Quobyte volume in the Backend Used with dynamically provisioned Quobyte volumes, value is set by the plugin





---

</details>

<details>
<summary>user: string</summary>

# Deployment.spec.template.spec.volumes.quobyte.user

---

**Type**: string

## Description
User to map volume access to Defaults to serivceaccount user





---

</details>

<details>
<summary>volume: string required!</summary>

# Deployment.spec.template.spec.volumes.quobyte.volume

---

**Type**: string (required)

## Description
Volume is a string that references an already created Quobyte volume by name.





---

</details>



---

</details>

<details>
<summary>rbd: Object</summary>

# Deployment.spec.template.spec.volumes.rbd

---

**Type**: Object

## Description
RBD represents a Rados Block Device mount on the host that shares a pod's lifetime. More info: https://examples.k8s.io/volumes/rbd/README.md




## Fields

<details>
<summary>fsType: string</summary>

# Deployment.spec.template.spec.volumes.rbd.fsType

---

**Type**: string

## Description
Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: https://kubernetes.io/docs/concepts/storage/volumes#rbd





---

</details>

<details>
<summary>image: string required!</summary>

# Deployment.spec.template.spec.volumes.rbd.image

---

**Type**: string (required)

## Description
The rados image name. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it





---

</details>

<details>
<summary>keyring: string</summary>

# Deployment.spec.template.spec.volumes.rbd.keyring

---

**Type**: string

## Description
Keyring is the path to key ring for RBDUser. Default is /etc/ceph/keyring. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it





---

</details>

<details>
<summary>monitors: []string required!</summary>

# Deployment.spec.template.spec.volumes.rbd.monitors

---

**Type**: []string (required)

## Description
A collection of Ceph monitors. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it





---

</details>

<details>
<summary>pool: string</summary>

# Deployment.spec.template.spec.volumes.rbd.pool

---

**Type**: string

## Description
The rados pool name. Default is rbd. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it





---

</details>

<details>
<summary>readOnly: boolean</summary>

# Deployment.spec.template.spec.volumes.rbd.readOnly

---

**Type**: boolean

## Description
ReadOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it





---

</details>

<details>
<summary>secretRef: Object</summary>

# Deployment.spec.template.spec.volumes.rbd.secretRef

---

**Type**: Object

## Description
SecretRef is name of the authentication secret for RBDUser. If provided overrides keyring. Default is nil. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it




## Fields

<details>
<summary>name: string</summary>

# Deployment.spec.template.spec.volumes.rbd.secretRef.name

---

**Type**: string

## Description
Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names





---

</details>



---

</details>

<details>
<summary>user: string</summary>

# Deployment.spec.template.spec.volumes.rbd.user

---

**Type**: string

## Description
The rados user name. Default is admin. More info: https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it





---

</details>



---

</details>

<details>
<summary>scaleIO: Object</summary>

# Deployment.spec.template.spec.volumes.scaleIO

---

**Type**: Object

## Description
ScaleIO represents a ScaleIO persistent volume attached and mounted on Kubernetes nodes.




## Fields

<details>
<summary>fsType: string</summary>

# Deployment.spec.template.spec.volumes.scaleIO.fsType

---

**Type**: string

## Description
Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Default is "xfs".





---

</details>

<details>
<summary>gateway: string required!</summary>

# Deployment.spec.template.spec.volumes.scaleIO.gateway

---

**Type**: string (required)

## Description
The host address of the ScaleIO API Gateway.





---

</details>

<details>
<summary>protectionDomain: string</summary>

# Deployment.spec.template.spec.volumes.scaleIO.protectionDomain

---

**Type**: string

## Description
The name of the ScaleIO Protection Domain for the configured storage.





---

</details>

<details>
<summary>readOnly: boolean</summary>

# Deployment.spec.template.spec.volumes.scaleIO.readOnly

---

**Type**: boolean

## Description
Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.





---

</details>

<details>
<summary>secretRef: Object required!</summary>

# Deployment.spec.template.spec.volumes.scaleIO.secretRef

---

**Type**: Object (required)

## Description
SecretRef references to the secret for ScaleIO user and other sensitive information. If this is not provided, Login operation will fail.




## Fields

<details>
<summary>name: string</summary>

# Deployment.spec.template.spec.volumes.scaleIO.secretRef.name

---

**Type**: string

## Description
Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names





---

</details>



---

</details>

<details>
<summary>sslEnabled: boolean</summary>

# Deployment.spec.template.spec.volumes.scaleIO.sslEnabled

---

**Type**: boolean

## Description
Flag to enable/disable SSL communication with Gateway, default false





---

</details>

<details>
<summary>storageMode: string</summary>

# Deployment.spec.template.spec.volumes.scaleIO.storageMode

---

**Type**: string

## Description
Indicates whether the storage for a volume should be ThickProvisioned or ThinProvisioned. Default is ThinProvisioned.





---

</details>

<details>
<summary>storagePool: string</summary>

# Deployment.spec.template.spec.volumes.scaleIO.storagePool

---

**Type**: string

## Description
The ScaleIO Storage Pool associated with the protection domain.





---

</details>

<details>
<summary>system: string required!</summary>

# Deployment.spec.template.spec.volumes.scaleIO.system

---

**Type**: string (required)

## Description
The name of the storage system as configured in ScaleIO.





---

</details>

<details>
<summary>volumeName: string</summary>

# Deployment.spec.template.spec.volumes.scaleIO.volumeName

---

**Type**: string

## Description
The name of a volume already created in the ScaleIO system that is associated with this volume source.





---

</details>



---

</details>

<details>
<summary>secret: Object</summary>

# Deployment.spec.template.spec.volumes.secret

---

**Type**: Object

## Description
Secret represents a secret that should populate this volume. More info: https://kubernetes.io/docs/concepts/storage/volumes#secret




## Fields

<details>
<summary>defaultMode: integer</summary>

# Deployment.spec.template.spec.volumes.secret.defaultMode

---

**Type**: integer

## Description
Optional: mode bits used to set permissions on created files by default. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.





---

</details>

<details>
<summary>items: []Object</summary>

# Deployment.spec.template.spec.volumes.secret.items

---

**Type**: []Object

## Description
If unspecified, each key-value pair in the Data field of the referenced Secret will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the Secret, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.




## Fields

<details>
<summary>key: string required!</summary>

# Deployment.spec.template.spec.volumes.secret.items.key

---

**Type**: string (required)

## Description
The key to project.





---

</details>

<details>
<summary>mode: integer</summary>

# Deployment.spec.template.spec.volumes.secret.items.mode

---

**Type**: integer

## Description
Optional: mode bits used to set permissions on this file. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.





---

</details>

<details>
<summary>path: string required!</summary>

# Deployment.spec.template.spec.volumes.secret.items.path

---

**Type**: string (required)

## Description
The relative path of the file to map the key to. May not be an absolute path. May not contain the path element '..'. May not start with the string '..'.





---

</details>



---

</details>

<details>
<summary>optional: boolean</summary>

# Deployment.spec.template.spec.volumes.secret.optional

---

**Type**: boolean

## Description
Specify whether the Secret or its keys must be defined





---

</details>

<details>
<summary>secretName: string</summary>

# Deployment.spec.template.spec.volumes.secret.secretName

---

**Type**: string

## Description
Name of the secret in the pod's namespace to use. More info: https://kubernetes.io/docs/concepts/storage/volumes#secret





---

</details>



---

</details>

<details>
<summary>storageos: Object</summary>

# Deployment.spec.template.spec.volumes.storageos

---

**Type**: Object

## Description
StorageOS represents a StorageOS volume attached and mounted on Kubernetes nodes.




## Fields

<details>
<summary>fsType: string</summary>

# Deployment.spec.template.spec.volumes.storageos.fsType

---

**Type**: string

## Description
Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.





---

</details>

<details>
<summary>readOnly: boolean</summary>

# Deployment.spec.template.spec.volumes.storageos.readOnly

---

**Type**: boolean

## Description
Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.





---

</details>

<details>
<summary>secretRef: Object</summary>

# Deployment.spec.template.spec.volumes.storageos.secretRef

---

**Type**: Object

## Description
SecretRef specifies the secret to use for obtaining the StorageOS API credentials. If not specified, default values will be attempted.




## Fields

<details>
<summary>name: string</summary>

# Deployment.spec.template.spec.volumes.storageos.secretRef.name

---

**Type**: string

## Description
Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names





---

</details>



---

</details>

<details>
<summary>volumeName: string</summary>

# Deployment.spec.template.spec.volumes.storageos.volumeName

---

**Type**: string

## Description
VolumeName is the human-readable name of the StorageOS volume. Volume names are only unique within a namespace.





---

</details>

<details>
<summary>volumeNamespace: string</summary>

# Deployment.spec.template.spec.volumes.storageos.volumeNamespace

---

**Type**: string

## Description
VolumeNamespace specifies the scope of the volume within StorageOS. If no namespace is specified then the Pod's namespace will be used. This allows the Kubernetes name scoping to be mirrored within StorageOS for tighter integration. Set VolumeName to any name to override the default behaviour. Set to "default" if you are not using namespaces within StorageOS. Namespaces that do not pre-exist within StorageOS will be created.





---

</details>



---

</details>

<details>
<summary>vsphereVolume: Object</summary>

# Deployment.spec.template.spec.volumes.vsphereVolume

---

**Type**: Object

## Description
VsphereVolume represents a vSphere volume attached and mounted on kubelets host machine




## Fields

<details>
<summary>fsType: string</summary>

# Deployment.spec.template.spec.volumes.vsphereVolume.fsType

---

**Type**: string

## Description
Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.





---

</details>

<details>
<summary>storagePolicyID: string</summary>

# Deployment.spec.template.spec.volumes.vsphereVolume.storagePolicyID

---

**Type**: string

## Description
Storage Policy Based Management (SPBM) profile ID associated with the StoragePolicyName.





---

</details>

<details>
<summary>storagePolicyName: string</summary>

# Deployment.spec.template.spec.volumes.vsphereVolume.storagePolicyName

---

**Type**: string

## Description
Storage Policy Based Management (SPBM) profile name.





---

</details>

<details>
<summary>volumePath: string required!</summary>

# Deployment.spec.template.spec.volumes.vsphereVolume.volumePath

---

**Type**: string (required)

## Description
Path that identifies vSphere volume vmdk





---

</details>



---

</details>



---

</details>



---

</details>



---

</details>



---

</details>

<details>
<summary>status: Object</summary>

# Deployment.status

---

**Type**: Object

## Description
Most recently observed status of the Deployment.




## Fields

<details>
<summary>availableReplicas: integer</summary>

# Deployment.status.availableReplicas

---

**Type**: integer

## Description
Total number of available pods (ready for at least minReadySeconds) targeted by this deployment.





---

</details>

<details>
<summary>collisionCount: integer</summary>

# Deployment.status.collisionCount

---

**Type**: integer

## Description
Count of hash collisions for the Deployment. The Deployment controller uses this field as a collision avoidance mechanism when it needs to create the name for the newest ReplicaSet.





---

</details>

<details>
<summary>conditions: []Object</summary>

# Deployment.status.conditions

---

**Type**: []Object

## Description
Represents the latest available observations of a deployment's current state.




## Fields

<details>
<summary>lastTransitionTime: string</summary>

# Deployment.status.conditions.lastTransitionTime

---

**Type**: string

## Description
Last time the condition transitioned from one status to another.





---

</details>

<details>
<summary>lastUpdateTime: string</summary>

# Deployment.status.conditions.lastUpdateTime

---

**Type**: string

## Description
The last time this condition was updated.





---

</details>

<details>
<summary>message: string</summary>

# Deployment.status.conditions.message

---

**Type**: string

## Description
A human readable message indicating details about the transition.





---

</details>

<details>
<summary>reason: string</summary>

# Deployment.status.conditions.reason

---

**Type**: string

## Description
The reason for the condition's last transition.





---

</details>

<details>
<summary>status: string required!</summary>

# Deployment.status.conditions.status

---

**Type**: string (required)

## Description
Status of the condition, one of True, False, Unknown.





---

</details>

<details>
<summary>type: string required!</summary>

# Deployment.status.conditions.type

---

**Type**: string (required)

## Description
Type of deployment condition.





---

</details>



---

</details>

<details>
<summary>observedGeneration: integer</summary>

# Deployment.status.observedGeneration

---

**Type**: integer

## Description
The generation observed by the deployment controller.





---

</details>

<details>
<summary>readyReplicas: integer</summary>

# Deployment.status.readyReplicas

---

**Type**: integer

## Description
Total number of ready pods targeted by this deployment.





---

</details>

<details>
<summary>replicas: integer</summary>

# Deployment.status.replicas

---

**Type**: integer

## Description
Total number of non-terminated pods targeted by this deployment (their labels match the selector).





---

</details>

<details>
<summary>unavailableReplicas: integer</summary>

# Deployment.status.unavailableReplicas

---

**Type**: integer

## Description
Total number of unavailable pods targeted by this deployment. This is the total number of pods that are still required for the deployment to have 100% available capacity. They may either be pods that are running but not yet available or pods that still have not been created.





---

</details>

<details>
<summary>updatedReplicas: integer</summary>

# Deployment.status.updatedReplicas

---

**Type**: integer

## Description
Total number of non-terminated pods targeted by this deployment that have the desired template spec.





---

</details>



---

</details>



---