# ⚡ CAT 2026 — SHORTCUT & ACCURACY BIBLE
### 60-Day Sprint | 99+ Percentile Target
**Last Updated:** Day 1 | This document grows daily as new shortcuts are added.

---

> 💡 **The CAT Mantra:** *Speed without accuracy is dangerous. Accuracy without speed is fatal. Train both together.*

---

## 📌 HOW TO USE THIS BIBLE

- **Before attempting any question:** Check if a shortcut applies.
- **After every set:** Add any new trick you discovered here.
- **Daily revision:** Spend 10 minutes before your set scanning this document.
- **60-day goal:** Every shortcut here should become a reflex, not a recall.

---

---

# 🔢 PART 1: NUMBER SYSTEM SHORTCUTS

---

## 1.1 — Remainders (Most CAT-Tested Area)

### ⚡ Shortcut 1: Cyclicity of Remainders
When a^n is divided by m, the remainders follow a cycle.
Find the cycle length first, then use n mod (cycle length).

```
7^1 mod 6 = 1
7^2 mod 6 = 1
→ Every power of 7 mod 6 = 1  ✅ (cycle = 1)

2^1 mod 3 = 2, 2^2 mod 3 = 1, 2^3 mod 3 = 2...
→ Cycle = 2. For 2^100: 100 is even → remainder = 1  ✅
```

### ⚡ Shortcut 2: Euler's Theorem (Advanced)
If gcd(a, n) = 1 → a^φ(n) ≡ 1 (mod n)
- φ(p) = p-1 for prime p
- φ(p²) = p(p-1)
- φ(mn) = φ(m)·φ(n) if gcd(m,n)=1

**When to use:** Large powers mod composite numbers (CAT loves 10, 36, 100)

### ⚡ Shortcut 3: Sum of Powers Remainder
For 1^n + 2^n + 3^n + ... + k^n, find each remainder separately, sum, then mod.

**CAT Trap:** 9^1 + 9^2 + ... + 9^85 mod 6
→ 9 mod 6 = 3. So problem becomes 3^1 + 3^2 + ... + 3^85 mod 6
→ 3^1=3, 3^2=9≡3, every power of 3 mod 6 = 3
→ Sum = 3 × 85 = 255. 255 mod 6 = **3** ✅

### ⚡ Shortcut 4: Last Two Digits (Unit + Tens)
For last two digits, work mod 100.
- Powers of 7: cycle of 4 (07, 49, 43, 01, 07...)
- Powers of 3: cycle of 20 mod 100
- Powers ending in 1: last two digits always end in 1

---

## 1.2 — Factors & Divisibility

### ⚡ Shortcut 5: Number of Factors
If N = p^a × q^b × r^c, number of factors = (a+1)(b+1)(c+1)

### ⚡ Shortcut 6: Sum of Factors
Sum = [(p^(a+1)-1)/(p-1)] × [(q^(b+1)-1)/(q-1)] × ...

### ⚡ Shortcut 7: HCF-LCM Relationship
HCF × LCM = Product of two numbers *(only for 2 numbers)*
For more than 2 numbers: **this formula does NOT apply** — classic CAT trap.

### ⚡ Shortcut 8: Highest Power of Prime p in n!
Use Legendre's Formula:
⌊n/p⌋ + ⌊n/p²⌋ + ⌊n/p³⌋ + ...

```
Highest power of 2 in 100!:
= 50 + 25 + 12 + 6 + 3 + 1 = 97
```

### ⚡ Shortcut 9: Trailing Zeros in n!
= Highest power of 10 = min(power of 2, power of 5) = power of 5 (always smaller)

```
Trailing zeros in 100! = ⌊100/5⌋ + ⌊100/25⌋ = 20 + 4 = 24
```

---

## 1.3 — Digit Problems

### ⚡ Shortcut 10: Two-Digit Number Trick
If a 2-digit number has digits (a, b): value = 10a + b
Reversed: 10b + a. Difference = 9(a-b) — always a multiple of 9.
**CAT uses this constantly in digit reversal problems.**

---

---

