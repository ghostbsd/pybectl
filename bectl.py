#!/usr/bin/env python

from subprocess import Popen, run, PIPE


def activate_be(beName, t=False):
    option = '-t' if t else ''
    cmd_list = ['bectl', 'activate', beName]
    if option == '-t':
        cmd_list.insert(2, option)
    bectl_process = run(cmd_list)
    assert bectl_process.returncode == 0


def create_be(newBeName, nonActiveBe=None, recursive=False):
    option = '-r' if recursive else ''
    cmd_list = ['bectl', 'create', newBeName]
    if nonActiveBe is not None:
        cmd_list.insert(2, f'-e {nonActiveBe}')
    if option == '-r':
        cmd_list.insert(2, option)
    bectl_process = run(cmd_list)
    assert bectl_process.returncode == 0


def destroy_be(beName, F=False, o=False):
    option = '-'
    option += 'F' if F else ''
    option += 'o' if o else ''
    cmd_list = ['bectl', 'destroy', beName]
    if option != '-':
        cmd_list.insert(2, option)
    bectl_process = run(cmd_list)
    assert bectl_process.returncode == 0


def rename_be(origBeName, newBeName):
    cmd_list = ['bectl', 'rename', origBeName, newBeName]
    bectl_process = run(cmd_list)
    assert bectl_process.returncode == 0


def get_be_list():
    cmd_list = ['bectl', 'list']
    bectl_output = Popen(
        cmd_list,
        stdout=PIPE,
        close_fds=True,
        universal_newlines=True,
        encoding='utf-8'
    )
    bectl_list = list(set(bectl_output.stdout.read().splitlines()))
    bectl_list.sort()
    return bectl_list
