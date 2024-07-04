#!/usr/bin/env python

from subprocess import Popen, run, PIPE


def activate_be(be_name: str, t: bool = False):
    """
    This function activate a BE.
    :param be_name: Name of the BE to activate.
    :param t: If True, the BE will be activated even if it is mounted.
    """
    option = '-t' if t else ''
    cmd_list = ['bectl', 'activate', be_name]
    if option == '-t':
        cmd_list.insert(2, option)
    bectl_process = run(cmd_list)
    assert bectl_process.returncode == 0


def create_be(new_be_name: str, non_active_be: str = None, recursive: bool = False):
    """
    This function create a BE.
    :param new_be_name: Name of the new BE.
    :param non_active_be: Name of the non active BE.
    :param recursive: If True, the BE will be created recursively.
    """
    option = '-r' if recursive else ''
    cmd_list = ['bectl', 'create', new_be_name]
    if non_active_be is not None:
        cmd_list.insert(2, f'-e {non_active_be}')
    if option == '-r':
        cmd_list.insert(2, option)
    bectl_process = run(cmd_list)
    assert bectl_process.returncode == 0


def destroy_be(be_name: str, F: bool = False, o: bool = False):
    """
    This function destroy a BE.
    :param be_name: Name of the BE to destroy.
    :param F: If True, the BE will be destroyed even if it is active.
    :param o: If True, the BE will be destroyed even if it is mounted.
    """
    option = '-'
    option += 'F' if F else ''
    option += 'o' if o else ''
    cmd_list = ['bectl', 'destroy', be_name]
    if option != '-':
        cmd_list.insert(2, option)
    bectl_process = run(cmd_list)
    assert bectl_process.returncode == 0


def rename_be(original_be_name: str, new_be_name: str):
    """
    This function rename a BE.
    :param original_be_name: Name of the BE to rename.
    :param new_be_name: New name of the BE.
    """
    cmd_list = ['bectl', 'rename', original_be_name, new_be_name]
    bectl_process = run(cmd_list)
    assert bectl_process.returncode == 0


def mount_be(be_name: str, path: str = None) -> str:
    """
This function mounts the BE.
:param be_name: Name of the BE to mount.
:param path: The path where the BE will be mounted. If not provided,
a bectl will create a random one.
:return: The path where the BE is mounted.
"""
    cmd_list = ['bectl', 'mount', be_name]
    cmd_list.append(path) if path else None
    bectl_process = run(
        cmd_list,
        universal_newlines=True,
        encoding='utf-8'
    )
    assert bectl_process.returncode == 0
    return bectl_process.stdout.strip()


def umount_be(be_name: str):
    """
    This function unmount the BE.
    :param be_name: Name of the BE to unmount.
    """
    cmd_list = ['bectl', 'umount', be_name]
    bectl_process = run(cmd_list)
    assert bectl_process.returncode == 0


def get_be_list() -> list:
    """
    This function get the list of BEs.
    :return: A list of BEs.
    """
    cmd_list = ['bectl', 'list']
    bectl_output: Popen[str] = Popen(
        cmd_list,
        stdout=PIPE,
        close_fds=True,
        universal_newlines=True,
        encoding='utf-8'
    )
    bectl_list = bectl_output.stdout.read().splitlines()
    bectl_list.pop(0)
    return bectl_list


def is_file_system_zfs() -> bool:
    """
    This function check if the file system is zfs.
    :return: True if the file system is zfs, False otherwise.
    """
    cmd_list = ['df', '-Tt', 'zfs', '/']
    df_output = run(cmd_list)
    return df_output.returncode == 0
