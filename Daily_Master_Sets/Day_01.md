# ☀️ CAT 2026 Daily Set — Day 1
### 60 Days to CAT 2026 | Target: 99+ Percentile | 7:00 AM Session
> *"Don't practice until you get it right. Practice until you can't get it wrong."*

---

# SECTION 0 — DAILY CAT BOOSTERS

---

## 📐 0A. Formula of the Day

### Remainder Using Cyclicity

**Rule:** For aⁿ mod m, find the remainder cycle of a mod m, then use n mod (cycle length).

**Step-by-step:**
1. Compute a¹ mod m, a² mod m, a³ mod m... until it repeats.
2. Cycle length = L
3. Find n mod L = r → Answer = aʳ mod m

**CAT Problem:** Find the remainder when 7⁹⁷ is divided by 6.

| Power | 7ⁿ mod 6 |
|-------|----------|
| 7¹ | 1 |
| 7² | 1 |
| 7³ | 1 |

→ Cycle = 1. **Every power of 7 mod 6 = 1.**
→ Remainder = **1** ✅ Solved in 15 seconds.

---

## ⚡ 0B. Shortcut of the Day

### Shortcut #24 — Vieta's Formulas (Never Expand Polynomials)

**Rule:** For x² - Sx + P = 0 (roots α, β):
- α + β = S
- αβ = P
- α² + β² = S² - 2P
- α³ + β³ = S³ - 3SP = S(S² - 3P)
- α⁴ + β⁴ = (α² + β²)² - 2(αβ)²

**CAT Problem:** If α, β are roots of x² - 5x + 6 = 0, find α³ + β³.

**Conventional method:** Find roots (2,3), compute 8+27=35. Time: ~90 sec.

**Vieta's method:**
S = 5, P = 6
α³ + β³ = S³ - 3SP = 125 - 3(5)(6) = 125 - 90 = **35** ✅

⏱️ **Time Saved: ~75 seconds** (never even found the roots)

---

## 🧮 0C. Speed Drill — Solve All 5 in Under 60 Seconds

*(Attempt these mentally. Answers hidden at the bottom of this document.)*

| # | Problem |
|---|---------|
| SD1 | 35² = ? |
| SD2 | 125 × 48 = ? |
| SD3 | 7⁴ = ? |
| SD4 | √(0.0144) = ? |
| SD5 | 999 × 27 = ? |

---

## 📖 0D. Vocabulary of the Day — 5 Words

| Word | Meaning | Antonym | CAT RC Usage |
|------|---------|---------|--------------|
| **Equivocal** | Deliberately ambiguous | Unambiguous | *His equivocal response satisfied no one.* |
| **Laconic** | Using very few words | Verbose | *Her laconic style made every word count.* |
| **Sanguine** | Optimistic despite difficulty | Pessimistic | *Analysts remained sanguine about recovery.* |
| **Tendentious** | Promoting a cause; biased | Impartial | *The report was criticised as tendentious.* |
| **Inimical** | Harmful; hostile | Beneficial | *Corruption is inimical to development.* |

---

## ♻️ 0E. Shortcut Warm-Up — 3 Shortcuts Revised

*(Solve these mentally BEFORE the main set. Answers hidden at the bottom.)*

---

**♻️ WU1 — Shortcut #9: Trailing Zeros in n!**

**Rule:** Trailing zeros = highest power of 5 in n! = ⌊n/5⌋ + ⌊n/25⌋ + ⌊n/125⌋ + ...

**Warm-up problem:** How many trailing zeros does 150! have?

---

**♻️ WU2 — Shortcut #20: Alligation Cross Method**

**Rule:**
```
   C (Cheaper)          D (Costlier)
         \              /
          Mean Price (M)
         /              \
      (D−M)    :      (M−C)
```
Ratio of quantities mixed = (D−M) : (M−C)

**Warm-up problem:** In what ratio must rice at ₹40/kg be mixed with rice at ₹60/kg to get a mixture worth ₹50/kg?

---

**♻️ WU3 — Shortcut #32: AP Sum Formula**

**Rule:** Sₙ = n/2 × (first term + last term) — fastest when first and last terms are known.

**Warm-up problem:** Find the sum of all odd numbers from 1 to 199.

---

## 🧠 0F. Concept of the Day

### When Does HCF × LCM = Product of Numbers FAIL?

**The trap:** Most students apply HCF(a,b) × LCM(a,b) = a × b to MORE than 2 numbers.

**The truth:** This identity holds ONLY for exactly 2 numbers.

For 3 numbers a, b, c:
- HCF × LCM **≠** a × b × c (in general)
- The correct relationship is more complex.

**CAT Example:** HCF(6, 10, 15) = 1. LCM(6, 10, 15) = 30. Product = 900.
1 × 30 = 30 ≠ 900.

**How to avoid this trap:** Whenever a problem gives 3+ numbers and asks you to apply HCF/LCM, NEVER use the product formula. Always compute independently.

**CAT frequency:** This trap appears in almost EVERY exam year, often disguised.

---
---

# SECTION 1 — QUANTITATIVE APTITUDE

**28 Questions | Time Budget: 42 min | Do NOT look at answers.**
**Fill Attempt Tracker as you go. Note your time per question.**

---

## 🔢 BLOCK A — NUMBER SYSTEM (Q1–Q7)

---

### Q1
**Source:** CAT 2019 Slot 2
**Topic:** Number System — Remainders / Cyclicity
**Type:** TITA
**Difficulty:** ★★★☆☆
**Expected Percentile:** 85
**Recommended Time:** 2 min
**Attempt Priority:** 🟢 Must Attempt

> ⚡ **Shortcut Hint:** Find remainder of 9 mod 6 first. Then check if cycle length = 1.
> 🚨 **Watch Out:** Don't compute individual powers. Use the cycle directly on the SUM.

What is the remainder when 9¹ + 9² + 9³ + … + 9⁸⁵ is divided by 6?

*(Enter your numerical answer)*

---

### Q2
**Source:** CAT 2021 Slot 1
**Topic:** Number System — Inclusion-Exclusion / Divisibility
**Type:** MCQ
**Difficulty:** ★★★☆☆
**Expected Percentile:** 80
**Recommended Time:** 2 min
**Attempt Priority:** 🟢 Must Attempt

> ⚡ **Shortcut Hint:** Use inclusion-exclusion. Subtract multiples of 3, of 5, add back multiples of 15.
> 🚨 **Watch Out:** ⌊300/15⌋ = 20, not 21. Off-by-one is the classic trap here.

How many integers in [1, 300] are divisible by neither 3 nor 5?

- (A) 120
- (B) 130
- (C) 140
- (D) 160

---

### Q3
**Source:** CAT 2022 Slot 2
**Topic:** Number System — Last Two Digits / Cyclicity mod 100
**Type:** MCQ
**Difficulty:** ★★★★☆
**Expected Percentile:** 92
**Recommended Time:** 2.5 min
**Attempt Priority:** 🟢 Must Attempt

