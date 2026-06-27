# BirdBrain Finch Activities — Grades 6–8 Analysis
## Learning Progression from Beginner to Expert

Source: [CSTA Standards for Finch](https://learn.birdbraintechnologies.com/standards/finch/csta/#grades-6-8)

---

## How This Analysis Was Built

Each activity listed under CSTA Grades 6–8 (and relevant activities from adjacent grade bands) was mapped by which standard it satisfies. The standard tells us what CS concepts the activity requires. Activities were then sorted into five progression levels based on prerequisite skills: what a student must already know before attempting the activity.

---

## Level 1: Beginner — Sequences, Basic Movement, Data Collection

Students need: ability to connect the Finch, write sequential commands, basic understanding of inputs/outputs.

| Activity | Required Skills | CSTA Standards | Link |
|---|---|---|---|
| **Finding Speed with Finch** | Sequences, movement commands, timing, measuring distance, recording data | 2-DA-08, 1B-DA-06, 1B-DA-07 | [Link](https://learn.birdbraintechnologies.com/finch/projects/finch-findspeed) |
| **Analyzing Finch Data I** | Sequences, data collection from sensors, organizing data in tables/charts | 2-DA-08, 1B-DA-06, 1B-DA-07 | [Link](https://learn.birdbraintechnologies.com/finch/projects/analyzing-data-1) |

**What students learn at this level:** How to write a sequence of commands that execute in order. How to collect and organize data from robot behavior. How to make claims based on observed data.

**Extension pathway:** Both activities can be extended by having students predict outcomes before testing, then compare predictions to results — building toward experimental design thinking.

---

## Level 2: Intermediate — Variables and Loops

Students need: Level 1 skills plus understanding of repeat loops and what a variable stores.

| Activity | Required Skills | CSTA Standards | Link |
|---|---|---|---|
| **Drawing Shapes** | Variables (side length, angle), repeat loops, geometry (interior angles), movement precision | 2-AP-11, 1B-AP-09 | [Link](https://learn.birdbraintechnologies.com/finch/projects/finch-drawingshapes) |
| **Finch Spirals** | Variables (changing value each loop iteration), repeat loops, math patterns (growing/shrinking), movement | 2-AP-11, 1B-AP-09 | [Link](https://learn.birdbraintechnologies.com/finch/projects/finch-spirals-2) |
| **Analyzing Finch Data II** | Variables, data collection, loops for repeated measurements, data transformation and analysis | 2-DA-08, 1B-DA-06, 1B-DA-07 | [Link](https://learn.birdbraintechnologies.com/finch/projects/analyzing-data-2) |

**What students learn at this level:** That variables store values which can change during program execution. That loops reduce repetitive code and enable patterns. That changing a variable inside a loop produces growing or shrinking effects.

**Extension pathway:** Drawing Shapes extends naturally to calculating interior angles for any polygon using a formula (360 ÷ number of sides). Finch Spirals extends to Fibonacci or logarithmic spirals using more complex variable math.

---

## Level 3: Intermediate-Advanced — Conditionals and Sensors

Students need: Level 2 skills plus understanding of if/else logic and how to read sensor values.

| Activity | Required Skills | CSTA Standards | Link |
|---|---|---|---|
| **ShyBot** | Conditionals (if/else), distance sensor, forever loops, threshold values — robot reacts to proximity | 2-AP-12 | [Link](https://learn.birdbraintechnologies.com/finch/projects/shybot-2) |
| **CricketBot** | Conditionals (if/else), light sensor, forever loops — robot behaves differently in light vs. dark | 2-AP-12 | [Link](https://learn.birdbraintechnologies.com/finch/projects/cricketbot-2) |
| **Emotional Finch** | Variables (storing emotional state), conditionals (sensor-triggered state changes), LEDs as output | 2-AP-11, 1B-AP-09 | [Link](https://learn.birdbraintechnologies.com/finch/projects/finch-emotions) |
| **Reaction Time** | Variables (timing, storing results), conditionals (button detection), data collection, loops | 2-DA-08 | [Link](https://learn.birdbraintechnologies.com/finch/projects/reaction-time) |
| **Simon Says I** | Conditionals (checking button input), loops, sequences, micro:bit buttons as input, LED/sound feedback | 2-AP-12 | [Link](https://learn.birdbraintechnologies.com/finch/projects/simon-says-i-2) |
| **SquirrelBot** | Variables (acorn count, state), conditionals (sensor-based decisions), randomness, loops | 2-AP-11, 1B-AP-09 | [Link](https://learn.birdbraintechnologies.com/finch/projects/squirrelbot-2) |

**What students learn at this level:** That programs can make decisions based on sensor input. That the same robot can exhibit different behaviors depending on its environment. That combining loops with conditionals creates autonomous, responsive behavior.

**Extension pathway:** ShyBot can be extended to have multiple proximity zones (close → run away, medium → cautious, far → approach). CricketBot can respond to light intensity gradients, not just light/dark binary. SquirrelBot can be extended with multiple foraging strategies.

---

## Level 4: Advanced — Compound Conditionals, Nested Loops, Multi-Sensor Integration

Students need: Level 3 skills plus ability to combine multiple conditions (AND/OR), nest control structures, and integrate multiple sensors.

| Activity | Required Skills | CSTA Standards | Link |
|---|---|---|---|
| **Animal Adaptations** | Compound conditionals (multiple sensor conditions combined), nested loops, multiple sensors (light, distance, line), designing behavior to simulate real animal responses | 2-AP-12 | [Link](https://learn.birdbraintechnologies.com/finch/projects/animal-adaptations-2) |
| **Special Delivery** | Compound conditionals, multi-step navigation, line sensors + distance sensor together, sequencing complex behaviors, decomposition of delivery route | 2-AP-12 | [Link](https://learn.birdbraintechnologies.com/finch/projects/finch-specialdelivery) |
| **Finch Hot Potato** | Variables (timer, score), conditionals (sensor-triggered events), randomness, timing logic, accelerometer input | 2-AP-11, 1B-AP-09 | [Link](https://learn.birdbraintechnologies.com/finch/projects/finch-hotpotato) |
| **Simon Says II** | Variables (lists/arrays for storing sequences), conditionals (comparing user input to stored sequence), loops (iterating through sequences), increasing difficulty logic | 2-AP-11, 1B-AP-09 | [Link](https://learn.birdbraintechnologies.com/finch/projects/simon-says-ii-2) |
| **Amazing Mazes** | Conditionals (distance-based decisions), loops, pre-programmed vs. sensor-based navigation, decomposition, iterative testing and refinement | 2-DA-08, 2-AP-10 | [Link](https://learn.birdbraintechnologies.com/finch/projects/finch-maze) |

**What students learn at this level:** How to combine multiple conditions into compound logic (if distance < 20 AND light > 50). How to nest loops inside conditionals and vice versa. How to decompose a complex problem into smaller manageable parts. How to use multiple sensors together to create rich, responsive behaviors.

**Extension pathway:** Animal Adaptations can be extended by researching a real animal and programming the Finch to mimic its behavior accurately. Amazing Mazes extends naturally into wall-following algorithms (see Level 5). Special Delivery extends into route optimization.

---

## Level 5: Expert — Functions/Procedures with Parameters, Algorithm Design, Complex Decomposition

Students need: Level 4 skills plus ability to create reusable code blocks with inputs, design algorithms for autonomous behavior, and decompose complex problems systematically.

| Activity | Required Skills | CSTA Standards | Link |
|---|---|---|---|
| **Light Show** | Procedures/functions with parameters (color values, timing, patterns), modularity, code reuse, designing parameterized light sequences | 2-AP-14 | [Link](https://learn.birdbraintechnologies.com/finch/projects/light-show) |
| **Turning with Encoders** | Functions with parameters (turn angle, speed), encoder reading, precision movement, calibration, mathematical relationship between encoder ticks and degrees | 2-AP-14 | [Link](https://learn.birdbraintechnologies.com/finch/projects/turning-with-encoders-i) |
| **Follow the Wall** | Wall-following algorithm, continuous sensor reading in a loop, conditionals for wall detection and correction, decomposition of algorithm into sub-behaviors, functions for reusable navigation routines | 1B-AP-12 (used at 6-8 level) | [Link](https://learn.birdbraintechnologies.com/finch/projects/follow-the-wall) |

**What students learn at this level:** How to create procedures that accept parameters, making code flexible and reusable. How to design and implement algorithms that solve complex navigation problems. How to use encoders for precision movement and calibration. How to decompose a complex autonomous behavior into modular, testable components.

**Extension pathway:** Light Show extends into choreographed multi-robot performances. Turning with Encoders extends into precise path planning and odometry. Follow the Wall extends into full maze-solving with dead-end detection and backtracking.

---

## Visual Learning Progression

```
Level 1 (Beginner)         Level 2 (Intermediate)      Level 3 (Int-Advanced)
─────────────────          ────────────────────         ──────────────────────
Finding Speed              Drawing Shapes               ShyBot
Analyzing Data I           Finch Spirals                CricketBot
                           Analyzing Data II            Emotional Finch
                                                        Reaction Time
                                                        Simon Says I
                                                        SquirrelBot

       ↓                          ↓                           ↓

Level 4 (Advanced)                          Level 5 (Expert)
──────────────────                          ────────────────
Animal Adaptations                          Light Show
Special Delivery                            Turning with Encoders
Finch Hot Potato                            Follow the Wall
Simon Says II
Amazing Mazes
```

---

## Skills Prerequisite Chain

```
Sequences → Loops → Variables → Conditionals → Compound Conditionals → Functions w/ Parameters
    ↓          ↓        ↓            ↓                  ↓                       ↓
 Finding    Drawing   Finch       ShyBot            Animal              Light Show
 Speed      Shapes    Spirals     CricketBot        Adaptations         Turning w/ Encoders
 Data I     Data II   Emotional   Simon Says I      Special Delivery    Follow the Wall
                      Finch       Reaction Time     Amazing Mazes
                      SquirrelBot                   Hot Potato
                                                    Simon Says II
```

---

## Mapping to Your Curriculum

| Your Curriculum Phase | BirdBrain Activities That Fit | When to Use |
|---|---|---|
| 7th Phase A (Foundations) | Finding Speed, Analyzing Data I | Periods 3–6 for sensor + variable practice |
| 7th Phase B (Loops + Conditionals) | Drawing Shapes, Finch Spirals, ShyBot, CricketBot | Periods 11–15 as supplemental challenges |
| 7th Phase B (Line Following) | Special Delivery | Periods 18–20 as extension after line following |
| 7th Phase C (Capstone) | Emotional Finch, SquirrelBot, Animal Adaptations | Period 24 as project menu options |
| 8th Phase B (Functions) | Light Show, Turning with Encoders | Periods 11–13 as function practice |
| 8th Phase B (Maze) | Amazing Mazes, Follow the Wall | Periods 21–22 as direct prep for maze competition |
| 8th Phase C (Capstone) | Simon Says II, Reaction Time | Period 24 as advanced project menu options |

---

## Notes

- All block-based activities can be completed in Snap!, BirdBlox, or MakeCode. For your curriculum, use Snap! for 7th grade and Python equivalents for 8th grade.
- BirdBrain also offers Python-specific lessons (separate from these block-based activities) at [learn.birdbraintechnologies.com/finch/python/program/](https://learn.birdbraintechnologies.com/finch/python/program/) which cover the same concepts in text code. These are ideal for your 8th grade Python transition.
- The CSTA standards page notes that "the list of suggested activities is not exhaustive" — any intermediate or advanced Finch activity can meet standards 2-AP-10, 2-AP-13, 2-AP-17, 2-AP-18, and 2-AP-19.
