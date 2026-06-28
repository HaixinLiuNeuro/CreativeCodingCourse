# 7th Grade CS Curriculum — Revised
## Finch Robot 2.0 with Snap! | 31 Periods

---

## Course Flow At a Glance

```
EXPLORE → FINCH CUP → JOUSTING → FINDING SPEED → SHAPES & LOOPS
    → PATTERNS → LEDs → OBSTACLE COURSE → SENSORS → CONDITIONALS
        → ACTIVITY MENUS → SUMO → LINE FOLLOWING → FUNCTIONS → CAPSTONE
```

---

## Language Policy

**7th grade is Snap! only.** Python is reserved for 8th grade.

Snap! fluency is the goal this year. Students finish the course confident with sequences, variables, loops, conditionals, sensors, and basic functions — all expressed in blocks. Introducing Python before those concepts are automatic creates confusion rather than acceleration.

**Exception — advanced individual extension only:** Students who consistently hit Gold on every challenge and finish early can be offered a printed Python reference card and invited to rewrite a completed program in Python on their own. This is individual enrichment, not class-wide instruction. No teaching period is used. The reference card is available at the extension station with the note: *"Already done? Try rewriting your sumo code in Python."* This plants the seed for 8th grade without derailing the class.

---
---

## Phase A: Explore and Play (Periods 1–4)

> Hook them before you teach them. Students meet the Finch, explore freely, then compete in Finch Cup — all before any formal instruction. By period 5, every student is invested.

---

### Period 1 — 🟦 TEACH: Meet the Finch + Snap!
**Teacher demos:** How to connect the Finch in Snap!, what each block category does (movement, lights, sound), how to drag-snap-run. Pair programming norms: driver/navigator, swap every 12 minutes.

Run one simple program live: move forward → turn → light up → play tone. Students predict what happens before each run.

> No student coding yet. Teacher models the platform. Students absorb the workflow. End with: "Tomorrow, it's your turn — build whatever you want."

---

### Period 2 — 🟩 EXPLORE: Free creation + share
**Open exploration.** No assignment. No rubric. Just: "Make the Finch do something interesting." Pairs experiment with movement, lights, sounds, micro:bit display — whatever catches their attention.

**Last 10 minutes: gallery walk.** Each pair shows their creation to the class (30 seconds each). Teacher highlights variety: "This pair made it dance. This pair made it draw. This pair made it play a melody. All of that is code."

> This period matters more than it looks. Students who've never coded discover they can make a real robot do things immediately. Students who are experienced get to flex. Everyone leaves wanting more. That's the foundation for everything that follows.

---

### Period 3 — 🟦 TEACH: Keyboard control
**Teacher demos:** How to use Snap! keyboard events to control the Finch in real time.

Key concepts in Snap!:
- `when [up arrow] key pressed` → move forward
- `when [down arrow] key pressed` → move backward
- `when [left arrow] key pressed` → turn left
- `when [right arrow] key pressed` → turn right
- `when [space] key pressed` → stop

**Students code their own controller.** Each pair builds a working keyboard controller by the end of the period. Test by driving around the table.

**Teacher instruction points:**
- Event-driven programming: "The robot waits for YOUR input. It responds to events — key presses."
- This is a different model than sequential programming (which comes next period 5).

---

### Period 4 — 🟥 COMPETE: Finch Cup ⚽
**1v1 robot soccer. Keyboard-controlled. Maximum chaos, maximum engagement.**

**Setup:**
- Both arenas become soccer fields. Print a soccer field poster (green with goal zones on each short end) or mark goals with tape.
- One small foam ball per arena (lightweight so the Finch can push it).
- One Finch per side, each driven by one student via keyboard.
- Partner acts as coach/strategist.

**Format:**
- 90-second matches. Score = goals (ball fully inside goal zone).
- Round-robin: 5–6 matches per arena running simultaneously.
- Pairs rotate: driver plays one match, navigator drives the next.
- Leaderboard on the board — wins, draws, goals scored.

**Rules:**
- No picking up the Finch during play.
- If the ball goes off the arena, restart at center.
- Robots start at their own goal line.

