# Computer Science Curriculum — Grades 7 & 8
## Coding Foundations Through Robotics — Finch Robot 2.0 with micro:bit

---

## Two-Year Design Philosophy

**7th grade builds fluency.** Students work entirely in Snap! (block coding). Every concept gets 2–3 periods with tiered challenges. Competitions are direct applications of single concepts. Students finish the year confident with sequences, variables, loops, conditionals, sensors, line following, and basic functions.

**8th grade builds mastery.** Students transition to Python over 8+ periods, revisiting every concept in text code. Then they go deeper — advanced functions with parameters, Boolean logic, decomposition, state machines, and algorithm design. Competitions are complex and integrative. The capstone is longer and more ambitious.

| | 7th Grade | 8th Grade |
|---|---|---|
| Language | Snap! (blocks) | Snap! review → Python (text) |
| Periods | 31 × 40 min | 31 × 40 min |
| Students | Pairs, rotating every phase | Pairs, rotating every phase |
| Competitions | Obstacle course, Sumo, Line following | Obstacle course (Python), Sumo (Python), Maze, Magnet collection v2 |
| Assessment | Checkpoints, engineering logs, showcase | Checkpoints, peer code reviews, showcase |

### Concept Progression Across Two Years

| Concept | 7th Grade | 8th Grade |
|---|---|---|
| Sequences | Introduced and practiced | Assumed fluency |
| Variables | Introduced period 3, used throughout | Revisited in Python, used in state machines |
| Loops | repeat, forever — periods 11–13 | for, while in Python — nested, variable-controlled |
| Conditionals | if/else, basic nested — periods 14–15 | if/elif/else, compound with Boolean operators |
| Sensors | Distance, light, IR (line) | Same sensors, multi-sensor with Boolean logic |
| Functions | Intro only — create and use simple custom blocks | Deep — parameters, return values, libraries, composition |
| Debugging | read-predict-compare framework introduced | Extended to print() tracing, syntax vs. logic errors |
| Decomposition | Not explicit | Pseudocode-first, flowcharts, function decomposition |
| Boolean logic | Not covered | AND, OR, NOT — compound sensor conditions |
| State machines | Not covered | Two-mode and three-mode robots |
| Algorithm design | Not covered | Wall-following, search patterns, optimization |

### Competition Difficulty Ramp Across Two Years

```
7th: Obstacle course ●○○○○ → Sumo ●●○○○ → Line following ●●●○○
8th: Obstacle (Python) ●●○○○ → Sumo (Python) ●●●○○ → Maze ●●●●○ → Magnet collection ●●●●●
```

---

# 7TH GRADE — 31 PERIODS
## Snap! Block Coding | Building Fluency | 3 Competitions

---

## Phase A: Foundations (Periods 1–10)

Students already know block coding from Hummingbird. This phase transitions them to the Finch platform, introduces variables and sensors with proper pacing, and ends with the first competition.

---

### Period 1 — Meet the Finch
**Connect in Snap!, pair norms, first programs**

- Bronze: Move forward, set tail LEDs green, play one tone, return to start
- Silver: Sequence of 8+ commands with timed color and sound changes
- Gold: "Personality intro" — Finch performs a choreographed self-introduction

> Frame as platform transition: "You know blocks from Hummingbird. Snap! works the same way — here's what's different about the Finch." Establish pair programming norms: driver/navigator, swap every 12 minutes.

---

### Period 2 — Precision movement
**Navigate a taped L-course, draw a square with the marker holder**

- Bronze: Navigate the L-course and stop in the target zone
- Silver: Draw a triangle (calculate the turn angle)
- Gold: Draw a pentagon or star — plan angles on paper first

> Math connection: degrees of rotation, interior angles. This is where the marker holder earns its keep — drawing makes movement precision visible.

---

### Period 3 — Variables intro
**Store speed in a variable, change with button press, display on micro:bit**

- Bronze: Variable-controlled speed — Finch drives at the stored value
- Silver: Button A speeds up, button B slows down, micro:bit display updates live
- Gold: Add a second variable for LED color mode — buttons cycle through speeds and colors

> Early variables. Students use them for the remaining 28 periods. Even experienced block coders may not have used variables with physical outputs — seeing speed change on a real robot makes the concept concrete.

---

### Period 4 — Variables in action
**Variable-controlled shapes, connecting variables to movement math**

- Bronze: Draw shapes at variable speed (fast vs. slow changes the shape)
- Silver: Variable-sized shapes — change a "side length" variable between drawings
- Gold: User-controlled drawing — buttons adjust turn angle variable in real time

> Second period on variables. The focus shifts from "what is a variable" to "how do I use one to control something interesting." Students who rushed through period 3 now apply variables in a creative context.

---