# ➕ PART 2: ARITHMETIC SHORTCUTS

---

## 2.1 — Percentages (Speed Essentials)

### ⚡ Shortcut 11: Percentage ↔ Fraction Conversion (MEMORISE)
| % | Fraction | | % | Fraction |
|---|----------|-|---|----------|
| 12.5% | 1/8 | | 33.33% | 1/3 |
| 16.67% | 1/6 | | 66.67% | 2/3 |
| 20% | 1/5 | | 11.11% | 1/9 |
| 25% | 1/4 | | 8.33% | 1/12 |
| 37.5% | 3/8 | | 14.28% | 1/7 |

**CAT Trick:** Whenever you see these percentages, instantly convert to fractions for speed.

### ⚡ Shortcut 12: Successive Percentage Change
If price increases by a% then b%:
**Net change = a + b + (ab/100)%**

```
+20% then -20% = 20 + (-20) + (20×(-20)/100) = -4% (net loss)
This is why "same % up and down" always gives a net loss.
```

### ⚡ Shortcut 13: Profit-Loss on Cost Price vs. Selling Price
- If profit% given on CP: SP = CP × (1 + p/100)
- If profit% given on SP (rare, tricky): CP = SP × (1 - p/100)
**CAT Trap:** Always check whether % is on CP or SP.

---

## 2.2 — Time, Speed & Distance

### ⚡ Shortcut 14: Relative Speed
- Same direction: |v₁ - v₂|
- Opposite direction: v₁ + v₂

### ⚡ Shortcut 15: Meeting Point Formula
If A and B start from P and Q towards each other:
- **1st meeting:** A covers [d × vA/(vA+vB)] from P
- **2nd meeting:** Together they cover 3d total. A covers 3 × [d × vA/(vA+vB)] from P (subtract d if > d)

```
A=50, B=25, d=300:
1st meeting: A covers 300×50/75 = 200 km from A
2nd meeting: A covers 3×200 = 600 km from A → 600-300=300 → 300-300=0? 
Re-check: 600 mod 300... A covers 600 from A. He reaches B at 300, returns. 
Remaining = 600-300 = 300 from B = 0 from A. 
Actual: use the formula carefully with direction reversals.
```

### ⚡ Shortcut 16: Boats & Streams
- Downstream = u + v (u=boat speed, v=stream speed)
- Upstream = u - v
- u = (D+U)/2, v = (D-U)/2

### ⚡ Shortcut 17: Trains
- Train crossing a pole/person: time = length of train / speed
- Train crossing a platform: time = (train length + platform length) / speed

---

## 2.3 — Time & Work

### ⚡ Shortcut 18: LCM Method (Fastest for CAT)
Assume total work = LCM of given days.
Convert to work/day units. No fractions needed.

```
A takes 12 days, B takes 15 days.
LCM = 60. A does 5 units/day, B does 4 units/day.
Together: 9 units/day → 60/9 = 6.67 days
```

### ⚡ Shortcut 19: Efficiency Method
If A is k times as efficient as B, A takes (1/k) times the time.

---

## 2.4 — Mixtures & Alligation

### ⚡ Shortcut 20: Alligation Cross Method
```
Cheaper price        Costlier price
     c          :         d
          \           /
           Mean price (m)
          /           \
      (d-m)       :      (m-c)

Ratio of quantities = (d-m) : (m-c)
```

### ⚡ Shortcut 21: Repeated Replacement
After k replacements of x litres from V litres:
Fraction of original = ((V-x)/V)^k

---

## 2.5 — Simple & Compound Interest

### ⚡ Shortcut 22: CI-SI Difference
- For 2 years: CI - SI = P(r/100)²
- For 3 years: CI - SI = P(r/100)² × (3 + r/100)

### ⚡ Shortcut 23: Rule of 72
Approximate years to double at r% = 72/r
At 12%: doubles in 6 years. (CAT uses this in approximation Qs)

---

---

# 📐 PART 3: ALGEBRA SHORTCUTS

---

## 3.1 — Quadratic & Polynomial

