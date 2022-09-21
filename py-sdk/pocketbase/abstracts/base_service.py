"""
pocketbase/models/abstracts/base_service.py

/**
 * BaseService class that should be inherited from all API services.
 */
declare abstract class BaseService {
    readonly client: Client;
    constructor(client: Client);
}
"""
from abc import ABC

class BaseService(ABC):
    def __init__(self, client):
        self.client = client

