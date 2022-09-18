"""
Logs Service

Source: https://github.com/pocketbase/js-sdk/blob/master/src/services/Logs.ts

import LogRequest  from '@/models/LogRequest';
import ListResult  from '@/models/utils/ListResult';
import BaseService from '@/services/utils/BaseService';




"""
from pocketbase.api.services.utils import BaseService
from pocketbase.models import LogRequest, ListResult

class HourlyStats:
    """
    export type HourlyStats = {
        total: number,
        date:  string,
    }
    """
    def __init__(self, total: int, date: str):
        self.total = total
        self.date = date
        
class Logs(BaseService):
    """
    export default class Logs extends BaseService {}
    """
    def __init__(self, client):
        super(Logs, self).__init__(client)

    def get_requests_list(self, page: int = 1, per_page: int = 30, query_params: dict = {}):
        """
        /**
         * Returns paginated logged requests list.
         */
        getRequestsList(page = 1, perPage = 30, queryParams = {}): Promise<ListResult<LogRequest>> {
            queryParams = Object.assign({
                'page':    page,
                'perPage': perPage,
            }, queryParams);
        
            return this.client.send('/api/logs/requests', {
                'method': 'GET',
                'params': queryParams,
            }).then((responseData: any) => {
                const items: Array<LogRequest> = [];
                if (responseData?.items) {
                    responseData.items = responseData?.items || [];
                    for (const item of responseData.items) {
                        items.push(new LogRequest(item));
                    }
                }
        
                return new ListResult<LogRequest>(
                    responseData?.page || 1,
                    responseData?.perPage || 0,
                    responseData?.totalItems || 0,
                    responseData?.totalPages || 0,
                    items,
                );
            });
        }
        """
        query_params = dict(query_params)
        query_params.update({
            'page': page,
            'perPage': per_page,
        })

        return self.client.send('/api/logs/requests', {
            'method': 'GET',
            'params': query_params,
        }).then(lambda response_data: ListResult(
            response_data.get('page', 1),
            response_data.get('perPage', 0),
            response_data.get('totalItems', 0),
            response_data.get('totalPages', 0),
            [LogRequest(item) for item in response_data.get('items', [])],
        ))

    def get_request(self, id, query_params: dict = {}):
        """
        /**
         * Returns a single logged request by its id.
         */
        getRequest(id: string, queryParams = {}): Promise<LogRequest> {
            return this.client.send('/api/logs/requests/' + encodeURIComponent(id), {
                'method': 'GET',
                'params': queryParams
            }).then((responseData: any) => new LogRequest(responseData));
        }
        """
        return self.client.send('/api/logs/requests/' + id, {
            'method': 'GET',
            'params': query_params,
        }).then(lambda response_data: LogRequest(response_data))
    
    def get_requests_stats(self, query_params: dict = {}):
        """
        /**
         * Returns request logs statistics.
         */
        getRequestsStats(queryParams = {}): Promise<Array<HourlyStats>> {
            return this.client.send('/api/logs/requests/stats', {
                'method': 'GET',
                'params': queryParams
            }).then((responseData: any) => responseData);
        }
        """
        return self.client.send('/api/logs/requests/stats', {
            'method': 'GET',
            'params': query_params,
        }).then(lambda response_data: response_data)