### Period 5 — Distance sensor
**Detect obstacles, stop before the wall, LED color shifts with proximity**

- Bronze: Stop when obstacle is within 20 cm
- Silver: Variable threshold — store detection distance in a variable, adjust with buttons
- Gold: Proximity gradient — LED shifts green → yellow → red as distance decreases

> First sensor. The connection between sensor input and robot output is the foundation of everything that follows.

---

### Period 6 — Light sensor + sensor combos
**Multi-sensor responses, "mood robot" challenge**

- Bronze: Finch responds differently to bright vs. dark areas
- Silver: Combine light + distance — unique behavior for each combination
- Gold: 3+ distinct sensor-driven behaviors, documented with a planning table

> Students make a planning table (if light is high AND distance is far, then...) before coding. This is informal Boolean logic prep for 8th grade.

---

### Period 7 — Debugging workshop
**Three intentionally broken programs, teach the read-predict-compare method**

- Bronze: Find and fix the bug in each program
- Silver: Explain in writing why each bug caused the observed wrong behavior
- Gold: Write a deliberately broken program for another pair to debug

> Teach the framework explicitly: (1) read each block, (2) predict what it does, (3) run and observe, (4) find where prediction and behavior diverge. Post the method on the wall. Students reference it all year.

---

### Period 8 — Obstacle course practice
**Timed runs on a multi-section arena course, combining all Phase A skills**

- All pairs practice on the arena courses (same course on both arenas)
- Focus on refining code, testing, and improving times
- No formal scoring — this is practice and strategy development

---

### Period 9 — Obstacle course competition ⚡
**Best of two timed attempts, both arenas running identical courses**

Difficulty: ●○○○○

> Low CS ceiling but high energy. The course is pre-programmed (no real-time sensor decisions), so the playing field is level. Establishes competition format, norms, and sportsmanship expectations. Round-robin: each pair gets two 60-second runs. Best time counts. Post results on leaderboard.

---

### Period 10 — Checkpoint 1
**Solo mini-challenge (move + sense + variable) + self-assessment**

- Individual assessment: each student completes a short task alone (partner observes, no helping)
- Task: program the Finch to drive forward, stop when it detects an obstacle, display the distance value on the micro:bit, back up, and turn
- Self-assessment form: "I can / I'm learning / I need help" for each concept

---

## Phase B: Core Concepts (Periods 11–23)

Loops, conditionals, line following, and introduction to functions. Competitions land every 4–5 teaching periods. Each concept gets at least two periods.

---

### Period 11 — Loops intro
**Repeat blocks to draw polygons with the marker holder**

- Bronze: Draw a square using a repeat-4 loop (compare to period 2 without loops — same result, way less code)
- Silver: Draw a hexagon or octagon — calculate the turn angle from the loop count
- Gold: Nested loop — row of triangles or expanding spiral

> The "aha" moment: students realize that their 16-block square program from period 2 is now 4 blocks inside a loop. Loops are a tool that makes code shorter and patterns possible.

---

### Period 12 — Loops + variables
**Variable-controlled loop count, growing and shrinking patterns**

- Bronze: Loop counter variable — shapes that grow each iteration
- Silver: Expanding spiral — increase distance variable each loop pass
- Gold: Fibonacci spiral or original mathematical art design

> Loops and variables together are more powerful than either alone. This period makes that visible through the marker drawings.

---

### Period 13 — Creative loop challenge 🎨
**Art bot showcase — draw the most creative design using loops + variables**

- Open-ended: design and draw an original pattern
- Pairs present their best drawing and explain the code behind it
- Display results on the classroom wall — "Code Art Gallery"

> Breather period. Low pressure, high creativity. No tiers — just explore. Students who are behind can make a simple pattern; students who are ahead can go wild. The physical drawings become a visible celebration of what the class has learned.

---

### Period 14 — Conditionals intro
**If/else with distance sensor, autonomous roaming robot**

- Bronze: If obstacle detected → stop. Else → drive forward.
- Silver: If obstacle → turn random direction and keep going. Robot roams indefinitely.
- Gold: Smart roaming — choose turn direction based on which side has more open space

> First if/else. The robot makes decisions. This is the moment coding feels like building something intelligent. Give students time to just watch their roaming robot — the engagement is intrinsic.

---

### Period 15 — Conditionals + loops
**Combined logic, nested ifs, multi-sensor decisions**

- Bronze: Forever-loop with conditional — roam until button press stops it
- Silver: Nested if — different responses for close (< 10 cm), medium (10–30 cm), and far (> 30 cm) distances
- Gold: Guard robot — patrol a set path (loop), alert with LED + sound when intruder detected (conditional)

> This is the first time students combine two major concepts (loops + conditionals) in one program. The guard robot gold challenge is especially engaging — students love showing off their "security system."