> This is pure engagement — no CS lecture needed. Students are learning event handling, real-time control, and cause-and-effect through play. The competitive energy sets the tone for the rest of the course: this class is different.

---
---

## Phase B: Movement Precision + Data (Periods 5–7)

> Transition from real-time control to programmed sequences. Students discover that precision requires planning, not reflexes.

---

### Period 5 — 🟦 TEACH: Programmed movement
**Teacher instruction:** "In Finch Cup, you controlled the robot live. Now you'll write instructions in advance. The robot follows your plan exactly — no steering wheel."

**Teacher demos:**
- `move forward [distance] at [speed]` — precise movement
- `turn [direction] [degrees] at [speed]` — precise turning
- How distance and angle values control the robot
- The difference between event-driven (keyboard) and sequential (programmed) execution

**Key insight for students:** "Keyboard control is like driving. Programmed movement is like giving directions. Both are coding — but directions have to be exact."

---

### Period 6 — 🟩 PRACTICE: Jousting 🏇

**The activity:** Each pair builds a LEGO lance (arm) and mounts it on the Finch's back. The Finch must navigate from a start position to a target and "strike" — touching the lance tip to a target object.

**Setup:**
- Start position marked on one side of the arena
- Target (a small LEGO tower or cup) placed at a set position — NOT straight ahead. Reaching it requires at least one turn.
- Lance restriction: maximum 6 LEGO studs long. Must be rigid and mounted on the Finch's top connector.

**The twist:** There is no prescribed path. Students discover that multiple routes work — some go straight then turn, some arc, some make an L-shape, some zig-zag. The leaderboard tracks:
1. **Accuracy** — did the lance hit the target? (Yes/No)
2. **Efficiency** — fewest blocks used
3. **Speed** — fastest completion time

**Leaderboard on the board.** Update after each pair's attempt. Pairs get 3 attempts.

**Share-out (last 8 minutes):** 3–4 pairs show their approach. Teacher highlights the variety: "Three different solutions, all correct. That's programming — there's rarely one right answer."

> Jousting replaces the L-course because it's inherently more engaging (competition + building) and teaches the same skills (precise movement, angles, sequencing). The open-ended nature means every pair's solution is genuinely different, which makes the share-out valuable rather than repetitive.

---

### Period 7 — 🟩 PRACTICE: Finding Speed

