# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, Callable, Dict, Generic, Iterable, Optional, TypeVar
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.mgmt.core.exceptions import ARMErrorFormat
from msrest import Serializer

from .. import models as _models
from .._vendor import _convert_request, _format_url_section
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False

def build_get_by_policy_mode_request(
    policy_mode: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2020-09-01"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/providers/Microsoft.Authorization/dataPolicyManifests/{policyMode}')
    path_format_arguments = {
        "policyMode": _SERIALIZER.url("policy_mode", policy_mode, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_list_request(
    *,
    filter: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    api_version = "2020-09-01"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/providers/Microsoft.Authorization/dataPolicyManifests')

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')
    if filter is not None:
        query_parameters['$filter'] = _SERIALIZER.query("filter", filter, 'str', skip_quote=True)

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )

class DataPolicyManifestsOperations(object):
    """DataPolicyManifestsOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.resource.policy.v2021_06_01.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace
    def get_by_policy_mode(
        self,
        policy_mode: str,
        **kwargs: Any
    ) -> "_models.DataPolicyManifest":
        """Retrieves a data policy manifest.

        This operation retrieves the data policy manifest with the given policy mode.

        :param policy_mode: The policy mode of the data policy manifest to get.
        :type policy_mode: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DataPolicyManifest, or the result of cls(response)
        :rtype: ~azure.mgmt.resource.policy.v2021_06_01.models.DataPolicyManifest
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.DataPolicyManifest"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_get_by_policy_mode_request(
            policy_mode=policy_mode,
            template_url=self.get_by_policy_mode.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('DataPolicyManifest', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_by_policy_mode.metadata = {'url': '/providers/Microsoft.Authorization/dataPolicyManifests/{policyMode}'}  # type: ignore


    @distributed_trace
    def list(
        self,
        filter: Optional[str] = None,
        **kwargs: Any
    ) -> Iterable["_models.DataPolicyManifestListResult"]:
        """Retrieves data policy manifests.

        This operation retrieves a list of all the data policy manifests that match the optional given
        $filter. Valid values for $filter are: "$filter=namespace eq '{0}'". If $filter is not
        provided, the unfiltered list includes all data policy manifests for data resource types. If
        $filter=namespace is provided, the returned list only includes all data policy manifests that
        have a namespace matching the provided value.

        :param filter: The filter to apply on the operation. Valid values for $filter are: "namespace
         eq '{value}'". If $filter is not provided, no filtering is performed. If $filter=namespace eq
         '{value}' is provided, the returned list only includes all data policy manifests that have a
         namespace matching the provided value.
        :type filter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either DataPolicyManifestListResult or the result of
         cls(response)
        :rtype:
         ~azure.core.paging.ItemPaged[~azure.mgmt.resource.policy.v2021_06_01.models.DataPolicyManifestListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.DataPolicyManifestListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_request(
                    filter=filter,
                    template_url=self.list.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_request(
                    filter=filter,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("DataPolicyManifestListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response


        return ItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': '/providers/Microsoft.Authorization/dataPolicyManifests'}  # type: ignore