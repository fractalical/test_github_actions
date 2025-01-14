from prometheus_client import Counter, Gauge, REGISTRY

# Метрики для мониторинга
http_requests_total = Counter(
    'http_requests_total',
    'Total number of HTTP requests',
    ['method', 'endpoint', 'status']
)

# Создаем глобальную переменную для хранения статуса
_HEALTH_STATUS = 0

health_status = Gauge(
    'health_status',
    'Health status of the application (1 = healthy, 0 = unhealthy)'
)

def set_health_status(value: int):
    """Устанавливает статус здоровья приложения"""
    global _HEALTH_STATUS
    _HEALTH_STATUS = value
    health_status.set(value)

def get_health_status() -> int:
    """Возвращает текущий статус здоровья"""
    return _HEALTH_STATUS 

health_check_total = Counter(
    'health_check_total',
    'Total number of successful health checks'
) 