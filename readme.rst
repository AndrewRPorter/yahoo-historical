================
yahoo-historical
================

Usage
-----

.. code::

    arguments:
        ticker          The ticker symbol to download historical data for
        start           Start day in form [Year,Month,Day]

    optional arguments:
        end             End day in form [Year,Month,Day]

Example output:

.. code::

    >>>data = Fetcher("AAPL", [2007,1,1], [2017,1,1]).getHistorical()
    >>>for row in data:
    >>>    print(row)

    ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
    ['2007-01-03', '12.327143', '12.368571', '11.700000', '83.800003', '10.812462', '309579900']
    ['2007-01-04', '12.007143', '12.278571', '11.974286', '85.659996', '11.052453', '211815100']
    ['2007-01-05', '12.252857', '12.314285', '12.057143', '85.049995', '10.973743', '208685400']
    ['2007-01-08', '12.280000', '12.361428', '12.182858', '85.470001', '11.027935', '199276700']
    ['2007-01-09', '12.350000', '13.282857', '12.164286', '92.570000', '11.944029', '837324600']
    ['2007-01-10', '13.535714', '13.971429', '13.350000', '97.000000', '12.515617', '738220000']
    ['2007-01-11', '13.705714', '13.825714', '13.585714', '95.800003', '12.360788', '360063200']
    ['2007-01-12', '13.512857', '13.580000', '13.318571', '94.620003', '12.208535', '328172600']
    ['2007-01-16', '13.668571', '13.892858', '13.635715', '97.099998', '12.528520', '311019100']
    ['2007-01-17', '13.937143', '13.942857', '13.545714', '94.949997', '12.251113', '411565000']
    ['2007-01-18', '13.157143', '13.158571', '12.721429', '89.070000', '11.492435', '591151400']
    ['2007-01-19', '12.661428', '12.807143', '12.588572', '88.500000', '11.418890', '341118400']
    ['2007-01-22', '12.734285', '12.737143', '12.235714', '86.789993', '11.198254', '363506500']
    ['2007-01-23', '12.247143', '12.501429', '12.215714', '85.699997', '11.057614', '301856100']
    ['2007-01-24', '12.382857', '12.450000', '12.297143', '86.700005', '11.186641', '231953400']
    ...
    ...

Motivation
----------

After struggling to download Yahoo Finance historical data since they closed
the ichart API, I decided to combine a few open source scripts into a
class that can do it all!

License
-------

MIT License

Copyright (c) 2017 Andrew Porter

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
