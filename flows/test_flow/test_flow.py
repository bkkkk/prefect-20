from prefect import flow, task, get_run_logger

@task(name="Reverse")
def reverse_string(name: str) -> str:
    return name.replace("!", "?")

@task(name="Compile message")
def compile_msg(name: str) -> str:
    return f"Hello!! {name}! You're the best."

@task(name="Do something else")
def print_msg(msg: str) -> str:
    get_run_logger().info(msg)

@flow(name="Say Hello!")
def log_flow(name: str) -> str:
    msg = compile_msg(name)
    print_msg(msg)
    kill_all_the_things(msg)

@flow(name="!olleH yaS!")
def kill_all_the_things(msg: str) -> str:
    msg = reverse_string(msg)
    print_msg(msg)

if __name__ == "__main__":
    log_flow("Jacob")