---

### Period 16 — Sumo prep ⚡
**Build LEGO arms, code sensor-driven pushing strategy**

- Bronze: Scan for opponent (loop + distance sensor), drive toward when detected
- Silver: Add retreat-and-reposition behavior when opponent is lost
- Gold: Multi-state strategy — search → charge → push → recover → search

> First competition where code quality determines the winner. The scan-and-charge logic directly applies the conditionals just learned. Building LEGO arms adds a hands-on design element that breaks up the coding pattern.

---

### Period 17 — Sumo tournament ⚡
**Round-robin in both arenas**

Difficulty: ●●○○○

> 5 teams per arena. Each bout: 90 seconds. 30-second reset between bouts. ~10 bouts per arena = ~20 minutes. Leaves time for brief debrief: which strategies won and why? Students observe that robots with conditional logic (turn when opponent disappears) beat robots that just drive forward.

---

### Period 18 — Line following intro
**IR sensors + forever-loop + conditional to track a black tape line**

- Bronze: Follow a straight black line across the arena poster
- Silver: Follow a curved line with gentle bends
- Gold: Follow a line with one sharp 90° turn

> New sensor type (IR). Students learn that the two IR sensors can detect dark vs. light surfaces. The basic algorithm: if left sensor is on line → turn left slightly, if right sensor is on line → turn right slightly. This is the first time they combine two sensors reading simultaneously.

---

### Period 19 — Line following: tuning
**Improve reliability and handle curves**

- Bronze: Complete a full loop on the printed track poster
- Silver: Complete the loop without going off-track more than twice
- Gold: Complete the loop at the fastest speed that remains reliable

> This is where students learn that getting something working (period 18) and getting it working well are different skills. Tuning speed, turn sharpness, and sensor thresholds is iterative and teaches patience and systematic testing.

---

### Period 20 — Line following timed challenge ⚡
**Informal competition — timed laps on a loop track**

Difficulty: ●●●○○

> Not a full tournament — more like a timed trial. Each pair gets two attempts on the track. Post times on the board. Speed vs. reliability tradeoff becomes visible: the fastest robots lose the line on curves. Brief discussion: "Is it better to be fast and risky or slow and reliable?" This is an optimization concept they'll revisit in 8th grade.

---

### Period 21 — Functions intro
**Create simple custom blocks in Snap!**

- Bronze: Create a "turn around" custom block and a "wiggle" custom block. Use each at least 3 times in a program.
- Silver: Create two custom blocks and combine them in a sequence to perform a complex maneuver
- Gold: Create a custom block with one input parameter (e.g., "move_distance" takes a number)

> Introduction only — students learn what a function is, why it's useful (reuse, clarity), and how to create one in Snap!. Don't rush to composition — just getting comfortable with the concept of "name this chunk of code" is the goal.

---

### Period 22 — Functions in practice
**Use custom blocks to build a navigation program**

- Bronze: Sequence 3+ custom blocks to navigate a multi-section path (e.g., call forward_and_turn, then wiggle, then turn_around)
- Silver: Combine custom blocks with conditionals — call different functions based on sensor input
- Gold: Refactor your line-following code — replace repeated patterns with named custom blocks

> The gold challenge (refactoring old code) is powerful. Students look at their period 18 line-following program and see how much cleaner it could be. Functions stop feeling abstract and start feeling like a tool they wish they'd had earlier. This plants the seed for 8th grade where functions become central.

---

### Period 23 — Checkpoint 2
**Solo integration challenge + self-assessment**

- Individual task: given a multi-step mission description, write pseudocode (plain English steps), then implement in Snap!
- Mission includes: movement with a loop, a sensor-based conditional, a variable, and at least one custom block
- Self-assessment: compare growth from Checkpoint 1

---

## Phase C: Capstone Project (Periods 24–31)

Student-directed projects with 6 full build periods (roughly 2.5 hours of actual work time). Structured with planning, peer review, and a showcase.

---

### Period 24 — Project kickoff
**Form teams, choose from project menu, plan on paper**

Project menu (choose one or propose your own):

- **Dance routine** — choreograph a performance with movement, LEDs, sound, and timed sequences. Good for creative students. Lower coding ceiling but high polish potential.
- **Art bot** — use the marker holder and loops/variables to draw a complex design. Must include at least two types of loops and one variable-controlled element.
- **Obstacle navigator** — program the Finch to navigate a complex course autonomously using distance sensor. Must reach a target zone without human intervention.
- **Sensor game** — create an interactive game using the Finch's sensors (e.g., reaction-time game, "hot/cold" finder, light-seeking robot). Must include score tracking with a variable.
- **Student-designed** — must include at least 2 sensors, a loop, a conditional, a variable, and one custom block. Submit a one-paragraph proposal for teacher approval.

