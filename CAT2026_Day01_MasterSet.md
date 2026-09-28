# ☀️ CAT 2026 — DAY 1 MASTER SET
**Saturday, 26 September 2026 | ~60 Days to CAT 2026**
*Week 1 | Focus: Arithmetic + Seating/Distribution + Philosophy/Economics RC*

> 🎯 **Today's Mindset:** "The 99th percentile is not about being smarter — it is about being more consistent. Day 1 starts now."

---

# ═══════════════════════════════════════
# SECTION 0 — DAILY CAT BOOSTERS
# ═══════════════════════════════════════

## 0A. 📐 Formula of the Day — Weighted Average

**Formula:**
$$\text{Combined Average} = \frac{n_1 \cdot a_1 + n_2 \cdot a_2}{n_1 + n_2}$$

Where $n_1, n_2$ = group sizes, $a_1, a_2$ = respective averages.

**Derivation:** Total sum = $n_1 a_1 + n_2 a_2$. Divide by total count $(n_1 + n_2)$.

**Worked CAT-style Example:**
> Class A has 20 students with avg score 60. Class B has 30 students with avg score 80. Find combined average.

Combined avg = (20×60 + 30×80) / (20+30) = (1200 + 2400) / 50 = **3600/50 = 72**

⚠️ **The Trap:** Many students write (60+80)/2 = 70. WRONG — that ignores group sizes.

---

## 0B. ⚡ Shortcut of the Day — #1: Alligation Cross Method

**Rule:** When two quantities with values C₁ and C₂ are mixed to give mean value M:
```
C₁          C₂
    \      /
      M
    /      \
(C₂−M) : (M−C₁)   ← ratio of quantities
```

**Conventional Method (1 min 30 sec):** Set up equations, solve for ratio.

**Alligation Method (20 sec):**

**Sample Problem:** Milk worth ₹16/litre is mixed with milk worth ₹25/litre to get a mixture worth ₹19/litre. Find the ratio.

```
16          25
    \      /
      19
    /      \
 (25−19):(19−16)
   6   :   3   = 2:1
```
**Answer: 2:1** | Time saved: ~70 seconds vs conventional method.

---

## 0C. ⏱️ Speed Drill — 60 Seconds | Solve All 5

*Start your timer NOW. Write answers before moving on.*

**SD1.** 15% of 480 = ?

**SD2.** Average of 11, 13, 15, 17, 19 = ?

**SD3.** If A:B = 3:5 and B:C = 4:7, find A:C.

**SD4.** 125 × 96 = ?

**SD5.** A sum doubles in 10 years at Simple Interest. What is the rate of interest?

*(Answers at the very bottom of this document)*

---

## 0D. 📚 Vocabulary of the Day — 5 High-Frequency CAT RC Words

| Word | Meaning | Antonym | Usage in RC Context |
|------|---------|---------|---------------------|
| **Empirical** | Based on observation/experience | Theoretical | *"The empirical evidence contradicted the long-held theoretical model."* |
| **Hegemony** | Dominance/leadership of one group over others | Subservience | *"American cultural hegemony reshaped global consumer patterns in the 20th century."* |
| **Epistemology** | Study of knowledge — what we know and how | — | *"The passage questions the epistemological foundations of modern science."* |
| **Utilitarian** | Focused on maximum benefit for maximum people | Idealistic | *"A utilitarian argument for the policy ignores minority rights."* |
| **Dialectic** | Logical debate between opposing ideas | Consensus | *"Hegel's dialectic — thesis, antithesis, synthesis — drives his philosophy of history."* |

---

## 0E. ♻️ Shortcut Warm-Up — 3 Shortcuts Revised

**Warm-Up 1 — Shortcut: Percentage ↔ Fraction Conversion**
> Rule: 12.5% = 1/8, 16.67% = 1/6, 33.33% = 1/3, 37.5% = 3/8, 62.5% = 5/8

**Your Problem:** A shopkeeper increases the price by 33.33% and then gives a discount of 25%. What is the net change in price?

**Warm-Up 2 — Shortcut: Ratio Combination**
> If A:B = m:n and B:C = p:q, then A:B:C = mp : np : nq

**Your Problem:** If P:Q = 2:3 and Q:R = 5:6, find P:R.

**Warm-Up 3 — Shortcut: Consecutive Integers Average**
> Average of n consecutive integers = middle term (if n is odd) = mean of first and last (always)

**Your Problem:** The average of 9 consecutive integers is 25. What is the largest integer?

*(Warm-Up Answers at the very bottom of this document)*

---

## 0F. 🧠 Concept of the Day — The "Average of Averages" Trap

**The Trap:** You CANNOT find the combined average by averaging two averages unless group sizes are equal.

**Classic CAT Mistake:**
> Team 1 (5 players) avg score = 40. Team 2 (8 players) avg score = 55.
> **Wrong:** Combined avg = (40+55)/2 = 47.5
> **Right:** (5×40 + 8×55) / 13 = (200+440)/13 = **49.2**

**Why CAT Loves This:** It appears in Profit/Loss (overall profit%), TSD (average speed), and Data Interpretation sets. The answer 47.5 is always provided as a trap option.

**The Fix:** Always identify group sizes before averaging. If not given, suspect a trick.

---

---

# ═══════════════════════════════════════
# SECTION 1 — QUANTITATIVE APTITUDE
# 22 Questions | 40 Minutes
# Week 1: Arithmetic + Number System
# ═══════════════════════════════════════

---

### 📦 BLOCK A — AVERAGES (5 Questions)

---

**Q1.**
Source: CAT 2018 Slot 1 | Topic: Averages | Type: MCQ | Difficulty: ★★★ | ~85th %ile | Time: 75 sec | 🟢 Must Attempt

The average of 5 consecutive integers starting with *m* is *n*. What is the average of 9 consecutive integers starting with *m* + 2?

(A) n + 3
(B) n + 4
(C) n + 5
(D) n + 6

