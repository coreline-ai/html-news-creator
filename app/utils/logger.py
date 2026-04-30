import structlog

structlog.configure(
    processors=[
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.stdlib.add_log_level,
        structlog.processors.JSONRenderer(),
    ],
    wrapper_class=structlog.BoundLogger,
    context_class=dict,
    logger_factory=structlog.PrintLoggerFactory(),
)


def get_logger(step: str = "", job_id: str = "") -> structlog.BoundLogger:
    log = structlog.get_logger()
    if step:
        log = log.bind(step=step)
    if job_id:
        log = log.bind(job_id=job_id)
    return log