**BirdBrain activity:** [Finding Speed with Finch](https://learn.birdbraintechnologies.com/finch/projects/finch-findspeed)

Students program the Finch to move at different speeds, measure the distance traveled in a set time, calculate speed (distance ÷ time), and record data.

**Teacher framing (first 5 minutes):** "You've been telling the Finch to move at speed 50 or speed 80. But how fast IS that? Let's measure."

**What students do:**
- Set up measured distances on the floor (use a meter stick)
- Run the Finch at different speed values
- Time each run
- Calculate actual speed in cm/sec
- Record in a simple data table

**Math connection:** Speed = distance ÷ time. Graphing speed values. Predicting how long a run at speed 60 would take to cover 100 cm.

> This bridges CS and math/science. The data they collect here also helps them write more precise movement code going forward — they'll know that speed 50 covers roughly X cm/sec.

---
---

## Phase C: Loops and Patterns (Periods 8–14)

> The longest phase — 7 periods. Loops are the most important concept in the course, and students need time to move from "I can draw a square" to "I can create complex patterns using loops and variables."

---

### Period 8 — 🟦 TEACH: Loops concept
**The demo that changes everything.** Teacher shows two programs side by side:

**Without loop (draw a square):**
```
move forward 10 cm
turn right 90°
move forward 10 cm
turn right 90°
move forward 10 cm
turn right 90°
move forward 10 cm
turn right 90°
```
16 blocks.

**With loop (same square):**
```
repeat 4 times:
    move forward 10 cm
    turn right 90°
```
3 blocks. Same result.

**Teacher says:** "The robot does the exact same thing. But the second version is shorter, cleaner, and — here's the key — if I want to change the side length, I change ONE number instead of four."

**Then the reveal:** "What if I change the 4 to a 3 and the 90° to 120°?" Students predict. Run it. Triangle.

"What about repeat 6, turn 60°?" Hexagon.

"What about repeat 36, turn 10°?" Circle.

**Key instruction:** "Loops let you repeat without rewriting. The repeat count and the turn angle together determine the shape. That's a formula: turn angle = 360 ÷ number of sides."

---

### Period 9 — 🟩 PRACTICE: Drawing shapes with loops (leveled)

**Marker holder in.** Students draw on paper in the arena.

| Level | Shape | Loop Count | Turn Angle | Challenge |
|---|---|---|---|---|
| 1 | Square | 4 | 90° | Given — just build the loop |
| 2 | Triangle | 3 | 120° | Calculate the angle |
| 3 | Rectangle | ? | ? | Two different side lengths — how? (hint: loop of 2 with alternating distances) |
| 4 | Pentagon | 5 | 72° | Calculate using 360 ÷ 5 |
| 5 | Hexagon | 6 | 60° | Calculate |
| 6 | Star | 5 | 144° | The angle isn't 360 ÷ 5 — students must experiment or research |

**Leaderboard:** Track which level each pair reaches. Pairs can attempt levels in order or skip ahead if confident.

> The star is the hook. Students who reach it discover that star angles work differently (exterior angle of a star = 144° for a 5-pointed star). This is a genuine mathematical puzzle embedded in a coding activity.

---

### Period 10 — 🟩 PRACTICE: Spirals + advanced loop patterns

**Challenge:** Use loops where the distance variable changes each iteration.

| Challenge | Description |
|---|---|
| Growing square spiral | Each side is slightly longer than the last — increase distance variable inside the loop |
| Shrinking spiral | Start big, decrease each iteration |
| Circular spiral | Small turn angle + growing distance = spiral curve |
| Starburst | Draw a line, return to center, turn slightly, repeat |

**BirdBrain resource:** [Finch Spirals](https://learn.birdbraintechnologies.com/finch/projects/finch-spirals-2)

> This is the bridge from "loops repeat" to "loops with changing values" — which is the door to variables.

---

### Period 11 — 🟦 TEACH: Variables + loop integration
**Teacher instruction:** "In the spiral, you changed the distance each time. But you changed it by hand — editing the number. What if the code could change it automatically?"

**Demo:** Create a variable called `side_length`. Set it to 2. Inside the loop: move forward `side_length`, turn, then `change side_length by 1`. Run it. The square spiral draws itself.

**Key instruction:**
- A variable is a named container that holds a value
- You can read it, change it, and use it inside loops
- When a variable changes inside a loop, the behavior evolves over time

**Then show:** Same concept with color — a `hue` variable that changes each loop iteration, so the tail LEDs shift color as the spiral grows.

---

### Period 12 — 🟩 PRACTICE: Patterns with loops + variables (Day 1)
**Extended creative challenge.** Students design original patterns using loops and variables together.

**Starter challenges:**
- Rainbow trail: loop where color variable changes each iteration
- Growing polygon: loop count variable increases, drawing bigger shapes each round
- Tiling pattern: nested loop — repeat a shape in a row, then shift and repeat the row

**Students work at their own pace.** No single "right answer." The marker drawings become visible artifacts of their code.

---

### Period 13 — 🟩 PRACTICE: Patterns with loops + variables (Day 2)
**Continue from period 12.** Pairs who finish early can attempt:
- Fibonacci spiral (each side = sum of previous two sides)
- Tessellation (interlocking shapes)
- Their own original design

**Last 8 minutes: Code Art Gallery.** Display all drawings on a wall or table. Brief walk-around. Vote on favorites. Teacher highlights the code behind 2–3 impressive designs.

> Two full periods for this section is intentional. Complex patterns require experimentation, debugging, and iteration. Rushing this undermines the deepest learning in the loops unit.

---

### Period 14 — 🟩 PRACTICE: Patterns with loops + variables (Day 3, if needed)

**Flexible period.** If the class needs more time on patterns, continue here. If they're solid, use this period for:
- Students who are behind catch up on shape levels from period 9
- Students who are ahead start exploring the [Drawing Shapes](https://learn.birdbraintechnologies.com/finch/projects/finch-drawingshapes) BirdBrain activity as extension
- Or transition to LED outputs (next phase) early

**Advanced extension station:** Students who have hit Gold on every challenge can visit the extension station and attempt to rewrite one of their loop programs in Python using the printed reference card. This is self-directed, ungraded, and framed as a preview of 8th grade — not a new expectation.

> This is the built-in buffer. Every class moves at a different pace through patterns. This period absorbs that variance.

---
---

## Phase D: Outputs and Obstacle Course (Periods 15–18)

> Shift from marker drawing to robot expression — LEDs, sound, and display. Then apply everything in the obstacle course.

---

### Period 15 — 🟦 TEACH: LED, sound, and display outputs
**Teacher demos the Finch's output toolkit:**
- Beak LED (tri-color, front)
- Tail LEDs (5 tri-color, back) — individually addressable
- Buzzer — play tones, melodies
- Micro:bit 5×5 LED display — show text, numbers, icons, custom patterns

**Show fun examples:**
- Rainbow chase: tail LEDs cycle through colors using a loop + variable
- Siren: alternating red/blue beak with two-tone buzzer
- Mood display: micro:bit shows a happy face, then changes to surprised when distance sensor detects something (preview of conditionals)

**Key instruction:** "Outputs are how the robot communicates. Movement is one output. Light, sound, and display are others. Great programs combine them."

---

### Period 16 — 🟩 PRACTICE: LED creative activity
**Challenge menu — pick one:**

| Activity | Description |
|---|---|
| Light Parade | Program a repeating light pattern that cycles through the tail LEDs like a marquee. Must use a loop and a variable. |
| Finch DJ | Combine LED color changes with buzzer tones to create a beat-synced light show. At least 8 beats. |
| Emoji Bot | Program the micro:bit display to show 3+ different emoji faces, cycling automatically or triggered by buttons. |
| Custom creation | Design your own LED/sound program. Must include a loop, a variable, and at least 2 output types. |

**Share-out:** Pairs demo their best creation. This is a low-stakes, high-creativity period — no leaderboard, just appreciation.

> LEDs and sound are engagement multipliers. Students who weren't excited by drawing shapes suddenly light up (literally) when their robot becomes a light show. This period ensures every output type is practiced before the obstacle course.

---

### Period 17 — 🟩 PRACTICE: Obstacle course practice
**Setup:** Both arenas have identical obstacle courses (using the printed poster + small LEGO or cardboard obstacles placed at marked positions).

**The course:** Start zone → straight section → turn → narrow gap → another turn → finish zone. Students program the entire course as a sequence — no keyboard control, no sensors yet.

**Must include:** Movement + at least one LED or sound output (e.g., beak turns green when starting, plays a tone at the finish).

**Students practice runs, refine code, and optimize.** This is the integration period — sequencing, precision, loops (if useful), variables (speed), and outputs, all in one program.

---

### Period 18 — 🟥 COMPETE: Obstacle course competition
**Timed runs, best of two attempts.** Both arenas, identical courses. Round-robin.

**Leaderboard tracks:**
1. Completion (did it finish? Yes/No)
2. Time (fastest wins)
3. Style points (bonus for creative LED/sound — class votes)

> Difficulty: ●○○○○. Low CS ceiling but high energy. This is the first formal competition since Finch Cup, and the format establishes the competition norms for sumo and line following later.

---
---

## Phase E: Sensors and Conditionals (Periods 19–23)

> The robot starts thinking. Sensors provide input; conditionals provide decision-making. Combined, they create autonomous behavior.

---

### Period 19 — 🟦 TEACH: Sensors
**Teacher demos each sensor with live values on screen:**

- **Distance sensor** — show values changing as teacher moves hand closer/farther
- **Light sensors (L/R)** — cover one, cover both, shine a flashlight
- **Line sensors (L/R)** — hold Finch over white paper, then over black tape
- **Micro:bit buttons (A/B)** — press and show the value change
- **Accelerometer** — tilt the Finch, show the values shift

**Key instruction:** "Sensors give the robot numbers. Right now, those numbers just sit there. Next period, you'll learn how to make the robot DO something with them."

> Show all sensors in one period so students have the full picture. They don't need to code with all of them yet — just understand what information the Finch can collect.

---

### Period 20 — 🟦 TEACH: Conditionals
**Teacher demos:** "What if the robot could make decisions?"

**Live demo 1:** `if distance < 20 then stop, else move forward.` Move hand in front of sensor — robot stops. Move it away — robot goes.

**Live demo 2:** `if light < 30 then turn on LEDs, else turn off LEDs.` Cover the light sensor — LEDs on. Uncover — LEDs off.

**Live demo 3:** `if button A pressed then play tone.` Press the button — tone plays.

**Key instruction:**
- "Conditionals let your code choose between two paths."
- "The sensor provides the information. The conditional makes the decision."
- Draw the if/else flowchart on the board. Students will see this diagram throughout the course.

---

### Period 21 — 🟩 PRACTICE: Conditional challenges
**Guided challenge with tiers:**

- Bronze: Robot stops when obstacle is within 20 cm. Otherwise drives forward.
- Silver: Robot roams autonomously — if obstacle, turn random direction and keep going.
- Gold: Robot has 3 behaviors based on distance ranges: far (drive fast + green LED), medium (drive slow + yellow LED), close (stop + red LED + alarm tone).

---

### Period 22–23 — 🟨 CHOOSE: Activity menus (Level 3)
**Menu — pick 2 activities over 2 periods:**

| Activity | Focus | Link |
|---|---|---|
| ShyBot | Distance sensor + conditionals — robot retreats from proximity | [Link](https://learn.birdbraintechnologies.com/finch/projects/shybot-2) |
| CricketBot | Light sensor + conditionals — different behavior in light vs. dark | [Link](https://learn.birdbraintechnologies.com/finch/projects/cricketbot-2) |
| Emotional Finch | Variables storing state, sensor-triggered state changes, LED output | [Link](https://learn.birdbraintechnologies.com/finch/projects/finch-emotions) |
| Reaction Time | Variables for timing, button detection, data collection | [Link](https://learn.birdbraintechnologies.com/finch/projects/reaction-time) |
| Simon Says I | Button input conditionals, loops, LED/sound sequences | [Link](https://learn.birdbraintechnologies.com/finch/projects/simon-says-i-2) |
| SquirrelBot | Variables + conditionals + randomness, foraging simulation | [Link](https://learn.birdbraintechnologies.com/finch/projects/squirrelbot-2) |

> Largest menu — 6 options. Different pairs work on different projects simultaneously. All exercise conditionals + sensors but in completely different contexts. Brief share-out at end of period 23: each pair demos one behavior from their chosen activity.

---
---

## Phase F: Advanced Competitions (Periods 24–27)

> Sumo and line following. Both require everything learned so far — movement, variables, loops, conditionals, sensors — applied in competitive contexts.

---

### Period 24 — 🟦 TEACH + BUILD: Sumo prep 🤖
**First 10 minutes — teacher instruction:**
"Sumo is a strategy competition. Your code determines whether you win. Here's how to think about it."

Demo the logic:
- **Search mode:** Spin slowly (loop), reading distance sensor each iteration
- **Attack mode:** When opponent detected (conditional: distance < threshold), drive forward at full speed
- **Recovery mode:** When opponent lost (distance > threshold), go back to searching

"The best sumo bots combine these modes. The worst ones just drive forward and hope."

**Remaining 30 minutes — build and code:**
- Build LEGO arms/pushers. Restriction: must fit within a size box (e.g., no wider than 15 cm total).
- Code the sumo strategy.
- Test in the arena against a stationary object first, then against a partner.

> Sumo is the first competition where code quality directly determines the outcome. Students who understand conditionals + loops + sensors build smarter robots. Students who just program "drive forward" lose to students who program "search, then charge."

---

### Period 25 — 🟥 COMPETE: Sumo tournament 🏆
**Round-robin in both arenas.** 5 teams per arena.

**Format:**
- 90-second bouts
- Robot pushed off the table (or pinned for 5 seconds) = loss
- 30-second reset between bouts
- Leaderboard on the board

**Post-tournament debrief (last 5 minutes):** "Which strategies won? Why?" Teacher highlights the connection between code sophistication and results.

> Difficulty: ●●○○○

---

### Period 26 — 🟦 TEACH + PRACTICE: Line following
**Teacher demos:** Show the IR sensors on the Finch's underside. Dark surface = low value. Light surface = high value.

**The algorithm:**
```
forever:
    if left sensor on dark:
        turn left slightly
    if right sensor on dark:
        turn right slightly
    move forward
```

**Students build it.** Start with a straight black tape line on the arena poster. Get the basic follow working. Then try a curved line.

**Key instruction:** "Line following combines everything: a forever-loop, conditionals checking two sensors, and speed for tuning."

---

### Period 27 — 🟩 PRACTICE: Line following challenge + leaderboard
**Timed laps on a loop track.** Each pair gets 3 attempts.

**Leaderboard tracks:**
1. Completion (did it complete the full loop? Yes/No)
2. Time (fastest complete lap)
3. Consistency (difference between best and worst attempts — smaller = better)

**Tuning challenge:** Speed vs. reliability tradeoff. Faster robots lose the line on curves. Students learn that optimization means balancing competing goals.

**Share-out:** Top 3 pairs explain their tuning strategy. What speed did they use? How did they handle curves? Did they adjust turn sharpness?

> Difficulty: ●●●○○

---
---

## Phase G: Functions and Capstone (Periods 28–31)

> Functions get a focused introduction, then students apply everything in a capstone project.

---

### Period 28 — 🟦 TEACH + PRACTICE: Functions
**Teacher instruction (15 minutes):**
"You've been writing the same turn-around code in every project. What if you could name it and reuse it?"

**Demo in Snap!:**
1. Create a custom block called `turn_around`
2. Define it: turn 180° at speed 50
3. Use it 5 times in a program — one block instead of two every time
4. Create another: `wiggle` — quick left-right-left movement
5. Compose them: `turn_around` → `wiggle` → `turn_around`

**Student practice (25 minutes):**
- Bronze: Create `turn_around` and `wiggle`, use each 3+ times in a program
- Silver: Create a movement library: `draw_square`, `draw_triangle`, `draw_circle` as custom blocks. Compose a dance using all three.
- Gold: Parameterized block — `draw_polygon(sides)` takes number of sides as input and draws any regular polygon

**Key instruction:** "Functions are named chunks of code. Write once, use anywhere. They make your code shorter, cleaner, and easier to fix."

> One period for functions is sufficient at the 7th grade level because:
> (1) Students already have the concept of "reusable patterns" from loops
> (2) They've been implicitly decomposing programs all course
> (3) 8th grade will go deep on parameters, return values, and composition
> The goal here is exposure and appreciation, not mastery.

---

### Period 29 — Project kickoff
**Form teams (pairs or trios). Choose from project menu. Plan on paper.**

**Project menu:**

| Project | Description | Minimum Requirements |
|---|---|---|
| Dance Routine | Choreograph a performance with movement, LEDs, sound, and timing | Loop, variable, 2+ output types |
| Art Bot | Draw a complex design using loops, variables, and the marker holder | Loop, variable, custom block |
| Obstacle Navigator | Navigate a complex course autonomously using distance sensor | Conditional, loop, sensor |
| Sensor Game | Create an interactive game using Finch sensors (reaction time, hot/cold finder, etc.) | Conditional, variable, sensor, loop |
| Student-Designed | Must be approved by teacher | Conditional, loop, variable, 2+ sensors, 1 custom block |

**All teams must:**
1. Write a plan in their engineering log (what will the robot do, step by step)
2. Identify which concepts they'll use (loops, variables, conditionals, sensors, functions)
3. Get teacher sign-off before coding begins

---

### Period 30 — Build sprint + peer review
**First 25 minutes:** Build sprint — code core behavior, test in arena, log progress.

**Last 15 minutes:** Quick peer review — swap with another team. Observer team: run the code, identify one thing that works well and one thing that could improve. 2 minutes per swap.

---

### Period 31 — 🟥 Showcase day 🎉
**Feature freeze first 5 minutes.** Whatever works now is the final version.

**Demos (20 minutes):** Each team presents (2 minutes + 1 question). Show the robot, explain the code briefly, demonstrate.

**Awards (5 minutes):** Best code, most creative, best debug story, most improved, best teamwork, audience favorite.

**Reflection (5 minutes):** Self-assessment: "What could you build on day 1 vs. what you can build now?"

**Preview (5 minutes):** "Next year: Python, maze racing, and magnet collection. Everything you learned this year — but harder."

---
---

# Summary

## Period Map

| Period | Type | Activity |
|---|---|---|
| 1 | 🟦 TEACH | Meet the Finch + Snap! |
| 2 | 🟩 EXPLORE | Free creation + share |
| 3 | 🟦 TEACH | Keyboard control |
| 4 | 🟥 COMPETE | Finch Cup ⚽ |
| 5 | 🟦 TEACH | Programmed movement |
| 6 | 🟩 PRACTICE | Jousting 🏇 + leaderboard |
| 7 | 🟩 PRACTICE | Finding Speed |
| 8 | 🟦 TEACH | Loops concept |
| 9 | 🟩 PRACTICE | Drawing shapes with loops (leveled) |
| 10 | 🟩 PRACTICE | Spirals + advanced loop patterns |
| 11 | 🟦 TEACH | Variables + loop integration |
| 12 | 🟩 PRACTICE | Patterns with loops + variables (Day 1) |
| 13 | 🟩 PRACTICE | Patterns with loops + variables (Day 2) |
| 14 | 🟩 PRACTICE | Patterns Day 3 / catch-up / extension |
| 15 | 🟦 TEACH | LED, sound, display outputs |
| 16 | 🟩 PRACTICE | LED creative activity |
| 17 | 🟩 PRACTICE | Obstacle course practice |
| 18 | 🟥 COMPETE | Obstacle course competition |
| 19 | 🟦 TEACH | Sensors |
| 20 | 🟦 TEACH | Conditionals |
| 21 | 🟩 PRACTICE | Conditional challenges (B/S/G) |
| 22–23 | 🟨 CHOOSE | Activity menus — Level 3 BirdBrain |
| 24 | 🟦 TEACH + BUILD | Sumo prep |
| 25 | 🟥 COMPETE | Sumo tournament 🏆 |
| 26 | 🟦 TEACH + PRACTICE | Line following |
| 27 | 🟩 PRACTICE | Line following challenge + leaderboard |
| 28 | 🟦 TEACH + PRACTICE | Functions |
| 29 | 🟩 PROJECT | Capstone kickoff + build |
| 30 | 🟩 PROJECT | Build sprint + peer review |
| 31 | 🟥 SHOWCASE | Demos + awards + reflection |

## Competitions and Leaderboards

| Event | Period | Type | Difficulty |
|---|---|---|---|
| Finch Cup | 4 | Keyboard-controlled soccer | ●○○○○ |
| Jousting | 6 | Programmed navigation + leaderboard | ●○○○○ |
| Obstacle course | 18 | Programmed sequence + style points | ●●○○○ |
| Sumo | 25 | Sensor-driven autonomous strategy | ●●●○○ |
| Line following | 27 | Algorithm tuning + leaderboard | ●●●○○ |

## Type Distribution

| Type | Count | Percentage |
|---|---|---|
| 🟦 TEACH (teacher instruction) | 10 | 32% |
| 🟩 PRACTICE / EXPLORE | 14 | 45% |
| 🟨 CHOOSE (activity menus) | 2 | 7% |
| 🟥 COMPETE / SHOWCASE | 5 | 16% |
