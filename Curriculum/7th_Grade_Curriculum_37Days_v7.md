# 7th Grade CS Curriculum — Revised v7
## Finch Robot 2.0 with Snap! | 37 Days

---

## Course Structure

| Detail | Info |
|---|---|
| Total Days | 37 instructional days |
| Session Length | 40 minutes |
| Platform | Finch Robot 2.0, Snap! (block coding) |
| Grouping | Pairs or 3-person teams |
| Ongoing Assignments | Team Engineering Journal + Self Engineering Journal |
| Language Policy | Snap! only; Python reserved for 8th grade |

**Each activity listed below is an assignment/assessment.** Activities are graded through journals, in-class demonstrations, and/or digital submissions.

---

## Team Roles

Roles **swap every class**. Each student experiences every role regularly across the course.

| Role | Responsibility |
|---|---|
| **Lead Engineer** | Leads team discussion. Drives the coding decisions. Writes and edits code in Snap!. Directs testing and debugging. |
| **Main Recorder** | Writes the Team Engineering Journal entry for the day. Documents what the team did, decisions made, code explanations, data collected, and team reflections. |
| **Associated Engineer** (3-person teams only) | Supports both roles. Assists with code review, building, testing, and research. Acts as a second set of eyes during debugging. |

**Swap rhythm:** Roles rotate at the start of each class. In a pair, students alternate Lead Engineer and Main Recorder daily. In a trio, roles cycle through all three positions over three days.

---

## Two Journals

| Journal | Who Writes | What Goes In | Frequency |
|---|---|---|---|
| **Team Engineering Journal** | Main Recorder (rotates daily) | Activity descriptions, code documentation, design sketches, data tables, competition strategies, project plans, peer review feedback, team reflections | Every class |
| **Self Engineering Journal** | Every student individually | Personal learning reflections, concept understanding, self-assessment, "what I learned / what confused me / what I'd do differently," connections to other subjects | Key reflection days (marked with ✍️) |

The **Team Journal** is the shared record of what the team built and did. The **Self Journal** is the individual record of what each student learned and thought. Both are ongoing primary assignments graded throughout the course.

---

## Course Flow

```
INTRO & NORMS → MEET THE FINCH → FINCH CUP → JOUSTING → FINDING SPEED
  → LOOPS & PATTERNS → OUTPUTS & OBSTACLE COURSE → SENSORS & CONDITIONALS
    → SUMO → LINE FOLLOWING → FUNCTIONS → CAPSTONE
```

---
---

## Days 1–2: Introduction and Class Norms

---

### Day 1 — Welcome + Classroom Culture
**Warm-up activity:** Icebreaker discussion — "What's one thing you've programmed, built, or created that you're proud of?" (Includes non-digital: recipes, LEGO builds, art, crafts — broadens who feels included.)

**Class discussion:**
- Course overview — what we'll do this year (robots, competitions, coding, building)
- Classroom expectations and shared norms (co-created with students where possible)
- Brief intro to the Finch robot — pass one around, let students hold it

**Habits for Success introduction:**
- Persistence: "When the robot does the wrong thing, that's data, not failure"
- Collaboration: "Your partner sees what you miss"
- Curiosity: "Try it and find out"
- Reflection: "What did you learn, not just what did you do"

**Team roles introduced:** Lead Engineer and Main Recorder explained. Roles swap every class. "Everyone leads. Everyone documents. No one does the same job two days in a row."

> No coding today. This is relationship-building and norm-setting. Students leave knowing what this class is about and what's expected.

---

### Day 2 — Routines + Team Formation + Journals Setup
**Warm-up activity:** "Think-Pair-Share" — show a 60-second video of a robot doing something impressive. Students predict: how many lines of code do you think that took? Discuss.

**Class routines practiced:**
- How to get and return robot bins (numbered bins, team numbers match)
- The 40-minute session rhythm: warm-up → instruction → work → share-out → cleanup
- Cleanup protocol: robots in bins, micro:bits seated, cables connected, stations clear
- How to save and submit work

**Team formation:** Assign pairs or 3-person teams for the first rotation. Practice the role swap: identify today's Lead Engineer and today's Main Recorder.

