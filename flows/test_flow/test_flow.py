from prefect import flow, task
from prefect import get_run_logger

@task(name="Compile message")
def compile_msg(name: str) -> str:
    return f"Hello!! {name}! You're the best."

@flow(name="Say Hello!")
def log_flow(name: str) -> str:
    msg = compile_msg(name)
    logger = get_run_logger()
    logger.info(msg)
    return msg


if __name__ == "__main__":
    log_flow("Jacob")
