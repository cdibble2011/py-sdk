"""
pocketbase/services/logs.py

declare class Logs extends BaseService {
    /**
     * Returns paginated logged requests list.
     */
    getRequestsList(page?: number, perPage?: number, queryParams?: {}): Promise<ListResult<LogRequest>>;
    /**
     * Returns a single logged request by its id.
     */
    getRequest(id: string, queryParams?: {}): Promise<LogRequest>;
    /**
     * Returns request logs statistics.
     */
    getRequestsStats(queryParams?: {}): Promise<Array<HourlyStats>>;
}
"""

from typing import Optional, Dict, Any, List

from ..abstracts import BaseService
from ..models import LogRequest, ListResult
from ..types import HourlyStats

class Logs(BaseService):
    def get_requests_list(self, page: Optional[int] = None, per_page: Optional[int] = None, query_params: Optional[Dict[str, Any]] = None) -> ListResult[LogRequest]:
        """
        Returns paginated logged requests list.
        """
        return self._list('requests', LogRequest, page, per_page, query_params)

    def get_request(self, id: str, query_params: Optional[Dict[str, Any]] = None) -> LogRequest:
        """
        Returns a single logged request by its id.
        """
        return self._get('requests', id, LogRequest, query_params)

    def get_requests_stats(self, query_params: Optional[Dict[str, Any]] = None) -> List[HourlyStats]:
        """
        Returns request logs statistics.
        """
        return self._get('requests/stats', None, HourlyStats, query_params)