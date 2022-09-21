"""
pocketbase/types/hourly_stats.py

type HourlyStats = {
    total: number;
    date: string;
};
"""

class HourlyStats:
    def __init__(self, total: int, date: str):
        self.total = total
        self.date = date