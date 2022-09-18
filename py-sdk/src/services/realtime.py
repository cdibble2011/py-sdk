"""
Realtime Service

Source: https://github.com/pocketbase/js-sdk/blob/master/src/services/Realtime.ts

import BaseService from '@/services/utils/BaseService';
import Record      from '@/models/Record';


"""
from .utils import BaseService
from pocketbase.api.models import Record

class MessageData:
    """
    export interface MessageData {
        [key: string]: any;
        action: string;
        record: Record;
    }
    """
    def __init__(self, action: str, record: Record):
        self.action = action
        self.record = record
        
class SubscriptionFunc:
    """
    export interface SubscriptionFunc{
        (data: MessageData):void;
    }
    """
    def __init__(self, data: MessageData):
        self.data = data

class Realtime(BaseService):
    """
    export default class Realtime extends BaseService {
        private clientId: string = "";
        private eventSource: EventSource | null = null;
        private subscriptions: { [key: string]: EventListener } = {};
    """
    def __init__(self, client):
        super().__init__(client)
        self.client_id = ""
        self.event_source = None
        self.subscriptions = {}
    
    async def subscribe(self, subscription, callback):
        """        
        /**
         * Inits the sse connection (if not already) and register the subscription.
         */
        async subscribe(subscription: string, callback: SubscriptionFunc): Promise<void> {
            if (!subscription) {
                throw new Error('subscription must be set.')
            }

            // unsubscribe existing
            if (this.subscriptions[subscription]) {
                this.eventSource?.removeEventListener(subscription, this.subscriptions[subscription]);
            }

            // register subscription
            this.subscriptions[subscription] = function (e: Event) {
                const msgEvent = (e as MessageEvent);

                let data;
                try {
                    data = JSON.parse(msgEvent?.data);
                } catch {}

                callback(data || {});
            }

            if (!this.eventSource) {
                // start a new sse connection
                this.connect();
            } else if (this.clientId) {
                // otherwise - just persist the updated subscriptions
                await this.submitSubscriptions();
            }
        }
        """
        if not subscription:
            raise Exception('subscription must be set.')
        
        # unsubscribe existing
        if self.subscriptions[subscription]:
            self.event_source.remove_event_listener(subscription, self.subscriptions[subscription])
        
        # register subscription
        self.subscriptions[subscription] = lambda e: callback(MessageData(e.data))
        
        if not self.event_source:
            # start a new sse connection
            self.connect()
        elif self.client_id:
            # otherwise - just persist the updated subscriptions
            await self.submit_subscriptions()
    
    async def unsubscribe(self, subscription=None):
        """
        /**
         * Unsubscribe from a subscription.
         *
         * If the `subscription` argument is not set,
         * then the client will unsubscribe from all registered subscriptions.
         *
         * The related sse connection will be autoclosed if after the
         * unsubscribe operations there are no active subscriptions left.
         */
        async unsubscribe(subscription?: string): Promise<void> {
            if (!subscription) {
                // remove all subscriptions
                this.removeSubscriptionListeners();
                this.subscriptions = {};
            } else if (this.subscriptions[subscription]) {
                // remove a single subscription
                this.eventSource?.removeEventListener(subscription, this.subscriptions[subscription]);
                delete this.subscriptions[subscription];
            } else {
                // not subscribed to the specified subscription
                return
            }

            if (this.clientId) {
                await this.submitSubscriptions();
            }

            // no more subscriptions -> close the sse connection
            if (!Object.keys(this.subscriptions).length) {
                this.disconnect();
            }
        }
        """
        if not subscription:
            # remove all subscriptions
            self.remove_subscription_listeners()
            self.subscriptions = {}
        elif self.subscriptions[subscription]:
            # remove a single subscription
            self.eventSource.remove_event_listener(subscription, self.subscriptions[subscription])
            del self.subscriptions[subscription]
        else:
            # not subscribed to the specified subscription
            return
        
        if self.client_id:
            await self.submit_subscriptions()
        
        # no more subscriptions -> close the sse connection
        if not len(self.subscriptions):
            self.disconnect()
    
    async def submit_subscriptions(self):
        """
        private async submitSubscriptions(): Promise<boolean> {
            // optimistic update
            this.addSubscriptionListeners();

            return this.client.send('/api/realtime', {
                'method': 'POST',
                'body': {
                    'clientId': this.clientId,
                    'subscriptions': Object.keys(this.subscriptions),
                },
            }).then(() => true);
        }
        """
        # optimistic update
        self.add_subscription_listeners()
        
        return self.client.send('/api/realtime', {
            'method': 'POST',
            'body': {
                'clientId': self.client_id,
                'subscriptions': list(self.subscriptions.keys()),
            },
        }).then(lambda: True)
    
    def add_subscription_listeners(self):
        """
        private addSubscriptionListeners(): void {
            if (!this.eventSource) {
                return;
            }

            this.removeSubscriptionListeners();
            
            for (let sub in this.subscriptions) {
                this.eventSource.addEventListener(sub, this.subscriptions[sub]);
            }
        }
        """
        if not self.event_source:
            return
        
        self.remove_subscription_listeners()
        
        for sub in self.subscriptions:
            self.event_source.add_event_listener(sub, self.subscriptions[sub])
    
    def remove_subscription_listeners(self):
        """
        private removeSubscriptionListeners(): void {
            if (!this.eventSource) {
                return;
            }

            for (let sub in this.subscriptions) {
                this.eventSource.removeEventListener(sub, this.subscriptions[sub]);
            }
        }
        """
        if not self.event_source:
            return
        
        for sub in self.subscriptions:
            self.event_source.remove_event_listener(sub, self.subscriptions[sub])
            
    def disconnect(self):
        """
        private disconnect(): void {
            this.removeSubscriptionListeners();
            this.eventSource?.removeEventListener('PB_CONNECT', (e) => this.connectHandler(e));
            this.eventSource?.close();
            this.eventSource = null;
            this.clientId = "";
        }
        """
        self.remove_subscription_listeners()
        self.event_source.remove_event_listener('PB_CONNECT', self.connect_handler)
        self.event_source.close()
        self.event_source = None
        self.client_id = ""
        
    def connect(self):
        """
        private connect(): void {
            this.disconnect();
            this.eventSource = new EventSource(this.client.getBaseUrl() + '/api/realtime');
            this.eventSource.addEventListener('PB_CONNECT', (e) => this.connectHandler(e));
        }
        """
        self.disconnect()
        self.event_source = EventSource(self.client.getBaseUrl() + '/api/realtime')
        self.event_source.add_event_listener('PB_CONNECT', self.connect_handler)
        
    def connect_handler(self, e: Event):
        """
        private connectHandler(e: Event): void {
            const msgEvent = (e as MessageEvent);
            this.clientId = msgEvent?.lastEventId;
            this.submitSubscriptions();
        }
        """
        msg_event = e
        self.client_id = msg_event.last_event_id
        self.submit_subscriptions()
        