⚡ **Shortcut Hint:** Average of consecutive integers = middle term. Find the new middle term in terms of n.
🚨 **Watch Out:** Don't confuse "starts with m+2" — the sequence shifts by 2, and you need 9 terms, so middle term shifts by more than 2.

---

**Q2.**
Source: CAT-Level Inspired | Topic: Averages | Type: TITA | Difficulty: ★★★★ | ~90th %ile | Time: 2 min | 🟡 Attempt Later

The average marks of 32 students in a class is 56. When the top scorer (who scored 92) and the bottom scorer are removed, the average of the remaining 30 students drops to 54. Find the marks of the bottom scorer.

⚡ **Shortcut Hint:** Use: Top + Bottom = Total sum − Reduced sum. One value is given; find the other.
🚨 **Watch Out:** Average DROPS after removal — that means the two removed students together pulled the average UP. Verify your sign.

---

**Q3.**
Source: CAT-Level Inspired | Topic: Averages | Type: MCQ | Difficulty: ★★★ | ~80th %ile | Time: 90 sec | 🟢 Must Attempt

A batsman's average after 16 innings is 38. In the 17th inning, he scores 72 runs. His average after the 17th inning is:

(A) 40
(B) 41
(C) 42
(D) 43

⚡ **Shortcut Hint:** New avg = Old avg + (New score − Old avg)/New number of innings.
🚨 **Watch Out:** Don't recalculate the full sum — use the shortcut formula directly.

---

**Q4.**
Source: CAT 2020 Slot 2 | Topic: Averages | Type: MCQ | Difficulty: ★★★★ | ~92nd %ile | Time: 2 min | 🟡 Attempt Later

In a group of 10 students, the mean of the lowest 9 scores is 42 while the mean of the highest 9 scores is 47. If the mean of all 10 scores is 45, then the difference between the highest and lowest score is:

(A) 5
(B) 10
(C) 13
(D) 15

⚡ **Shortcut Hint:** Let lowest = L, highest = H. Write two equations using given means. Eliminate middle 8 scores.
🚨 **Watch Out:** "Lowest 9" excludes the highest. "Highest 9" excludes the lowest. Don't mix them up.

---

**Q5.**
Source: CAT-Level Inspired | Topic: Averages/Mixtures | Type: TITA | Difficulty: ★★★★★ | ~97th %ile | Time: 2.5 min | 🔴 Skip Round 1

The average age of a group of 12 boys and 16 girls is 21.5 years. If the average age of the boys is 2 years more than that of the girls, find the average age of the girls.

⚡ **Shortcut Hint:** Let girl avg = g. Boy avg = g+2. Set up weighted average equation. One unknown.
🚨 **Watch Out:** Assign correct group sizes — 12 boys, 16 girls. Easy to flip them under time pressure.

---

### 📦 BLOCK B — RATIO, PROPORTION & PERCENTAGES (6 Questions)

---

**Q6.**
Source: CAT 2019 Slot 1 | Topic: Ratios | Type: MCQ | Difficulty: ★★★ | ~82nd %ile | Time: 90 sec | 🟢 Must Attempt

Two numbers are in the ratio 3:5. If 9 is subtracted from each, they are in the ratio 12:23. What is the smaller number?

(A) 27
(B) 33
(C) 36
(D) 42

⚡ **Shortcut Hint:** Let the numbers be 3k and 5k. Form one equation from the second condition and solve for k.
🚨 **Watch Out:** "Smaller number" — after finding k, return 3k not 5k.

---

**Q7.**
Source: CAT-Level Inspired | Topic: Percentages | Type: MCQ | Difficulty: ★★★ | ~80th %ile | Time: 90 sec | 🟢 Must Attempt

The price of an article is increased by 20% and then decreased by 20%. The net change in price is:

(A) 0%
(B) +4%
(C) −4%
(D) −2%

⚡ **Shortcut Hint:** Net effect of x% up then x% down = −x²/100 %. Here x=20, so −400/100 = −4%.
🚨 **Watch Out:** Many students say "no change" (0%) — that is the trap answer. Always net change = negative.

---

**Q8.**
Source: CAT 2021 Slot 1 | Topic: Percentages | Type: TITA | Difficulty: ★★★★ | ~91st %ile | Time: 2 min | 🟡 Attempt Later

Arun's monthly salary is ₹24,000. He spends 40% on rent, 25% of the remaining on food, and 20% of what is left on transport. What percentage of his salary does he save?

⚡ **Shortcut Hint:** Work with fractions of the original. Remaining after each step = multiply successive fractions.
🚨 **Watch Out:** "25% of the remaining" is NOT 25% of the original. Each percentage applies to the running balance.

---

**Q9.**
Source: CAT-Level Inspired | Topic: Profit & Loss | Type: MCQ | Difficulty: ★★★★ | ~88th %ile | Time: 2 min | 🟡 Attempt Later

A trader marks up goods by 40% and then gives a discount of 25%. Find the overall profit or loss percentage.

(A) 5% profit
(B) 5% loss
(C) 10% profit
(D) No profit, no loss

⚡ **Shortcut Hint:** Net multiplier = 1.40 × 0.75. No need to assume CP.
🚨 **Watch Out:** Markup is on Cost Price; Discount is on Marked Price — do NOT add/subtract percentages directly.

---

**Q10.**
Source: CAT 2022 Slot 2 | Topic: Ratios | Type: TITA | Difficulty: ★★★★ | ~90th %ile | Time: 2 min | 🟡 Attempt Later

The ratio of A's salary to B's salary is 4:3. A's salary is increased by 25% and B's salary is increased by ₹2,000. After the increments, their salaries are equal. What was A's original salary?

⚡ **Shortcut Hint:** Let A = 4k, B = 3k. After increment: 4k × 1.25 = 3k + 2000. Solve for k.
🚨 **Watch Out:** "Equal after increments" — set up the equation correctly before computing.

---

**Q11.**
Source: CAT-Level Inspired | Topic: Percentages | Type: MCQ | Difficulty: ★★★★★ | ~96th %ile | Time: 2.5 min | 🔴 Skip Round 1