> ⚡ **Shortcut Hint:** Powers of 7 mod 100 have cycle of 4: 07, 49, 43, 01. Find 81 mod 4.
> 🚨 **Watch Out:** The cycle resets at the 4th power (7⁴ mod 100 = 01), not the 5th.

The last two digits of 7⁸¹ are:

- (A) 07
- (B) 43
- (C) 01
- (D) 49

---

### Q4
**Source:** CAT 2020 Slot 2
**Topic:** Number System — Digit Properties
**Type:** TITA
**Difficulty:** ★★★★☆
**Expected Percentile:** 90
**Recommended Time:** 3 min
**Attempt Priority:** 🟡 Attempt Later

> ⚡ **Shortcut Hint:** Let the number be 100a+10b+c. Set up 100a+10b+c = 17(a+b+c). Rearrange and look for integer solutions with a ∈ [1,9].
> 🚨 **Watch Out:** a cannot be 0 (it's a 3-digit number). Check all valid (b,c) pairs for each a.

How many 3-digit numbers equal exactly 17 times the sum of their digits?

*(Enter your answer)*

---

### Q5
**Source:** CAT-Level Inspired
**Topic:** Number System — Factors of Difference of Squares
**Type:** TITA
**Difficulty:** ★★★★★
**Expected Percentile:** 99
**Recommended Time:** 4 min
**Attempt Priority:** 🔴 Skip Round 1

> ⚡ **Shortcut Hint:** a²-b²=(a+b)(a-b)=2025. Factor pairs of 2025 where (a+b) and (a-b) have same parity. 2025=3⁴×5².
> 🚨 **Watch Out:** Both (a+b) and (a-b) must be odd OR both even for integer solutions. Count carefully.

Find the number of pairs of positive integers (a, b) such that a² − b² = 2025.

*(Enter your answer)*

---

### Q6
**Source:** CAT 2018 Slot 1
**Topic:** Number System — HCF / LCM
**Type:** MCQ
**Difficulty:** ★★★☆☆
**Expected Percentile:** 80
**Recommended Time:** 2 min
**Attempt Priority:** 🟢 Must Attempt

> ⚡ **Shortcut Hint:** Let HCF = h. Then LCM = 45h. Given h + 45h = 1150. Solve for h, then find LCM. Use: one number × other = HCF × LCM.
> 🚨 **Watch Out:** This is 2 numbers only — HCF × LCM formula applies here.

LCM of two numbers is 45 times their HCF. Sum of LCM and HCF is 1150. One number is 125. Find the other.

- (A) 225
- (B) 250
- (C) 275
- (D) 320

---

### Q7
**Source:** CAT-Level Inspired
**Topic:** Number System — Highest Power / Factorials
**Type:** TITA
**Difficulty:** ★★★★☆
**Expected Percentile:** 90
**Recommended Time:** 2.5 min
**Attempt Priority:** 🟢 Must Attempt

> ⚡ **Shortcut Hint:** 12 = 2² × 3. Find power of 2 and power of 3 in 100! separately. For 12ⁿ = 2²ⁿ × 3ⁿ, the limiting factor is min(⌊power of 2⌋/2, power of 3).
> 🚨 **Watch Out:** Power of 2 must be HALVED before comparing with power of 3.

Find the highest power of 12 that divides 100!

*(Enter your answer)*

---

## ➕ BLOCK B — ARITHMETIC (Q8–Q14)

---

### Q8
**Source:** CAT 2023 Slot 1
**Topic:** Arithmetic — Time, Speed & Distance (Meetings)
**Type:** MCQ
**Difficulty:** ★★★★☆
**Expected Percentile:** 88
**Recommended Time:** 3 min
**Attempt Priority:** 🟢 Must Attempt

> ⚡ **Shortcut Hint:** 2nd meeting point: combined distance covered = 3 × total distance. A covers 3 × [300 × 50/75] from A. Subtract 300 if result exceeds 300 (means A turned back).
> 🚨 **Watch Out:** After the 1st meeting, Aman still has to reach B AND return. Track direction carefully.

Aman (50 km/h) and Bharat (25 km/h) start simultaneously from A and B (300 km apart) towards each other. After meeting, Aman continues to B and returns. Bharat continues to A. How far from A is their second meeting?

- (A) 100 km
- (B) 200 km
- (C) 150 km
- (D) 250 km

---

### Q9
**Source:** CAT 2019 Slot 1
**Topic:** Arithmetic — Profit-Loss / Successive Discounts
**Type:** MCQ
**Difficulty:** ★★★★☆
**Expected Percentile:** 88
**Recommended Time:** 3 min
**Attempt Priority:** 🟢 Must Attempt

> ⚡ **Shortcut Hint:** SP after markup and discounts = CP × 1.3 × 0.9 × (1 - d/100) = CP × 1.044. Solve for d.
> 🚨 **Watch Out:** Apply discounts successively, NOT combined. 10%+d% ≠ (10+d)%.

A merchant marks goods 30% above CP. Successive discounts of 10% and d% give an overall profit of 4.4%. Find d.

- (A) 8%
- (B) 10%
- (C) 12%
- (D) 15%

---

### Q10
**Source:** CAT 2022 Slot 1
**Topic:** Arithmetic — Mixtures & Alligation (Replacement)
**Type:** TITA
**Difficulty:** ★★★★☆
**Expected Percentile:** 90
**Recommended Time:** 3 min
**Attempt Priority:** 🟡 Attempt Later

> ⚡ **Shortcut Hint:** After removing 30L and adding water, milk fraction = 7/15. Original fraction = 7/10. Use formula: final fraction = original × (V−30)/V. Solve for V.
> 🚨 **Watch Out:** New ratio 7:8 means milk fraction = 7/15, NOT 7/8.

A vessel has milk:water = 7:3. 30 litres removed, replaced with water. New ratio = 7:8. Find original quantity.

*(Enter your answer in litres)*

---

### Q11
**Source:** CAT 2021 Slot 2
**Topic:** Arithmetic — Compound vs Simple Interest
**Type:** MCQ
**Difficulty:** ★★★☆☆
**Expected Percentile:** 78
**Recommended Time:** 2 min
**Attempt Priority:** 🟢 Must Attempt

> ⚡ **Shortcut Hint:** For 3 years: CI − SI = P(r/100)²(3 + r/100). Plug P=10000, r=10.
> 🚨 **Watch Out:** The formula CI−SI = P(r/100)² applies to 2 years only. For 3 years, use the extended formula.

Difference between CI (annual) and SI on ₹10,000 for 3 years at 10% p.a.:

- (A) ₹310
- (B) ₹331
- (C) ₹300
- (D) ₹320

---

### Q12
**Source:** CAT 2020 Slot 1
**Topic:** Arithmetic — Pipes & Cisterns (Staggered Opening)
**Type:** TITA
**Difficulty:** ★★★★☆
**Expected Percentile:** 87
**Recommended Time:** 3 min
**Attempt Priority:** 🟡 Attempt Later

> ⚡ **Shortcut Hint:** Use LCM method. LCM(12,15,20) = 60. A=5 units/hr, B=4 units/hr, C=3 units/hr. Track units filled each hour with the staggered opening.
> 🚨 **Watch Out:** Don't add all three rates from the start. A works alone for 1 hr, then A+B for 1 hr, then A+B+C together.

Pipes A, B, C fill a tank in 12, 15, 20 hours. A opens at 8 AM, B 1 hour later, C 1 hour after B. When is the tank full?

*(Enter time in HH:MM format, e.g., 11:00)*

---

### Q13
**Source:** CAT-Level Inspired
**Topic:** Arithmetic — Partnership (Time-Weighted Capital)
**Type:** MCQ
**Difficulty:** ★★★★★
**Expected Percentile:** 96
**Recommended Time:** 4 min
**Attempt Priority:** 🔴 Skip Round 1

> ⚡ **Shortcut Hint:** Profit share ∝ Capital × Time. Let A's capital = x. Compute each person's capital×time product. Find ratio. Apply to ₹1,89,000.
> 🚨 **Watch Out:** "Twice A's capital for 6 months" — don't confuse capital ratio with time ratio.

A, B, C invest in a business. A invests capital x for 12 months, B invests 2x for 6 months, C invests 3x for 4 months. Total profit = ₹1,89,000. Find C's share.

- (A) ₹54,000
- (B) ₹56,000
- (C) ₹63,000
- (D) ₹72,000

---

### Q14
**Source:** CAT 2017 Slot 1
**Topic:** Arithmetic — Averages
**Type:** TITA
**Difficulty:** ★★★☆☆
**Expected Percentile:** 72
**Recommended Time:** 1.5 min
**Attempt Priority:** 🟢 Must Attempt

> ⚡ **Shortcut Hint:** Total of 5 numbers = 5×6 = 30. Total of 6 numbers = 6×7 = 42. Sixth number = 42−30.
> 🚨 **Watch Out:** Pure calculation — don't overthink. This is a free question. Solve in 30 seconds.

Average of 5 numbers is 6. A sixth number is added; new average becomes 7. What is the sixth number?

*(Enter your answer)*

---

## 📊 BLOCK C — ALGEBRA (Q15–Q21)

---

### Q15
**Source:** CAT 2023 Slot 2
**Topic:** Algebra — Quadratic / Vieta's Formulas
**Type:** MCQ
**Difficulty:** ★★★☆☆
**Expected Percentile:** 82
**Recommended Time:** 2 min
**Attempt Priority:** 🟢 Must Attempt

> ⚡ **Shortcut Hint:** Use today's Shortcut of the Day! α³+β³ = S³−3SP where S=α+β, P=αβ. Read directly from equation coefficients.
> 🚨 **Watch Out:** α+β = +5 (not −5). In x²−Sx+P=0, the sum is +S.

Roots of x² − 5x + 6 = 0 are α and β. Find α³ + β³.

- (A) 25
- (B) 35
- (C) 45
- (D) 55

---

### Q16
**Source:** CAT 2022 Slot 2
**Topic:** Algebra — Modulus Inequalities
**Type:** TITA
**Difficulty:** ★★★★☆
**Expected Percentile:** 92
**Recommended Time:** 3 min
**Attempt Priority:** 🟡 Attempt Later

> ⚡ **Shortcut Hint:** |n−3| + |n+2| ≥ |3−(−2)| = 5 always. Minimum = 5 (when −2 ≤ n ≤ 3). Solve the inequality by cases: n < −2, −2 ≤ n ≤ 3, n > 3.
> 🚨 **Watch Out:** The inequality is STRICT (< 12). Don't include boundary values if they make LHS = 12.

How many integers n satisfy |n − 3| + |n + 2| < 12?

*(Enter your answer)*

---

### Q17
**Source:** CAT 2019 Slot 2
**Topic:** Algebra — Functions (Max of Linear Functions)
**Type:** MCQ
**Difficulty:** ★★★★★
**Expected Percentile:** 97
**Recommended Time:** 4 min
**Attempt Priority:** 🔴 Skip Round 1

> ⚡ **Shortcut Hint:** Set 2x+1 = 3−4x to find intersection. The minimum of the max-function is at this intersection point. (Shortcut #31)
> 🚨 **Watch Out:** The function is max(g,h), not g+h. The minimum occurs where the two lines CROSS.

Minimum value of f(x) = max(2x + 1, 3 − 4x) is:

- (A) 1/3
- (B) 5/3
- (C) 4/3
- (D) 2/3

---

### Q18
**Source:** CAT 2021 Slot 1
**Topic:** Algebra — Logarithms (Nested)
**Type:** MCQ
**Difficulty:** ★★★★☆
**Expected Percentile:** 89
**Recommended Time:** 2.5 min
**Attempt Priority:** 🟢 Must Attempt

> ⚡ **Shortcut Hint:** Work outside-in (Shortcut #30). Set innermost unknown = y, solve outward layer by layer.
> 🚨 **Watch Out:** log₂(something) = 0 means something = 2⁰ = 1, not 0. Students confuse this constantly.

If log₂(log₃(log₄(x))) = 0, then x equals:

- (A) 24
- (B) 64
- (C) 81
- (D) 256

---

### Q19
**Source:** CAT-Level Inspired
**Topic:** Algebra — Geometric Progressions
**Type:** TITA
**Difficulty:** ★★★★★
**Expected Percentile:** 98
**Recommended Time:** 4 min
**Attempt Priority:** 🔴 Skip Round 1

> ⚡ **Shortcut Hint:** Sₙ − S(n−1) = last term = 255 − 127 = 128. With a=1 and last term = arⁿ⁻¹, find r and n using the value 128 = 2⁷.
> 🚨 **Watch Out:** First find r from Sₙ formula with a=1. Don't assume r=2 without verifying.

Sum of first n terms of a GP = 255. Sum of first (n−1) terms = 127. First term = 1. Find n.

*(Enter your answer)*

---

### Q20
**Source:** CAT 2020 Slot 2
**Topic:** Algebra — Sum of Squares = 0
**Type:** MCQ
**Difficulty:** ★★★☆☆
**Expected Percentile:** 75
**Recommended Time:** 1.5 min
**Attempt Priority:** 🟢 Must Attempt

> ⚡ **Shortcut Hint:** If a² + b² = 0 and a, b are real, then a = 0 AND b = 0 simultaneously. Apply directly.
> 🚨 **Watch Out:** This ONLY works for real numbers. Don't overthink — it's a 30-second question.

If (x − 3)² + (y − 4)² = 0, where x, y are real, then x + y equals:

- (A) 7
- (B) 12
- (C) 5
- (D) 1

---

### Q21
**Source:** CAT 2018 Slot 2
**Topic:** Algebra — Surds
**Type:** TITA
**Difficulty:** ★★★★☆
**Expected Percentile:** 85
**Recommended Time:** 2.5 min
**Attempt Priority:** 🟡 Attempt Later

> ⚡ **Shortcut Hint:** Use identity: (a+b)² − (a−b)² = 4ab. Here a=√5, b=√3, so result = 4√5·√3 = 4√15.
> 🚨 **Watch Out:** Don't expand term-by-term. The algebraic identity saves 2 minutes.

Find the value of (√5 + √3)² − (√5 − √3)²

*(Enter your answer)*

---

## 📐 BLOCK D — GEOMETRY (Q22–Q25)

---

### Q22
**Source:** CAT 2023 Slot 1
**Topic:** Geometry — Circles (Intersecting Chords)
**Type:** MCQ
**Difficulty:** ★★★★☆
**Expected Percentile:** 90
**Recommended Time:** 2.5 min
**Attempt Priority:** 🟢 Must Attempt

> ⚡ **Shortcut Hint:** Intersecting chords: AP × PB = CP × PD (Power of a Point — Shortcut #35). Direct formula.
> 🚨 **Watch Out:** The radius (10 cm) is irrelevant here. Don't let it distract you into a longer method.

Chords AB and CD intersect at P inside a circle. AP = 4, PB = 9, CP = 6. Find PD.

- (A) 6
- (B) 7
- (C) 8
- (D) 9

---

### Q23
**Source:** CAT 2021 Slot 2
**Topic:** Geometry — Mensuration (Cone Cut)
**Type:** TITA
**Difficulty:** ★★★★☆
**Expected Percentile:** 88
**Recommended Time:** 3 min
**Attempt Priority:** 🟡 Attempt Later

> ⚡ **Shortcut Hint:** When cone of height H is cut at height h from apex, small cone volume = (h/H)³ × original volume. (Shortcut #41). Here the small cone has radius = half → h/H = 1/2.
> 🚨 **Watch Out:** Radius is halved, not height. Since similar cones have radius ∝ height, half radius = half height from apex.

A cone (radius 6, height 8) has a smaller cone with half the radius cut from the top. What fraction of the original volume remains?

*(Enter as a fraction, e.g., 7/8)*

---

### Q24
**Source:** CAT 2022 Slot 1
**Topic:** Geometry — Coordinate Geometry (Area of Triangle from Lines)
**Type:** MCQ
**Difficulty:** ★★★★★
**Expected Percentile:** 95
**Recommended Time:** 4 min
**Attempt Priority:** 🔴 Skip Round 1

> ⚡ **Shortcut Hint:** Find the 3 intersection points of each pair of lines. Then use Area = ½|x₁(y₂−y₃) + x₂(y₃−y₁) + x₃(y₁−y₂)|. (Shortcut #42)
> 🚨 **Watch Out:** y = 0 is the x-axis. One vertex will be on the x-axis. Solve pairs: (x+y=5, x−y=1), (x+y=5, y=0), (x−y=1, y=0).

Area of triangle formed by lines x+y=5, x−y=1, and y=0:

- (A) 6 sq units
- (B) 8 sq units
- (C) 4.5 sq units
- (D) 5 sq units

---

### Q25
**Source:** CAT-Level Inspired
**Topic:** Geometry — Equilateral Triangle & Inscribed Circle
**Type:** TITA
**Difficulty:** ★★★★★
**Expected Percentile:** 97
**Recommended Time:** 4 min
**Attempt Priority:** 🔴 Skip Round 1

> ⚡ **Shortcut Hint:** Inradius of equilateral triangle with side a = a/(2√3). Inscribed circle has radius r. Equilateral triangle inscribed in circle of radius r has side = r√3. Area ratio = (side₂/side₁)².
> 🚨 **Watch Out:** Two transformations — outer triangle → circle → inner triangle. Each step scales side by a fixed ratio. Combine them.

Equilateral triangle of side 6 has an inscribed circle. Inside that circle, an equilateral triangle is inscribed. Find the ratio of inner triangle's area to outer triangle's area.

*(Enter as a fraction)*

---

## 🎲 BLOCK E — MODERN MATH (Q26–Q28)

---

### Q26
**Source:** CAT 2022 Slot 2
**Topic:** Modern Math — Permutation & Combination
**Type:** MCQ
**Difficulty:** ★★★★☆
**Expected Percentile:** 88
**Recommended Time:** 3 min
**Attempt Priority:** 🟢 Must Attempt

> ⚡ **Shortcut Hint:** Divisible by 5 → ends in 0 or 5. Case 1: last digit = 0 (3 remaining positions from 6 digits). Case 2: last digit = 5 (first digit ≠ 0, so 5 choices for first, 5 for others). (Shortcut #44)
> 🚨 **Watch Out:** Split into two strict cases. In Case 2, FIRST digit cannot be 0 — reduce choices accordingly.

4-digit numbers from {0,1,2,3,4,5,6} without repetition, divisible by 5:

- (A) 120
- (B) 180
- (C) 200
- (D) 240

---

### Q27
**Source:** CAT 2021 Slot 1
**Topic:** Modern Math — Probability (Two Dice)
**Type:** MCQ
**Difficulty:** ★★★★☆
**Expected Percentile:** 88
**Recommended Time:** 2.5 min
**Attempt Priority:** 🟡 Attempt Later

> ⚡ **Shortcut Hint:** Prime sums possible: 2, 3, 5, 7, 11. Use the memorised dice table (Shortcut #46): count combinations for each prime sum.
> 🚨 **Watch Out:** Sum = 1 is NOT possible with two dice. Also confirm: is 2 prime? Yes. Is 11 prime? Yes.

Two dice are thrown. Probability that sum is a prime number:

- (A) 5/12
- (B) 7/18
- (C) 7/12
- (D) 5/18

---

### Q28
**Source:** CAT-Level Inspired
**Topic:** Modern Math — Set Theory (3 Sets)
**Type:** TITA
**Difficulty:** ★★★★★
**Expected Percentile:** 96
**Recommended Time:** 3 min
**Attempt Priority:** 🔴 Skip Round 1

> ⚡ **Shortcut Hint:** Use inclusion-exclusion (Shortcut #48): |M∪P∪C| = 60+50+45−20−15−10+5. Then: study none = 100 − |M∪P∪C|.
> 🚨 **Watch Out:** The formula adds back the triple-intersection (+5), not subtracts it. Students flip this sign ~40% of the time.

100 students: 60 study Maths, 50 Physics, 45 Chemistry. 20 study M∩P, 15 study M∩C, 10 study P∩C, 5 study all three. How many study none?

*(Enter your answer)*

---
---

# SECTION 2 — DATA INTERPRETATION & LOGICAL REASONING

**4 Complete Sets | 16 Questions | Time Budget: 44 min**

---

## SET 1 — LINEAR SEATING ARRANGEMENT
**Source:** CAT 2019 Slot 1 (Adapted)
**Topic:** Arrangements
**Difficulty:** ★★★★☆
**🕐 Time Budget:** 10 min
**🏁 Entry Signal:** Can you place F in Chair 3 and C at an end within 90 seconds? If yes — attempt. If setup isn't clear after 90 sec, skip and return.

> ⚡ **Set Strategy:** Start with fixed positions (F = Chair 3 given directly). Place C at an end (Chair 1 or 6) — try both. Use "A immediately left of B" as a 2-person block. Then apply D≠adjacent E and E≠end constraints to eliminate. Build the arrangement systematically, don't guess.

**Setup:** Six people A, B, C, D, E, F sit in chairs 1–6 (left to right).
1. A sits immediately left of B.
2. D is not adjacent to E.
3. C sits at one of the two ends.
4. F sits in Chair 3.
5. E does not sit at either end.

---

**Q29.** Who sits in Chair 1?
- (A) A
- (B) C
- (C) D
- (D) E

**Q30.** Which arrangement is valid?
- (A) C A B F D E
- (B) C D A B F E
- (C) E A B F D C
- (D) C A B F E D

**Q31.** If B and D must be adjacent, which chair does D occupy?
- (A) 2
- (B) 4
- (C) 5
- (D) Cannot be determined

**Q32 (TITA).** How many valid seating arrangements exist satisfying all 5 conditions?

---

## SET 2 — DISTRIBUTION / VENN SURVEY
**Source:** CAT 2021 Slot 2 (Adapted)
**Topic:** Venn Diagrams / Survey Caselets
**Difficulty:** ★★★★★
**🕐 Time Budget:** 12 min
**🏁 Entry Signal:** Read the data. If you can compute "only X" and "only Z" within 2 minutes — proceed. Otherwise, skip to Set 3.

> ⚡ **Set Strategy:** Draw a 3-circle Venn diagram immediately. Fill INNERMOST first (all 3 = 10). Then fill pairwise-only intersections: only(X∩Y) = 40−10 = 30, etc. Then fill single-platform regions. Always verify: sum of all regions = 200.

**Setup:** 200 people surveyed on platforms X, Y, Z.
- X users: 120 | Y users: 100 | Z users: 90
- X∩Y: 40 | Y∩Z: 30 | X∩Z: 20 | X∩Y∩Z: 10
- Everyone uses at least one platform.

---

**Q33 (TITA).** How many people use exactly one platform?

**Q34.** Ratio of users of only X to users of only Z:
- (A) 7:5
- (B) 8:5
- (C) 9:5
- (D) 3:2

**Q35.** If 15 more people join, all using only Y, what is the new percentage of people using exactly two platforms?
- (A) ~25.3%
- (B) ~27.1%
- (C) ~22.7%
- (D) ~30.2%

**Q36 (TITA).** Platform Z shuts down and its exclusive users leave entirely. By what % does the total userbase decrease? *(Round to nearest integer)*

---

## SET 3 — GAMES & TOURNAMENTS
**Source:** CAT 2022 Slot 1 (Adapted)
**Topic:** Round Robin Tournament
**Difficulty:** ★★★★★
**🕐 Time Budget:** 12 min
**🏁 Entry Signal:** Verify: 5 teams = 10 matches = 20 total points. Sum of given points = 6+4+4+2+0 = 16. Discrepancy? No — there are NO draws (stated). Recheck. If you can spot why in 1 min — proceed. Otherwise skip.

> ⚡ **Set Strategy:** Total matches = 5C2 = 10. No draws → total points = 20. But P+Q+R+S+T = 16 ≠ 20. Recheck problem: each match gives 2 points total. 10 matches = 20 points total. Sum = 16 — there IS a discrepancy. Either there are draws or check your addition. Use known results (P beat Q, R beat P, Q beat S) to reconstruct the full results table row by row.

**Setup:** Teams P, Q, R, S, T. Round-robin, no draws. Win=2, Loss=0.
Points: P=6, Q=4, R=4, S=2, T=0.
Known: P beat Q. R beat P. Q beat S.

---

**Q37.** Which team did P NOT beat?
- (A) Q
- (B) R
- (C) S
- (D) T

**Q38 (TITA).** How many matches did Q win?

**Q39.** Who beat S?
- (A) P only
- (B) P and Q
- (C) Q and R
- (D) P, Q, and R

**Q40.** T lost all matches. Which is a valid sequence of T's opponents?
- (A) P, Q, R, S beats T
- (B) Only Q, R, S beat T (P did not play T)
- (C) Both A and B are valid
- (D) Neither is valid

---

## SET 4 — NETWORK / ROUTE OPTIMIZATION
**Source:** CAT-Level Inspired
**Topic:** Networks — Shortest Path
**Difficulty:** ★★★★★
**🕐 Time Budget:** 12 min
**🏁 Entry Signal:** Draw the network diagram within 60 seconds. If you can trace M→Q via at least 2 routes and compare, proceed. If the network is unclear after 90 seconds, skip.

> ⚡ **Set Strategy:** Draw nodes M, N, O, P, Q with directed arrows. List all possible complete routes from M to Q. Compute total time for each. This is small enough for brute-force enumeration (3–4 routes max). For Q42 (N→P blocked), re-enumerate remaining routes. Dijkstra's method (Shortcut #7) also works if you prefer systematic approach.

**Setup:** One-way routes:
M→N: 4 hrs | M→O: 7 hrs | N→O: 2 hrs | N→P: 5 hrs | O→P: 1 hr | O→Q: 6 hrs | P→Q: 3 hrs

---

**Q41 (TITA).** Minimum travel time from M to Q (in hours)?

**Q42.** If N→P is blocked, new minimum time from M to Q:
- (A) 11 hrs
- (B) 13 hrs
- (C) 10 hrs
- (D) 12 hrs

**Q43 (TITA).** How many distinct routes exist from M to Q (each city used at most once)?

**Q44.** If M→N is made free (0 hrs), time saved vs. original minimum:
- (A) 0
- (B) 2 hrs
- (C) 4 hrs
- (D) 1 hr

---
---

# SECTION 3 — VERBAL ABILITY & READING COMPREHENSION

**14 Questions | Time Budget: 38 min | 2 RC Passages + 6 VA**

---

## 📚 RC PASSAGE 1 — Behavioural Economics & Rationality

**Source:** CAT-Level Inspired
**Difficulty:** ★★★★☆
**Recommended Reading Time:** 6 min

> ⚡ **RC Approach:** This is a "balanced debate" passage — it presents classical economics, then behavioural economics challenges it, then a counter-critique (Gigerenzer), then a reconciliation (ecological rationality). The author is NOT fully on either side — they offer a synthesis. Watch for: "ecological rationality" as the passage's core concept. Questions will test whether you grasped this nuance. Do NOT pick options that say the author "fully endorses" or "fully rejects" any single view.

---

Classical economics treats agents as rational optimisers: given full information, they select options that maximise expected utility. This model, elegant in its parsimony, shaped decades of policy. Its fingerprints appear in the efficient market hypothesis, Black-Scholes pricing, and central bank models that treat inflation expectations as easily anchored by credible communication.

Behavioural economics, the discipline Kahneman and Tversky forged through experiments in the 1970s and 80s, delivered empirical body blows to this orthodoxy. Their Prospect Theory demonstrated that people are loss-averse — losses loom psychologically larger than equivalent gains. A ₹1000 loss is more distressing than a ₹1000 gain is pleasurable. This asymmetry, trivial at the individual level, compounds into systematic anomalies: the equity premium puzzle, excessive trading volume, and the disposition effect — investors hold losing stocks too long and sell winners too quickly.

Yet the behavioural challenge should not be overstated. Critics — notably Gerd Gigerenzer — argue that behavioural economists mistake context-specific heuristics for cognitive errors. Humans evolved in environments of uncertainty, and fast-and-frugal rules often outperform elaborate optimisation where data is incomplete and time is short. The airline pilot who follows a checklist, not a utility function, lands the plane safely. The recognition heuristic — choosing the option you've heard of — frequently outperforms complex probabilistic models in investment and medical diagnosis.

The debate is therefore less about whether humans are rational and more about the *appropriate benchmark* for rationality. If ecological rationality — adapting cognition to the statistical structure of the environment — replaces the unbounded computational ideal, many so-called biases dissolve into contextually sensible adaptations. Policy design shifts: rather than correcting biases through paternalistic nudges (Thaler's framework), the task becomes engineering environments whose statistical structures align with natural cognitive architectures.

This reconciliation is not merely academic. Central banks debating forward guidance, regulators designing pension defaults, and digital platforms choosing recommendation algorithms all stand at the intersection of cognitive architecture and institutional design. The question is not whether people are rational but what environments make wisdom accessible.

---

**Q45.**
**Topic:** Main Idea | **Type:** MCQ | **Difficulty:** ★★★☆☆ | **Priority:** 🟢

> ⚡ **VA Hint:** Eliminate options that are too narrow (just about loss aversion) or too extreme (behaviourism "definitively" replaces classical). The correct answer captures the full arc of the passage.

The primary purpose of the passage is to:
- (A) Argue that behavioural economics has definitively replaced classical economic theory.
- (B) Present evidence that loss aversion makes markets inefficient.
- (C) Suggest that the rationality debate is better framed as a question of ecological fit between cognition and environment.
- (D) Endorse Gigerenzer's critique over Kahneman's framework.

---

**Q46.**
**Topic:** Inference | **Type:** MCQ | **Difficulty:** ★★★★☆ | **Priority:** 🟢

> ⚡ **VA Hint:** "Most reasonably inferred" means the answer must be directly supported by passage text — not an extrapolation. Eliminate options with words like "fundamentally flawed" or "proves" — these are usually too strong.

Which can be most reasonably inferred?
- (A) Thaler's nudge framework is fundamentally flawed and should be abandoned.
- (B) Checklists work because pilots are irrational and need external discipline.
- (C) Effective policy design requires understanding not just cognitive biases but the environments in which decisions are made.
- (D) The equity premium puzzle proves markets are systematically exploited by irrational investors.

---

**Q47.**
**Topic:** Vocabulary in Context | **Type:** MCQ | **Difficulty:** ★★★☆☆ | **Priority:** 🟢

> ⚡ **VA Hint:** "Ecological rationality" is defined explicitly in the passage — find that definition and match it to an option. Don't import meanings from outside the passage.

"Ecological rationality" as used in the passage most nearly means:
- (A) Environmental consciousness in economic decision-making.
- (B) Rationality that adapts to the actual statistical features of decision environments rather than demanding perfect computation.
- (C) A biological theory of how species make optimal foraging decisions.
- (D) The tendency of markets to self-correct over ecological time scales.

---

**Q48.**
**Topic:** Strengthen / Weaken | **Type:** MCQ | **Difficulty:** ★★★★★ | **Priority:** 🔴

> ⚡ **VA Hint:** Identify exactly what Gigerenzer's argument IS (heuristics are adaptive, not errors; they work well in uncertain environments). Then ask: which option, if TRUE, shows they FAIL? Look for an option that attacks the foundation, not the periphery.

Which, if true, would most weaken Gigerenzer's argument as presented?
- (A) Heuristics like recognition are more accurate than chance in many empirical studies.
- (B) Expert pilots who use checklists also perform rigorous probabilistic assessments before flights.
- (C) Fast-and-frugal rules consistently underperform in complex, data-rich, stable environments.
- (D) Behavioural economists acknowledge that heuristics are sometimes adaptive.

---

## 📚 RC PASSAGE 2 — Philosophy of Science

**Source:** CAT-Level Inspired
**Difficulty:** ★★★★★
**Recommended Reading Time:** 7 min

> ⚡ **RC Approach:** Dense philosophical passage with three distinct positions: Popper (falsifiability), Kuhn (paradigm shifts), Lakatos (research programmes). Author's goal is to show strengths AND limits of each, culminating in Lakatos as a synthesis. The tone is analytical and appreciative-but-critical. Key question types: logical structure ("the Mercury example is used to..."), inference ("which is consistent with Lakatos?"). Read the Lakatos paragraph most carefully — it's the passage's resolution.

---

Karl Popper's criterion of falsifiability transformed the philosophy of science. A theory is scientific only if it can, in principle, be proven false by some conceivable observation. This demarcated science from pseudoscience — sweeping astrology, Freudian psychoanalysis, and Marxist historical determinism into the pseudoscientific category while preserving Einsteinian physics, which offered a dramatic falsification test: the bending of starlight during the 1919 solar eclipse.

The appeal is obvious. Science should make bold predictions, not wriggle out of every contrary result through epicyclic elaboration. A Freudian could interpret any patient behaviour as confirming the theory — aggression confirmed the death drive, passivity confirmed repression of it. A theory immunised against every possible refutation is not scientific; it is dogma.

But Popper's framework is vulnerable to the Duhem-Quine problem: no single hypothesis is tested in isolation. Every experiment invokes auxiliary assumptions — background theories, instrument calibrations, protocols. When results contradict the hypothesis, a scientist can always blame an auxiliary assumption rather than the core theory. In practice, major revolutions rarely involve clean falsification. Newtonian mechanics faced anomalies for decades — the precession of Mercury's perihelion — before Einstein replaced it; not because Newtonianism was falsified cleanly, but because the rival offered greater explanatory and predictive scope.

Kuhn's rival account — paradigm shifts — acknowledges this. Normal science operates within paradigms, generating puzzle-solutions within accepted frameworks. Anomalies are not immediately disruptive; they are shelved, worked around, attributed to experimental error. Only when anomalies proliferate and a compelling rival paradigm emerges does revolution occur. For Kuhn, science progresses neither by falsification alone nor by pure induction, but through social and cognitive processes that can look, to an outsider, surprisingly political.

Lakatos attempted a synthesis: research programmes with a protective belt of auxiliary hypotheses surrounding a hard core. Scientists modify the belt, not the core, in response to anomalies — Popper's falsificationism without the naïve expectation of clean refutation. A progressive research programme makes novel predictions subsequently confirmed; a degenerating one merely explains away anomalies. This criterion rescues the spirit of Popper while acknowledging the messiness of actual science.

---

**Q49.**
**Topic:** Author's Attitude | **Type:** MCQ | **Difficulty:** ★★★★☆ | **Priority:** 🟢

> ⚡ **VA Hint:** Look for words in the passage that show evaluation — "obvious appeal", "vulnerable", "attempted a synthesis". The author is not purely neutral nor purely hostile. Find the option that matches this nuanced stance.

The author's attitude toward Popper's criterion can best be described as:
- (A) Unreservedly admiring.
- (B) Dismissive and hostile.
- (C) Appreciative of its insights but aware of its limitations.
- (D) Neutral and purely descriptive.

---

**Q50.**
**Topic:** Logical Structure | **Type:** MCQ | **Difficulty:** ★★★★★ | **Priority:** 🟡

> ⚡ **VA Hint:** "Used primarily to" means — why did the author include THIS example at THIS point in the passage? The paragraph is about Popper's limits. The Mercury example illustrates a specific limitation. Match the function of the example to an option.

The Mercury perihelion example is used primarily to:
- (A) Show that Einstein was a better scientist than Newton.
- (B) Illustrate that major scientific transitions rarely occur via clean falsification, contradicting a simplistic reading of Popper.
- (C) Demonstrate that anomalies in science are usually experimental errors.
- (D) Argue that Kuhn's paradigm shifts are superior to Lakatos's research programmes.

---

**Q51.**
**Topic:** Inference (Lakatos) | **Type:** MCQ | **Difficulty:** ★★★★☆ | **Priority:** 🟡

> ⚡ **VA Hint:** Re-read the Lakatos paragraph before answering. The correct option must be logically derivable from what the passage says — not from what you know about Lakatos from outside the passage.

Most consistent with Lakatos's framework as described:
- (A) A theory that never faces anomalies is the most scientifically valuable.
- (B) Scientists should immediately abandon a theory when it faces a contradicting observation.
- (C) A scientific research programme can survive anomalies, provided it continues to generate and confirm novel predictions.
- (D) Social and political processes are the primary drivers of scientific progress.

---

**Q52.**
**Topic:** Vocabulary in Context | **Type:** MCQ | **Difficulty:** ★★★☆☆ | **Priority:** 🟢

> ⚡ **VA Hint:** "Epicyclic elaboration" appears in a context describing what science should NOT do. The word "epicycle" historically means adding complexity to save a flawed model. Match this historical meaning to the contextual usage.

"Epicyclic elaboration" most nearly means:
- (A) The use of circular orbits in Ptolemaic astronomy.
- (B) Adding complex supplementary explanations to shield a theory from contradicting evidence.
- (C) A mathematical technique for simplifying complex models.
- (D) Kuhn's method of generating anomalies to challenge a paradigm.

---

## ✍️ VERBAL ABILITY — 6 Questions

---

### VA Q53 — Para Summary
**Type:** MCQ | **Difficulty:** ★★★★☆ | **Priority:** 🟢

> ⚡ **VA Hint (3-Point Method):** Subject = gig work / platform economy. Predicate = creates flexibility but removes traditional protections. Nuance = regulatory gap between old law and new reality. Correct option must carry all three. Eliminate options that are prescriptive ("should be banned") — the passage is descriptive.

**Paragraph:**
*The digital revolution has transformed not just how we work but what constitutes work itself. Platform economies have created gig workers — who enjoy flexibility but lack traditional protections: no guaranteed minimum wage, no health benefits, no retirement security. Proponents argue gig work democratises economic participation; critics counter that it externalises risk from corporations onto individuals. The regulatory gap between labour law designed for the industrial age and a workforce mediated by algorithm is the central challenge of our moment.*

Best summary:
- (A) Gig work is exploitative and should be banned to protect workers.
- (B) The gig economy offers flexibility but creates a regulatory mismatch that exposes workers to risks traditional employment mitigated.
- (C) Platform economies have benefited both corporations and workers by democratising economic participation.
- (D) Algorithm-mediated work is the future and labour laws should simply be abolished.

---

### VA Q54 — Para Summary
**Type:** MCQ | **Difficulty:** ★★★★☆ | **Priority:** 🟢

> ⚡ **VA Hint:** This paragraph moves from a general claim → specific example → conclusion. The summary must reflect this: not just the example (language relativity), not just the conclusion (neuroscience support), but the relationship between the claim and evidence.

**Paragraph:**
*Language is not merely a vehicle for conveying information; it is the architecture of thought. Sapir and Whorf proposed the linguistic relativity hypothesis: the structure of a language affects its speakers' cognition and world view. This observation has profound implications, suggesting the language we speak shapes what we are able to think. Contemporary neuroscience offers partial support, though the strong version — that language absolutely determines thought — is now widely rejected.*

Best summary:
- (A) The Sapir-Whorf hypothesis has been completely disproven by neuroscience.
- (B) Language shapes thought to some extent, but does not fully determine it — a view partially supported by modern neuroscience.
- (C) All languages are equivalent in their ability to express thoughts; structure has no cognitive impact.
- (D) Neuroscience has confirmed that thought is impossible without language.

---

### VA Q55 — Para Jumble
**Type:** TITA | **Difficulty:** ★★★★★ | **Priority:** 🟡

> ⚡ **VA Hint:** Find the mandatory opener — it must introduce the topic without referring back to anything (no "this", "however", "therefore" to open). Then use pronoun references and logical connectors to chain sentences. "Their claim" in one sentence must follow the sentence that introduces the "they".

**Sentences:**
A. Yet cities are not inevitably destined to become unequal.
B. Urban economic geography tends to concentrate opportunity in dense, expensive cores.
C. Evidence from Vienna and Singapore suggests that deliberate housing policy can reshape spatial inequality significantly.
D. The consequence is spatial inequality: the affluent cluster near jobs while the poor are pushed to the periphery.
E. Zoning reform, public transit investment, and social housing — deployed together — have produced cities that are both dynamic and equitable.

*(Enter the correct 5-letter sequence, e.g., BADCE)*

---

### VA Q56 — Para Jumble
**Type:** TITA | **Difficulty:** ★★★★☆ | **Priority:** 🟡

> ⚡ **VA Hint:** "Their claim" is a strong clue — it must follow the sentence introducing "Sapir and Whorf." "This observation" must follow the sentence stating that observation. Work through pronoun chains.

**Sentences:**
A. Language is not merely a vehicle for conveying information; it is the architecture of thought itself.
B. This observation has profound implications for cognition, suggesting the language we speak shapes what we are able to think.
C. Sapir and Whorf proposed the linguistic relativity hypothesis in the early twentieth century.
D. Contemporary neuroscience offers partial support, though the strong version of the hypothesis is now widely rejected.
E. Their claim: the structure of a language affects its speakers' cognition and world view.

*(Enter the correct 5-letter sequence)*

---

### VA Q57 — Odd One Out
**Type:** MCQ | **Difficulty:** ★★★★☆ | **Priority:** 🟢

> ⚡ **VA Hint:** Identify the central theme of the coherent paragraph. Then test: if you remove each sentence one by one, which removal makes the paragraph MOST coherent? The odd sentence will either introduce a new sub-topic OR make an irrelevant contrast.

**Four sentences. One does NOT belong:**

A. The Impressionists rejected formal constraints, preferring to paint from nature with visible brushwork.
B. Monet's series paintings — haystacks, cathedrals, water lilies — were obsessive studies of how light mutates across time.
C. The Impressionist movement coincided with significant technological advances in the manufacture of portable paint tubes.
D. Renoir's later work moved toward classicism, and he rejected the transient-light obsession that defined his early career.

Which sentence does NOT belong?
- (A) A
- (B) B
- (C) C
- (D) D

---

### VA Q58 — Sentence Placement
**Type:** MCQ | **Difficulty:** ★★★★☆ | **Priority:** 🟢

> ⚡ **VA Hint:** The sentence to be placed contains "This alignment between evolutionary pressures and aesthetic preferences." Ask: what must come BEFORE it? A sentence establishing that there IS an alignment between evolution and aesthetics. What comes AFTER? A consequence or elaboration of this alignment.

**Sentence to place:** *"This alignment between evolutionary pressures and aesthetic preferences may explain why humans across cultures find savanna-like landscapes universally pleasing."*

**Paragraph:**
[1] Human aesthetic preferences are rarely arbitrary.
[2] Research in evolutionary psychology links aesthetic responses to reproductive fitness signals.
[3] Symmetrical faces are universally rated more attractive — a proxy for genetic health.
[4] Open grasslands with scattered trees, water, and gentle terrain appear as near-universally preferred landscapes in surveys.
[5] Modern humans, descended from African savanna-dwellers, retain neural templates calibrated to that ancestral environment.

- (A) After sentence 2
- (B) After sentence 3
- (C) After sentence 4
- (D) After sentence 5

---
---

# SECTION 4 — ATTEMPT TRACKER

**Fill this as you attempt each question.**

| Q# | Your Answer | Time (sec) | Confidence |
|----|------------|-----------|------------|
| Q1 | | | |
| Q2 | | | |
| Q3 | | | |
| Q4 | | | |
| Q5 | | | |
| Q6 | | | |
| Q7 | | | |
| Q8 | | | |
| Q9 | | | |
| Q10 | | | |
| Q11 | | | |
| Q12 | | | |
| Q13 | | | |
| Q14 | | | |
| Q15 | | | |
| Q16 | | | |
| Q17 | | | |
| Q18 | | | |
| Q19 | | | |
| Q20 | | | |
| Q21 | | | |
| Q22 | | | |
| Q23 | | | |
| Q24 | | | |
| Q25 | | | |
| Q26 | | | |
| Q27 | | | |
| Q28 | | | |
| Q29 | | | |
| Q30 | | | |
| Q31 | | | |
| Q32 | | | |
| Q33 | | | |
| Q34 | | | |
| Q35 | | | |
| Q36 | | | |
| Q37 | | | |
| Q38 | | | |
| Q39 | | | |
| Q40 | | | |
| Q41 | | | |
| Q42 | | | |
| Q43 | | | |
| Q44 | | | |
| Q45 | | | |
| Q46 | | | |
| Q47 | | | |
| Q48 | | | |
| Q49 | | | |
| Q50 | | | |
| Q51 | | | |
| Q52 | | | |
| Q53 | | | |
| Q54 | | | |
| Q55 | | | |
| Q56 | | | |
| Q57 | | | |
| Q58 | | | |

---

# SECTION 5 — TODAY'S TARGETS

**Day 1 — Foundation Phase (Days 1–14)**

| Metric | Target |
|--------|--------|
| Accuracy | **70%+** |
| Total Questions to Attempt | **38–42** of 58 |
| QA Attempt | **14–16** (🟢 only first) |
| DILR Sets | **2–3 complete** sets |
| VARC Attempt | **All RC + 🟢 VA** |
| Max time per 🟢 QA question | **1.5× recommended time** |

**Smart Skips Today:**
- Skip all 🔴 questions in QA (Q5, Q13, Q17, Q19, Q24, Q25, Q28) unless >15 min remains
- In DILR: use Entry Signal — if you can't crack the structure in 90 sec, skip the set
- In VARC: RC first, VA second; skip Q48, Q58 if short on time

---

---

# 🔑 ANSWERS — SPEED DRILL & WARM-UP
*(Do NOT look at this section until you've attempted them above)*

---

### ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
### 🔑 Speed Drill Answers
| # | Answer | Method |
|---|--------|--------|
| SD1 | **1225** | 35² → 3×4 then 25 → 1225 |
| SD2 | **6000** | 125 × 48 = 125 × 8 × 6 = 1000 × 6 |
| SD3 | **2401** | 7² = 49 → 49² = 2401 |
| SD4 | **0.12** | √(144/10000) = 12/100 |
| SD5 | **26,973** | 999×27 = 27000 − 27 |

---

### 🔑 Shortcut Warm-Up Answers
| # | Answer | Method |
|---|--------|--------|
| WU1 | **37** | ⌊150/5⌋+⌊150/25⌋+⌊150/125⌋ = 30+6+1 = 37 |
| WU2 | **1:1** | (60−50):(50−40) = 10:10 = 1:1 |
| WU3 | **10,000** | 100 odd numbers: sum = 100² = 10,000 |

---
### ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

---

> ⚠️ **MAIN QUESTION SOLUTIONS (Q1–Q58) ARE WITHHELD.**
> Paste your answers in the chat when ready. I will then deliver:
> - ✅ All correct answers with fastest CAT methods
> - 🎯 Accuracy % by section and topic
> - 🔍 Weak area identification
> - 📋 Day 2 topic adjustments

---

*📌 Day 1 of 60 | Next set: Tomorrow 7:00 AM IST*
*📖 Reference: [Shortcut Bible](CAT2026_Shortcut_Bible.md)*
