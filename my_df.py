
from spawn import spawn
import regex
import sys


if __name__ == '__main__':
    def main():
        """ print the 'df' command the way I like it """
        if sys.platform == 'darwin':
            ln = 'gdf --total -BG -t apfs -t ntfs -t msdos -l --output=size,used,avail,pcent,fstype,target'
        else:
            ln = 'df --total -BG -t ext4 -t xfs -t ntfs -t msdos -l --output=size,used,avail,pcent,fstype,target'

        titles = ['Blocks', 'Used', 'Avail', 'Use%', 'Type', 'Mounted']
        for title in titles:
            print(title.ljust(10), end='')
        print()
        print('-'*60)
        # print('123456789|'*7)

        for index, line in enumerate(spawn(ln)):
            if index == 0:
               continue
            split = regex.split(r' *', line.lstrip())
            for item in split:
                print('{}'.format(item.rstrip().ljust(10)), end='')
            print()

    main()