**Journals setup:**
- **Team Engineering Journal:** Set up shared document (digital or physical notebook). First entry structure demonstrated: Date, Roles, Activity, What We Did, What Happened, Reflection.
- **Self Engineering Journal:** Each student sets up their personal journal. First entry structure: Date, What I Learned, What Confused Me, What I Want to Try Next.

**Assignment overview:** Introduce grading structure, rubrics, and how both journals are assessed.

> Students practice the full routine with a dry run — get bins, set up, assign roles, pack up — without actually coding. The recorder practices writing a journal entry about the dry run.

---
---

## Days 3–5: Meet the Finch + Snap!

---

### Day 3 — 🟦 TEACH: Connect and First Programs
**Roles assigned for today.** Lead Engineer drives the setup. Recorder documents.

**Teacher demos:** How to launch Snap!, connect the Finch, find block categories. Run a simple program: move forward → turn → light up → play tone. Students predict before each run.

**Student work:** Each team connects their Finch and runs the demo program. Verify every team has working connection. Lead Engineer drives the code; Recorder watches for errors.

**Key instruction:** How to save Snap! projects, name them properly, and store/submit code.

**📋 Team Journal #1:** (Recorder) "What is the Finch? What can it do? Draw and label the robot. List the block categories we explored."

**✍️ Self Journal #1:** "What was your role today? How did it feel? What's one thing you're excited to try with the Finch?"

---

### Day 4 — 🟩 EXPLORE: Guided Exploration
**Roles swap from yesterday.**

**Open exploration with guardrails.** Teams experiment with different block categories — movement, LEDs, sounds, micro:bit display. Must try at least one block from each category.

**Lead Engineer** decides what to try; **Recorder** documents what each block does and what happened.

**📋 Team Journal #2:** (Recorder) "List each block category we tried. For each: what block did we use, what happened, and what surprised us?"

---

### Day 5 — 🟩 EXPLORE: Free Creation + Share → Keyboard Intro
**Roles swap.**

**First 20 minutes — Free creation.** "Make the Finch do something interesting. Anything." Lead Engineer codes; Recorder documents decisions and sketches the code flow.

**Share-out (10 minutes):** Each team demos their creation (30 seconds each). Recorder presents while Lead Engineer runs the code.

**Last 10 minutes — Keyboard control preview.** Teacher demos: `when [up arrow] key pressed` → move forward. "Tomorrow, you'll use this to play robot soccer."

**📋 Team Journal #3:** (Recorder) "Describe our free creation. What blocks did we use? Sketch the code flow."

**📋 Assignment:** Free Creation program (saved in Snap!).

---
---

## Days 6–7: Finch Cup ⚽

---

### Day 6 — 🟦 TEACH + BUILD: Keyboard Control + Finch Cup Prep
**Roles swap.**

**Teacher instruction (10 minutes):** How to use Snap! keyboard events:
- `when [up arrow] key pressed` → move forward
- `when [down arrow] key pressed` → move backward
- `when [left arrow] key pressed` → turn left
- `when [right arrow] key pressed` → turn right
- `when [space] key pressed` → stop

**Student work (20 minutes):** Lead Engineer builds the keyboard controller. Associated Engineer (if trio) tests while Recorder logs which keys map to which actions and any issues found.

**LEGO build (10 minutes):** Whole team designs and builds LEGO modifications — bumpers, pushers, guards. Restriction: no wider than 4 studs from Finch body.

**📋 Team Journal #4:** (Recorder) "Draw our Finch Cup robot design. Explain our LEGO modifications and why we chose them. List the keyboard controls."

**📋 Assignment:** Working keyboard controller program + LEGO build.

---

### Day 7 — 🟥 COMPETE: Finch Cup Tournament ⚽
**Roles swap. During matches: one teammate drives, the other coaches/strategizes. Swap for the next match.**

**2v2 robot soccer.** Two teams (4 students, 2 Finches) compete per match.

**Setup:** Both arenas as soccer fields (green poster with goal zones). One foam ball per arena.

**Format:** 90-second matches. Round-robin. Leaderboard on the board.

**Rules:** No picking up the Finch during play. Ball restarts at center after a goal.

**📋 Team Journal #5:** (Recorder) "Match results: wins, losses, goals. What strategy worked best? What would we change?"

