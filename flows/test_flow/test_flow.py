from prefect import flow, task
from prefect import get_run_logger

@task(name="Reverse")
def reverse_string(name: str) -> str:
    return name.replace("a", "p")

@task(name="Compile message")
def compile_msg(name: str) -> str:
    return f"Hello!! {name}! You're the best."

@flow(name="Say Hello!")
def log_flow(name: str) -> str:
    msg = compile_msg(name)
    logger = get_run_logger()
    logger.info(msg)
    kill_all_the_things(msg)

@flow(name="!olleH yaS!")
def kill_all_the_things(msg: str) -> str:
    msg = reverse_string(msg)
    get_run_logger().info(msg)

if __name__ == "__main__":
    log_flow("Jacob")
