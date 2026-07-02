
# Introduction


# Definition and Description
AMD Precisiion PBO Overdrive (PBO) is AMD'S automatic performance manager.
Think of it as the CPU's brain.

Instead of always running at one speed, it constantly ask:
- Do I have the enough power?
- Am I cool enough?
- Is the motherboard able to supply enough current?

If the answer is yes, the CPU boost itself automatically.

If not it slows down just enough to stay within its limits.

PBO is not a manual overclocking - it's AMD letting the CPU inteligently use whatever headroom is available.

## PPT (Package Power Tracking)
Think of PPT as your monthly budget.
PPT tells the CPU:
- "This is the maximum amount of power you're allowed to spend."

Example:
If PPT is 45 W, the CPU won't try to use more power than about 45 watts for long.

Higher PPT:
- More performance
- More heat
- More electricity

Lower PPT:
- Less heat
- Less power usage
- Slightly lower performance during heavy work


## TDC (Thermal Design Current)
Think of TDC as your normal driving speed.
Imaginge driving a highway.
You are comfortably cruise at 100 km/h all day.
That's what TDC is.

It controls how much current the CPU can contrinuously draw during long workloads like:
- Rendering
- Compiling code
- Stress tests
- Long gaming sessions

Lower TDC means the CPU has to ease off sooner during heavy, sustained work.

## DC (Electrical Design Current)
Think of EDC as overtaking another car.
Normaly you're cruising at 100 km/h.
But when you need to pass someone, you briefly accelerate to 130 km/h.
That's EDC.

It allows the CPU to draw extra current for a short burst so it feels fast when:
- Opening programs
- Loading games
- Switching applications
- Loading webpages
After the burst, it goes back to normal.


## PBO Scalar
Think of Scalar as how willing the CPU is to take risks.
Normally, AMD has built-in safety rules for voltage and boosting.

The Scalar tells the CPU:
- "It's okay to keep boosting even if it means using higher voltage."

### Simple analogy
Imagine you're running a marathon.

Scalar= 1X
- You run at a comfortable pace.
- You save energy.
- You can keep going for a long time.

Scalar= 10X
- You sprint more often.
- You're faster.
- You get tired much sooner.

The CPU behaves the same way.
Higher Scalar:
- Higher voltage
- More heat
- More power consumption
- Sometimes slightly better performance

Lower Scalar (1X or Auto):
- Lower voltage
- Cooler temperatures
- Better efficiency
- Longer CPU lifespan(in theory, due to spending less time at high voltage)


## Max CPU Boost Block Override
This setting tells the CPU:
- "You're allowed to boost a little higher than AMD's normal limit."
Example:
If your Ryzen normally boosts up to 4.6 GHz:
- 0 Mhz-> Maximum boost stays around 4.6 Ghz
- +100 Mhz-> CPU may boost up to 4.8 GHz (If supported by the CPU, motherboard, cooling, and power limits)

### Important 
Boost override does not force the CPU to run faster all the time.
It only raises the ceilling.
The CPU will still check:
- Temperature
- PPT
- TDC
- EDC
- Voltage
- Workload

before deciding whether it can actually reach the higher frequency
Think of it like increasing a car's speed limiter from 180 km/h to 200 km/h.

### Reminder
Just because the limiter is higher doesn't mean you'll always drive at 200 km/h- you'll only reach if it the road and condition allow.


## How They Work Together
Image you're driving.

PPT= Your fuel budget.
TDC= Your comfortable cruising speed.
EDC= The quick burst of speed you use when overtaking
Scalar= How aggressive should i be?
Boost Override= How high am I allowed to boost?
The CPU is constantly balancing these three to give you the best mix of performance temperatur, and efficiency.






# My 24/7 Configurations (Ryzen 7 5700G)
## PBO
- PBO: Advanced / Manual
- Scalar: Autho (or 1x)
- Boost Override: 0 Mhz

## limits
PPT: 40 W
TDC: 35 A
EDC: 40 A


# Why I chose these Settings
My goal isn't to get the highest benchmark score.
My goal is to have a computer that:
- Runs 24/7
- stays cool
- Uses less electricity
- Is quiet
- Still feels fast every day

With these settings, the CPU can still boost high during normal task, but it avoids wasting power during long, heavy workloads.

# Simnple Rule
- PPT= Power Limit
- TDC= Long-term current limit
- EDC= Short burst current limit


# Experimental Configurations
## config 1
PPT: 45 W
TDC: 35 A
EDC: 45 A

## config 2
PPT: 40 W
TDC: 35 A
EDC: 40 A

## config 3
PPT: 35 W
TDC: 25 A
EDC: 35 A