All teams write a plan before touching any code: what will the robot do, what blocks/concepts will you use, and what's your testing plan. Teacher reviews plans before coding begins.

---

### Period 25 — Build sprint 1
**Code core behavior, test in arena, log progress**

> Teams work on their primary robot behavior. Engineering log entry: "What we planned, what we built, what happened when we tested."

---

### Period 26 — Build sprint 2
**Add sensors, conditional logic, and polish**

> Layer in sensor-based features. Focus on getting the core behavior reliable before adding complexity.

---

### Period 27 — Mid-project peer review 🔍
**Swap code with another team, use read-predict-compare to find bugs**

> Structured protocol: receiving team reads code aloud block-by-block, predicts behavior, runs the robot, identifies one bug and one improvement suggestion. Giving team listens without defending. Both teams log the feedback received.

---

### Period 28 — Build sprint 3
**Respond to peer feedback, refine and improve**

> Address the bug and improvement from peer review. This is where most teams make their biggest leap in quality.

---

### Period 29 — Build sprint 4
**Final feature push, optimize and clean up**

> Feature freeze at end of period. Whatever works at the end of this session is the final version. No more adding — only fixing.

---

### Period 30 — Demo rehearsal + peer feedback
**Practice 2-minute demo, get audience reactions**

> Each team does a dry-run demo for one other team. Feedback: "one thing that impressed me, one question I have." Teams revise their presentation (not their code) based on feedback.

---

### Period 31 — Showcase day 🎉
**Team demos, class awards, self-assessment, 8th grade preview**

- Each team demos their project (2 minutes + 1 question)
- Awards in multiple categories: best code, best design, best debug story, most creative, most improved, best teamwork
- Self-assessment: reflect on growth across the year
- Preview: "Next year you'll do all of this in Python — and your competitions will be harder."

> Invite admin, other teachers, or parents if possible. Awards cover multiple categories so recognition is wide, not winner-take-all.

---
---

# 8TH GRADE — 31 PERIODS
## Snap! → Python Transition | Building Mastery | 4 Competitions

---

## Phase A: Python Transition (Periods 1–10)

Students return with Snap! fluency from 7th grade. This phase transitions them to Python through side-by-side translation, rebuilding familiar programs in text code. The obstacle course competition (now in Python) bookends the transition.

---

### Period 1 — Welcome back: Snap! refresher
**Challenge: build a program using loops + conditionals + variables in Snap!**

- Bronze: Navigate a course with a loop, stop on sensor detection, display variable on micro:bit
- Silver: Add conditional logic — different behavior based on distance ranges
- Gold: Complete the full challenge in under 5 minutes with clean, well-organized code

> Diagnostic period. You're assessing what students retained over summer. Don't teach — let them work and observe. Note which students need more support in Phase A and which are ready to move fast.

---

### Period 2 — Meet Python
**Side-by-side: same program in Snap! and Python**

- Bronze: Translate a 5-block Snap! program (move, turn, LED) to Python line by line
- Silver: Translate a 10-line program with a variable
- Gold: Write a new Python program from scratch — not translated, just written

> Show the Snap! program on one side of the screen, Python on the other. Students see that each block has a direct Python equivalent. The message: "You already know what to tell the robot. Python is just a different way of saying it."

---

### Period 3 — Python: movement + LEDs
**Drive, turn, set tail LED colors in Python**

- Bronze: Forward, turn, back, stop with LED color changes between steps
- Silver: Sequence of 8+ lines with timed movements and color transitions
- Gold: Choreographed routine written entirely in Python — no block reference needed

> Students may struggle with syntax (colons, indentation, parentheses). Normalize this: "Syntax errors aren't bugs in your thinking — they're typos. The computer is just pickier about spelling than Snap! was."

---

### Period 4 — Python: variables + sensors
**Read sensors, store values in variables, display on micro:bit**

- Bronze: Read distance sensor, store in a variable, print the value
- Silver: Variable threshold — store detection distance, adjust with button, display on micro:bit
- Gold: Continuous sensor readout — formatted print showing distance, light level, and line sensor values updating in real time

> Python variables don't have the visual "orange bubble" that Snap! uses. Students need to understand that `speed = 50` creates a container even though they can't see it. Printing values makes the invisible visible.

---

### Period 5 — Python: loops
**for loops and while loops**

- Bronze: for loop to draw a square (4 repetitions of move + turn)
- Silver: while loop for continuous roaming (while True: move and check sensor)
- Gold: Nested for loops for complex polygon patterns — variable loop count

