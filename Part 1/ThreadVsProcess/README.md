# ThreadVsProcess
- Run the [Test Code] under the stack overflow
- Install [gnuplot] 
```
  brew install gnuplot
```
- Using gnuplot to plot. The screenshot of the source code as the below

<p align="middle">
  <img src= "https://github.com/BUEC500C1/video-Jie1995tbc/blob/master/Part%201/ThreadVsProcess/gnuplot_code1.png" width= 500>
</p>


<p align="middle">
  <img src= "https://github.com/BUEC500C1/video-Jie1995tbc/blob/master/Part%201/ThreadVsProcess/gnuplot_code2.png" width= 500>
</p>

- The result plot from gnuplot

<p align="middle">
  <img src= "https://github.com/BUEC500C1/video-Jie1995tbc/blob/master/Part%201/ThreadVsProcess/ThreadVsProcess.png" width= 500>
</p>

## Conclusion
- For CPU bound work, multiprocessing is always faster, presumably due to the GIL
- For IO bound work. both are exactly the same speed
- Threads only scale up to about 4x instead of the expected 8x since I'm on an 8 hyperthread machine.


[Test Code]: https://stackoverflow.com/questions/3044580/multiprocessing-vs-threading-python
[gnuplot]: http://www.gnuplot.info/download.html

