# matplotlib_gif_gen
Uses imageio to generate a point-by-point .gif animation of a simple plot generated by matplotlib.

You can install imageio easily using conda or pip - see their page for more info: https://imageio.readthedocs.io/en/latest/installation.html

The Cartesian script has a line and a parabola function built in. It's a work in progress, so the capability to include extra variables in the function calls has not been tested, & plenty of it probably doesn't work very well in its current state. No error handling either (yet). (Gimme a break, it's the weekend!) But the main function of the code - to generate a .gif of plotting with matplotlib - does work.

The Polar script is more basic but still accomplishes the main goal just fine.