### ⚡ Shortcut 24: Vieta's Formulas
For ax² + bx + c = 0:
- α + β = -b/a
- αβ = c/a
- α² + β² = (α+β)² - 2αβ
- α³ + β³ = (α+β)³ - 3αβ(α+β)
- α³ + β³ = (α+β)(α²-αβ+β²)

**Never expand unless forced. Always use Vieta's.**

### ⚡ Shortcut 25: Nature of Roots (Discriminant)
D = b² - 4ac
- D > 0: Two distinct real roots
- D = 0: Equal roots
- D < 0: No real roots (complex)
- D = perfect square: Rational roots

---

## 3.2 — Inequalities

### ⚡ Shortcut 26: Wavy Curve Method
For (x-a)(x-b)(x-c) > 0 where a < b < c:
Draw number line, mark a, b, c. Sign alternates starting + from rightmost.

### ⚡ Shortcut 27: AM-GM Inequality
For positive numbers: AM ≥ GM
(a+b)/2 ≥ √(ab)
**Equality when a = b.**
CAT uses this to find minimum/maximum of expressions.

### ⚡ Shortcut 28: Modulus Shortcuts
|x - a| < k → a-k < x < a+k
|x - a| + |x - b| ≥ |a - b| (triangle inequality)
Minimum of |x-a| + |x-b| = |a-b| (when x is between a and b)

---

## 3.3 — Logarithms

### ⚡ Shortcut 29: Log Rules (Drill These Cold)
```
log(mn) = log m + log n
log(m/n) = log m - log n
log(m^k) = k·log m
log_b(a) = log(a)/log(b)  [Change of base]
log_b(b) = 1
log_b(1) = 0
log_a(b) × log_b(a) = 1
```

### ⚡ Shortcut 30: Nested Log Trick
log₂(log₃(log₄(x))) = 0
→ log₃(log₄(x)) = 2⁰ = 1
→ log₄(x) = 3¹ = 3
→ x = 4³ = **64** ✅
*Work from outside in.*

---

## 3.4 — Functions & Graphs

### ⚡ Shortcut 31: Max/Min of f(x) = max(g(x), h(x))
Set g(x) = h(x) to find the intersection point.
Minimum of the max-function occurs at the intersection.

```
f(x) = max(2x+1, 3-4x)
Set equal: 2x+1 = 3-4x → 6x = 2 → x = 1/3
f(1/3) = 2(1/3)+1 = 5/3
```

---

## 3.5 — Progressions

### ⚡ Shortcut 32: AP Formulas
- nᵗʰ term: a + (n-1)d
- Sum: n/2 × (2a + (n-1)d) = n/2 × (first + last)

### ⚡ Shortcut 33: GP Shortcut
- Sum of n terms: a(rⁿ-1)/(r-1) for r≠1
- If last term (l) is known: Sum = (lr - a)/(r-1)
- For infinite GP (|r|<1): Sum = a/(1-r)

### ⚡ Shortcut 34: GP — Finding n from Sum
If Sn = 255, S(n-1) = 127, first term = 1:
→ Last term = Sn - S(n-1) = 255 - 127 = 128 = 2^7
→ Since a=1, r=2: last term = 2^(n-1) = 128 = 2^7 → n-1=7 → **n=8** ✅

---

---

# 📏 PART 4: GEOMETRY SHORTCUTS

---

## 4.1 — Circles

### ⚡ Shortcut 35: Intersecting Chords
PA × PB = PC × PD (Power of a Point)

```
AP=4, PB=9, CP=6: 4×9 = 6×PD → PD = 6 ✅
```

### ⚡ Shortcut 36: Tangent-Secant
(Tangent)² = External × Whole secant

### ⚡ Shortcut 37: Angles in Circles
- Inscribed angle = ½ × Central angle (same arc)
- Angle in semicircle = 90°
- Tangent-chord angle = Inscribed angle in alternate segment

---

## 4.2 — Triangles

### ⚡ Shortcut 38: Area Formulas (Know All)
- Base × Height / 2
- (1/2)ab·sin C
- √[s(s-a)(s-b)(s-c)] — Heron's formula
- r × s (r = inradius, s = semi-perimeter)
- abc / (4R) (R = circumradius)

