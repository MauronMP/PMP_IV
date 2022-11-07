from invoke import task, run

@task
def install(c):
    run("poetry install")

@task
def test(c):
    run("poetry run pytest")

@task
def jupyter(c):
    run("poetry run jupyter notebook")