# CAT 2026 — DAILY MASTER SET
## Day 54 | Actual CAT Difficulty → 99+ Percentile Track

**Target time: 120 minutes**

| Section | Questions | Target Time |
|---|---:|---:|
| QA | 12 | 40 min |
| DILR | 8 | 40 min |
| VARC | 14 | 40 min |

### Today's progression
- **QA:** More emphasis on selecting the correct representation rather than brute-force calculation.
- **DILR:** Arrangement constraints + multi-variable DI.
- **VARC:** Inference and author's-position questions are deliberately closer to the upper CAT difficulty band.
- **99+ focus:** Don't spend 3 minutes calculating a problem whose structure can be identified in 30 seconds.

**Source policy:** Every question below is **CAT-level inspired**. I am not falsely labelling generated questions as CAT PYQs.

---

# SECTION I — QUANTITATIVE APTITUDE

## ARITHMETIC

### Q1. CAT-level inspired
**Topic:** Time & Work | **Type:** MCQ | **Difficulty:** 4/5 | **Recommended time:** 1.5 min

A can complete a work in 18 days and B can complete the same work in 24 days. They work together for 6 days, after which A leaves. B completes the remaining work alone.

How many more days does B need?

A. 8  
B. 10  
C. 12  
D. 14

---

### Q2. CAT-level inspired
**Topic:** Mixtures & Alligation | **Type:** TITA | **Difficulty:** 4/5 | **Recommended time:** 2 min

A vessel contains 60 litres of pure milk. Twelve litres are removed and replaced with water. The process is repeated once more.

How many litres of milk remain in the vessel?

---

### Q3. CAT-level inspired
**Topic:** Time, Speed & Distance | **Type:** TITA | **Difficulty:** 4/5 | **Recommended time:** 1.5 min

A person travels from A to B at 50 km/h and returns from B to A at 75 km/h. The total time taken for the complete journey is 5 hours.

Find the distance between A and B.

---

# ALGEBRA

### Q4. CAT-level inspired
**Topic:** Modulus | **Type:** MCQ | **Difficulty:** 5/5 | **Recommended time:** 2 min

For real \(x\),

\[
|x-1|+|x-4|=7.
\]

The complete solution set is:

A. \(\{-1,6\}\)  
B. \([-1,6]\)  
C. \(x\leq -1\) or \(x\geq6\)  
D. \(\{-3,7\}\)

---

### Q5. CAT-level inspired
**Topic:** Quadratic Equations / Symmetric Expressions | **Type:** TITA | **Difficulty:** 5/5 | **Recommended time:** 2 min

If \(\alpha\) and \(\beta\) are the roots of

\[
x^2-8x+11=0,
\]

find

\[
\frac{\alpha^3+\beta^3}{\alpha\beta}.
\]

---

# GEOMETRY

### Q6. CAT-level inspired
**Topic:** Right Triangle / Altitude to Hypotenuse | **Type:** TITA | **Difficulty:** 4/5 | **Recommended time:** 2 min

In a right-angled triangle, the altitude from the right angle to the hypotenuse divides the hypotenuse into segments of lengths 9 cm and 16 cm.

Find the area of the triangle.

---

### Q7. CAT-level inspired
**Topic:** Circle / Tangent | **Type:** TITA | **Difficulty:** 4/5 | **Recommended time:** 1 min

A tangent is drawn from an external point P to a circle with centre O and radius 8 cm.

If

\[
OP=17\text{ cm},
\]

find the length of the tangent.

---

# NUMBER SYSTEM

### Q8. CAT-level inspired
**Topic:** Number of Divisors | **Type:** MCQ | **Difficulty:** 5/5 | **Recommended time:** 2 min

How many positive divisors of

\[
N=2^5\cdot3^4\cdot5^2\cdot7
\]

are divisible by

\[
420?
\]

A. 24  
B. 32  
C. 36  
D. 40

---

### Q9. CAT-level inspired
**Topic:** Remainders / Cyclicity | **Type:** TITA | **Difficulty:** 4/5 | **Recommended time:** 1.5 min

Find the remainder when

\[
10^{100}+10^{101}+10^{102}
\]

is divided by 7.

---

# MODERN MATH

### Q10. CAT-level inspired
**Topic:** Permutations / Divisibility | **Type:** TITA | **Difficulty:** 5/5 | **Recommended time:** 3 min

Using each of the digits

\[
0,1,2,3,4,5,6
\]

at most once, how many **5-digit numbers divisible by 5** can be formed?

---

### Q11. CAT-level inspired
**Topic:** Conditional Probability | **Type:** MCQ | **Difficulty:** 4/5 | **Recommended time:** 1.5 min

A bag contains 4 red, 3 blue and 2 green balls. Two balls are drawn simultaneously.

Given that **at least one ball is red**, what is the probability that **both balls are red**?

A. \(\frac{1}{13}\)  
B. \(\frac{3}{13}\)  
C. \(\frac{4}{13}\)  
D. \(\frac{6}{13}\)

---

# Q12 — MIXED 99+ PERCENTILE CHALLENGE

**Topic:** Number Theory + Perfect Squares + Pythagorean Triples  
**Type:** TITA | **Difficulty:** 5/5 | **Recommended time:** 4 min

\(x\) and \(y\) are positive integers satisfying

\[
x+y=70
\]

and

\[
xy
\]

is a perfect square.

Find the sum of \(xy\) over **all ordered pairs** \((x,y)\).

---

# SECTION II — DILR