> Key distinction: for = "do this N times" (like Snap!'s repeat), while = "keep going until something changes" (like Snap!'s forever/repeat-until). Both are essential. Most students grasp for quickly; while takes a second period to solidify.

---

### Period 6 — Python: conditionals
**if / elif / else**

- Bronze: if obstacle < 20: stop. else: drive forward.
- Silver: elif for distance ranges — close/medium/far trigger different behaviors
- Gold: Autonomous roaming with smart turn decisions based on sensor comparison

> elif is new — Snap! nests if/else blocks visually, but Python's elif is cleaner for multiple conditions. Show a 3-level distance response: close → back up + red LED, medium → slow down + yellow LED, far → full speed + green LED.

---

### Period 7 — Python: debugging
**Syntax errors, logic errors, and print() debugging**

- Bronze: Fix 3 programs with syntax errors (missing colons, wrong indentation, unclosed parentheses)
- Silver: Fix 3 programs with logic errors (wrong variable used, condition reversed, loop runs wrong number of times)
- Gold: Use print() statements to trace variable values through a program and identify where a logic error occurs

> Three types of errors: syntax (Python tells you), runtime (crashes while running), logic (runs fine but does the wrong thing). The last type is hardest because Python can't help you — only reading and reasoning about your code works. The read-predict-compare method from 7th grade still applies.

---

### Period 8 — Integration practice
**Combine all Python skills on a multi-section challenge course**

- Open practice: navigate a course using movement, loops, conditionals, variables, and sensors — all in Python
- Pairs compare their Python code to what they would have written in Snap! — which is more readable? Which was faster to write?

---

### Period 9 — Obstacle course competition (Python) ⚡ + checkpoint
**Same arena, same format as 7th grade — but now in text code**

Difficulty: ●●○○○

- Same obstacle course format: timed runs, best of two attempts
- Must be written in Python (no Snap!)
- After competition: solo checkpoint — translate a given Snap! program to Python and predict its behavior

> Students feel the difference between block and text coding under pressure. Some will find Python faster once fluent; others will miss the visual clarity of blocks. Both reactions are valid and worth discussing.

---

### Period 10 — Debrief: Python vs. Snap!
**When is text code better? When are blocks better? Reflection and discussion**

- Class discussion: advantages of each (blocks: visual, no syntax errors, great for beginners. Python: faster to type once fluent, easier to share/read as text, used in industry, more powerful libraries)
- Written reflection: "Which do I prefer right now, and why? Which do I think I'll prefer in a year?"

> This isn't a "Python is better" lecture. It's honest comparison. The goal is metacognition — students thinking about their own learning tools.

---

## Phase B: Advanced Concepts (Periods 11–23)

Functions in depth, Boolean logic, decomposition, state machines, and algorithm design. Two competitions: sumo (Python) and maze. Concepts build on each other intentionally — each period's new idea uses the previous period's concept.

---

### Period 11 — Functions: def, parameters, calling
**Define reusable functions with inputs**

- Bronze: Define move_forward(speed) and turn(degrees) — call each with different values
- Silver: Function with two parameters — move_timed(speed, seconds)
- Gold: Function that returns a value — check_distance() returns True/False for obstacle detection

> This is deeper than 7th grade functions. Parameters mean the same function does different things depending on what you pass in. Return values let functions answer questions, not just do actions.

---

### Period 12 — Functions: building a library
**Create a reusable collection of movement and sensor functions**

- Bronze: Create 3+ functions, organize them into a library file that can be called from a main program
- Silver: Library with parameterized shape functions — draw_polygon(sides, size)
- Gold: Import and use another team's library in your own program (collaboration challenge)

> The library concept matters: professional programmers don't rewrite everything from scratch. They build tools and reuse them. The gold challenge (using another team's library) teaches reading other people's code and understanding their naming choices — a critical real-world skill.

---

### Period 13 — Functions: compose and refactor
**Build complex behavior from function building blocks, clean up old code**

- Bronze: Sequence 4+ library functions to navigate a complex multi-section path
- Silver: Refactor 7th grade sumo strategy in Python using functions (pull up old code, rewrite with clean function calls)
- Gold: Create a general-purpose navigator(target_distance, turn_angle) function that can be reused in any navigation task

> Refactoring 7th grade code is the most powerful exercise here. Students see their own growth: "I wrote that mess a year ago? This is so much cleaner now."

---

### Period 14 — Boolean logic: AND, OR, NOT
**Compound conditions with multiple sensors**

- Bronze: Compound condition — if distance < 20 AND light < 50: enter "dark and close" mode
- Silver: Three-condition logic — if (left_line AND right_line) OR button_pressed: execute action
- Gold: Create a truth table documenting all sensor combinations and the robot's response to each, then implement in code