In an election, 80% of eligible voters voted. Of those who voted, 60% voted for Candidate A and the rest for Candidate B. Candidate A won by 2,400 votes. How many eligible voters were there?

(A) 25,000
(B) 30,000
(C) 36,000
(D) 40,000

⚡ **Shortcut Hint:** Express everything in terms of total eligible voters N. Margin = 20% of 80% of N = 0.16N = 2400.
🚨 **Watch Out:** The margin is the DIFFERENCE in votes, not just A's votes. 60% vs 40% → margin = 20% of voters who voted.

---

### 📦 BLOCK C — TIME, SPEED & DISTANCE + TIME & WORK (5 Questions)

---

**Q12.**
Source: CAT 2019 Slot 2 | Topic: Time, Speed & Distance | Type: MCQ | Difficulty: ★★★ | ~83rd %ile | Time: 90 sec | 🟢 Must Attempt

A train 200 m long crosses a platform 300 m long at a speed of 50 m/s. How long does it take to cross the platform completely?

(A) 8 sec
(B) 10 sec
(C) 12 sec
(D) 14 sec

⚡ **Shortcut Hint:** Distance = Length of train + Length of platform. Time = Total distance / Speed.
🚨 **Watch Out:** Don't use only the platform length or only the train length — you need the SUM.

---

**Q13.**
Source: CAT-Level Inspired | Topic: TSD — Boats & Streams | Type: TITA | Difficulty: ★★★★ | ~89th %ile | Time: 2 min | 🟡 Attempt Later

A boat goes 30 km upstream in 6 hours and 30 km downstream in 3 hours. What is the speed of the current?

⚡ **Shortcut Hint:** Speed upstream = 30/6 = 5 km/h; downstream = 30/3 = 10 km/h. Current = (downstream − upstream)/2.
🚨 **Watch Out:** Current = (D−U)/2, NOT (D+U)/2. That formula gives the boat's speed in still water.

---

**Q14.**
Source: CAT 2017 Slot 2 | Topic: Time & Work | Type: MCQ | Difficulty: ★★★★ | ~88th %ile | Time: 2 min | 🟡 Attempt Later

A and B together can complete a work in 12 days. B and C together in 15 days. A and C together in 20 days. In how many days can A, B, and C together complete the work?

(A) 8
(B) 10
(C) 12
(D) 16

⚡ **Shortcut Hint:** (A+B) + (B+C) + (A+C) = 2(A+B+C). Find combined rate, then time for all three.
🚨 **Watch Out:** The sum gives 2 × (A+B+C)'s work rate, not 1× . Divide by 2 after adding.

---

**Q15.**
Source: CAT-Level Inspired | Topic: Time & Work | Type: TITA | Difficulty: ★★★★ | ~90th %ile | Time: 2 min | 🟡 Attempt Later

Pipe A can fill a tank in 12 hours. Pipe B can empty it in 18 hours. If both are opened together when the tank is 1/3 full, how many hours will it take to fill the tank completely?

⚡ **Shortcut Hint:** Net fill rate = 1/12 − 1/18 = 1/36 per hour. Remaining = 2/3 of tank.
🚨 **Watch Out:** Don't forget the tank starts at 1/3 full — only 2/3 remains to be filled, not the full tank.

---

**Q16.**
Source: CAT 2021 Slot 3 | Topic: TSD — Relative Speed | Type: MCQ | Difficulty: ★★★★★ | ~95th %ile | Time: 2.5 min | 🔴 Skip Round 1

Two cars A and B start simultaneously from towns P and Q respectively towards each other. After meeting, A takes 4 more hours and B takes 9 more hours to reach their destinations. What is the ratio of speeds of A to B?

(A) 2:3
(B) 3:2
(C) 4:9
(D) 9:4

⚡ **Shortcut Hint:** Classic result: Speed ratio = √(time of B after meeting) : √(time of A after meeting) = √9:√4 = 3:2.
🚨 **Watch Out:** Speed ratio uses SQUARE ROOT of times — most common error is writing 4:9 directly.

---

### 📦 BLOCK D — NUMBER SYSTEM (4 Questions)

---

**Q17.**
Source: CAT 2019 Slot 1 | Topic: Remainders | Type: TITA | Difficulty: ★★★★ | ~90th %ile | Time: 2 min | 🟡 Attempt Later

What is the remainder when $4^{96}$ is divided by 6?

⚡ **Shortcut Hint:** Find pattern of 4^n mod 6: 4¹=4, 4²=16→4, 4³→4... Cyclicity = 1.
🚨 **Watch Out:** Don't apply Euler's theorem blindly — check if gcd(4,6)=1 first. It's not 1 here. Use pattern instead.

---

**Q18.**
Source: CAT-Level Inspired | Topic: Factors | Type: MCQ | Difficulty: ★★★★ | ~88th %ile | Time: 90 sec | 🟡 Attempt Later

How many factors does 1080 have?

(A) 30
(B) 32
(C) 36
(D) 40

⚡ **Shortcut Hint:** 1080 = 2³ × 3³ × 5. Number of factors = (3+1)(3+1)(1+1).
🚨 **Watch Out:** Include 1 and the number itself. The formula (a+1)(b+1)... already accounts for them.

---

**Q19.**
Source: CAT 2020 Slot 1 | Topic: HCF & LCM | Type: MCQ | Difficulty: ★★★ | ~82nd %ile | Time: 90 sec | 🟢 Must Attempt

The HCF of two numbers is 12 and their LCM is 180. If one number is 36, what is the other?

(A) 48
(B) 54
(C) 60
(D) 72

⚡ **Shortcut Hint:** Product of numbers = HCF × LCM. Other number = (12 × 180) / 36.
🚨 **Watch Out:** This formula works ONLY for two numbers. For three or more numbers, it does NOT hold.

---

**Q20.**
Source: CAT-Level Inspired | Topic: Factorials & Trailing Zeros | Type: TITA | Difficulty: ★★★★★ | ~95th %ile | Time: 2 min | 🔴 Skip Round 1

Find the highest power of 5 in 100!