# SET 1 — SEVEN PRESENTATIONS

Seven speakers — **A, B, C, D, E, F and G** — are scheduled in seven consecutive slots, numbered 1 to 7.

The following conditions apply:

1. A speaks before D.
2. B speaks immediately before C.
3. E speaks after A.
4. F cannot speak in slot 1 or slot 7.
5. G speaks before B.

---

### Q13.
Which of the following speakers **can** occupy slot 1?

A. A or G  
B. A or D  
C. D or G  
D. A, D or G

---

### Q14.
If C occupies slot 5, how many valid schedules are possible?

A. 10  
B. 12  
C. 14  
D. 16

---

### Q15.
If D occupies slot 7, how many valid schedules are possible?

A. 18  
B. 20  
C. 22  
D. 24

---

### Q16.
If A occupies slot 3, how many valid schedules are possible?

A. 4  
B. 6  
C. 8  
D. 10

---

# SET 2 — STORE SALES

Four stores A, B, C and D record sales of products P, Q and R in two quarters. Values are in ₹ lakh.

| Store | Q1-P | Q1-Q | Q1-R | Q2-P | Q2-Q | Q2-R |
|---|---:|---:|---:|---:|---:|---:|
| A | 40 | 30 | 20 | 50 | 35 | 25 |
| B | 35 | 25 | 30 | 45 | 30 | 35 |
| C | 50 | 20 | 25 | 55 | 30 | 30 |
| D | 30 | 40 | 25 | 35 | 50 | 35 |

---

### Q17.
Which store had the highest total sales in Q2?

A. A  
B. B  
C. C  
D. D

---

### Q18.
By approximately what percentage did total sales across all four stores increase from Q1 to Q2?

**Type:** TITA

---

### Q19.
What is the ratio of total sales of product P to product R in Q2?

A. \(37:25\)  
B. \(25:37\)  
C. \(15:11\)  
D. \(11:15\)

---

### Q20.
Store D's Q2 sales constitute what fraction of the total Q2 sales?

A. \(\frac{24}{91}\)  
B. \(\frac{25}{91}\)  
C. \(\frac{24}{95}\)  
D. \(\frac{25}{95}\)

---

# SECTION III — VARC

# RC 1 — THE LIMITS OF MEASUREMENT

### Passage

Measurement is often treated as though it merely records features of the world that already exist independently of the observer. Yet measurement is never entirely separable from decisions about what counts as relevant. Before a phenomenon can be measured, someone must determine which aspect of it deserves to be represented numerically, what units are appropriate, and what level of precision matters.

This does not make measurement arbitrary. Once a measurement system has been specified, observations can often be made with remarkable consistency, and different observers can reproduce the same result. The important point is rather that consistency within a system should not be confused with neutrality in the choice of the system itself.

This distinction becomes especially important when measurements are used to guide policy. A government that chooses unemployment as a central indicator may obtain a very different picture of economic well-being from one that gives equal prominence to job security, working hours or household debt. The numbers may be accurate in both cases. What differs is the aspect of reality that the measurement framework makes visible.

Measurement therefore does not simply reveal reality; it also organises attention. The challenge is not to eliminate judgment from measurement—which may be impossible—but to make the judgments embedded in measurement sufficiently explicit to permit informed evaluation.

---

### Q21.
The central argument of the passage is that:

A. measurement is inherently subjective and therefore unreliable.  
B. measurement can be consistent and useful while still reflecting prior choices about what to measure and how.  
C. numerical measurements are less useful than qualitative observations in policymaking.  
D. governments deliberately manipulate measurements to produce misleading conclusions.

---

### Q22.
The author mentions unemployment, job security and household debt primarily to:

A. demonstrate that unemployment is an inaccurate economic indicator.  
B. show that different measurement frameworks can make different aspects of the same reality visible.  
C. argue that household debt is the most important measure of economic well-being.  
D. prove that government policy should avoid numerical indicators.

---

### Q23.
Which of the following can be most reasonably inferred?

A. If two observers obtain the same measurement, their underlying assumptions must also be identical.  
B. A measurement may be reproducible without the choice of what was measured being completely neutral.  
C. Measurement systems cannot be compared with one another.  
D. Any measurement involving human judgment is necessarily inaccurate.

---

### Q24.
The author's attitude toward measurement is best described as:

A. dismissive  
B. cautiously critical  
C. hostile  
D. unreservedly enthusiastic

---

# RC 2 — MEMORY AND FORGETTING

### Passage

Institutions often preserve the past through archives, monuments and official records. Such preservation is valuable because memory is vulnerable to disappearance: documents decay, witnesses die and experiences that were never recorded can become difficult to recover. Yet preservation is not the opposite of forgetting. Every archive has limits, and every act of preservation involves selection.

The decision to preserve one document rather than another may reflect practical constraints, political priorities or assumptions about what future generations will consider important. A monument may commemorate an event while simultaneously leaving other experiences outside the public narrative. Even a comprehensive digital archive cannot escape selection completely, because the categories used to organise information influence how it will later be searched and interpreted.

This does not mean that archives are simply instruments of manipulation. Their partiality is often unavoidable rather than deliberate. The more useful response is therefore not to demand a perfectly complete record—which may be impossible—but to cultivate awareness of what has been preserved, what has been excluded and why.

Historical understanding consequently requires both attention to records and sensitivity to their absences. What is missing from an archive may not tell us exactly what happened, but the pattern of absence can itself reveal something about the conditions under which the archive was created.

---

