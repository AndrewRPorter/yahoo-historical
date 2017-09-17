================
yahoo-historical
================

Installation
------------

.. code::

    python -m pip install yahoo-historical

Usage
-----

.. code::

    arguments:
        ticker          The ticker symbol to download historical data for
        start           Start day in form [Year,Month,Day]

    optional arguments:
        end             End day in form [Year,Month,Day]
        interval        Interval to fetch historical data (can be 1d, 1wk, 1mo, defaults to 1d)

Usage Examples:

.. code::

    >>>from yahoo_historical import Fetcher
    >>>data = Fetcher("AAPL", [2007,1,1], [2017,1,1])
    >>>print(data.getHistorical())

                Date        Open        High         Low       Close   Adj Close      Volume
    0     2007-01-03   12.327143   12.368571   11.700000   10.812462   11.971429   309579900
    1     2007-01-04   12.007143   12.278571   11.974286   11.052453   12.237143   211815100
    2     2007-01-05   12.252857   12.314285   12.057143   10.973743   12.150000   208685400
    3     2007-01-08   12.280000   12.361428   12.182858   11.027935   12.210000   199276700
    4     2007-01-09   12.350000   13.282857   12.164286   11.944029   13.224286   837324600
    5     2007-01-10   13.535714   13.971429   13.350000   12.515617   13.857142   738220000
    6     2007-01-11   13.705714   13.825714   13.585714   12.360788   13.685715   360063200
    7     2007-01-12   13.512857   13.580000   13.318571   12.208535   13.517143   328172600
    8     2007-01-16   13.668571   13.892858   13.635715   12.528520   13.871428   311019100
    9     2007-01-17   13.937143   13.942857   13.545714   12.251113   13.564285   411565000
    10    2007-01-18   13.157143   13.158571   12.721429   11.492435   12.724286   591151400

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
