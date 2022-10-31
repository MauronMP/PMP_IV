from invoke import task, run

@task
def install(c):
    run("poetry install")

@task
def check(c):
    run("poetry check")