### Q25.
The primary purpose of the passage is to:

A. argue that archives are politically manipulated and should not be trusted.  
B. explain why preservation of history is valuable but necessarily selective, making absences important to historical interpretation.  
C. demonstrate that digital archives are superior to physical archives.  
D. argue that historical records are too incomplete to be useful.

---

### Q26.
The statement that “preservation is not the opposite of forgetting” means that:

A. preserving records is actually a form of forgetting.  
B. even systems designed to preserve information inevitably leave some things unrecorded or less visible.  
C. people should stop creating archives because forgetting is unavoidable.  
D. archives deliberately erase inconvenient historical events.

---

### Q27.
Which of the following can be inferred from the passage?

A. Every omission from an archive was deliberate.  
B. The absence of evidence can sometimes provide information about the circumstances in which a record was created.  
C. A complete archive would eliminate the need for historical interpretation.  
D. Digital archives are immune to the biases of classification.

---

### Q28.
The author would most likely disagree with which statement?

A. Historical interpretation should consider both preserved records and significant absences.  
B. The limitations of archives do not automatically make them useless.  
C. A perfectly complete historical archive is a realistic standard that institutions should be expected to achieve.  
D. Selection can occur even without deliberate manipulation.

---

# VERBAL ABILITY

## Q29 — Para Jumble

1. This is why the apparent objectivity of a dataset can be misleading.  
2. Data are often treated as though they simply exist, waiting to be collected.  
3. Yet collecting data requires decisions about what should count as relevant information.  
4. Those decisions determine which features of a phenomenon become visible.

**Type:** TITA

---

## Q30 — Para Jumble

1. The archive therefore records not merely the past but also the priorities of those who preserved it.  
2. Historical records are indispensable because memories and experiences can disappear.  
3. Yet preservation always involves some degree of selection.  
4. What survives in an archive may consequently reflect practical or institutional choices.

**Type:** TITA

---

## Q31 — Para Summary

Measurement provides consistent ways of representing aspects of reality, but the decision about what to measure and how to measure it involves judgment. Consequently, accurate measurements can still highlight some aspects of a phenomenon while leaving others less visible.

A. Measurement is subjective and therefore cannot produce reliable knowledge.  
B. Measurement can be reliable while still reflecting choices about which aspects of reality are made visible.  
C. Numerical measurement should be replaced by qualitative analysis.  
D. Measurement is useful only when observers disagree about what to measure.

---

## Q32 — Para Summary

Archives preserve valuable evidence about the past, but they are necessarily selective because preservation involves practical and institutional choices. Therefore, historians should examine both what archives contain and what patterns of absence may reveal about the circumstances in which those records were created.

A. Archives are unreliable because they inevitably omit information.  
B. Archives should be abandoned because complete historical records are impossible.  
C. Historical interpretation should consider both preserved evidence and the significance of archival absences.  
D. Institutional archives are always politically manipulated.

---

## Q33 — Odd One Out

A. Measurement requires decisions about what should be considered relevant.  
B. Measurement can be reproducible even when its framework reflects prior choices.  
C. Measurement frameworks can influence which aspects of reality receive attention.  
D. Measurements are valuable only when they eliminate every form of human judgment.

---

## Q34 — Sentence Placement

Sentence:

**“This makes the choice of a measurement framework an important part of the reasoning process rather than a merely technical preliminary.”**

Where should it be inserted?

1. Measurement is often treated as though it simply records features of the world.  
2. Yet before something can be measured, decisions must be made about what counts as relevant.  
3. Different choices can therefore make different aspects of a phenomenon visible.  
4. Once a measurement system has been specified, observations may nevertheless be highly consistent.  
5. Consistency within a system should not be confused with neutrality in choosing that system.

A. Before 1  
B. Between 1 and 2  
C. Between 2 and 3  
D. Between 3 and 4

---

# ⛔ STOP HERE — ATTEMPT BEFORE READING SOLUTIONS

### QA
**1-__ 2-__ 3-__ 4-__ 5-__ 6-__  
7-__ 8-__ 9-__ 10-__ 11-__ 12-__**

### DILR
**13-__ 14-__ 15-__ 16-__  
17-__ 18-__ 19-__ 20-__**

### VARC
**21-__ 22-__ 23-__ 24-__  
25-__ 26-__ 27-__ 28-__  
29-__ 30-__ 31-__ 32-__ 33-__ 34-__**

---

# DETAILED SOLUTIONS

# QUANT

## Q1 — **B, 10 days**

Take total work as LCM of 18 and 24:

\[
72.
\]

A's rate:

\[
72/18=4.
\]

B's rate:

\[
72/24=3.
\]

Together:

\[
4+3=7.
\]

In 6 days:

\[
6\times7=42.
\]

Remaining:

\[
72-42=30.
\]

B alone takes:

\[
30/3=\boxed{10}.
\]

**Answer: B**

**Source:** CAT-level inspired  
**Topic:** Time & Work  
**Difficulty:** 4/5  
**Recommended time:** 1.5 min  

**Time-saving shortcut:** Use LCM units instead of fractional work rates.

**Common trap:** Calculating the remaining fraction incorrectly.

**Key concept revision:**

\[
\text{Work}=\text{Rate}\times\text{Time}.
\]

**Alternate method:**

\[
6\left(\frac1{18}+\frac1{24}\right)
=\frac7{12}
\]

so \(5/12\) remains; B takes

\[
\frac{5/12}{1/24}=10.
\]

---

## Q2 — **38.4 litres**

Each replacement retains:

\[
1-\frac{12}{60}
=
\frac45
\]

of the milk.

After two repetitions:

\[
60\left(\frac45\right)^2
=
60\cdot\frac{16}{25}
=
\boxed{38.4}.
\]

**Source:** CAT-level inspired  
**Topic:** Mixtures  
**Difficulty:** 4/5  
**Recommended time:** 1.5 min  

**Shortcut:**

For repeated replacement:

\[
\boxed{\text{original quantity}\left(1-\frac{\text{removed}}{\text{total}}\right)^n}.
\]

**Common trap:** Subtracting 12 litres twice from the original 60.

**Key concept:** The second removal is from the **new mixture**, not the original milk.

**Alternate:** Track milk after first replacement = 48 L, then retain \(4/5\) again.

---

## Q3 — **150 km**

Let one-way distance be \(d\).

\[
\frac d{50}+\frac d{75}=5.
\]

LCM = 150:

\[
\frac{3d+2d}{150}=5.
\]

Therefore:

\[
5d=750
\]

\[
\boxed{d=150}.
\]

**Source:** CAT-level inspired  
**Topic:** Time, Speed & Distance  
**Difficulty:** 4/5  
**Recommended time:** 1 min  

**Shortcut:** Combine reciprocal speeds:

\[
\frac1{50}+\frac1{75}=\frac1{30}.
\]

Thus:

\[
d/30=5\Rightarrow d=150.
\]

**Common trap:** Taking average speed as 62.5 km/h.

**Key concept:** Average speed is not generally the arithmetic mean.

**Alternate:** Equal-distance average speed:

\[
\bar v=\frac{2(50)(75)}{50+75}=60.
\]

Total distance:

\[
60(5)=300,
\]

so one-way distance = 150 km.

---

# ALGEBRA

## Q4 — **A, \(\{-1,6\}\)**

Breakpoints:

\[
x=1,\quad x=4.
\]

### \(x\le1\)

\[
|x-1|+|x-4|
=(1-x)+(4-x)
=5-2x.
\]

Set equal to 7:

\[
5-2x=7
\]

\[
x=-1.
\]

### \(1\le x\le4\)

\[
(x-1)+(4-x)=3,
\]

which cannot equal 7.

### \(x\ge4\)

\[
(x-1)+(x-4)=2x-5.
\]

\[
2x-5=7
\]

\[
x=6.
\]

Therefore:

\[
\boxed{\{-1,6\}}.
\]

**Source:** CAT-level inspired  
**Topic:** Modulus  
**Difficulty:** 5/5  
**Recommended time:** 2 min  

**Shortcut:** Think geometrically: the expression is the sum of distances from \(x\) to 1 and 4. Outside the interval, the sum grows linearly.

**Common trap:** Assuming every \(x\) between \(-1\) and 6 works.

**Key concept revision:** Absolute-value expressions change slope at their breakpoints.

**Alternate method:** Number-line distance interpretation.

---

## Q5 — **\(\frac{248}{11}\)**

For roots \(\alpha,\beta\):

\[
\alpha+\beta=8,
\qquad
\alpha\beta=11.
\]

Use:

\[
\alpha^3+\beta^3
=
(\alpha+\beta)^3-3\alpha\beta(\alpha+\beta).
\]

Therefore:

\[
=8^3-3(11)(8)
\]

\[
=512-264
\]

\[
=248.
\]

Hence:

\[
\frac{\alpha^3+\beta^3}{\alpha\beta}
=
\boxed{\frac{248}{11}}.
\]

**Source:** CAT-level inspired  
**Topic:** Quadratic roots / identities  
**Difficulty:** 5/5  
**Recommended time:** 1.5 min  

**Shortcut:** Never solve for \(\alpha,\beta\). Use Vieta.

**Common trap:** Factoring the quadratic unnecessarily.

**Key concept revision:**

\[
\boxed{\alpha^3+\beta^3=(\alpha+\beta)^3-3\alpha\beta(\alpha+\beta)}.
\]

**Alternate:** Find roots explicitly, but this is slower.

---

# GEOMETRY

## Q6 — **150 cm²**

Let the hypotenuse be:

\[
9+16=25.
\]

For the altitude \(h\) to the hypotenuse:

\[
h^2=(9)(16)=144.
\]

Thus:

\[
h=12.
\]

Area:

\[
\frac12\times25\times12
=
\boxed{150}.
\]

**Source:** CAT-level inspired  
**Topic:** Right triangle / geometric mean  
**Difficulty:** 4/5  
**Recommended time:** 1.5 min  

**Shortcut:**

If altitude to hypotenuse divides it into \(m,n\):

\[
\boxed{h=\sqrt{mn}}.
\]

**Common trap:** Using \(9+16\) as the altitude.

**Key concept revision:**

\[
h^2=mn.
\]

**Alternate:** Recognise the resulting sides as a \(15-20-25\) right triangle.

---

## Q7 — **15 cm**

Radius to point of tangency is perpendicular to tangent.

Thus:

\[
OP^2=OT^2+PT^2.
\]

\[
17^2=8^2+PT^2.
\]

\[
PT^2=289-64=225.
\]

Therefore:

\[
\boxed{PT=15}.
\]

**Source:** CAT-level inspired  
**Topic:** Circle/tangent  
**Difficulty:** 4/5  
**Recommended time:** 45 sec  

**Shortcut:** Recognise the \(8-15-17\) triple.

**Common trap:** Taking OP itself as tangent length.

**Key concept revision:**

