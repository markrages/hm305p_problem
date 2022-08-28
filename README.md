# HM305P transient problem

I noticed a problem with my Hanmatek HM305p power supply.

This is a cheap USB-controlled switchmode desktop supply.

!(eTM-305p.jpg)

According to [EEVBlog Forums](https://www.eevblog.com/forum/testgear/power-supply-ripe-for-the-picking/) it is a rebadged eTOMMENS eTM-305.

## Problem description

When the voltage is changed, and a load is applied during the change,
there is a severe output voltage undershoot.

## Test setup

!(test_setup.jpg)

This is a transient problem, so I am using an oscilloscope.

To apply the load, I am applying a 5 ohm resistor using a LabJack U3 and
relay board.

This is scripted by [test_hm305p.py](test_hm305p.py)

## Results

### Figure 1

!(figure1.png)

The first test is applying the 5 V load at a constant 10 V output.

This is a basic __Load Regulation__ test.

This shows a dip of about 1 V for 10 ms or so.

### Figure 2

!(figure2.png)

The second test is changing the output voltage from 10 V to 8 V.  This
shows the __Step Response__ of the unloaded power supply.

This shows a slow ramp down, but mostly settled after 400 ms.

### Figure 3

!(figure3.png)

This test is the same as the previous one, but with the 5 ohm load
applied for the duration.  It doesn't perceptibly change the step
response.

### Figure 4

!(figure4.png)

This test shows the problem. It is a combined step response and load
test.  Apparently the load regulation is severely degraded during the
transition to a new output voltage. The voltage dips by about 5 V for
a dozen ms or so.  This can cause a brownout reset to some loads.

## Mitigation

This seems to be related to the transition from no-load to heavy load. One thing that seems to help is adding a constant load.

Here is Figure 4 taken with a constant 50 ohm load across the supply:

!(figure4_const_load.png)

Now the transient response is restored to similar to Figure 1.

## Other supplies in the series.

This supply is available in other output voltages and current ratings.

Here is Figure 4 taken from the Rockseed RS605P, which is the 60V
version of the same eTommens supply:

!(figure4_rs610.png)

It does not exhibit the same behavior. Although the switch noise on
the loaded output is fairly atrocious!
