from .resource import NamespacedResource


class KubevirtTemplateValidator(NamespacedResource):

    api_group = NamespacedResource.ApiGroup.SSP_KUBEVIRT_IO