⚡ **Shortcut Hint:** Use Legendre's formula: ⌊100/5⌋ + ⌊100/25⌋ + ⌊100/125⌋ = 20 + 4 + 0.
🚨 **Watch Out:** Don't stop at ⌊100/5⌋=20. Keep dividing by higher powers of 5 until the quotient = 0.

---

### 📦 BLOCK E — ALGEBRA BASICS (2 Questions)

---

**Q21.**
Source: CAT 2022 Slot 1 | Topic: Quadratic Equations | Type: MCQ | Difficulty: ★★★★ | ~90th %ile | Time: 2 min | 🟡 Attempt Later

If α and β are roots of x² − 7x + k = 0 and α − β = 1, find the value of k.

(A) 10
(B) 12
(C) 13
(D) 15

⚡ **Shortcut Hint:** Use Vieta's: α+β=7, α−β=1 → find α,β → k = α×β.
🚨 **Watch Out:** Vieta's gives SUM and PRODUCT of roots. Don't confuse product with sum.

---

**Q22.**
Source: CAT-Level Inspired | Topic: Inequalities | Type: TITA | Difficulty: ★★★★★ | ~97th %ile | Time: 2.5 min | 🔴 Skip Round 1

How many integer values of x satisfy: $\frac{x^2 - 5x + 6}{x - 4} < 0$?

⚡ **Shortcut Hint:** Factorise numerator: (x−2)(x−3). Critical points: x=2, 3, 4. Use wavy curve / sign chart.
🚨 **Watch Out:** x=4 is excluded (denominator = 0). Also count only INTEGER values in the valid range.

---

---

# ═══════════════════════════════════════
# SECTION 2 — DILR
# 4 Sets | ~20 Questions | 40 Minutes
# Week 1: Seating + Distribution + DI
# ═══════════════════════════════════════

---

## SET 1 — Linear Seating Arrangement

🕐 **Time Budget:** 8–10 minutes
🏁 **Entry Signal:** Attempt this set if you can place at least 2 people from the clues within 90 seconds — else skip and return.
⚡ **Set Strategy:** Draw a row of 8 seats. Start with ABSOLUTE clues (fixed positions). Then use relative clues. Box unknown positions and revisit.

**Source:** CAT-Level Inspired | Difficulty: ★★★★ | ~88th %ile

---

**Setup:**
Eight people — A, B, C, D, E, F, G, H — are sitting in a straight row of 8 seats, all facing north.

**Clues:**
1. A is at one of the ends.
2. There are exactly 3 people between A and E.
3. B sits immediately to the right of E.
4. C and D are adjacent to each other.
5. F is not adjacent to A.
6. G sits exactly 2 seats to the left of H.
7. Neither C nor D is at any end.

**S1.1** Who sits at the other end (not A)?
(A) B  (B) F  (C) G  (D) H

**S1.2** How many people sit between B and H?
(A) 1  (B) 2  (C) 3  (D) 4

**S1.3** Which of the following pairs is definitely adjacent?
(A) A and G  (B) F and G  (C) E and G  (D) B and H

**S1.4** If F sits at position 6, who sits at position 3?
(A) C  (B) D  (C) G  (D) H

---

## SET 2 — Distribution/Allocation Set

🕐 **Time Budget:** 9–11 minutes
🏁 **Entry Signal:** Attempt if you can identify at least one person's complete allocation from clue 1 alone within 90 sec.
⚡ **Set Strategy:** Make a grid: Rows = People, Columns = attributes (subject, floor, score etc). Fill definites first. Use elimination for the rest. Never assume — only deduce.

**Source:** CAT-Level Inspired | Difficulty: ★★★★ | ~90th %ile

---

**Setup:**
Five students — P, Q, R, S, T — each scored different marks in a test: 45, 55, 62, 71, 88 (not necessarily in this order). Each belongs to one of five cities: Delhi, Mumbai, Pune, Chennai, Kolkata.

**Clues:**
1. P scored more than Q but less than R.
2. The student from Delhi scored 88.
3. T is from Mumbai and scored less than S.
4. Q is from Pune.
5. R scored 71. S scored more than 62.
6. The student from Chennai scored 45.

**S2.1** Who scored 88?
(A) R  (B) S  (C) T  (D) Cannot be determined

**S2.2** Who is from Chennai?
(A) P  (B) Q  (C) T  (D) S

**S2.3** What did P score?
(A) 45  (B) 55  (C) 62  (D) 71

**S2.4** Which city is S from?
(A) Delhi  (B) Chennai  (C) Kolkata  (D) Mumbai

---

## SET 3 — Data Interpretation (Table)

🕐 **Time Budget:** 7–8 minutes
🏁 **Entry Signal:** Attempt if you can compute at least one row value in under 60 seconds — numbers should be simple.
⚡ **Set Strategy:** Read ALL questions BEFORE touching the table. Some questions use 1–2 columns only. Calculate only what's needed — don't pre-compute entire table.

**Source:** CAT-Level Inspired | Difficulty: ★★★ | ~82nd %ile

---

**Setup:**
The table below shows the number of students enrolled in 5 courses (A–E) across 3 years at a college.

| Course | 2022 | 2023 | 2024 |
|--------|------|------|------|
| A | 120 | 150 | 180 |
| B | 80 | 100 | 90 |
| C | 60 | 90 | 120 |
| D | 200 | 180 | 160 |
| E | 40 | 60 | 100 |

**S3.1** In 2024, which course saw the highest percentage increase compared to 2022?
(A) A  (B) C  (C) E  (D) B

**S3.2** What is the total enrolment across all courses in 2023?
(A) 560  (B) 580  (C) 600  (D) 620

**S3.3** The percentage decrease in Course D's enrolment from 2022 to 2024 is:
(A) 15%  (B) 20%  (C) 25%  (D) 30%

**S3.4** In which year was the combined enrolment of Courses A and E the maximum?
(A) 2022  (B) 2023  (C) 2024  (D) Equal in 2023 and 2024

---

## SET 4 — Games & Tournaments (Round Robin)

