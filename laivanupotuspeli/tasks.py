import os
from invoke import task

def use_pty():
    if os.name == "nt":
        return False
    else:
        return True

@task
def start(ctx):
    ctx.run("python src/index.py", pty=use_pty())

@task
def test(ctx):
    ctx.run("pytest src", pty=use_pty())

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src", pty=use_pty())

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=use_pty())

@task
def lint(ctx):
    ctx.run("pylint src", pty=use_pty())