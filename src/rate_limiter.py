"""Rate limiting and abuse protection for OpenClaw Telegram Bot."""

import time
import logging
from collections import defaultdict
from typing import Dict, Optional
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)


class RateLimiter:
    """Token bucket based rate limiter for protecting against abuse."""

    def __init__(self, max_requests: int = 10, time_window: int = 60):
        """Initialize rate limiter.
        
        Args:
            max_requests: Maximum requests allowed per time window
            time_window: Time window in seconds
        """
        self.max_requests = max_requests
        self.time_window = time_window
        self.user_requests: Dict[int, list] = defaultdict(list)
        logger.info(f"RateLimiter initialized: {max_requests} requests per {time_window}s")

    def is_allowed(self, user_id: int) -> bool:
        """Check if user is allowed to make a request.
        
        Args:
            user_id: Telegram user ID
            
        Returns:
            bool: True if request is allowed, False otherwise
        """
        now = time.time()
        cutoff = now - self.time_window
        
        # Clean old requests
        self.user_requests[user_id] = [
            req_time for req_time in self.user_requests[user_id]
            if req_time > cutoff
        ]
        
        # Check limit
        if len(self.user_requests[user_id]) < self.max_requests:
            self.user_requests[user_id].append(now)
            return True
        
        logger.warning(f"Rate limit exceeded for user {user_id}")
        return False

    def get_remaining_time(self, user_id: int) -> Optional[float]:
        """Get remaining time until next request is allowed.
        
        Args:
            user_id: Telegram user ID
            
        Returns:
            float: Seconds until next request is allowed, or None if allowed
        """
        if self.is_allowed(user_id):
            return None
        
        now = time.time()
        cutoff = now - self.time_window
        oldest_request = min(
            (req for req in self.user_requests[user_id] if req > cutoff),
            default=None
        )
        
        if oldest_request:
            return max(0, oldest_request + self.time_window - now)
        return None

    def reset_user(self, user_id: int) -> None:
        """Reset rate limit for a user.
        
        Args:
            user_id: Telegram user ID
        """
        if user_id in self.user_requests:
            del self.user_requests[user_id]
        logger.info(f"Rate limit reset for user {user_id}")


class AbuseDetector:
    """Detect and prevent abusive usage patterns."""

    def __init__(
        self,
        warning_threshold: int = 5,
        block_threshold: int = 10,
        reset_period: int = 3600
    ):
        """Initialize abuse detector.
        
        Args:
            warning_threshold: Number of violations before warning
            block_threshold: Number of violations before blocking
            reset_period: Seconds to reset violation count
        """
        self.warning_threshold = warning_threshold
        self.block_threshold = block_threshold
        self.reset_period = reset_period
        self.violations: Dict[int, tuple] = {}  # user_id -> (count, timestamp)
        logger.info(f"AbuseDetector initialized with thresholds: {warning_threshold}/{block_threshold}")

    def record_violation(self, user_id: int) -> str:
        """Record a violation for a user.
        
        Args:
            user_id: Telegram user ID
            
        Returns:
            str: Status - 'ok', 'warning', or 'blocked'
        """
        now = time.time()
        
        if user_id in self.violations:
            count, timestamp = self.violations[user_id]
            if now - timestamp < self.reset_period:
                count += 1
            else:
                count = 1
        else:
            count = 1
        
        self.violations[user_id] = (count, now)
        
        if count >= self.block_threshold:
            logger.error(f"User {user_id} blocked after {count} violations")
            return 'blocked'
        elif count >= self.warning_threshold:
            logger.warning(f"User {user_id} warned after {count} violations")
            return 'warning'
        
        return 'ok'

    def is_blocked(self, user_id: int) -> bool:
        """Check if user is blocked.
        
        Args:
            user_id: Telegram user ID
            
        Returns:
            bool: True if user is blocked, False otherwise
        """
        if user_id not in self.violations:
            return False
        
        count, timestamp = self.violations[user_id]
        if time.time() - timestamp > self.reset_period:
            # Reset violations after period
            del self.violations[user_id]
            return False
        
        return count >= self.block_threshold

    def clear_violations(self, user_id: int) -> None:
        """Clear violations for a user.
        
        Args:
            user_id: Telegram user ID
        """
        if user_id in self.violations:
            del self.violations[user_id]
        logger.info(f"Violations cleared for user {user_id}")