🕐 **Time Budget:** 9–11 minutes
🏁 **Entry Signal:** Attempt only if you enjoy tournament sets. If you haven't practiced this type, skip and return only after completing Sets 1–3.
⚡ **Set Strategy:** In a Round Robin of n teams: Total matches = n(n−1)/2. Points: Win=2, Draw=1, Loss=0 (or Win=3 as given). Build a points table. Use given total to cross-check consistency.

**Source:** CAT-Level Inspired | Difficulty: ★★★★★ | ~95th %ile

---

**Setup:**
Five teams — Falcons, Hawks, Eagles, Kites, Owls — played a round-robin tournament. Each pair played exactly once. Win = 2 points, Loss = 0, No draws occurred.

**Clues:**
1. Falcons won all their matches.
2. Owls lost all their matches.
3. Eagles beat Hawks and Kites.
4. Hawks beat Kites.
5. Total points of all teams combined = 20.

**S4.1** How many matches did Eagles win in total?
(A) 2  (B) 3  (C) 4  (D) Cannot be determined

**S4.2** What are the total points of Hawks?
(A) 2  (B) 4  (C) 6  (D) 8

**S4.3** Which team finished second in the points table?
(A) Hawks  (B) Eagles  (C) Kites  (D) Cannot be determined

**S4.4** If the top 2 teams advance to the finals, which pair plays the final?
(A) Falcons and Eagles  (B) Falcons and Hawks  (C) Falcons and Eagles or Hawks  (D) Cannot be determined

---

---

# ═══════════════════════════════════════
# SECTION 3 — VARC
# 2 RC Passages + 6 VA Questions
# Week 1: Philosophy + Economics RC
# ═══════════════════════════════════════

---

## 📖 RC PASSAGE 1 — Philosophy

⚡ **RC Approach:**
- **Tone:** Academic, analytical — the author is arguing a position, not just describing.
- **Structure:** Look for the central claim in paragraph 1 or 2. Each subsequent paragraph either supports or qualifies it.
- **Watch For:** The author likely distinguishes between two philosophical positions. Questions will test whether you understood the distinction correctly.

---

**Source:** CAT-Level Inspired | Difficulty: ★★★★ | ~90th %ile

---

The question of whether moral knowledge is possible has occupied philosophers since antiquity. At its heart, the debate concerns the status of moral judgments — are they objective truths that we discover, much like mathematical truths, or are they merely expressions of subjective preference, with no more claim to universality than a preference for vanilla over chocolate?

The objectivist tradition, represented by thinkers such as Plato and later G.E. Moore, holds that certain moral propositions — "cruelty is wrong," "justice is good" — are true independently of what any individual or culture believes. On this view, moral knowledge is possible precisely because its objects exist independently of the knower. Critics, however, argue that this account is mysterious: it requires us to posit a realm of abstract moral facts without explaining how human beings, as physical creatures, come to know them.

Emotivists like A.J. Ayer took the opposite extreme. For Ayer, moral statements are not truth-apt at all. When I say "cruelty is wrong," I am not describing a fact — I am merely expressing a feeling of disapproval. On this view, moral "knowledge" is a category error: there is nothing to know, only feelings to have. This elegantly dissolves the epistemological problem but at a severe cost: it makes moral reasoning appear groundless and reduces ethical discourse to a clash of non-rational attitudes.

Contemporary philosophers have sought a middle path. Constructivists like John Rawls and Christine Korsgaard argue that moral norms, while not discovered in a Platonic realm, are neither arbitrary. They are constructed through processes of rational reflection and agreement among agents who share certain commitments. This view preserves the intersubjective authority of morality without requiring mysterious metaphysical entities.

The debate is far from settled. But what emerges clearly is that the choice between moral objectivism and subjectivism is not forced. The space between blind moral realism and relativistic emotivism is wider — and more philosophically inhabitable — than either extreme suggests.

---

**RC1.1** | Type: MCQ | Difficulty: ★★★ | ~82nd %ile | 🟢 Must Attempt
What is the primary purpose of the passage?

(A) To argue conclusively in favour of constructivism over both objectivism and emotivism
(B) To show that the debate between moral objectivism and subjectivism is unresolvable
(C) To map the philosophical terrain between moral objectivism and subjectivism and suggest a middle ground exists
(D) To critique emotivism as philosophically incoherent

⚡ **RC Hint:** The last paragraph is the key. The author doesn't pick a winner — they assert a "middle path" is inhabitable. Look for the option that matches "survey + middle ground."

---

**RC1.2** | Type: MCQ | Difficulty: ★★★★ | ~90th %ile | 🟡 Attempt Later
The author mentions G.E. Moore and Plato primarily to:

(A) endorse their position as the most philosophically defensible
(B) illustrate the objectivist tradition as examples of those who believe moral facts exist independently
(C) contrast them with Ayer's emotivist position regarding the nature of moral statements
(D) demonstrate that ancient philosophy is more reliable than modern moral theory

⚡ **RC Hint:** Always ask — *why does the author introduce these names?* They are examples serving a purpose. Find what that purpose is in the sentence that introduces them.

---

**RC1.3** | Type: MCQ | Difficulty: ★★★★ | ~88th %ile | 🟡 Attempt Later
According to the passage, Ayer's emotivism "dissolves the epistemological problem" but at a "severe cost." What is that cost?

(A) It cannot explain how physical creatures can know abstract moral facts
(B) It requires positing a mysterious Platonic realm of moral entities
(C) It makes moral reasoning appear groundless and reduces ethics to non-rational attitudes
(D) It fails to distinguish between objective and subjective moral claims

⚡ **RC Hint:** The answer is directly stated in paragraph 3. Scan for "severe cost" in the passage — the author explicitly names it.

---

**RC1.4** | Type: MCQ | Difficulty: ★★★★★ | ~95th %ile | 🔴 Skip Round 1
Which of the following is most analogous to the constructivist position as described in the passage?

(A) Mathematical truths are discovered by the human mind, not created by it
(B) Legal norms are created through legislative processes but have binding authority once established
(C) Aesthetic judgments are entirely personal and cannot be disputed
(D) Scientific facts exist independently of scientific communities but are progressively uncovered

