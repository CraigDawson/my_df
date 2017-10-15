# -*- coding: utf-8 -*-

import subprocess
import sys


def spawn(cmd):
    """ Function to spawn command to OS and yields output lines """
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)

    line = process.stdout.readline().decode('utf-8')
    while line != '' or process.poll() is None:
        yield line
        line = process.stdout.readline().decode('utf-8')


if __name__ == '__main__':
    def main():
        """ Test case and example for spawn() """
        for line in spawn('df --total -BG -t ext4 -t xfs -t ntfs -t msdos -l --output=size,used,avail,pcent,fstype,target'):
            sys.stdout.write(line)
            sys.stdout.flush()

    main()