### ⚡ Shortcut 39: Special Triangles
| Triangle | Sides | Area |
|----------|-------|------|
| 30-60-90 | 1:√3:2 | (√3/4)a² for equilateral side a |
| 45-45-90 | 1:1:√2 | — |
| Equilateral side a | a:a:a | (√3/4)a² |

### ⚡ Shortcut 40: Similar Triangle Ratio
If sides ratio = k, then:
- Area ratio = k²
- Volume ratio = k³

```
Inscribed equilateral inside circle inside equilateral:
Inner triangle side = half of outer → Area ratio = 1/4
```

---

## 4.3 — Mensuration

### ⚡ Shortcut 41: Cone Cut Parallel to Base
If a cone of height H and radius R is cut at height h from apex:
- Small cone height = h, radius = R × h/H
- Volume of small cone = (1/3)π(Rh/H)²h
- Remaining fraction = 1 - (h/H)³

```
Cut at half height: remaining = 1 - (1/2)³ = 1 - 1/8 = 7/8
```

---

## 4.4 — Coordinate Geometry

### ⚡ Shortcut 42: Area of Triangle from Lines
Find the three vertices (intersection points of each pair of lines).
Use: Area = (1/2)|x₁(y₂-y₃) + x₂(y₃-y₁) + x₃(y₁-y₂)|

---

---

# 🎲 PART 5: MODERN MATH SHORTCUTS

---

## 5.1 — Permutation & Combination

### ⚡ Shortcut 43: The STOP & CHECK Framework
Before any P&C question, identify:
1. Are objects distinct or identical?
2. Are positions distinct or identical?
3. Are there restrictions?

### ⚡ Shortcut 44: Divisibility by 5 (Digit Problems)
Numbers divisible by 5 must end in 0 or 5.
Case 1: Last digit = 0. Fill remaining positions freely.
Case 2: Last digit = 5. First digit ≠ 0.
**Always split into cases.**

### ⚡ Shortcut 45: Distribution Tricks
- n identical items into r distinct groups (0 allowed): C(n+r-1, r-1)
- n identical items into r distinct groups (at least 1 each): C(n-1, r-1)

---

## 5.2 — Probability

### ⚡ Shortcut 46: Two Dice — Sum Probabilities
| Sum | Combinations | Probability |
|-----|-------------|-------------|
| 2 | 1 | 1/36 |
| 7 | 6 | 6/36 (most likely) |
| 12 | 1 | 1/36 |
| Prime sums (2,3,5,7,11) | 1+2+4+6+2=15 | 15/36 = 5/12 |

### ⚡ Shortcut 47: Complementary Counting
P(at least one) = 1 - P(none)
Use this when "none" is easier to calculate.

---

## 5.3 — Set Theory

### ⚡ Shortcut 48: Three-Set Inclusion-Exclusion
|A∪B∪C| = |A|+|B|+|C| - |A∩B| - |B∩C| - |A∩C| + |A∩B∩C|
Those studying none = Total - |A∪B∪C|

---

---

# 🧩 PART 6: DILR SHORTCUTS & FRAMEWORKS

---

## 6.1 — Seating Arrangements

### ⚡ Framework 1: Fixed Anchor Method
1. Find the most constrained position first (given directly)
2. Use it as anchor
3. Fill remaining using elimination

### ⚡ Framework 2: Contradiction Check
Before finalising any arrangement, verify ALL conditions.
CAT often gives 4-5 conditions — miss one = wrong answer.

---

## 6.2 — Venn Diagram / Survey Sets

### ⚡ Framework 3: Inner-Out Method
Fill from innermost (all three) outward.
- Only A∩B (not C) = (A∩B) - (A∩B∩C)
- Only A = A - (A∩B) - (A∩C) + (A∩B∩C)

### ⚡ Framework 4: Quick Sanity Check
Sum of all regions = Total. Always verify.

---

## 6.3 — Tournaments

### ⚡ Framework 5: Total Matches = nC2
For n teams round robin: n(n-1)/2 total matches.
Total points distributed = 2 × total matches (since each match gives 2 pts total).