\[
\boxed{\text{Radius}\perp\text{tangent}}.
\]

---

# NUMBER SYSTEM

## Q8 — **B, 32**

We have:

\[
420=2^2\cdot3\cdot5\cdot7.
\]

A divisor of N has form:

\[
2^a3^b5^c7^d.
\]

Since it must be divisible by 420:

\[
a\ge2,\quad b\ge1,\quad c\ge1,\quad d\ge1.
\]

Available exponent choices:

### For 2

\[
a=2,3,4,5
\]

→ 4 choices.

### For 3

\[
b=1,2,3,4
\]

→ 4 choices.

### For 5

\[
c=1,2
\]

→ 2 choices.

### For 7

\[
d=1
\]

→ 1 choice.

Hence:

\[
4\cdot4\cdot2\cdot1
=
\boxed{32}.
\]

**Answer: B**

**Source:** CAT-level inspired  
**Topic:** Number of divisors  
**Difficulty:** 5/5  
**Recommended time:** 1.5 min  

**Shortcut:** For “divisors divisible by M”, start exponents at the minimum required by M.

**Common trap:** Counting all divisors of N:

\[
6\cdot5\cdot3\cdot2.
\]

**Key concept revision:** Exponent choices, not divisor listing.

**Alternate:** Count all divisors and impose the exponent restrictions through subtraction, but the direct method is faster.

---

## Q9 — **3**

Modulo 7:

\[
10\equiv3.
\]

Powers of 3:

\[
3^1=3,\quad3^2=2,\quad3^3=6,\quad3^4=4,\quad3^5=5,\quad3^6=1.
\]

Cycle length = 6.

Since:

\[
100\equiv4\pmod6,
\]

\[
10^{100}\equiv3^4\equiv4.
\]

Similarly:

\[
10^{101}\equiv3^5\equiv5,
\]

\[
10^{102}\equiv3^6\equiv1.
\]

Thus:

\[
4+5+1=10\equiv\boxed3\pmod7.
\]

**Source:** CAT-level inspired  
**Topic:** Remainder cycles  
**Difficulty:** 4/5  
**Recommended time:** 1 min  

**Shortcut:** Reduce the base first:

\[
10\rightarrow3\pmod7.
\]

**Common trap:** Handling each giant exponent independently.

**Key concept revision:** Find the smallest useful cycle.

---

# MODERN MATH

## Q10 — **660**

A number is divisible by 5 iff its last digit is 0 or 5.

### Case 1: Last digit = 0

The first four digits come from:

\[
1,2,3,4,5,6.
\]

Number of arrangements:

\[
{}^6P_4
=
6\cdot5\cdot4\cdot3
=
360.
\]

### Case 2: Last digit = 5

Remaining digits:

\[
0,1,2,3,4,6.
\]

First digit cannot be zero.

All 4-position arrangements:

\[
{}^6P_4=360.
\]

Those beginning with 0:

\[
{}^5P_3=60.
\]

Valid:

\[
360-60=300.
\]

Total:

\[
360+300
=
\boxed{660}.
\]

**Source:** CAT-level inspired  
**Topic:** Permutations / divisibility  
**Difficulty:** 5/5  
**Recommended time:** 3 min  

**Shortcut:** Divisibility by 5 reduces the problem immediately to two last-digit cases.

**Common trap:** Forgetting the leading-zero restriction in the last-digit-5 case.

**Key concept revision:**

\[
\boxed{5\mid n\iff \text{last digit is 0 or 5}}.
\]

**Alternate:** Count all 5-digit permutations and separately impose last-digit restrictions.

---

## Q11 — **B, \(\frac3{13}\)**

Given at least one red.

Total ways to choose 2 balls:

\[
{9\choose2}=36.
\]

Ways with **no red**:

There are 5 non-red balls.

\[
{5\choose2}=10.
\]

Therefore conditional sample space:

\[
36-10=26.
\]

Ways to choose two red:

\[
{4\choose2}=6.
\]

Thus:

\[
P(\text{both red}\mid\text{at least one red})
=
\frac6{26}
=
\boxed{\frac3{13}}.
\]

**Answer: B**

**Source:** CAT-level inspired  
**Topic:** Conditional probability  
**Difficulty:** 4/5  
**Recommended time:** 1.5 min  

**Shortcut:** Directly redefine the sample space after the condition.

**Common trap:** Using denominator 36 instead of 26.

**Key concept revision:**

\[
P(A|B)=\frac{P(A\cap B)}{P(B)}.
\]

**Alternate:** Sequential probability with conditional branches.

---

# Q12 — **3675**

Given:

\[
x+y=70,
\qquad xy=m^2.
\]

Use:

\[
(x+y)^2=(x-y)^2+4xy.
\]

Therefore:

\[
(x-y)^2+(2m)^2=70^2.
\]

So we need integer Pythagorean triples with hypotenuse 70.

The relevant triples are:

\[
42-56-70
\]

and

\[
14-? 
\]

More systematically, checking the integer possibilities gives:

\[
(7,63),\quad(14,56),\quad(35,35),\quad(56,14),\quad(63,7).
\]

Their products are:

\[
441,\quad784,\quad1225,\quad784,\quad441.
\]

Therefore:

\[
441+784+1225+784+441
\]

\[
=\boxed{3675}.
\]

**Source:** CAT-level inspired  
**Topic:** Number theory / perfect squares  
**Difficulty:** 5/5  
**Recommended time:** 4 min  

**Time-saving shortcut:**