> New concept not covered in 7th grade. This unlocks complex sensor decisions. The truth table exercise (gold) makes Boolean logic concrete and connects to math curriculum. Post example truth tables on the wall for reference.

---

### Period 15 — Decomposition + pseudocode
**Plan before coding: pseudocode-first design**

- Bronze: Given a complex mission description, write numbered English steps before writing any Python
- Silver: Decompose the mission into sub-problems, identify which sub-problems become functions
- Gold: Draw a flowchart with decision diamonds showing all conditional paths, then code directly from the flowchart

> This is explicit instruction in a skill they'll need for the maze and magnet collection competitions. Emphasize: professionals spend more time planning than coding. The pseudocode IS the hard part — translating to Python is mechanical.

---

### Period 16 — Sumo in Python
**Advanced strategy with functions + Boolean logic**

- Bronze: Basic scan-and-charge in Python — translate 7th grade Snap! strategy to text code
- Silver: Add Boolean multi-sensor conditions — use distance AND light to distinguish opponent from wall
- Gold: Adaptive strategy — change behavior based on match time (aggressive early, defensive late) using a timer variable

> Students compete against their 7th-grade selves. The Python version should be cleaner and smarter. Boolean logic (period 14) enables strategies that weren't possible last year — distinguishing the opponent from the arena wall using multiple sensors.

---

### Period 17 — Sumo tournament (Python) ⚡
**Round-robin in both arenas, Python code only**

Difficulty: ●●●○○

> Same format as 7th grade sumo, but the average code quality should be noticeably higher. More sophisticated strategies, cleaner code structure, better debugging when things go wrong. Brief debrief: "What strategies worked that wouldn't have been possible in 7th grade?"

---

### Period 18 — Line following in Python + optimization
**Revisit line following with text code, add speed optimization**

- Bronze: Translate 7th grade Snap! line follower to Python — get it working on the track
- Silver: Add speed optimization — go faster on straight sections, slower on curves (use sensor readings to detect curve intensity)
- Gold: Proportional correction — instead of binary left/right, adjust turn sharpness based on how far off the line the sensor is (PID-style concept)

> The gold challenge introduces proportional control, which is a real robotics concept. Full PID is too complex, but the idea that "a little off → small correction, a lot off → big correction" is accessible and powerful.

---

### Period 19 — State machines: concept introduction
**Two-mode robot using a state variable**

- Bronze: Patrol mode (drive a set pattern) vs. alert mode (stop, flash LEDs, play alarm) — switch with a variable. Distance sensor triggers the switch from patrol → alert.
- Silver: Three modes — patrol, alert, and return-to-base. Each mode has distinct behavior.
- Gold: Mode transitions triggered by different sensors — distance triggers alert, button triggers return, light level triggers patrol resume

> State machines are the key concept that makes 8th grade competitions harder than 7th grade. The idea: the robot's behavior depends not just on what it senses right now, but also on what "mode" it's in. Same sensor reading, different response depending on state. This is genuinely new thinking.

---

### Period 20 — State machines: application
**Implement a complex multi-mode robot**

- Bronze: Search-and-respond robot — search mode (drive pattern) switches to respond mode (stop + signal) when target found, then back to search
- Silver: Add a counter — respond mode tracks how many targets found, changes behavior after a threshold
- Gold: Fully autonomous multi-behavior robot with timed mode switching (patrol for 10 seconds, scan for 5 seconds, repeat) — functions for each mode

> This is the direct preparation for the magnet collection competition. Students who can build a search → detect → respond → resume robot here are ready for the final competition.

---

### Period 21 — Maze: algorithm design
**Design a wall-following algorithm on paper, pseudocode first**

- Bronze: Pseudocode a right-wall-follower — always keep the wall on your right. Write every step in plain English.
- Silver: Add dead-end handling — if wall ahead AND wall right, turn left. If wall on all three sides, turn around.
- Gold: Plan speed zones — identify where in the algorithm the robot can safely go faster and where it must slow down. Annotate the pseudocode with speed variables.

> No coding this period — paper and pencil only. Students draw the maze poster and trace their algorithm by hand, step by step, to verify it works before writing a single line of Python. This is decomposition in action.

---

### Period 22 — Maze: implementation
**Code the wall-following algorithm in Python, test and debug on the maze poster**

- Bronze: Basic right-wall-follower working — robot enters maze and makes progress through at least 3 turns
- Silver: Robot completes the maze with dead-end handling
- Gold: Robot completes the maze with speed optimization — variable speed based on corridor detection

> Students translate their period 21 pseudocode to Python. Debugging is intense here — the algorithm may be correct on paper but fail in practice due to sensor timing, turn precision, or speed. This is where print() debugging and systematic testing pay off. Both arenas should have the same maze poster for fair testing.

---