```
5 teams: 5×4/2 = 10 matches. Total points = 20.
P+Q+R+S+T = 6+4+4+2+0 = 16 ≠ 20 → Check for draws!
```

### ⚡ Framework 6: Elimination Constraint
If a team has 0 points → lost all matches.
If a team has maximum possible points → won all matches.
Use to reconstruct match results.

---

## 6.4 — Network/Routes

### ⚡ Framework 7: Dijkstra's Mental Algorithm
1. Start from source, distance = 0.
2. At each step, pick unvisited node with minimum current distance.
3. Update neighbour distances.
4. Mark visited. Repeat.

```
M→N→O→P→Q = 4+2+1+3 = 10 hrs ✅ (Minimum)
```

---

---

# 📖 PART 7: VARC SHORTCUTS & FRAMEWORKS

---

## 7.1 — Reading Comprehension

### ⚡ Framework 8: The 4-Step RC Method (TIME Standard)
1. **Read the first and last sentence** of each paragraph (30 sec)
2. **Identify the author's stance** — does the author agree, disagree, or present balanced view?
3. **Map the paragraph structure** — contrast, example, counter-argument?
4. **Attack questions in this order:** Main Idea → Inference → Vocabulary → Strengthen/Weaken

### ⚡ Framework 9: Elimination for RC Options
CAT RC wrong options follow patterns:
- **Too extreme** (always, never, all, none)
- **Out of scope** (true but not mentioned)
- **Opposite** (direct contradiction)
- **Partially correct** (correct first half, wrong second half)

---

## 7.2 — Para Jumbles

### ⚡ Framework 10: Sentence Connector Method
1. Find the **mandatory first sentence** — introduces topic, no pronoun reference, no "however/but/therefore" start.
2. Find **mandatory last sentence** — conclusion, summary, or result.
3. Find **connector pairs** (pronouns, demonstratives, logical connectors).
4. Use elimination if stuck — wrong options violate these rules.

### ⚡ Para Jumble Connectors to Watch
- "This/That/These/Those" → refers to previous sentence
- "However/But" → contrasts with previous
- "Therefore/Thus/Hence" → conclusion from previous
- "For example/For instance" → follows a general claim

---

## 7.3 — Odd One Out

### ⚡ Framework 11: Theme Coherence Test
All sentences in OOO form one coherent paragraph. The odd sentence:
- Introduces a different sub-topic
- Breaks the logical flow
- Makes an irrelevant contrast

**Test:** Remove each sentence one by one. The paragraph that reads most coherently after removal identifies the odd sentence.

---

## 7.4 — Para Summary

### ⚡ Framework 12: The 3-Point Summary Method
1. **Subject** — what/who is the paragraph about?
2. **Predicate** — what is being said about it?
3. **Nuance** — any qualification, contrast, or caveat?

Correct option must capture all 3. Options that overstate or miss the nuance are wrong.

---

---

# 🎯 PART 8: ACCURACY TRAINING PROTOCOL

---

## The 60-Day Accuracy Framework

### Week 1–2: Foundation (Target: 70% accuracy)
- Attempt only 🟢 Must Attempt questions
- No guessing on MCQs unless >50% confident
- Skip TITA if unsure (no negative marking)
- After every set: identify 1 concept gap and revise it

### Week 3–4: Building (Target: 78% accuracy)
- Add 🟡 questions to your attempt list
- Start timed practice (use Recommended Time per question)
- Track time per question in Attempt Tracker
- Goal: Never exceed 1.5x recommended time

### Week 5–6: Consolidation (Target: 83% accuracy)
- Full 58-question sets under exam conditions
- Attempt strategy: QA first or VARC first? Test both in mock.
- Identify your "confidence zone" — topics where accuracy > 85%

### Week 7–8 (Last 2 weeks): Sharpening (Target: 87%+ accuracy)
- Only strong areas: attempt more qs, higher difficulty
- Weak areas: selective — only high-confidence questions
- Stop learning new concepts. Consolidate known ones.

---

