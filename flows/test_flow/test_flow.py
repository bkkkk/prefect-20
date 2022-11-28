from prefect import flow, task
from prefect import get_run_logger

@flow(name="Say Hello!")
def log_flow(name: str):
    logger = get_run_logger()
    logger.info(f"Hello!! {name}! You're the best.")


if __name__ == "__main__":
    log_flow("Jacob")
