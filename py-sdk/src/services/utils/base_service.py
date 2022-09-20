"""
Base Service

Source: https://github.com/pocketbase/js-sdk/blob/master/src/services/utils/BaseService.ts

import Client from '@/Client';

"""
from abc import ABC, abstractmethod
from ...client import Client

class BaseService(ABC):
    """
    BaseService class that should be inherited from all API services.
    
    export default abstract class BaseService { readonly client: Client; }
    """
    def __init__(self, client: Client):
        """
        constructor(client: Client) { this.client = client;}
        """
        self.client = client

    @abstractmethod
    def __repr__(self):
        pass
    
    @abstractmethod
    def __str__(self):
        pass
