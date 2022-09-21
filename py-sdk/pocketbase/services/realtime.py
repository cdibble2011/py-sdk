"""
pocketbase/services/realtime

declare class Realtime extends BaseService {
    private clientId;
    private eventSource;
    private subscriptions;
    /**
     * Inits the sse connection (if not already) and register the subscription.
     */
    subscribe(subscription: string, callback: SubscriptionFunc): Promise<void>;
    /**
     * Unsubscribe from a subscription.
     *
     * If the `subscription` argument is not set,
     * then the client will unsubscribe from all registered subscriptions.
     *
     * The related sse connection will be autoclosed if after the
     * unsubscribe operations there are no active subscriptions left.
     */
    unsubscribe(subscription?: string): Promise<void>;
    private submitSubscriptions;
    private addSubscriptionListeners;
    private removeSubscriptionListeners;
    private connectHandler;
    private connect;
    private disconnect;
}
"""

from typing import Optional, Dict, Any, List

from ..abstracts import BaseService
from ..ifaces import SubscriptionFunc 

class Realtime(BaseService):
    def __init__(self, client):
        super().__init__(client)
        self.client_id = None
        self.event_source = None
        self.subscriptions = []

    def subscribe(self, subscription: str, callback: SubscriptionFunc) -> None:
        """
        Inits the sse connection (if not already) and register the subscription.
        """
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)
        self.submit_subscriptions()
        self.add_subscription_listeners(callback)

    def unsubscribe(self, subscription: Optional[str] = None) -> None:
        """
        Unsubscribe from a subscription.
        
        If the `subscription` argument is not set,
        then the client will unsubscribe from all registered subscriptions.
        
        The related sse connection will be autoclosed if after the
        unsubscribe operations there are no active subscriptions left.
        """
        if subscription:
            if subscription in self.subscriptions:
                self.subscriptions.remove(subscription)
        else:
            self.subscriptions = []
        self.submit_subscriptions()
        self.remove_subscription_listeners()

    def submit_subscriptions(self):
        if self.subscriptions:
            self.connect()
        else:
            self.disconnect()

    def add_subscription_listeners(self, callback: SubscriptionFunc):
        self.event_source.on('open', self.connect_handler)
        self.event_source.on('message', callback)

    def remove_subscription_listeners(self):
        self.event_source.off('open', self.connect_handler)
        self.event_source.off('message')

    def connect_handler(self):
        self.client_id = self.event_source.lastEventId

    def connect(self):
        if self.event_source:
            self.event_source.close()
        self.event_source = new EventSource(self.client.getApiUrl() + 'realtime', {
            headers: {
                'X-Client-ID': this.clientId,
                'X-Client-Token': this.client.getToken(),
                'X-Client-Auth-Type': this.client.getAuthType(),
            },
        })

    def disconnect(self):
        if self.event_source:
            self.event_source.close()
            self.event_source = None
            self.client_id = None
    