For:

\[
x+y=S,\quad xy=\text{perfect square},
\]

immediately transform into:

\[
\boxed{(x-y)^2+(2\sqrt{xy})^2=S^2}.
\]

For \(S=70\), search Pythagorean triples with hypotenuse 70.

**Common trap:** Considering only \(x<y\) and forgetting that the question asks for **ordered pairs**.

**Key concept revision:**

\[
\boxed{(x+y)^2-(x-y)^2=4xy}.
\]

**Alternate method:** Let \(x=70-y\) and test when \(y(70-y)\) is a square. This is much slower.

---

# DILR — SET 1

The key structural block is:

\[
\boxed{BC}
\]

because B must immediately precede C.

Also:

\[
A<D,\qquad A<E,\qquad G<B.
\]

The valid schedules can be systematically enumerated.

---

## Q13 — **A**

For slot 1:

- B cannot be first because G must precede B.
- C cannot be first because B must immediately precede C.
- E cannot be first because E must come after A.
- F cannot be first by condition.
- D can technically be first, but then A must occur before D — impossible.

Thus only:

\[
\boxed{A\text{ or }G}.
\]

**Answer: A**

**Source:** CAT-level inspired  
**Topic:** Arrangement  
**Difficulty:** 3/5  
**Recommended time:** 1 min  

**Shortcut:** Eliminate using predecessor constraints before arranging anything.

**Common trap:** Forgetting that D requires A before it.

**Key concept:** In CAT arrangements, “must be before” often eliminates positions without enumeration.

---

## Q14 — **C, 14**

If C is 5th, B must be 4th:

\[
\_\,\_\,\_\,B\,C\,\_\,\_.
\]

Since G must be before B, G must occupy one of positions 1–3.

Also A must be before both D and E.

Systematic placement of A, D, E, F, G in positions 1,2,3,6,7 subject to F not being 1 or 7 gives:

\[
\boxed{14}
\]

valid schedules.

**Answer: C**

**Source:** CAT-level inspired  
**Topic:** Arrangement / block method  
**Difficulty:** 5/5  
**Recommended time:** 3 min  

**Shortcut:** Fix BC first:

\[
BC=45.
\]

Then treat the remaining five people as a restricted arrangement.

**Common trap:** Counting BC as two independent positions.

**Key concept:** Immediate adjacency should almost always be treated as a block.

**Alternate:** Enumerate the possible locations of G among positions 1–3, then place A,D,E,F.

---

## Q15 — **D, 24**

If D occupies 7th:

\[
A<7
\]

is automatically satisfied.

We still require:

\[
BC,\quad G<B,\quad E>A,\quad F\neq1,7.
\]

Since D occupies 7, F can only be in positions 2–6.

Enumerating valid placements of the BC block and then A,E,G,F gives:

\[
\boxed{24}.
\]

**Answer: D**

**Source:** CAT-level inspired  
**Topic:** Arrangement  
**Difficulty:** 5/5  
**Recommended time:** 3 min  

**Shortcut:** Fixing D at 7 removes the A<D constraint completely.

**Common trap:** Continuing to treat A<D as an active restriction after D is fixed at the final position.

**Key concept:** After fixing a variable, eliminate constraints that become automatically satisfied.

---

## Q16 — **B, 6**

If A occupies slot 3:

- E must be after 3.
- D must be after 3.
- BC must be consecutive.
- G must precede B.
- F cannot be 1 or 7.

Enumerating the feasible placements produces:

\[
\boxed6}.
\]

**Answer: B**

**Source:** CAT-level inspired  
**Topic:** Arrangement  
**Difficulty:** 5/5  
**Recommended time:** 2.5 min  

**Shortcut:** Fix A=3 first; then the remaining positions split naturally into before-A and after-A.

**Common trap:** Allowing E in positions 1–2.

---

# DILR — SET 2

Calculate store totals.

### Q1 totals

- A: \(40+30+20=90\)
- B: \(35+25+30=90\)
- C: \(50+20+25=95\)
- D: \(30+40+25=95\)

Total Q1:

\[
90+90+95+95=370.
\]

### Q2 totals

- A: \(50+35+25=110\)
- B: \(45+30+35=110\)
- C: \(55+30+30=115\)
- D: \(35+50+35=120\)

Total Q2:

\[
110+110+115+120=455.
\]

---

## Q17 — **D, Store D**

Q2 totals:

\[
110,\ 110,\ 115,\ 120.
\]

Highest:

\[
\boxed{120}.
\]

**Answer: D**

**Source:** CAT-level inspired  
**Topic:** DI  
**Difficulty:** 2/5  
**Recommended time:** 30 sec  

**Shortcut:** Sum each row only once.

**Common trap:** Comparing a single product rather than total store sales.

---

## Q18 — **22.97%**

Increase:

\[
455-370=85.
\]

Percentage increase:

\[
\frac{85}{370}\times100.
\]

\[
=\frac{17}{74}\times100
\approx\boxed{22.97\%}.
\]

**Source:** CAT-level inspired  
**Topic:** DI / Percentage  
**Difficulty:** 3/5  
**Recommended time:** 1 min  

**Shortcut:**

\[
85/370=17/74.
\]

Since \(17/74\approx0.2297\), answer is about 22.97%.

**Common trap:** Dividing by 455.

**Key concept:**

\[
\%\text{ increase}=
\frac{\text{increase}}{\text{original}}\times100.
\]

---

## Q19 — **A, \(37:25\)**

Q2 product P:

\[
50+45+55+35=185.
\]

Q2 product R:

\[
25+35+30+35=125.
\]

Therefore:

\[
185:125
=
\boxed{37:25}.
\]

**Answer: A**

**Source:** CAT-level inspired  
**Topic:** DI / Ratios  
**Difficulty:** 3/5  
**Recommended time:** 45 sec  

**Shortcut:** Aggregate columns before simplifying.

**Common trap:** Calculating store-wise ratios and attempting to combine them.

---

## Q20 — **A, \(\frac{24}{91}\)**

Store D Q2 total:

\[
35+50+35=120.
\]

Total Q2:

\[
455.
\]

Therefore:

\[
\frac{120}{455}
=
\frac{24}{91}.
\]

\[
\boxed A
\]

**Source:** CAT-level inspired  
**Topic:** DI / Fractions  
**Difficulty:** 3/5  
**Recommended time:** 45 sec  

**Shortcut:** Divide numerator and denominator by 5 immediately.

---

# VARC — RC 1

## Q21 — **B**

The passage explicitly rejects two extremes:

- measurement is arbitrary;
- measurement is completely neutral.

Instead, it argues that measurement can be reproducible and useful while the choice of framework still contains judgment.

\[
\boxed B
\]

**Source:** CAT-level inspired  
**Topic:** Main idea  
**Difficulty:** 4/5  
**Recommended time:** 2 min  

**Time-saving shortcut:** Identify the author's qualification in paragraph 2 and conclusion in paragraph 4.

**Common trap:** Choosing A because the passage discusses subjectivity.

**Key concept revision:** CAT often tests the distinction between **“contains judgment”** and **“is entirely subjective.”**

---

## Q22 — **B**

The examples show that changing what is measured changes what aspects of economic well-being become visible.

\[
\boxed B
\]

**Difficulty:** 3/5  
**Recommended time:** 1 min  

**Shortcut:** Ask: “Why did the author insert these examples?”

**Common trap:** A incorrectly says unemployment is inaccurate; the passage says the number may be accurate.

---

## Q23 — **B**

The passage explicitly says a system can produce consistent results without the choice of that system being neutral.

Therefore:

\[
\boxed B.
\]

**Difficulty:** 4/5  
**Recommended time:** 1 min  

**Common trap:** D uses the absolute word “necessarily.”

---

## Q24 — **B**

The author is not anti-measurement. The criticism is directed at treating measurement as completely neutral.

Therefore:

\[
\boxed{\text{cautiously critical}}.
\]

**Difficulty:** 3/5  
**Recommended time:** 45 sec  

**Key concept:** Tone questions require the **strength** of the author's position, not merely its direction.

---

# VARC — RC 2

## Q25 — **B**

The passage recognises the importance of archives while arguing that selection is unavoidable and absences can themselves be informative.

\[
\boxed B.
\]

**Source:** CAT-level inspired  
**Topic:** Main idea  
**Difficulty:** 4/5  
**Recommended time:** 2 min  

**Shortcut:** The final paragraph usually contains the author's synthesis.

**Common trap:** A is too conspiratorial; the passage explicitly says partiality need not be deliberate manipulation.

---

## Q26 — **B**

“Preservation is not the opposite of forgetting” means that even preservation systems inevitably select what is kept and what becomes less visible.

\[
\boxed B.
\]

**Difficulty:** 4/5  
**Recommended time:** 1 min  

**Key concept:** A nuanced statement usually requires a nuanced paraphrase, not a reversal.

---

## Q27 — **B**

The final sentence explicitly argues that patterns of absence can reveal something about the conditions under which the archive was created.

\[
\boxed B.
\]

**Difficulty:** 4/5  
**Recommended time:** 1 min  

**Common trap:** A says every omission was deliberate; the passage explicitly rejects that assumption.

---

## Q28 — **C**

The author says a perfectly complete record may be impossible and should not be treated as the standard.

Thus the author would disagree with:

\[
\boxed C.
\]

**Difficulty:** 4/5  
**Recommended time:** 1 min  

**Shortcut:** Look for the option contradicting the author's explicit conclusion.

---

# VERBAL ABILITY

## Q29 — **2341**

Sentence 2 introduces the common assumption about data.

Sentence 3 begins with **“Yet”**, so:

\[
2\rightarrow3.
\]

Sentence 4 begins with **“Those decisions”**, referring directly to sentence 3:

\[
3\rightarrow4.
\]

Sentence 1 gives the consequence.

Therefore:

\[
\boxed{2341}.
\]

**Source:** CAT-level inspired  
**Topic:** Para Jumble  
**Difficulty:** 4/5  
**Recommended time:** 1.5 min  

**Shortcut:** Lock the chain:

\[
\boxed{2\rightarrow3\rightarrow4}.
\]

**Common trap:** Starting with 1 even though “This” needs an antecedent.

---

## Q30 — **2314**

Sentence 2 introduces the importance of historical records.

Sentence 3 qualifies:

> preservation always involves selection.

Sentence 1 draws the consequence:

> archive reflects preservers' priorities.

Sentence 4 further explains this consequence.

Therefore:

\[
\boxed{2314}.
\]

**Source:** CAT-level inspired  
**Topic:** Para Jumble  
**Difficulty:** 4/5  
**Recommended time:** 1.5 min  

**Shortcut:** Identify the logical chain:

\[
\boxed{2\rightarrow3\rightarrow1\rightarrow4}.
\]

**Common trap:** Starting with 1 because it sounds like a conclusion; it requires the preceding idea of selection.

