from invoke import task, run

@task
def install(c):
    run("poetry install")

@task
def test(c):
    run("poetry run pytest")

@task
def check(c):
    run("poetry check")

    