**✍️ Self Journal #2:** "What was your role during the matches — driver or coach? Which did you prefer and why? What did you learn from watching other teams?"

---
---

## Days 8–9: Programmed Movement + Jousting 🏇

---

### Day 8 — 🟦 TEACH: Programmed Movement
**Roles swap.**

**Teacher instruction (12 minutes):** "In Finch Cup, you controlled the robot live. Now you'll write instructions in advance. The robot follows your plan exactly — no steering wheel."

**Teacher demos:**
- `move Finch forward [distance] at [speed]` — precise movement
- `turn Finch [direction] [degrees] at [speed]` — precise turning
- Event-driven (keyboard) vs. sequential (programmed) execution

**Student work (25 minutes):** Lead Engineer codes navigation paths. Recorder documents distance and angle values that worked. Guided challenges: straight-turn-straight, L-shaped path, U-turn.

**📋 Team Journal #6:** (Recorder) "What's the difference between keyboard control and programmed movement? What distance and angle values did we use for each path? Include a sketch of our path."

**📋 Assignment:** L-path navigation program (saved).

---

### Day 9 — 🟩 PRACTICE: Jousting 🏇
**Roles swap.**

**The activity:** Build a LEGO lance (max 6 studs), mount on Finch. Navigate from start to target and strike.

**The twist:** No prescribed path. Teams discover multiple routes — L-shape, arc, zig-zag.

**Leaderboard tracks:** Accuracy (hit target?), Efficiency (fewest blocks), Speed (fastest time). Lead Engineer codes; Recorder tracks attempts and results on the leaderboard sheet.

**Share-out (last 8 minutes):** 3–4 teams present their approach. Recorder explains while Lead Engineer demos.

**📋 Team Journal #7:** (Recorder) "Sketch our jousting path. How many blocks? What was our time? What strategy did another team use that was different from ours?"

**✍️ Self Journal #3:** "We saw multiple solutions to the same problem. Why do you think there are many correct answers in coding? Which solution did you think was best and why?"

**📋 Assignment:** Jousting program (saved).

---
---

## Day 10: Finding Speed

---

### Day 10 — 🟩 PRACTICE: Finding Speed
**Roles swap.**