### Period 23 — Maze competition ⚡ + checkpoint
**Identical mazes on both arenas, fastest complete run wins**

Difficulty: ●●●●○

- Both arenas run the same printed maze poster
- Each pair gets two attempts. Between attempts, 60 seconds to modify code
- Time starts when robot enters the maze, stops when it exits
- Pairs that don't complete can score partial credit (furthest point reached)

> After competition: checkpoint assessment. Solo task — given a new, simple maze diagram on paper, write the pseudocode for a wall-following solution. This tests whether students understand the algorithm, not just whether their robot happened to finish. Self-assessment form.

---

## Phase C: Capstone + Grand Finale (Periods 24–31)

Extended project build with more ambitious options than 7th grade, followed by the grand finale competition: magnet collection v2.

---

### Period 24 — Advanced project kickoff
**Form teams, choose from advanced project menu, decompose into subtasks**

Advanced project menu (choose one or propose your own):

- **Maze solver (advanced)** — build a robot that solves any maze, not just the competition maze. Test on multiple maze posters.
- **Multi-sensor game** — create an interactive game using 3+ sensors. Must include scoring, a state machine for game states (start, playing, game over), and player feedback.
- **Autonomous delivery** — program the Finch to travel a route with multiple stops, "pick up" (simulate) and "deliver" items to marked zones, tracking deliveries with variables.
- **Interactive art installation** — Finch creates drawings that respond to audience interaction (light sensor, proximity, buttons). Must produce different art based on sensor input.
- **Student-designed** — must use Python, include functions with parameters, a state machine or multi-mode behavior, 2+ sensor types, and solve a real-world-inspired problem. Submit a one-paragraph proposal for teacher approval.

All teams decompose their project into sub-problems, identify which sub-problems become functions, and write pseudocode for the main program flow. Teacher reviews plans.

---

### Period 25 — Build sprint 1
**Code core behavior in Python, test in arena**

> Engineering log: pseudocode plan, what was coded, test results.

---

### Period 26 — Build sprint 2
**Add sensor integration and conditional logic**

> Layer in the sensor-driven features. Emphasize testing each new feature before adding the next.

---

### Period 27 — Mid-project peer review 🔍
**Swap code with another team for structured review**

> Protocol: receiving team reads the Python code line by line, adds comments explaining what each section does, identifies one bug and one improvement. Both teams log feedback. This is harder in Python than it was in Snap! — reading text code is a skill being practiced here.

---

### Period 28 — Build sprint 3
**Respond to peer feedback, add state management, optimize**

> Address peer review findings. Add functions for clean organization. This is the sprint where code quality improves the most.

---

### Period 29 — Magnet collection v2: prep ⚡
**Design detect/collect algorithm, build LEGO magnet arms, calibrate**

- Bronze: Lawn-mower search pattern with pause-on-detection (if IR senses dark → stop for 1 second, then resume)
- Silver: Full collect function — detect dark circle → drive forward by calibrated offset → pause → wiggle → increment counter → resume search. LED shows mode.
- Gold: Spiral pattern with adaptive behavior — tighten spiral if no detections for 2+ rows. Speed optimization: fast on empty rows, slow near detections.

> This is the most complex programming task in the two-year curriculum. It requires: search algorithm (loops), detection (IR conditionals), positioning (calibrated variable), collection routine (function), state switching (search ↔ collect), counter tracking (variable), and micro:bit display. Everything converges here.

> Critical: students must measure the physical offset between their IR sensors and their magnet arm tip, and store that as a variable. This bridges physical measurement to code parameter — the deepest engineering moment in the course.

---

### Period 30 — Magnet collection tournament ⚡
**Most washers collected in 90 seconds wins**

Difficulty: ●●●●●

- Teacher places 10 washers on dark circles (from secret layout sheet) — same layout on both arenas
- Each pair gets two 90-second attempts. 30-second code modification window between attempts.
- Score = washers on magnet when time is called
- New layout for each round
- Round-robin format — top scores advance to a final round if time permits

> Grand finale competition. The whole class should feel the weight of this one. It's the culmination of two years of learning. Even the bronze approach (lawn-mower with simple pauses) demonstrates loops, conditionals, and sensor reading. The gold approach demonstrates mastery-level integration.

---

### Period 31 — Showcase day 🎉
**Capstone project demos, final awards, course reflection**

- Each team demos their capstone project (2–3 minutes + 1 question)
- Awards span both competitions and projects: best algorithm, best code quality, best debug story, most creative project, most improved coder, best teamwork, best documentation
- Written reflection: "Compare your first program in period 1 of 7th grade to what you can build now. What changed?"
- If applicable: student portfolios collecting their best code, engineering logs, and reflections from both years