⚡ **RC Hint:** Constructivism = norms not "discovered" in a Platonic realm, not arbitrary either — constructed through rational reflection. Find the option that matches this pattern (constructed through process, yet authoritative).

---

## 📖 RC PASSAGE 2 — Economics

⚡ **RC Approach:**
- **Tone:** Analytical, mildly critical. Author is examining a concept with some scepticism.
- **Structure:** Problem introduced → standard explanation offered → limitation of that explanation → nuanced take.
- **Watch For:** The author likely challenges a widely held economic assumption. Questions will test whether you track the author's critique accurately.

---

**Source:** CAT-Level Inspired | Difficulty: ★★★★ | ~88th %ile

---

The concept of rational economic man — homo economicus — has been the cornerstone of classical economic theory for two centuries. This idealized agent is assumed to have stable, well-defined preferences, access to all relevant information, and the cognitive capacity to process that information and maximize utility. Economic models built on these assumptions have generated remarkable predictive and analytical tools. Yet the rational actor model has attracted sustained criticism from behavioural economists, psychologists, and sociologists who argue that real human behaviour deviates systematically and predictably from its prescriptions.

Daniel Kahneman and Amos Tversky's foundational research demonstrated that people are not probability calculators. They rely on cognitive shortcuts — heuristics — that work well in familiar situations but generate systematic errors in complex or unfamiliar ones. Loss aversion, the tendency to feel losses more acutely than equivalent gains, and anchoring, the tendency to be disproportionately influenced by the first piece of information encountered, are among the best-documented deviations. Critically, these are not random errors that average out; they are consistent, directional biases.

Defenders of the rational actor model respond with two arguments. First, they contend that while individuals may err, markets aggregate behaviour efficiently, correcting individual mistakes through competition and arbitrage. Second, they invoke the "as if" defence: even if people don't literally maximize utility, they behave "as if" they do, making the model a useful approximation. Neither response is fully satisfying. Market aggregation fails precisely when biases are systematic and widespread — as demonstrated by speculative bubbles. And the "as if" defence makes the model unfalsifiable: any behaviour can be post-hoc rationalized as maximizing some utility function.

What is needed is not a wholesale rejection of rationality as a modelling tool, but its calibration. Models that incorporate bounded rationality — acknowledging cognitive limits — and predictable irrationality can retain analytical rigour while better describing and predicting human economic behaviour.

---

**RC2.1** | Type: MCQ | Difficulty: ★★★ | ~80th %ile | 🟢 Must Attempt
The author's attitude towards the rational actor model is best described as:

(A) Strongly supportive — it remains the most reliable framework for economics
(B) Mildly critical — it has value but needs to be calibrated with insights from behavioural economics
(C) Dismissive — it should be abandoned in favour of behavioural models
(D) Neutral — the passage merely describes both sides without taking a position

⚡ **RC Hint:** Author tone is in the last paragraph. "Not a wholesale rejection" + "calibration needed" = mild criticism, not dismissal. Look for the option that captures this nuance.

---

**RC2.2** | Type: MCQ | Difficulty: ★★★★ | ~90th %ile | 🟡 Attempt Later
According to the passage, why is the "as if" defence insufficient?

(A) Because people demonstrably do not maximize utility in laboratory experiments
(B) Because it makes the model unfalsifiable — any behaviour can be rationalized as maximizing utility
(C) Because market aggregation also fails to correct individual biases
(D) Because heuristics generate random, not directional, errors

⚡ **RC Hint:** The answer is directly stated in paragraph 3. Find the sentence containing "as if" and what follows it.

---

**RC2.3** | Type: MCQ | Difficulty: ★★★★ | ~88th %ile | 🟡 Attempt Later
The author cites "speculative bubbles" as evidence that:

(A) rational actors sometimes fail to predict market outcomes
(B) individual cognitive biases can be corrected through market arbitrage
(C) market aggregation fails when biases are systematic and widespread
(D) behavioural economics cannot explain macro-level phenomena

⚡ **RC Hint:** Speculative bubbles are cited to refute the "market aggregation corrects errors" argument. Track the logical chain in paragraph 3.

---

**RC2.4** | Type: MCQ | Difficulty: ★★★★★ | ~95th %ile | 🔴 Skip Round 1
Which of the following would the author most likely agree with?

(A) Kahneman and Tversky's research proves that human beings are fundamentally irrational and cannot make good decisions
(B) Economic models should be built entirely on sociological observations rather than mathematical frameworks
(C) A refined model incorporating bounded rationality would be more descriptively accurate than the classic homo economicus model
(D) The debate between rational actor theorists and behavioural economists is purely academic with no policy implications

⚡ **RC Hint:** The author's conclusion (last para) is the direct source. Find what the author proposes as the solution — that is what they would agree with.

---

## ✍️ VERBAL ABILITY — 6 Questions

---

**VA1 — Para Summary**
Source: CAT-Level Inspired | Type: MCQ | Difficulty: ★★★ | ~80th %ile | 🟢 Must Attempt

*"Language is not merely a tool for communication — it is the very medium through which thought is organised and expressed. Without language, abstract reasoning would be impossible: we could not classify, compare, or analyse beyond immediate sensory experience. Far from being a neutral vehicle for pre-existing ideas, language shapes and constrains the concepts available to us, making some thoughts easier and others nearly impossible to formulate."*

Which of the following best summarises the above paragraph?

(A) Language is a communication tool that humans have developed over millennia.
(B) Abstract thought is impossible without the structures and constraints that language provides.
(C) Language both enables and limits thought, being more than a neutral medium of communication.
(D) Without language, human beings could not interact with one another socially.

⚡ **VA Hint:** Para Summary = the MOST COMPLETE option that captures ALL the author's points without adding new ideas. Eliminate options that are too narrow (cover only part) or too broad (go beyond the passage).

---

**VA2 — Para Summary**
Source: CAT-Level Inspired | Type: MCQ | Difficulty: ★★★★ | ~88th %ile | 🟡 Attempt Later

