#!/usr/bin/env python
"""
Run gaze tracking pipeline on all sessions within a data directory

Example
----
>>> gt_batch /Data

Author
----
Mike Tyszka, Caltech Brain Imaging Center

Dates
----
2014-05-07 JMT From scratch

License
----
This file is part of mrgaze.

    mrgaze is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    mrgaze is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with mrgaze.  If not, see <http://www.gnu.org/licenses/>.

Copyright
----
2014 California Institute of Technology.
"""

__version__ = '0.7.2'

import os
import sys
import datetime as dt
from mrgaze import pipeline


def main():

    # Get single session directory from command line
    if len(sys.argv) > 1:
        data_dir = sys.argv[1]
    else:
        data_dir = os.getcwd()

    # Text splash
    print('')
    print('--------------------------------------------------')
    print('mrgaze Batch Gaze Tracking Video Analysis')
    print('--------------------------------------------------')
    print('Version   : %s' % __version__)
    print('Date      : %s' % dt.datetime.now())
    print('Data dir  : %s' % data_dir)

    print('')
    print('Starting batch analysis')

    pipeline.RunBatch(data_dir)

    print('')
    print('Completed batch analysis')

    # Clean exit
    sys.exit(0)


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