> Invite admin, parents, and 7th graders (future students). Let 8th graders explain what they built and what they learned. This is both assessment and recruitment for the program.

---
---

# APPENDIX A: Competition Summary

| Competition | Grade | Periods | Difficulty | Key CS Concepts Tested |
|---|---|---|---|---|
| Obstacle course | 7th (P9) | 1 prep + 1 event | ●○○○○ | Sequences, movement precision, variables |
| Sumo | 7th (P16–17) | 1 prep + 1 event | ●●○○○ | Conditionals, distance sensor, basic strategy |
| Line following | 7th (P20) | Informal timed | ●●●○○ | Loops + conditionals, IR sensors, tuning |
| Obstacle course (Python) | 8th (P9) | Within checkpoint | ●●○○○ | Python fluency, same concepts in new language |
| Sumo (Python) | 8th (P16–17) | 1 prep + 1 event | ●●●○○ | Functions, Boolean logic, advanced strategy |
| Maze | 8th (P21–23) | 2 prep + 1 event | ●●●●○ | Functions, decomposition, wall-following algorithm |
| Magnet collection v2 | 8th (P29–30) | 1 prep + 1 event | ●●●●● | State machines, functions, multi-sensor, calibration |

---

# APPENDIX B: Materials for All Competitions

## Arena (×2)
- 2× half-inch sanded plywood panel, 2 ft × 4 ft (cut to 31.5" × 24.25")
- 2× 1×4 common pine board, 8 ft
- 1× 1×2 common pine strip, 4 ft
- 1× box #6 × 1-1/4" wood screws (50 ct)
- 1× box #6 × 3/4" wood screws (25 ct)
- 1× pack adhesive felt pads, 1" round (16 ct)
- 1× Minwax Polycrylic, satin, half-pint (optional)
- 2× foam brush, 2" disposable (optional)
- 1× 220-grit sandpaper sheet (optional)
- **Arena cost: ~$55–65**

## Competition-specific materials
- Steel flat washers, 3/4" — box of 100 (~$5)
- Neodymium disc magnets, 10mm × 3mm — pack of 20 (~$8)
- LEGO Technic beams, connectors, axle pins — from existing supply
- Electrical tape — for magnet mounting and line-following tracks
- Black electrical tape or printed posters for line following
- **Competition materials cost: ~$15**

## Printed posters (teacher-created)
- Obstacle course layout (7th and 8th grade)
- Sumo ring
- Line following track (loop with curves)
- Maze (2–3 difficulty variants)
- Magnet collection field (with 5 cm dark circles, multiple layout variants)
- **Poster printing: school printer or office supply store, ~$2–5 per poster**

## Total added cost beyond Finch robots: ~$75–85

---

# APPENDIX C: Assessment Framework (Both Years)

| Type | When | What It Measures |
|---|---|---|
| Engineering log | Every build session | Process, planning, reflection, debugging thinking |
| Checkpoint 1 | End of Phase A (both years) | Individual skill with core concepts (solo task) |
| Checkpoint 2 | End of Phase B (both years) | Integration of concepts, problem-solving ability |
| Peer code review | Mid-project (both years) | Ability to read, understand, and critique code |
| Capstone project | Phase C (both years) | Integration, teamwork, presentation, creativity |
| Self-assessment | 3× per year (end of each phase) | Student reflection on growth and confidence |

**Grading philosophy:** Weight toward process and growth (logs, participation, collaboration, improvement between checkpoints) rather than robot performance. A robot that doesn't perfectly follow the line but has a well-documented debugging history shows more learning than a perfect run with no reflection.

---

# APPENDIX D: Classroom Management Quick Reference

**Session rhythm (40 minutes):**
- 0:00–0:05 — Warm-up prompt on board, no robots yet
- 0:05–0:12 — Mini-lesson or demo, students watch
- 0:12–0:32 — Work time, robots out, driver/navigator swap at 0:22
- 0:32–0:37 — Share-out (1–2 pairs show work or describe a bug they solved)
- 0:37–0:40 — Cleanup: robots in bins, micro:bits seated, cables connected, stations clear

**Pair programming:**
- Fixed pairs for each phase (~8–10 periods), then rotate
- Driver writes code, navigator reviews and strategizes
- Timer-cued swap halfway through work time
- Intentional pairing: one stronger + one developing coder (without labeling)

**Tiered challenges (Bronze / Silver / Gold):**
- Bronze is mandatory for all — core concept
- Silver adds complexity or combines concepts
- Gold requires optimization, debugging, or creative extension
- Students self-select after completing bronze
- "Expert consultant" badges for students who master concepts early

**Robot care norms:**
- Numbered bins match pair numbers
- Robots stay on table or designated test area
- No code runs until partner has reviewed it
- Report damage immediately — no consequences for accidents
