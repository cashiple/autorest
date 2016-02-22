# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .resource import Resource


class StorageAccountCreateParameters(Resource):
    """
    The parameters to provide for the account.

    :param str id: Resource Id
    :param str name: Resource name
    :param str type: Resource type
    :param str location: Resource location
    :param dict tags: Resource tags
    :param str account_type: Gets or sets the account type. Possible values
     include: 'Standard_LRS', 'Standard_ZRS', 'Standard_GRS',
     'Standard_RAGRS', 'Premium_LRS'
    """

    _required = []

    _attribute_map = {
        'account_type': {'key': 'properties.accountType', 'type': 'AccountType', 'flatten': True},
    }

    def __init__(self, location, id=None, name=None, type=None, tags=None, account_type=None):
        super(StorageAccountCreateParameters, self).__init__(id=id, name=name, type=type, location=location, tags=tags)
        self.account_type = account_type