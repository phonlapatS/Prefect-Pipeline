from prefect import task , flow

@task
def say_hello():
    print("Hello Prefect!")

@task
def say_prefect():
    print("Welcome to Prefect!")

@flow
def my_flow():
    say_hello()
    say_prefect()

if __name__== "__main__":
    my_flow()