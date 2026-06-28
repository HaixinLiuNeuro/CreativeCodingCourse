# 8th Grade CS Curriculum
## Finch Robot 2.0 — Snap! to Python | 31 Periods

---

## Course Flow At a Glance

```
FINCH CUP → SNAP! ACTIVITY → PYTHON TRANSLATION → LOOPS IN PYTHON
    → CONDITIONALS → SUMO (PYTHON) → BOOLEAN → FUNCTIONS
        → STATE MACHINES → MAZE → BEACH CLEANUP → CAPSTONE
```

---

## Language Transition

**Students arrive fluent in Snap! from 7th grade.** This course transitions them to Python through translation — not from scratch. Every concept is one they've already mastered in blocks. Python is just a new way of saying what they already know.

**The Snap! ↔ Python Cheatsheet** is provided on day one and referenced all year. It lives on every table, gets updated as new concepts are introduced, and is the bridge between "I know how to do this in blocks" and "now I can do it in text."

---
---

## Phase A: Welcome Back + Python Transition (Periods 1–4)

> Start with play, then bridge to Python through a program they already understand.

---

### Period 1 — 🟥 COMPETE: Finch Cup Returns ⚽
**Welcome back! Same format as 7th grade — keyboard-controlled 1v1 robot soccer.**

Students reconnect with the Finch, rediscover Snap!, and compete immediately. No lecture. No review. Just play.

**Format:** 90-second matches, round-robin, both arenas. Leaderboard on the board.

> This serves two purposes: it's a high-energy course opener, and it's a diagnostic. Watch which students remember Snap! cold and which need a moment to re-orient. That tells you who'll need extra support during the Python transition.

---

### Period 2 — 🟨 CHOOSE: Snap! activity (movement + sensor)
**Each pair picks one activity that uses at least one movement command and one sensor input.** They code it in Snap! and get it fully working.

**Menu — pick 1:**