---

## Q31 — **B**

B captures all three major ideas:

- measurement is useful;
- it can be reliable;
- choices determine what becomes visible.

\[
\boxed B.
\]

**Source:** CAT-level inspired  
**Topic:** Para Summary  
**Difficulty:** 3/5  
**Recommended time:** 1 min  

**Common trap:** A changes “contains judgment” into “is unreliable.”

---

## Q32 — **C**

C preserves both halves:

1. archives contain valuable evidence;
2. absences can also be meaningful.

\[
\boxed C.
\]

**Source:** CAT-level inspired  
**Topic:** Para Summary  
**Difficulty:** 4/5  
**Recommended time:** 1 min  

**Common trap:** A is too negative; the author does not reject archives.

---

## Q33 — **D**

A, B and C are compatible with the passage.

D says measurement is valuable **only when all human judgment is eliminated**, directly contradicting the passage.

\[
\boxed D.
\]

**Source:** CAT-level inspired  
**Topic:** Odd One Out  
**Difficulty:** 3/5  
**Recommended time:** 45 sec  

**Shortcut:** Identify the one statement that changes the author's nuanced position into an extreme one.

---

## Q34 — **C**

Sentence 2 says choices are required before measurement.

The inserted sentence explains the significance of those choices.

Sentence 3 then naturally follows with:

> “Different choices can therefore…”

Thus:

\[
\boxed C}.
\]

**Source:** CAT-level inspired  
**Topic:** Sentence Placement  
**Difficulty:** 4/5  
**Recommended time:** 1 min  

**Shortcut:** Track the causal connector **“This makes…”** and the following **“therefore.”**

---

# FINAL ANSWER KEY

## QA

| Q | Answer |
|---|---|
| 1 | **B — 10** |
| 2 | **38.4 L** |
| 3 | **150 km** |
| 4 | **A — \{-1, 6\}** |
| 5 | **248/11** |
| 6 | **150 cm²** |
| 7 | **15 cm** |
| 8 | **B — 32** |
| 9 | **3** |
| 10 | **660** |
| 11 | **B — 3/13** |
| 12 | **3675** |

## DILR

| Q | Answer |
|---|---|
| 13 | **A — A or G** |
| 14 | **C — 14** |
| 15 | **D — 24** |
| 16 | **B — 6** |
| 17 | **D — Store D** |
| 18 | **22.97%** |
| 19 | **A — 37:25** |
| 20 | **A — 24/91** |

## VARC

| Q | Answer |
|---|---|
| 21 | **B** |
| 22 | **B** |
| 23 | **B** |
| 24 | **B** |
| 25 | **B** |
| 26 | **B** |
| 27 | **B** |
| 28 | **C** |
| 29 | **2341** |
| 30 | **2314** |
| 31 | **B** |
| 32 | **C** |
| 33 | **D** |
| 34 | **C** |

---

# 🔥 DAY 54 — 99+ SHORTCUT BANK

### Arithmetic

**Repeated replacement**

\[
\boxed{Q_{\text{remaining}}=Q\left(1-\frac rV\right)^n}
\]

**Equal-distance average speed**

\[
\boxed{\frac{2uv}{u+v}}
\]

**Work**

\[
\boxed{\text{Rate}=\frac1{\text{time}}}
\]

---

### Algebra

For two absolute values, immediately identify the breakpoints.

For quadratic roots, Vieta is often enough:

\[
\boxed{\alpha+\beta=-b/a,\quad\alpha\beta=c/a}.
\]

Don't solve for roots unless necessary.

---

### Geometry

If altitude to hypotenuse divides it into \(m,n\):

\[
\boxed{h=\sqrt{mn}}.
\]

Tangent from an external point:

\[
\boxed{PT=\sqrt{OP^2-r^2}}.
\]

---

### Number System

For:

\[
N=p^aq^br^c,
\]

divisors divisible by:

\[
p^rq^st^u
\]

can be counted through restricted exponent ranges.

This is much faster than listing divisors.

---

### Modern Math

Divisibility:

\[
5\mid n\Rightarrow\text{last digit }0\text{ or }5.
\]

Conditional probability:

> **Change the denominator after receiving the condition.**

---

# 🎯 DAY 54 — ATTEMPT PRIORITY

### QA Round 1
**Q1 → Q3 → Q4 → Q7 → Q8 → Q9 → Q11**

### QA Round 2
**Q2 → Q5 → Q6 → Q10**

### 99+ challenge
**Q12**

### DILR
**Set 2 is the quicker set.**  
Set 1 is the better test of arrangement discipline.

### VARC
Start with:

\[
Q21\rightarrow Q22\rightarrow Q25\rightarrow Q27
\]

then move to VA.

---

# 🧠 TODAY'S 99+ PRINCIPLE

Today's central skill is:

\[
\boxed{\textbf{Do not calculate until you know what structure you are calculating.}}
\]

Examples:

- Q5 → Vieta instead of solving roots.
- Q6 → geometric-mean property instead of constructing the triangle.
- Q8 → exponent ranges instead of listing divisors.
- Q10 → last-digit restriction before permutation counting.
- Q11 → redefine the conditional sample space.
- Q12 → convert a perfect-square product into a Pythagorean condition.
- DILR Set 1 → treat **BC as a block**.
- RC → distinguish **reliability of measurement** from **neutrality of measurement**.

**For the 99+ track, the goal is now to increasingly identify the structural shortcut before touching the arithmetic.**

---
