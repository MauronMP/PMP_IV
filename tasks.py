from invoke import task, run
import os

@task
def install(c):
    run("poetry install")

@task
def test(c):
    run("poetry run pytest -v")

@task
def check(c):
    cmd = "python3 -m compileall pmp_iv"
    result = run(cmd, hide=True, warn=True)
    print(result.ok)
