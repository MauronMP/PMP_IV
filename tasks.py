from invoke import task, run

@task
def install(c):
    run("poetry install")

@task
def test(c):
    run("poetry run pytest --tap-stream")

@task
def jupyter(c):
    run("poetry run jupyter notebook")

@task
def check(c):
    run("poetry check")