*"Urbanisation brings prosperity — that is the conventional wisdom. Yet studies increasingly suggest that rapid, unplanned urbanisation generates more poverty than it alleviates. Migrant workers who flood into megacities often find themselves in informal settlements without access to basic services. Far from escaping rural poverty, they encounter a different, often harsher, form of deprivation. The city, in these cases, is not a poverty trap — it is a poverty transfer mechanism."*

Which of the following best summarises the above paragraph?

(A) Cities are the engines of economic growth in developing nations.
(B) Migrants who move to cities are generally worse off than they were in rural areas.
(C) Unplanned urbanisation may redistribute rather than reduce poverty, contradicting the conventional view.
(D) Governments should prevent rural-to-urban migration to protect the urban poor.

⚡ **VA Hint:** Watch for the author's twist on conventional wisdom. The summary must reflect BOTH the conventional view AND the author's critique of it.

---

**VA3 — Para Jumble**
Source: CAT-Level Inspired | Type: TITA | Difficulty: ★★★★ | ~88th %ile | 🟡 Attempt Later

*Arrange the following sentences into a coherent paragraph. Enter only the correct sequence (e.g., DACB).*

**A.** This is not merely a technical oversight — it reflects a deeper assumption that women's experiences are a deviation from a universal human norm.
**B.** Medical research has historically used male subjects as the default, from drug trials to anatomical studies.
**C.** As a result, dosages, diagnostic criteria, and treatment protocols developed from this research are often poorly calibrated for women.
**D.** The consequences for women's health have been significant, ranging from under-diagnosis of heart disease to adverse drug reactions.

⚡ **VA Hint:** Find the OPENING sentence (must be self-contained, no pronoun reference that dangles). Then find logical chains: cause → effect. "This" in A must refer to something stated before.

---

**VA4 — Para Jumble**
Source: CAT 2019 Slot 2 (Inspired) | Type: TITA | Difficulty: ★★★★★ | ~94th %ile | 🔴 Skip Round 1

*Arrange into coherent paragraph:*

**A.** Yet the standard account of scientific progress as linear accumulation of knowledge misrepresents how science actually works.
**B.** Thomas Kuhn's concept of paradigm shifts captured this: science advances not by smoothly building on the past, but through revolutionary breaks.
**C.** Science is widely regarded as the most reliable method humanity has for generating knowledge about the natural world.
**D.** Old frameworks are not refined — they are overturned, and the very questions asked change fundamentally.

⚡ **VA Hint:** Look for the "pivot" sentence — the one that introduces a contrast (often with "Yet," "However," "But"). That sentence connects the positive claim to the critique.

---

**VA5 — Odd One Out**
Source: CAT-Level Inspired | Type: TITA | Difficulty: ★★★ | ~82nd %ile | 🟢 Must Attempt

*Three of the following four sentences form a coherent paragraph. Identify the sentence that does NOT belong. Enter its label (A/B/C/D).*

**A.** The placebo effect — improvement in a patient's condition due to belief in treatment rather than the treatment itself — is one of medicine's most documented and least understood phenomena.
**B.** Studies show that placebo responses can produce measurable physiological changes, including altered brain activity and hormone levels.
**C.** Alternative medicine practitioners have long argued that the mind and body are inseparably connected.
**D.** Even in double-blind trials, controlling for placebo effects remains one of the central methodological challenges of medical research.

⚡ **VA Hint:** The odd sentence introduces a NEW actor (alternative medicine practitioners) or a new claim not logically tied to the main theme. Ask: which sentence, if removed, makes the paragraph most coherent?

---

**VA6 — Para Completion (Fill in the Blank)**
Source: CAT-Level Inspired | Type: MCQ | Difficulty: ★★★★ | ~90th %ile | 🟡 Attempt Later

*Choose the sentence that most logically completes the paragraph:*

"The most dangerous ideas are not those that are obviously wrong — those are easily dismissed. The ideas that most threaten rational discourse are those that are half-right: they contain enough truth to be plausible, enough falsity to mislead, and enough emotional resonance to spread. ________________."

(A) Therefore, we must develop better tools for identifying misinformation online.
(B) This is why critical thinking education is important for young students.
(C) A half-truth is, in this sense, more corrosive to public reasoning than an outright lie.
(D) However, some dangerous ideas eventually turn out to be correct when re-examined carefully.

⚡ **VA Hint:** Para Completion = the sentence that FLOWS logically from the last sentence AND wraps up the idea without introducing a digression. The paragraph is building to a conclusion about half-truths — look for the option that names that conclusion directly.

---

---

# ═══════════════════════════════════════
# SECTION 4 — ATTEMPT TRACKER
# ═══════════════════════════════════════

Fill this out as you go. Be honest with your confidence ratings.