| Activity | Sensors Used | Link |
|---|---|---|
| ShyBot | Distance sensor — robot retreats from proximity | [Link](https://learn.birdbraintechnologies.com/finch/projects/shybot-2) |
| CricketBot | Light sensor — different behavior in light vs. dark | [Link](https://learn.birdbraintechnologies.com/finch/projects/cricketbot-2) |
| SquirrelBot | Distance + randomness — foraging simulation | [Link](https://learn.birdbraintechnologies.com/finch/projects/squirrelbot-2) |

**Or design your own:** Any program that includes movement + at least one sensor reading + a conditional.

**Key requirement:** The program must be fully working in Snap! by end of period. They'll translate it to Python tomorrow.

> Students who did these activities in 7th grade can pick a different one or build a custom program. The point isn't the activity itself — it's having a working Snap! program they understand deeply, so the translation to Python is about the language, not the logic.

---

### Period 3 — 🟦 TEACH: Meet Python + cheatsheet
**Teacher instruction (15 minutes):**

Show the Snap! ↔ Python Cheatsheet on the projector. Walk through it section by section:

| Snap! Block | Python Code |
|---|---|
| `move Finch forward distance at speed` | `finch.setMove('F', distance, speed)` |
| `turn Finch right degrees at speed` | `finch.setTurn('R', degrees, speed)` |
| `Finch beak R G B` | `finch.setBeak(R, G, B)` |
| `Finch tail all R G B` | `finch.setTail('all', R, G, B)` |
| `Finch distance` | `finch.getDistance()` |
| `Finch light left` | `finch.getLight('L')` |
| `Finch line left` | `finch.getLine('L')` |
| `set myVar to 5` | `myVar = 5` |
| `if <> then ... else` | `if condition:` / `else:` |
| `repeat 4` | `for i in range(4):` |
| `forever` | `while True:` |
| `wait 1 secs` | `time.sleep(1)` |

**Teacher says:** "Every block you know has a Python twin. You already know what to tell the robot. Python is just spelling it differently."

**Student work (25 minutes):**
Open your period 2 Snap! program. Open a Python editor. Using the cheatsheet, translate it line by line. Get it running on the Finch.

> The cheatsheet is printed and placed at every table. Students keep it all year. It gets updated as new concepts (loops, functions, Boolean) are introduced.

---

### Period 4 — 🟩 PRACTICE: Python basics + debugging
**Finish translations from period 3.** Pairs that finished early work on extensions:

- Add a second sensor to your program
- Change the LED behavior
- Modify the movement pattern

**Teacher circulates** helping with the three most common Python stumbles:
1. **Missing colons** after if/else/for/while
2. **Indentation errors** — Python cares about spaces
3. **= vs ==** — assignment vs comparison

**Key instruction:** "Syntax errors aren't thinking errors. They're typos. Python is just pickier about spelling than Snap! was."

> By end of this period, every pair should have at least one Python program running on the Finch. That's the foundation for everything that follows.

---
---

## Phase B: Core Concepts in Python (Periods 5–11)

> Every concept is one students already mastered in Snap!. The work here is fluency in the new syntax, not learning new ideas — until Boolean logic, which is genuinely new.

---

### Period 5 — 🟦 TEACH: Loops in Python
**Teacher instruction (10 minutes):**

Side-by-side comparison:

**Snap!:** `repeat 4: [move forward 10, turn right 90]`

**Python:**
```python
for i in range(4):
    finch.setMove('F', 10, 50)
    finch.setTurn('R', 90, 50)
```

"The `for` loop is Python's repeat block. `range(4)` means 4 times. Everything indented inside the loop repeats."

Then show `while` loops:

**Snap!:** `forever: [if distance < 20 stop, else move forward]`

**Python:**
```python
while True:
    if finch.getDistance() < 20:
        finch.stop()
    else:
        finch.setMove('F', 5, 50)
```

---

### Period 6 — 🟩 PRACTICE: Crop Circle Challenge 👽
**Scenario:** *Your Finch is an alien probe sent to Earth to create mysterious crop circles. Farmers keep finding geometric patterns in their fields. Your mission: recreate the most complex crop circle using Python loops.*

**The activity:** Redo 7th grade shape drawing — but in Python, with the marker holder.

| Level | Crop Circle | Python Concept |
|---|---|---|
| 1 | Square | `for i in range(4)` — direct translation from 7th grade |
| 2 | Triangle | Change range and angle — `range(3)`, turn 120° |
| 3 | Hexagon | `range(6)`, calculate angle |
| 4 | Star | `range(5)`, 144° — the tricky angle returns |
| 5 | Growing spiral | `for i in range(20)` with distance variable increasing each iteration |
| 6 | Nested crop circle | Nested loops — circle of triangles, ring of squares |

**Leaderboard:** Track which level each pair reaches. Display crop circle drawings on the wall.

> Same math, same robot, same marker. The only difference is the language. This makes the Python syntax feel like a minor hurdle rather than a mountain — because the hard part (the geometry) is already solved.

---

### Period 7 — 🟩 PRACTICE: Crop circles continued + patterns
**Continue from period 6.** Pairs who finished all levels attempt:
- Fibonacci spiral in Python
- Concentric polygons (square inside hexagon inside circle)
- Their own original crop circle design

**Last 8 minutes: Crop Circle Gallery.** Display all drawings. Vote on "most authentic alien pattern."

---

### Period 8 — 🟦 TEACH: Conditionals in Python
**Teacher instruction (10 minutes):**

Side-by-side:

**Snap!:** `if distance < 20 then [stop] else [move forward]`

**Python:**
```python
if finch.getDistance() < 20:
    finch.stop()
else:
    finch.setMove('F', 5, 50)
```

New in Python: **elif** (not in Snap!)

```python
distance = finch.getDistance()
if distance < 10:
    finch.setBeak(255, 0, 0)     # Red — danger close
elif distance < 30:
    finch.setBeak(255, 255, 0)   # Yellow — caution
else:
    finch.setBeak(0, 255, 0)     # Green — all clear
```

**Key instruction:** "`elif` is Python's way of checking multiple conditions in order. Snap! nests if/else blocks inside each other — Python uses elif to keep it flat and readable."

---

### Period 9 — 🟩 PRACTICE: Finch Bodyguard 🕶️ + activity choice
**Scenario:** *A VIP (small LEGO figure) is placed on the arena. Your Finch is the bodyguard. It must patrol around the VIP and respond to threats.*

**Challenges:**
- Bronze: If something approaches (distance < 20), Finch intercepts — drives toward the threat, flashes red, plays alarm tone. Otherwise, drives a patrol circle around the VIP.
- Silver: Add light sensor — if the room goes dark, activate "night vision" mode (green LEDs, slow cautious movement). If light returns, resume normal patrol.
- Gold: Add elif chain — close threat (< 10 cm) → aggressive intercept + siren. Medium distance (10–30 cm) → warning stance + yellow LED. Far (> 30 cm) → calm patrol + green.

**Or choose a BirdBrain activity in Python:**

| Activity | Focus | Link |
|---|---|---|
| Emotional Finch | Variable state + sensor-triggered changes | [Link](https://learn.birdbraintechnologies.com/finch/projects/finch-emotions) |
| Simon Says I | Button conditionals + sequences | [Link](https://learn.birdbraintechnologies.com/finch/projects/simon-says-i-2) |

---

### Period 10 — 🟦 TEACH + BUILD: Sumo prep (Python) 🤖
**Teacher instruction (10 minutes):** Review sumo strategy from 7th grade. "You coded this in Snap! last year. Now build a smarter version in Python."

Show the Python structure:
```python
while True:
    distance = finch.getDistance()
    if distance < 25:
        # Opponent detected — charge!
        finch.setMotors(100, 100)
    else:
        # Searching — spin slowly
        finch.setMotors(-30, 30)
```

**Student work (30 minutes):** Build LEGO arms. Code sumo strategy in Python. Test in arena.

---

### Period 11 — 🟥 COMPETE: Sumo tournament (Python) 🏆
**Round-robin in both arenas.** All code must be Python. Leaderboard.

**Post-tournament debrief:** "How did your Python sumo compare to your 7th grade Snap! version? What did you do differently?"

> Difficulty: ●●●○○

---
---

## Phase C: Advanced Concepts (Periods 12–18)

> New territory. Boolean logic, functions, and state machines — concepts not covered in 7th grade.

---

### Period 12 — 🟦 TEACH: Boolean logic — AND, OR, NOT
**Teacher instruction (15 minutes):**

"Your bodyguard robot checked one condition at a time. What if it needs to check two conditions at once?"

**Demo:**
```python
distance = finch.getDistance()
light = finch.getLight('L')

if distance < 20 and light < 30:
    # Dark AND close — intruder in the shadows!
    finch.setBeak(255, 0, 0)
    finch.setMotors(100, 100)
```

Show truth tables on the board:
- `and` → both must be true
- `or` → either can be true
- `not` → flips true/false

**Live demos with the Finch:** Cover the light sensor AND move hand close → triggers. Only one → doesn't. Students predict before each test.

---

### Period 13 — 🟩 PRACTICE: Search & Rescue Bot 🔦 + activity choice
**Scenario:** *An earthquake has struck. Survivors are trapped in collapsed buildings. Your robot must search the disaster zone. Survivors are located in specific conditions: dark areas (light sensor low) behind walls (distance sensor detects obstacle). Your robot must check multiple Boolean conditions to distinguish a survivor location from an empty wall or an open dark area.*

**Challenges:**
- Bronze: `if light < 30 and distance < 15:` → flash rescue signal (blue LEDs) + play alert tone. Otherwise, keep searching (drive forward).
- Silver: Add `or` — rescue signal triggers if (dark AND close) OR (button A pressed by a teammate spotting from above). Add a `rescue_count` variable displayed on micro:bit.
- Gold: Three-condition compound: `if light < 30 and distance < 15 and not finch.getLine('L'):` — dark AND close AND not on a road (line sensor). Build a full sweep pattern that covers the arena systematically.

**Or choose a BirdBrain activity to practice Boolean logic:**

| Activity | Focus | Link |
|---|---|---|
| Animal Adaptations | Compound conditionals, multi-sensor, simulate real animal behaviors | [Link](https://learn.birdbraintechnologies.com/finch/projects/animal-adaptations-2) |
| Special Delivery | Multi-step navigation with compound sensor conditions | [Link](https://learn.birdbraintechnologies.com/finch/projects/finch-specialdelivery) |

---

### Period 14 — 🟦 TEACH: Functions in Python
**Teacher instruction (15 minutes):**

"In 7th grade you made custom blocks in Snap!. In Python, those are called functions. But Python functions are more powerful — they take inputs and give back answers."

**The key difference from Snap! custom blocks:** Parameters and return values.

**Demo with the Finch — build a "Robot Movie Director" toolkit:**

```python
def dramatic_entrance(speed):
    """Robot zooms in from off-stage"""
    finch.setBeak(255, 255, 0)          # Spotlight on
    finch.setMove('F', 30, speed)
    finch.setBeak(255, 255, 255)         # Flash!

def scan_the_room(pause_time):
    """Robot looks around slowly, building suspense"""
    for i in range(4):
        finch.setTurn('R', 90, 20)
        time.sleep(pause_time)
        if finch.getDistance() < 20:
            return True                   # Something found!
    return False                          # Nothing here

def victory_dance(spins):
    """Celebration after finding the target"""
    for i in range(spins):
        finch.setTurn('R', 360, 80)
        finch.setTail('all', 0, 255, 0)
        time.sleep(0.3)
        finch.setTail('all', 0, 0, 255)
        time.sleep(0.3)
```

"Now direct the scene":
```python
dramatic_entrance(80)
found = scan_the_room(0.5)
if found:
    victory_dance(3)
```

**Key instruction:**
- `def` creates a function. The name describes what it does.
- Parameters in parentheses make it flexible — `victory_dance(3)` vs `victory_dance(10)`.
- `return` lets a function answer a question — `scan_the_room` returns True/False.
- "Functions are reusable behaviors. Write once, call anywhere, customize with parameters."

---

### Period 15 — 🟩 PRACTICE: Robot Movie Director 🎬 + activity choice
**Scenario:** *You're directing a robot action movie. Each function is an "action call." Build your toolkit of actions, then compose them into a scene.*

**Challenges:**
- Bronze: Write 3 functions — `dramatic_entrance(speed)`, `scan_the_room(pause_time)`, and `victory_dance(spins)`. Compose them into a 30-second scene.
- Silver: Add `chase_sequence(target_distance)` — robot drives toward the nearest object, matching a target distance, using a while loop and distance sensor inside the function. Direct a scene with entrance → scan → chase → victory.
- Gold: Add `plot_twist()` — randomly choose between two different endings using a random number + conditional inside the function. The "movie" plays differently each time.

**Or choose a BirdBrain activity to practice functions:**

| Activity | Focus | Link |
|---|---|---|
| Light Show | Procedures with parameters — color, timing, pattern functions | [Link](https://learn.birdbraintechnologies.com/finch/projects/light-show) |
| Turning with Encoders | Functions with parameters for precision turns, calibration math | [Link](https://learn.birdbraintechnologies.com/finch/projects/turning-with-encoders-i) |

---

### Period 16 — 🟨 CHOOSE: Level 5 activities + function practice (continued)
**Continue from period 15**, or pick a new activity:

| Activity | Focus | Link |
|---|---|---|
| Light Show | Parameterized light/sound sequences | [Link](https://learn.birdbraintechnologies.com/finch/projects/light-show) |
| Turning with Encoders | Precision movement functions | [Link](https://learn.birdbraintechnologies.com/finch/projects/turning-with-encoders-i) |
| Follow the Wall | Wall-following algorithm using functions — direct prep for maze | [Link](https://learn.birdbraintechnologies.com/finch/projects/follow-the-wall) |

> Students who choose Follow the Wall get a significant head start on the maze competition.

---

### Period 17 — 🟦 TEACH: State machines
**Scenario for teaching: Robot Pet 🐾**

**Teacher instruction (15 minutes):**

"Your Finch has moods. Its behavior changes based on what state it's in — and sensor events trigger state changes."

| State | Behavior | Trigger to Enter |
|---|---|---|
| 😊 HAPPY | Drives around, green LEDs, cheerful tones | Default / light sensor goes bright |
| 😠 GRUMPY | Turns away, red LEDs, growling tone | Distance sensor blocked (something in its face) |
| 🎮 PLAYFUL | Spins, rainbow LEDs, melody | Micro:bit button A pressed |
| 😴 SLEEPY | Slow drift, dim blue LEDs, quiet humming | Left alone in the dark (light < 20 for 5+ seconds) |

**Demo the code structure:**
```python
state = "happy"

while True:
    if state == "happy":
        finch.setBeak(0, 255, 0)
        finch.setMove('F', 5, 30)
        if finch.getDistance() < 15:
            state = "grumpy"
        if finch.getLight('L') < 20:
            state = "sleepy"

    elif state == "grumpy":
        finch.setBeak(255, 0, 0)
        finch.setTurn('R', 180, 50)
        time.sleep(2)
        state = "happy"

    elif state == "playful":
        finch.setBeak(0, 0, 255)
        finch.setTurn('R', 360, 80)
        state = "happy"

    elif state == "sleepy":
        finch.setBeak(0, 0, 50)
        finch.setMotors(10, 10)
        if finch.getLight('L') > 50:
            state = "happy"
```

**Key instruction:** "The robot's behavior depends not just on what it senses right now, but on what mood it's in. Same sensor reading, different response depending on state. That's a state machine."

Draw the state diagram on the board with arrows showing transitions.

---

### Period 18 — 🟩 PRACTICE: Robot Pet 🐾 + state machine challenges
**Build your own Robot Pet.** Design its personality with custom states.

- Bronze: 2 states (happy + grumpy) with sensor-triggered transitions. Each state has distinct movement, LED color, and sound.
- Silver: 4 states with the full transition diagram. Draw the state diagram on paper first, then code.
- Gold: Add functions for each state behavior — `be_happy()`, `be_grumpy()`, `be_playful()`, `be_sleepy()`. Add a "mood counter" variable that tracks how many times each mood was entered, displayed on micro:bit.

**Share-out:** Pairs demo their pet's personality. Vote on most realistic robot pet.

---
---

## Phase D: Advanced Competitions (Periods 19–25)

> The two hardest competitions in the two-year curriculum. Each one integrates everything students have learned.

---

### Period 19 — 🟩 PRACTICE: Line following in Python (bridge to maze)
**Translate 7th grade line-following algorithm to Python.** This is a bridge period — students need working line-following code before tackling wall-following.

```python
while True:
    left = finch.getLine('L')
    right = finch.getLine('R')
    if left < 50:              # Left sensor on line
        finch.setMotors(20, 50)   # Turn left
    elif right < 50:           # Right sensor on line
        finch.setMotors(50, 20)   # Turn right
    else:
        finch.setMotors(40, 40)   # Drive straight
```

**Timed laps on the track.** Leaderboard. Speed vs. reliability tradeoff returns.

---

### Period 20 — 🟦 TEACH: Maze algorithm — Dungeon Crawler 🏰
**Scenario:** *Your robot knight must escape a dungeon. The walls are closing in. Navigate the corridors, avoid dead ends, find the exit. Fastest escape wins glory and treasure.*

**Teacher instruction — paper only, no coding:**

Right-wall-following algorithm explained and traced on a maze diagram:

1. If you can turn right → turn right (there's an opening)
2. If you can't turn right but can go straight → go straight
3. If you can't turn right or go straight but can turn left → turn left
4. If you're trapped on three sides → turn around

**Students trace the algorithm by hand** on a printed maze worksheet. Mark each decision point. Verify the algorithm reaches the exit.

**Pseudocode the solution.** Teacher reviews pseudocode before anyone opens Python.

**Key instruction:** "The algorithm is the hard part. The code is just translating your pseudocode. If your pseudocode works on paper, your Python will work on the robot."

---

### Period 21 — 🟩 PRACTICE: Maze implementation
**Code the wall-following algorithm in Python.** Test on the maze poster in the arena.

- Bronze: Basic right-wall-follower — robot makes progress through 3+ turns
- Silver: Handles dead ends (wall ahead AND wall right → turn left)
- Gold: Speed optimization — fast in long corridors, slow at decision points. Use functions: `check_right()`, `check_ahead()`, `turn_to_opening()`

**Both arenas have identical maze posters.** Pairs test and debug.

---

### Period 22 — 🟥 COMPETE: Maze competition — Dungeon Escape 🏰
**Both arenas, identical maze posters.** Two attempts per pair, 60-second code modification window between attempts.

**Scoring:**
- Time from entry to exit
- Partial credit for furthest point reached
- Bonus: cleanest code (teacher's choice — reviewed post-competition)

**Leaderboard tracks time and furthest progress.**

> Difficulty: ●●●●○

---

### Period 23 — 🟦 TEACH: Operation Shore Sweep — Beach Cleanup 🏖️
**Scenario:** *The coastline is contaminated with metal debris — bottle caps, scrap metal, and industrial waste washed up by storms. Satellite imagery has identified debris hotspots (dark circles on the beach). Your cleanup robot must search the beach, detect hotspot zones with its ground sensors, collect metal debris with its magnetic arm, and bring it for proper recycling. Every piece of debris collected is one less pollutant in the ocean.*

**Teacher instruction (15 minutes):**

Review the task mechanics:
- Arena poster = the beach. Dark circles = debris hotspots detected by satellite.
- Steel washers = metal debris (placed on the dark circles by teacher).
- LEGO magnetic arm = debris collection tool.
- IR sensors detect the dark hotspot circles.
- The magnet tip and IR sensors are offset — students must measure and calibrate.

**State machine connection:**
```
SEARCH mode → Drive sweep pattern, IR sensors scanning
    ↓ (IR detects dark circle)
COLLECT mode → Stop, position magnet, pause, wiggle, increment counter
    ↓ (collection done)
SEARCH mode → Resume pattern
```

"This is everything you've learned combined: loops (search pattern), conditionals (detection), Boolean logic (IR left OR IR right triggers collect), functions (collect_debris as a reusable routine), variables (counter, offset, direction), and state machine (search ↔ collect)."

**Student work (25 minutes):** Build LEGO magnetic arms. Measure the offset between IR sensors and magnet tip — store as variable. Start coding the search pattern.

---

### Period 24 — 🟩 PRACTICE: Beach Cleanup prep + calibration
**Full build and testing session.**

- Bronze — Beachcomber: Lawn-mower sweep pattern. When IR detects dark → pause 1 second, let magnet attract debris, then resume. Simple but effective.
- Silver — Shore Patrol: Full collect cycle — detect → drive forward by calibrated offset → pause → wiggle → increment `debris_count` → display count on micro:bit → resume sweep. LED shows green in search mode, yellow in collect mode.
- Gold — Eco-Optimizer: Spiral pattern with adaptive behavior. If no detections for 2 full rows, tighten the spiral. Speed optimization: fast on empty sections, slow near detections. Track collection rate (debris per minute) and display.

**Calibration is critical:** Each pair must:
1. Measure the distance from IR sensors to magnet tip on their specific arm build
2. Store it as `magnet_offset` variable
3. Test with a single washer on a dark circle — does the magnet land on the washer?
4. Adjust until pickup is reliable

---

### Period 25 — 🟥 COMPETE: Operation Shore Sweep tournament 🏖️
**Most debris collected in 90 seconds wins.**

**Setup:** Teacher places 10 washers on dark circles using a secret layout sheet. Same layout on both arenas.

**Format:**
- Two 90-second attempts per pair
- 30-second code modification window between attempts
- Score = washers on magnet when time is called
- New layout for final round

**Leaderboard and awards:** Most debris collected, most efficient sweep pattern, best-calibrated robot.

**Environmental connection (last 3 minutes):** "Real beach cleanup robots exist. They use the same principles — search patterns, sensor detection, collection mechanisms. The code you wrote today is a simplified version of what's being developed to clean our oceans."

> Difficulty: ●●●●●

---
---

## Phase E: Capstone + Showcase (Periods 26–31)

---

### Period 26 — Project kickoff
**Form teams. Choose from advanced menu. Decompose into subtasks. Pseudocode.**

**Project menu:**

| Project | Scenario | Requirements |
|---|---|---|
| Maze Solver Pro | Build a robot that solves ANY maze, not just the competition one. Test on 2+ maze posters. | Functions, distance sensor, wall-following algorithm |
| Robot Wildlife Documentary | Your Finch mimics a real animal's behavior. Research the animal, program the Finch to react to its environment the way the animal would. Present as a "nature documentary." | State machine (3+ states), 2+ sensors, functions |
| Autonomous Delivery Service | Program a delivery route with multiple stops. Finch picks up (simulates) packages and delivers to marked zones, tracking deliveries. | Functions, variables, line sensors, decomposition |
| Interactive Escape Room | Design a mini escape room game using the Finch. Players interact with sensors to "solve puzzles" — shine a light, press a button, block the path — each correct action triggers the next clue. | State machine, 3+ sensors, Boolean logic, functions |
| Student-Designed | Must solve a real-world-inspired problem. | Functions with parameters, state machine, 2+ sensors, Boolean logic |

**All teams:** Decompose into functions on paper. Write pseudocode for main program. Teacher reviews before coding.

---

### Period 27 — Build sprint 1
Code core behavior in Python. Test in arena. Engineering log entry.

---

### Period 28 — Build sprint 2
Add sensor integration and state management.

---

### Period 29 — Mid-project peer review 🔍
Swap code with another team. Read Python line by line. Add comments explaining each section. Identify one bug and one improvement.

---

### Period 30 — Build sprint 3 + polish
Respond to peer feedback. Refine. Feature freeze at end of period.

---

### Period 31 — 🟥 Showcase day 🎉
**Capstone demos (2–3 minutes each + 1 question).**

**Awards:**
- Best Algorithm
- Best Code Quality (cleanest Python, best function design)
- Best Debug Story
- Most Creative Project
- Most Improved Coder
- Best Teamwork
- Environmental Impact Award (for beach cleanup innovation)
- Audience Favorite

**Reflection:** "Compare your first Snap! program in 7th grade period 1 to what you can build now in Python. What changed?"

**Invite:** Admin, parents, 7th graders (future students). Let 8th graders explain what they built and inspire the next class.

---
---

# Summary

## Period Map

| Period | Type | Activity |
|---|---|---|
| 1 | 🟥 COMPETE | Finch Cup ⚽ |
| 2 | 🟨 CHOOSE | Snap! activity (movement + sensor) |
| 3 | 🟦 TEACH | Python intro + cheatsheet + translate |
| 4 | 🟩 PRACTICE | Python basics + debugging |
| 5 | 🟦 TEACH | Python loops |
| 6 | 🟩 PRACTICE | Crop Circle Challenge 👽 (Day 1) |
| 7 | 🟩 PRACTICE | Crop Circle Challenge 👽 (Day 2) |
| 8 | 🟦 TEACH | Python conditionals + elif |
| 9 | 🟩 PRACTICE | Finch Bodyguard 🕶️ + activity choice |
| 10 | 🟦 TEACH + BUILD | Sumo prep (Python) |
| 11 | 🟥 COMPETE | Sumo tournament 🏆 |
| 12 | 🟦 TEACH | Boolean logic (AND, OR, NOT) |
| 13 | 🟩 PRACTICE | Search & Rescue Bot 🔦 + activity choice |
| 14 | 🟦 TEACH | Functions (def, parameters, return) |
| 15 | 🟩 PRACTICE | Robot Movie Director 🎬 + activity choice |
| 16 | 🟨 CHOOSE | Level 5 activities |
| 17 | 🟦 TEACH | State machines |
| 18 | 🟩 PRACTICE | Robot Pet 🐾 |
| 19 | 🟩 PRACTICE | Line following in Python |
| 20 | 🟦 TEACH | Maze algorithm — Dungeon Crawler 🏰 (paper) |
| 21 | 🟩 PRACTICE | Maze implementation |
| 22 | 🟥 COMPETE | Maze competition — Dungeon Escape 🏰 |
| 23 | 🟦 TEACH | Operation Shore Sweep intro 🏖️ |
| 24 | 🟩 PRACTICE | Beach cleanup prep + calibration |
| 25 | 🟥 COMPETE | Operation Shore Sweep tournament 🏖️ |
| 26 | 🟩 PROJECT | Capstone kickoff |
| 27 | 🟩 PROJECT | Build sprint 1 |
| 28 | 🟩 PROJECT | Build sprint 2 |
| 29 | 🔍 REVIEW | Mid-project peer review |
| 30 | 🟩 PROJECT | Build sprint 3 + polish |
| 31 | 🟥 SHOWCASE | Demos + awards + reflection |

## Competitions

| Event | Period | Difficulty | Key Concepts |
|---|---|---|---|
| Finch Cup | 1 | ●○○○○ | Keyboard events (Snap! review) |
| Sumo (Python) | 11 | ●●●○○ | Conditionals, loops, sensors in Python |
| Maze — Dungeon Escape | 22 | ●●●●○ | Wall-following algorithm, functions, decomposition |
| Beach Cleanup — Shore Sweep | 25 | ●●●●● | State machine, functions, Boolean, multi-sensor, calibration |

## Type Distribution

| Type | Count | Percentage |
|---|---|---|
| 🟦 TEACH | 9 | 29% |
| 🟩 PRACTICE / EXPLORE | 13 | 42% |
| 🟨 CHOOSE | 2 | 6% |
| 🟥 COMPETE / SHOWCASE | 5 | 16% |
| 🟩 PROJECT (capstone) | 4 | 13% |

## Scenario Themes

| Concept | Dry Version | Fun Version |
|---|---|---|
| Loops | Draw polygons | Crop Circle Challenge 👽 |
| Conditionals | If distance < 20 stop | Finch Bodyguard 🕶️ |
| Boolean | Compound sensor conditions | Search & Rescue Bot 🔦 |
| Functions | def move_forward(speed) | Robot Movie Director 🎬 |
| State Machines | Two-mode robot | Robot Pet 🐾 |
| Maze | Wall-following algorithm | Dungeon Crawler 🏰 |
| Magnet Collection | Search and collect washers | Operation Shore Sweep 🏖️ |