**BirdBrain Activity:** [Finding Speed with Finch](https://learn.birdbraintechnologies.com/finch/projects/finch-findspeed)

**Teacher framing (5 minutes):** "You've been setting speed to 50 or 80. But how fast IS that? Let's measure."

**Student work (30 minutes):** Lead Engineer programs movement at different speeds. Recorder measures distance, times runs with stopwatch, and fills in data table. Associated Engineer (trio) handles the stopwatch.

- Test speeds: 20, 40, 60, 80, 100
- Calculate: speed (cm/sec) = distance ÷ time
- Record in data table

**📋 Team Journal #8:** (Recorder) Data table with speed setting, distance, time, and calculated speed. "What pattern do you notice?"

**📋 Assignment:** Finding Speed data table + calculations.

---
---

## Days 11–17: Loops and Patterns

---

### Day 11 — 🟦 TEACH: Loops Concept
**Roles swap.**

**The demo that changes everything.** Without loop: 16 blocks for a square. With loop: 3 blocks. Same result.

**The reveal:** Change repeat count to 3 and angle to 120° → triangle. Repeat 6, turn 60° → hexagon. Repeat 36, turn 10° → circle.

**Key formula:** Turn angle = 360 ÷ number of sides.

**Student work:** Lead Engineer builds the square loop. Recorder documents the formula and one additional shape.

**📋 Team Journal #9:** (Recorder) "How do loops make code shorter? Write the formula. Show our square code AND the non-loop version side by side."

**📋 Assignment:** Square loop program + one additional shape (saved).

---

### Day 12 — 🟩 PRACTICE: Drawing Shapes with Loops (Leveled)
**Roles swap.** Marker holder in — drawing on paper.

| Level | Shape | Loop Count | Turn Angle | Challenge |
|---|---|---|---|---|
| 1 | Square | 4 | 90° | Given |
| 2 | Triangle | 3 | 120° | Calculate |
| 3 | Rectangle | ? | ? | Alternating sides |
| 4 | Pentagon | 5 | 72° | Calculate |
| 5 | Hexagon | 6 | 60° | Calculate |
| 6 | Star | 5 | 144° | Experiment |

**Leaderboard:** Track which level each team reaches. Lead Engineer codes; Recorder logs each level attempt and result.

**📋 Team Journal #10:** (Recorder) "Which levels did we complete? For each shape: what loop count and angle? Include our drawings."

**📋 Assignment:** Highest shape level completed (program saved) + drawings.

---

### Day 13 — 🟩 PRACTICE: Spirals + Advanced Loop Patterns
**Roles swap.**

**BirdBrain Activity:** [Finch Spirals](https://learn.birdbraintechnologies.com/finch/projects/finch-spirals-2)

Challenges: growing square spiral, shrinking spiral, circular spiral, starburst.

**📋 Team Journal #11:** (Recorder) "Which spiral patterns did we complete? Describe how the distance changes each loop iteration. Include drawings."

**📋 Assignment:** Spiral program (saved) + drawings.

---

### Day 14 — 🟦 TEACH: Variables + Loop Integration
**Roles swap.**

**Teacher demos:** Variable `side_length` set to 2. Inside loop: move forward `side_length`, turn, then `change side_length by 1`. The spiral draws itself.

**Student work:** Lead Engineer replicates the demo, then experiments. Recorder documents what different starting values and increments produce.

**📋 Team Journal #12:** (Recorder) "What is a variable? What happens when the variable changes inside the loop? Table showing: starting value, increment, and resulting pattern."

**✍️ Self Journal #4:** "Explain variables in your own words, as if teaching a friend who's never coded. Use an everyday example."

**📋 Assignment:** Variable-controlled spiral program (saved).

---

### Day 15 — 🟩 PRACTICE: Patterns with Loops + Variables (Day 1)
**Roles swap.**

**Extended creative challenge.** Teams design original patterns using loops and variables.

Starters: rainbow trail (color variable changes each iteration), growing polygon, tiling pattern (nested loops).

**📋 Team Journal #13:** (Recorder) "Describe our pattern design plan. What variables do we use? What do they control? Sketch the expected result."

**📋 Assignment:** Pattern program (saved).

---

### Day 16 — 🟩 PRACTICE: Patterns with Loops + Variables (Day 2)
**Roles swap.**

Continue from Day 15. Refine and extend. Attempt: Fibonacci spiral, tessellation, concentric shapes.

**📋 Team Journal #14:** (Recorder) "What changes did we make from yesterday? What debugging did we do? What improved?"

**📋 Assignment:** Continued pattern work (saved).

---

### Day 17 — 🟩 PRACTICE: Patterns with Loops + Variables (Day 3) + Code Art Gallery 🎨
**Roles swap.**

**First 25 minutes:** Final work time. Polish best designs.

**Last 15 minutes — Code Art Gallery:** Display drawings on wall. Walk-around. Vote on: most complex, most creative, most precise, most surprising. Teacher highlights code behind 2–3 designs.

**📋 Team Journal #15:** (Recorder) "Describe our best design and the code behind it. Which other team's design impressed us and why?"

**✍️ Self Journal #5:** "Look at all the designs on the wall. Pick one that's not yours. What do you think the code looks like? Try to describe the loop and variables they used."

**📋 Assignment:** Final pattern (saved) + Code Art Gallery participation.

---
---

## Days 18–21: Outputs and Obstacle Course

---

### Day 18 — 🟦 TEACH: LED, Sound, and Display Outputs
**Roles swap.**

**Teacher demos:** Beak LED (tri-color), tail LEDs (5, individually addressable), buzzer (tones, melodies), micro:bit display (text, icons, custom patterns).

**Fun live examples:** Rainbow chase, siren, mood display.

**Student work:** Lead Engineer experiments with each output type. Recorder catalogs each output and what it does.

**📋 Team Journal #16:** (Recorder) "List the four output types. For each: describe the block, the values it takes, and one idea for using it in a future program."

**📋 Assignment:** Output exploration programs (saved).

---

### Day 19 — 🟩 PRACTICE: LED Creative Activity
**Roles swap.**

**Challenge menu — pick one:**

| Activity | Description |
|---|---|
| Light Parade | Marquee pattern through tail LEDs. Loop + variable required. |
| Finch DJ | LED synced with buzzer tones. At least 8 beats. |
| Emoji Bot | 3+ emoji faces on micro:bit, cycling or button-triggered. |
| Custom Creation | Loop + variable + 2+ output types. |

**Share-out:** Recorder presents while Lead Engineer runs the demo.

**📋 Team Journal #17:** (Recorder) "Which activity did we choose? Describe the program. What was the hardest part?"

**📋 Assignment:** LED creative program (saved).

---

### Day 20 — 🟩 PRACTICE: Obstacle Course Practice
**Roles swap.**

Both arenas with identical courses. Start → straight → turn → narrow gap → turn → finish. Fully pre-programmed. Must include movement + at least one LED or sound output.

**📋 Team Journal #18:** (Recorder) "Sketch our course path with distance and angle values labeled. What was our biggest error and how did we fix it?"

**📋 Assignment:** Obstacle course program (saved).

---

### Day 21 — 🟥 COMPETE: Obstacle Course Competition
**Roles swap. During runs: Lead Engineer starts the program, Recorder times the run.**

Timed runs, best of two. Both arenas. Round-robin. Leaderboard tracks: completion, time, style points (class votes on LED/sound creativity).

**📋 Team Journal #19:** (Recorder) "Our times: Attempt 1 ___  Attempt 2 ___. What we'd change with one more attempt."

**✍️ Self Journal #6:** "Think about your debugging process throughout this course so far. When your robot does the wrong thing, what steps do you take to fix it? Describe your personal debugging method."

**📋 Assignment:** Competition results recorded.

---
---

## Days 22–26: Sensors and Conditionals

---

### Day 22 — 🟦 TEACH: Sensors
**Roles swap.**

**Teacher demos each sensor with live values:** distance, light (L/R), line (L/R), micro:bit buttons, accelerometer.

**Student work:** Lead Engineer reads each sensor. Recorder fills in a sensor data table.

**📋 Team Journal #20:** (Recorder) Sensor data table — for each sensor: what it measures, range of values observed, one program idea.

**📋 Assignment:** Sensor data table.

---

### Day 23 — 🟦 TEACH: Conditionals
**Roles swap.**

**Teacher demos:**
- `if distance < 20 then stop, else move forward.`
- `if light < 30 then LEDs on, else LEDs off.`
- `if button A pressed then play tone.`

**Key instruction:** If/else flowchart drawn on the board.

**Student work:** Lead Engineer builds one if/else program. Recorder draws the flowchart.

**📋 Team Journal #21:** (Recorder) "Draw an if/else flowchart for our program. Label the condition, the true path, and the false path. Describe what the robot does."

**✍️ Self Journal #7:** "Conditionals let robots make decisions. Think of 3 decisions YOU make every day that follow an if/else pattern. Write them as if/else statements."

**📋 Assignment:** If/else program (saved).

---

### Day 24 — 🟩 PRACTICE: Conditional Challenges
**Roles swap.**

- Bronze: If obstacle → stop. Else → drive forward.
- Silver: If obstacle → turn random direction, keep roaming forever.
- Gold: Three distance ranges — close (red + stop), medium (yellow + slow), far (green + full speed).

**📋 Team Journal #22:** (Recorder) "Which tier did we complete? Describe our robot's behavior. What decisions does it make?"

**📋 Assignment:** Highest tier completed (program saved).

---

### Days 25–26 — 🟨 CHOOSE: Level 3 BirdBrain Activity Menu (2 days)
**Roles swap each day.**

**Menu — pick 2 activities over 2 days:**

| Activity | Focus | Link |
|---|---|---|
| ShyBot | Distance sensor — retreats from proximity | [Link](https://learn.birdbraintechnologies.com/finch/projects/shybot-2) |
| CricketBot | Light sensor — behavior changes in light vs. dark | [Link](https://learn.birdbraintechnologies.com/finch/projects/cricketbot-2) |
| Emotional Finch | Variables storing state, sensor-triggered changes | [Link](https://learn.birdbraintechnologies.com/finch/projects/finch-emotions) |
| Reaction Time | Variables for timing, button detection, data | [Link](https://learn.birdbraintechnologies.com/finch/projects/reaction-time) |
| Simon Says I | Button conditionals, loops, LED/sound sequences | [Link](https://learn.birdbraintechnologies.com/finch/projects/simon-says-i-2) |
| SquirrelBot | Variables + conditionals + randomness, foraging | [Link](https://learn.birdbraintechnologies.com/finch/projects/squirrelbot-2) |

**Day 25:** Complete first activity. **Day 26:** Complete second + share-out (Recorder presents, Lead Engineer demos).

**📋 Team Journal #23:** (Day 25 Recorder) "Activity 1: what we chose, how it works, what code we wrote."

**📋 Team Journal #24:** (Day 26 Recorder) "Activity 2: what we chose, how it works. Compare the two activities — what CS concepts did they share?"

**✍️ Self Journal #8:** "Of the 6 activities on the menu, which one interested you the most (even if your team didn't pick it)? Why? What sensor and conditional logic would it require?"

**📋 Assignment:** Two BirdBrain activity programs (saved).

---
---

## Days 27–30: Sumo Competition 🤖

---

### Day 27 — 🟦 TEACH + BUILD: Sumo Strategy + Build Day 1
**Roles swap.**

**Teacher instruction (10 minutes):** Sumo strategy: search mode (spin + read distance), attack mode (charge when detected), recovery mode (opponent lost → search again).

**Student work (30 minutes):** Whole team collaborates on LEGO arms (max 15 cm total width). Lead Engineer starts coding strategy. Recorder sketches the design and documents the strategy logic.

**📋 Team Journal #25:** (Recorder) "Sketch our sumo robot design. Describe our strategy as if/else logic: what does the robot do when it detects the opponent? When it loses track?"

**📋 Assignment:** LEGO sumo build + strategy code (in progress).

---

### Day 28 — 🟩 PRACTICE: Sumo Build Day 2 + Testing
**Roles swap.**

Full work session. Finish building, refine code, test against other teams in the arenas.

**📋 Team Journal #26:** (Recorder) "What did we change after testing against another team? What worked? What failed? What's our plan for tomorrow's tournament?"

**📋 Assignment:** Completed sumo program (saved).

---

### Day 29 — 🟥 COMPETE: Sumo Tournament Round-Robin
**Roles swap. During bouts: Lead Engineer manages the robot start, Recorder tracks match results.**

Round-robin in both arenas. 90-second bouts. 30-second resets. Leaderboard.

**📋 Team Journal #27:** (Recorder) "Match-by-match results. Which opponents were hardest? What patterns did we notice in winning strategies?"

**📋 Assignment:** Tournament results recorded.

---

### Day 30 — 🟥 COMPETE: Sumo Finals + Debrief
**Roles swap.**

Top teams from each arena compete in cross-arena finals. Whole class watches.

**Post-tournament debrief (10 minutes):** "Which strategies won and why? What's the connection between better code and better results?"

**📋 Team Journal #28:** (Recorder) "What was the most effective strategy we saw? Break it down into code logic (if/else steps)."

**✍️ Self Journal #9:** "Think about your growth from the Finch Cup (keyboard control, Day 7) to Sumo (autonomous code, Day 30). What can your robot do now that it couldn't do then? What concepts made that possible?"

**📋 Assignment:** Sumo final reflection.

---
---

## Day 31: Line Following

---

### Day 31 — 🟦 TEACH + PRACTICE: Line Following
**Roles swap.**

**Teacher instruction (10 minutes):** IR sensors, dark = low value, light = high value. The algorithm: if left sensor on dark → turn left, if right sensor on dark → turn right, else → forward. Repeat forever.

**Student work (25 minutes):** Lead Engineer codes the algorithm. Recorder documents sensor values observed and tracks lap times.

**Leaderboard:** Timed laps for teams that complete the full loop.

**📋 Team Journal #29:** (Recorder) "Explain the line-following algorithm step by step. What sensor values trigger each action? Our best lap time: ___."

**📋 Assignment:** Line-following program (saved) + timed lap result.

---
---

## Days 32–33: Functions

---

### Day 32 — 🟦 TEACH: Functions Concept
**Roles swap.**

**Teacher instruction (15 minutes):** Create custom block `turn_around`, define it, use it 5 times. Create `wiggle`. Compose: `turn_around` → `wiggle` → `turn_around`. "Functions are named chunks of code. Write once, use anywhere."

**Student work (20 minutes):** Lead Engineer creates custom blocks. Recorder documents each function: name, what it does, and where it's used in the program.

**📋 Team Journal #30:** (Recorder) "List each custom block we created. For each: name, what it does (in plain English), and how many times we used it."

**📋 Assignment:** Custom block program (saved).

---

### Day 33 — 🟩 PRACTICE: Functions Challenge
**Roles swap.**

- Bronze: Create 2 custom blocks, compose into a 30-second routine
- Silver: Movement library — `draw_square`, `draw_triangle`, `draw_circle` as custom blocks. Compose a dance using all three.
- Gold: Parameterized block — `draw_polygon(sides)` takes number of sides as input

**📋 Team Journal #31:** (Recorder) "Which tier did we reach? Describe our custom blocks and how they connect to make the full program. How is this different from writing everything without functions?"

**✍️ Self Journal #10:** "Functions let you name and reuse code. Think about everyday life — what's something you do repeatedly that you could 'name as a function'? (Example: 'morning_routine' = wake up, brush teeth, eat, grab bag, leave.) Write 2–3 'life functions.'"

**📋 Assignment:** Functions challenge — highest tier (saved).

---
---

## Days 34–37: Capstone Project

---

### Day 34 — 🟩 PROJECT: Capstone Kickoff
**Roles swap.**

**Form teams. Choose from project menu. Plan on paper.**

| Project | Description | Minimum Requirements |
|---|---|---|
| Dance Routine | Choreograph a performance with movement, LEDs, sound, timing | Loop, variable, 2+ output types |
| Art Bot | Complex design using loops, variables, marker holder | Loop, variable, custom block |
| Obstacle Navigator | Navigate complex course autonomously using sensors | Conditional, loop, sensor |
| Sensor Game | Interactive game using Finch sensors | Conditional, variable, sensor, loop |
| Student-Designed | Must be approved by teacher | Conditional, loop, variable, 2+ sensors, 1 custom block |

**All teams must:** Write project plan in Team Journal. List CS concepts used. Get teacher sign-off before coding.

**📋 Team Journal #32:** (Recorder) "Project: ___. What the robot will do (step by step). CS concepts we'll use. Who is responsible for what."

**📋 Assignment:** Approved project plan.

---

### Day 35 — 🟩 PROJECT: Build Sprint 1
**Roles swap.**

Code core behavior. Test in arena. Log progress.

**📋 Team Journal #33:** (Recorder) "What we built today. What works. What doesn't yet. Plan for tomorrow."

**📋 Assignment:** Project code (in progress, saved).

---

### Day 36 — 🟩 PROJECT: Build Sprint 2 + Peer Review
**Roles swap.**

**First 20 minutes:** Continue building. **Last 20 minutes:** Peer review — swap with another team. Observers run the code. Identify one strength and one improvement.

**📋 Team Journal #34:** (Recorder) "Feedback we received: strength ___, improvement ___. What we'll change based on feedback."

**📋 Assignment:** Project code (near-final, saved) + peer review feedback.

---

### Day 37 — 🟥 SHOWCASE: Demos + Awards + Reflection 🎉
**Feature freeze (first 5 minutes).**

**Demos (20 minutes):** Each team presents (2 min + 1 question). Recorder introduces the project, Lead Engineer runs the demo, Associated Engineer (if trio) answers questions.

**Awards (5 minutes):** Best Code, Most Creative, Best Debug Story, Most Improved, Best Teamwork, Audience Favorite.

**Reflection (10 minutes):**

**📋 Team Journal #35 (Final):** (Recorder) "Our project summary. What we're most proud of as a team. One thing we'd improve."

**✍️ Self Journal #11 (Final):** "Compare what you could do on Day 1 to what you can build now. What concept was hardest to learn? What are you most proud of? What do you want to learn in 8th grade?"

**📋 Assignment:** Final project (saved) + presentation + both final journal entries.

---
---

# Summary

## Day-by-Day Map

| Day | Type | Activity | Team Journal | Self Journal |
|---|---|---|---|---|
| 1 | 🟦 INTRO | Welcome + culture | — | — |
| 2 | 🟦 INTRO | Routines + teams + journals | Setup | Setup |
| 3 | 🟦 TEACH | Meet Finch + Snap! | #1 | ✍️ #1 |
| 4 | 🟩 EXPLORE | Guided exploration | #2 | — |
| 5 | 🟩 EXPLORE | Free creation + share | #3 | — |
| 6 | 🟦 TEACH + BUILD | Keyboard control + Cup prep | #4 | — |
| 7 | 🟥 COMPETE | Finch Cup ⚽ | #5 | ✍️ #2 |
| 8 | 🟦 TEACH | Programmed movement | #6 | — |
| 9 | 🟩 PRACTICE | Jousting 🏇 | #7 | ✍️ #3 |
| 10 | 🟩 PRACTICE | Finding Speed | #8 | — |
| 11 | 🟦 TEACH | Loops concept | #9 | — |
| 12 | 🟩 PRACTICE | Drawing shapes (leveled) | #10 | — |
| 13 | 🟩 PRACTICE | Spirals + patterns | #11 | — |
| 14 | 🟦 TEACH | Variables + loops | #12 | ✍️ #4 |
| 15 | 🟩 PRACTICE | Patterns (Day 1) | #13 | — |
| 16 | 🟩 PRACTICE | Patterns (Day 2) | #14 | — |
| 17 | 🟩 PRACTICE | Patterns (Day 3) + Gallery 🎨 | #15 | ✍️ #5 |
| 18 | 🟦 TEACH | LED, sound, display | #16 | — |
| 19 | 🟩 PRACTICE | LED creative activity | #17 | — |
| 20 | 🟩 PRACTICE | Obstacle course practice | #18 | — |
| 21 | 🟥 COMPETE | Obstacle course competition | #19 | ✍️ #6 |
| 22 | 🟦 TEACH | Sensors | #20 | — |
| 23 | 🟦 TEACH | Conditionals | #21 | ✍️ #7 |
| 24 | 🟩 PRACTICE | Conditional challenges | #22 | — |
| 25 | 🟨 CHOOSE | Activity menu Day 1 | #23 | — |
| 26 | 🟨 CHOOSE | Activity menu Day 2 | #24 | ✍️ #8 |
| 27 | 🟦 TEACH + BUILD | Sumo build Day 1 | #25 | — |
| 28 | 🟩 PRACTICE | Sumo build Day 2 | #26 | — |
| 29 | 🟥 COMPETE | Sumo round-robin | #27 | — |
| 30 | 🟥 COMPETE | Sumo finals + debrief | #28 | ✍️ #9 |
| 31 | 🟦 TEACH + PRACTICE | Line following | #29 | — |
| 32 | 🟦 TEACH | Functions concept | #30 | — |
| 33 | 🟩 PRACTICE | Functions challenge | #31 | ✍️ #10 |
| 34 | 🟩 PROJECT | Capstone kickoff | #32 | — |
| 35 | 🟩 PROJECT | Build sprint 1 | #33 | — |
| 36 | 🟩 PROJECT | Build sprint 2 + review | #34 | — |
| 37 | 🟥 SHOWCASE | Demos + awards 🎉 | #35 | ✍️ #11 |

## Journal Counts

| Journal | Total Entries | Description |
|---|---|---|
| Team Engineering Journal | 35 entries | One per instructional day, written by that day's Recorder |
| Self Engineering Journal | 11 entries | At key reflection moments (marked ✍️), written by every student individually |

## Self Journal Reflection Schedule

| Entry | Day | Reflection Focus |
|---|---|---|
| ✍️ #1 | 3 | First impressions, role experience |
| ✍️ #2 | 7 | Finch Cup — driver vs. coach, learning from others |
| ✍️ #3 | 9 | Multiple solutions to same problem |
| ✍️ #4 | 14 | Explaining variables in own words |
| ✍️ #5 | 17 | Reading and analyzing another team's code |
| ✍️ #6 | 21 | Personal debugging process |
| ✍️ #7 | 23 | Conditionals in everyday life |
| ✍️ #8 | 26 | Activity menu choice and interest |
| ✍️ #9 | 30 | Growth: keyboard control to autonomous code |
| ✍️ #10 | 33 | Functions in everyday life |
| ✍️ #11 | 37 | Final course reflection and growth |