## ⚡ The STAR Accuracy System (Use Every Question)

**S — Scan:** Read the question once fast. Identify what's being asked.
**T — Trap Check:** What's the likely CAT trap here? (Wrong formula? Missed case?)
**A — Apply:** Apply the fastest known method.
**R — Review:** Does the answer feel reasonable? Check units, signs, scale.

---

## 🔴 Common CAT Traps by Topic

| Topic | Most Common Trap |
|-------|-----------------|
| HCF/LCM | Applying HCF×LCM=Product to 3+ numbers |
| Percentage | Forgetting that % change is on different bases |
| CI/SI | Using SI formula for CI problems |
| Averages | Adding wrong number of elements |
| P&C | Forgetting cases where first digit = 0 |
| Probability | Sampling with/without replacement |
| Geometry | Assuming figure is to scale |
| Logarithms | log(a+b) ≠ log a + log b |
| Functions | Domain restrictions |
| Para Jumbles | Assuming the most natural-sounding order is correct |

---

## 📊 Daily Accuracy Log (Fill After Every Set)

| Date | QA Accuracy | DILR Accuracy | VARC Accuracy | Overall | Weak Area |
|------|-------------|---------------|---------------|---------|-----------|
| Day 1 | | | | | |
| Day 2 | | | | | |
| Day 3 | | | | | |
| Day 4 | | | | | |
| Day 5 | | | | | |
| Day 6 | | | | | |
| Day 7 | | | | | |

*(This table will be updated as you submit answers)*

---

## 🧠 Mental Math Drills (5 min daily warmup)

Practice these before every session:

### Multiplication Tricks
- ×11: Add adjacent digits (e.g., 73×11 = 7_(7+3)_3 = 803)
- ×25: Divide by 4, multiply by 100
- ×125: Divide by 8, multiply by 1000
- ×99: Multiply by 100, subtract the number

### Squaring Tricks
- Numbers ending in 5: (a5)² = a(a+1) followed by 25
  - 35² = 3×4 | 25 = 1225
  - 65² = 6×7 | 25 = 4225
- Numbers near 100: (100-a)² = (100-2a) | a²
  - 97² = 94 | 09 = 9409
  - 96² = 92 | 16 = 9216

### Division Tricks
- ÷7: Multiply by 1/7 ≈ 0.1428... (memorise)
- ÷9: Numerator/(9...9) → use decimal expansion
- ÷11: Alternating digit sum rule for divisibility

---

## 📐 Must-Memorise Values

### Squares (1–30)
1,4,9,16,25,36,49,64,81,100,121,144,169,196,225,256,289,324,361,400,441,484,529,576,625,676,729,784,841,900

### Cubes (1–15)
1,8,27,64,125,216,343,512,729,1000,1331,1728,2197,2744,3375

### Powers of 2 (1–20)
2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072,262144,524288,1048576

### Powers of 3 (1–10)
3,9,27,81,243,729,2187,6561,19683,59049

### √ Values
√2=1.414, √3=1.732, √5=2.236, √6=2.449, √7=2.646, √8=2.828, √10=3.162

---

## 🎯 CAT Attempt Strategy (60-Day Target)

### Ideal Attempt Distribution

| Section | Total Qs | Target Attempt | Target Correct | Net Score Target |
|---------|----------|---------------|----------------|-----------------|
| QA | 22 | 16–18 | 13–14 | ~39–42 |
| DILR | 20 | 14–16 | 11–13 | ~33–39 |
| VARC | 24 | 20–22 | 17–19 | ~51–57 |
| **Total** | **66** | **50–56** | **41–46** | **~123–138** |

*(CAT 2026 exact format may vary — adjust based on official notification)*

### The 99+ Percentile Formula
1. **VARC:** Attempt 20+, accuracy 80%+ — this section has highest score ceiling
2. **DILR:** Pick 3 easiest sets completely — don't touch difficult sets partially
3. **QA:** Attempt only what you're confident about — CAT rewards selectivity

---

*📎 This document is updated after every session with new shortcuts as they arise.*
*Last updated: Day 1 | Next update after Day 2 set.*