| Q# | Section | Your Answer | Time Taken | Confidence |
|----|---------|-------------|------------|------------|
| Q1 | QA — Averages | | | ✓ / ? / ✗ |
| Q2 | QA — Averages | | | ✓ / ? / ✗ |
| Q3 | QA — Averages | | | ✓ / ? / ✗ |
| Q4 | QA — Averages | | | ✓ / ? / ✗ |
| Q5 | QA — Averages | | | ✓ / ? / ✗ |
| Q6 | QA — Ratios | | | ✓ / ? / ✗ |
| Q7 | QA — Percentages | | | ✓ / ? / ✗ |
| Q8 | QA — Percentages | | | ✓ / ? / ✗ |
| Q9 | QA — Profit & Loss | | | ✓ / ? / ✗ |
| Q10 | QA — Ratios | | | ✓ / ? / ✗ |
| Q11 | QA — Percentages | | | ✓ / ? / ✗ |
| Q12 | QA — TSD | | | ✓ / ? / ✗ |
| Q13 | QA — TSD Boats | | | ✓ / ? / ✗ |
| Q14 | QA — T&W | | | ✓ / ? / ✗ |
| Q15 | QA — T&W | | | ✓ / ? / ✗ |
| Q16 | QA — TSD | | | ✓ / ? / ✗ |
| Q17 | QA — Number System | | | ✓ / ? / ✗ |
| Q18 | QA — Factors | | | ✓ / ? / ✗ |
| Q19 | QA — HCF/LCM | | | ✓ / ? / ✗ |
| Q20 | QA — Factorials | | | ✓ / ? / ✗ |
| Q21 | QA — Algebra | | | ✓ / ? / ✗ |
| Q22 | QA — Inequalities | | | ✓ / ? / ✗ |
| S1.1 | DILR Set 1 | | | ✓ / ? / ✗ |
| S1.2 | DILR Set 1 | | | ✓ / ? / ✗ |
| S1.3 | DILR Set 1 | | | ✓ / ? / ✗ |
| S1.4 | DILR Set 1 | | | ✓ / ? / ✗ |
| S2.1 | DILR Set 2 | | | ✓ / ? / ✗ |
| S2.2 | DILR Set 2 | | | ✓ / ? / ✗ |
| S2.3 | DILR Set 2 | | | ✓ / ? / ✗ |
| S2.4 | DILR Set 2 | | | ✓ / ? / ✗ |
| S3.1 | DILR Set 3 | | | ✓ / ? / ✗ |
| S3.2 | DILR Set 3 | | | ✓ / ? / ✗ |
| S3.3 | DILR Set 3 | | | ✓ / ? / ✗ |
| S3.4 | DILR Set 3 | | | ✓ / ? / ✗ |
| S4.1 | DILR Set 4 | | | ✓ / ? / ✗ |
| S4.2 | DILR Set 4 | | | ✓ / ? / ✗ |
| S4.3 | DILR Set 4 | | | ✓ / ? / ✗ |
| S4.4 | DILR Set 4 | | | ✓ / ? / ✗ |
| RC1.1 | VARC — RC1 | | | ✓ / ? / ✗ |
| RC1.2 | VARC — RC1 | | | ✓ / ? / ✗ |
| RC1.3 | VARC — RC1 | | | ✓ / ? / ✗ |
| RC1.4 | VARC — RC1 | | | ✓ / ? / ✗ |
| RC2.1 | VARC — RC2 | | | ✓ / ? / ✗ |
| RC2.2 | VARC — RC2 | | | ✓ / ? / ✗ |
| RC2.3 | VARC — RC2 | | | ✓ / ? / ✗ |
| RC2.4 | VARC — RC2 | | | ✓ / ? / ✗ |
| VA1 | VARC — Para Summary | | | ✓ / ? / ✗ |
| VA2 | VARC — Para Summary | | | ✓ / ? / ✗ |
| VA3 | VARC — Para Jumble | | | ✓ / ? / ✗ |
| VA4 | VARC — Para Jumble | | | ✓ / ? / ✗ |
| VA5 | VARC — Odd One Out | | | ✓ / ? / ✗ |
| VA6 | VARC — Para Completion | | | ✓ / ? / ✗ |

---

# ═══════════════════════════════════════
# SECTION 5 — TODAY'S ACCURACY TARGET
# ═══════════════════════════════════════

**Day 1 | Week 1 of 8**

| Phase | Target Accuracy | Today's Goal |
|-------|----------------|-------------|
| Days 1–14 | **70%** | ✅ TODAY |
| Days 15–28 | 78% | — |
| Days 29–42 | 83% | — |
| Days 43–60 | 87%+ | — |

### Today's Targets

| Section | Total Qs | Attempt | Get Correct |
|---------|---------|---------|------------|
| **QA** | 22 | 14–16 | 10–12 |
| **DILR** | 16 | 8–12 (2–3 full sets) | 6–9 |
| **VARC** | 14 | 11–13 | 9–11 |

### Smart Skip Guide for Day 1
🟢 **Attempt first:** Q1, Q3, Q7, Q9, Q12, Q14, Q19, S3 (DI Table), RC1.1, RC2.1, VA1, VA5
🟡 **Attempt if time permits:** Q2, Q4, Q6, Q8, Q13, Q15, S1, S2, RC1.2, RC1.3, RC2.2
🔴 **Skip Round 1:** Q5, Q11, Q16, Q20, Q22, S4 (Tournament), RC1.4, RC2.4, VA4

> 💡 **Day 1 Mantra:** Accuracy over speed. Complete 2 DILR sets fully rather than touching all 4 partially. In QA, skip 🔴 questions without guilt — your target today is the 🟢 pool.

---

---

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔒 STOP HERE — DO NOT SCROLL FURTHER
# Submit your answers to your mentor first.
# Main question solutions revealed AFTER submission.
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

.
.
.
.
.
.
.
.
.
.
.
.

---

# 🔑 SPEED DRILL ANSWERS

| # | Answer | Working |
|---|--------|---------|
| SD1 | **72** | 15% of 480 = 480 × 15/100 = 72 |
| SD2 | **15** | Average of AP = middle term = 15 |
| SD3 | **12:35** | A:B=3:5, B:C=4:7 → multiply: A:B:C = 12:20:35 → A:C = 12:35 |
| SD4 | **12,000** | 125 × 96 = 125 × 100 − 125 × 4 = 12500 − 500 = 12000 |
| SD5 | **10%** | SI: P doubles → Interest = P in 10 years → Rate = 100/10 = 10% |

---

# 🔑 SHORTCUT WARM-UP ANSWERS

| # | Answer | Working |
|---|--------|---------|
| WU1 | **5% profit** | 33.33% up = ×4/3; 25% down = ×3/4. Net = 4/3 × 3/4 = 1.00 → No change? Actually: mark up 33.33% then discount 25% → net = (1+1/3)(1−1/4) = 4/3 × 3/4 = 1. So 0% change. Check: marked price = 100×4/3 = 133.33; after 25% discount = 133.33×0.75 = 100. Net = 0% change. |
| WU2 | **P:R = 10:18 = 5:9** | P:Q=2:3, Q:R=5:6 → P:Q:R = 10:15:18 → P:R = 10:18 = 5:9 |
| WU3 | **29** | 9 consecutive integers, avg = 25 = middle term (5th term). Largest = 25 + 4 = 29 |
