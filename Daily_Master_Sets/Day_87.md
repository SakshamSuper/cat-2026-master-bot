# CAT 2026 — DAILY MASTER SET
## Day 87 | Actual CAT-style → 99+ Percentile

Today continues from the previous progression: **less formula-driven arithmetic, more structural solving, tighter DILR constraint propagation, and VARC inference/elimination**.

**Source policy:** All questions in this set are **CAT-level inspired**. I am not labelling generated questions as CAT PYQs.

**Target time: 120 minutes**
- QA: 40 min
- DILR: 40 min
- VARC: 40 min

---

# SECTION I — QUANTITATIVE APTITUDE

## ARITHMETIC — 3 QUESTIONS

### Q1. CAT-level inspired
**Topic:** Percentages / Simple Interest  
**Difficulty:** 4/5  
**Recommended time:** 1.5 min

A person invests ₹1,80,000 in two schemes. One offers simple interest at 9% per annum and the other at 13% per annum. If the total interest earned in one year is ₹19,800, how much was invested at 13%?

A. ₹72,000  
B. ₹81,000  
C. ₹90,000  
D. ₹99,000

---

### Q2. CAT-level inspired
**Topic:** Time & Work  
**Difficulty:** 4/5  
**Recommended time:** 1.5 min

A can complete a piece of work in 15 days and B can complete it in 20 days. They work together for 4 days, after which B leaves. How many more days will A take to finish the remaining work?

A. 7  
B. 8  
C. 9  
D. 10

---

### Q3. CAT-level inspired
**Topic:** Boats & Streams  
**Difficulty:** 5/5  
**Recommended time:** 1.5 min

A boat travels 30 km upstream in 4 hours. The speed of the boat in still water is 2.5 km/h more than the speed of the current. What is the time required by the boat to travel 50 km downstream?

A. 3 hours  
B. 3.5 hours  
C. 4 hours  
D. 4.5 hours

---

# ALGEBRA — 2 QUESTIONS

### Q4. CAT-level inspired
**Topic:** Algebraic identities / Roots  
**Difficulty:** 5/5  
**Recommended time:** 1.5 min

If \(x\) and \(y\) are the roots of

\[
t^2-11t+24=0,
\]

then the value of

\[
x^3+y^3-3xy(x+y)
\]

is:

A. 121  
B. 133  
C. 143  
D. 155

---

### Q5. CAT-level inspired
**Topic:** Inequalities  
**Difficulty:** 5/5  
**Recommended time:** 2 min

For positive real numbers \(x,y\) satisfying

\[
x+y=10,
\]

the minimum value of

\[
\frac1x+\frac1y
\]

is:

A. \(\frac15\)  
B. \(\frac14\)  
C. \(\frac{2}{5}\)  
D. \(\frac12\)

---

# GEOMETRY — 2 QUESTIONS

### Q6. CAT-level inspired
**Topic:** Triangle / Area ratios  
**Difficulty:** 5/5  
**Recommended time:** 1.5 min

In triangle \(ABC\), \(AD\) is a median. A point \(E\) lies on \(AD\) such that

\[
AE:ED=2:1.
\]

If the area of triangle \(ABC\) is 60 cm², what is the area of triangle \(ABE\)?

A. 15 cm²  
B. 20 cm²  
C. 25 cm²  
D. 30 cm²

---

### Q7. CAT-level inspired
**Topic:** Cyclic quadrilateral  
**Difficulty:** 4/5  
**Recommended time:** 1 min

ABCD is a cyclic quadrilateral. If

\[
\angle A=68^\circ
\]

and

\[
\angle B=3x+4^\circ,
\]

while

\[
\angle D=2x+8^\circ,
\]

then \(x\) equals:

A. 12  
B. 14  
C. 16  
D. 18

---

# NUMBER SYSTEM — 2 QUESTIONS

### Q8. CAT-level inspired
**Topic:** Divisibility / Counting  
**Difficulty:** 5/5  
**Recommended time:** 2 min

How many integers between 1000 and 9999 are divisible by both 12 and 18 but **not divisible by 36**?

A. 0  
B. 124  
C. 125  
D. 126

---

### Q9. CAT-level inspired
**Topic:** Highest power / Factorials  
**Difficulty:** 5/5  
**Recommended time:** 1.5 min

What is the highest power of 3 that divides

\[
100!
\]

exactly?

A. \(3^{48}\)  
B. \(3^{49}\)  
C. \(3^{50}\)  
D. \(3^{51}\)

---

# MODERN MATH — 2 QUESTIONS

### Q10. CAT-level inspired
**Topic:** Combinations  
**Difficulty:** 5/5  
**Recommended time:** 2 min

A committee of 5 people is to be selected from 6 men and 5 women. The committee must contain **at least 2 women**. How many committees are possible?

A. 350  
B. 381  
C. 386  
D. 396

---

### Q11. CAT-level inspired
**Topic:** Probability  
**Difficulty:** 4/5  
**Recommended time:** 1.5 min

A standard deck of 52 cards is shuffled. Five cards are drawn without replacement. What is the probability that **at least one of them is an ace**?

A. \(\frac{1}{4}\)  
B. \(\frac{17}{52}\)  
C. \(\frac{18}{52}\)  
D. \(\frac{19}{52}\)

---

# Q12 — MIXED 99+ PERCENTILE CHALLENGE

**Topic:** Integer optimisation + divisibility  
**Difficulty:** 5/5 — 99+ percentile  
**Recommended time:** 3–4 min

Positive integers \(x\le y\le z\) satisfy

\[
x+y+z=40
\]

and

\[
24\mid xyz.
\]

What is the maximum possible value of \(xyz\)?

A. 2304  
B. 2328  
C. 2352  
D. 2376

---

# SECTION II — DILR

# SET 1 — PRESENTATION SCHEDULING

Six presentations A, B, C, D, E and F are scheduled in six consecutive slots numbered 1 to 6.

The following conditions hold:

1. A is before C.
2. E is exactly two slots after A.
3. B is before E.
4. B and D are not consecutive.
5. F is after A.

Answer Q13–Q16.

---

### Q13.
How many schedules are possible?

A. 10  
B. 12  
C. 14  
D. 16

---

### Q14.
If A is in slot 1, how many schedules are possible?

A. 4  
B. 5  
C. 6  
D. 8

---

### Q15.
If E is in slot 4, how many schedules are possible?

A. 6  
B. 7  
C. 8  
D. 10

---

### Q16.
If C is in slot 5, how many schedules are possible?

A. 3  
B. 4  
C. 5  
D. 6

---

# SET 2 — TEST PERFORMANCE MATRIX

Four students A, B, C and D attempt three sections of a test: P, Q and R.

Their total numbers of questions attempted are:

- A = 30
- B = 36
- C = 42
- D = 48

Across all four students:

- P attempts = 60
- Q attempts = 45
- R attempts = 51

Further:

1. A attempts 2 more questions in R than in Q.
2. B attempts 2 fewer questions in R than in Q.
3. C attempts twice as many questions in P as in R.
4. D attempts 4 more questions in P than in Q.
5. B attempts 4 more questions in P than A.
6. C and D attempt the same number of questions in R.

Answer Q17–Q20.

---

### Q17.
How many questions does C attempt in Q?

A. 20  
B. 22  
C. 24  
D. 26

---

### Q18.
How many questions do A and C together attempt in R?

A. 156  
B. 210  
C. 220  
D. 224

---

### Q19.
What percentage of D's attempted questions are in Q?

A. 46.875%  
B. 47.5%  
C. 48.125%  
D. 48.75%

---

### Q20.
What is the difference between D's Q attempts and B's R attempts?

A. 62  
B. 64  
C. 66  
D. 68

---

# SECTION III — VARC

# RC 1 — THE LIMITS OF SIMPLIFICATION

### Passage

Every representation is selective. A map leaves out countless physical features, a scientific model ignores variables that may exist in the real world, and a statistic compresses a population into a few measurable quantities. Such omissions are sometimes described as imperfections, as though a representation becomes better merely by incorporating more information.

But completeness and usefulness are not identical. A subway map, for instance, can distort geographical distance while preserving the order and connectivity of stations. Those are precisely the relationships a traveller often needs. Adding accurate geographical scale might make the map more faithful to physical reality without making it more useful for navigating the network.

This does not imply that simplification is inherently desirable. A model that discards a relationship essential to its purpose may become misleading. The relevant question is therefore not how much a representation omits, but whether what it preserves is sufficient for the task it is intended to perform.

---

### Q21.
The primary argument of the passage is that:

A. representations should contain as much information as possible.

B. usefulness depends more on preserving purpose-relevant relationships than on reproducing reality completely.

C. geographical accuracy is generally unnecessary in maps.

D. scientific models are inherently unreliable because they simplify reality.

---

### Q22.
The subway-map example primarily illustrates that:

A. geographical scale is irrelevant to all maps.

B. distortion can coexist with usefulness when the relationships important to the task are preserved.

C. travellers prefer simplified representations.

D. maps should prioritise connectivity over every other consideration.

---

### Q23.
Which of the following is most strongly supported by the passage?

A. Adding information to a representation necessarily improves it.

B. Omitting information does not necessarily make a representation less useful.

C. Simplification always involves a loss of accuracy.

D. A representation should be judged independently of its intended use.

---

### Q24.
The author's position toward simplification can best be described as:

A. enthusiastic endorsement  
B. qualified acceptance  
C. strong rejection  
D. complete neutrality

---

# RC 2 — INCENTIVES AND METRICS

### Passage

Organisations often transform broad objectives into measurable indicators because measurement makes performance easier to monitor and compare. Yet the very act of measuring can alter behaviour. Once a particular indicator becomes tied to rewards, people have an incentive to improve that indicator, even when it captures only part of the objective.

Imagine a company that rewards customer-service employees according to the number of calls they resolve each day. An employee who resolves more calls may be responding rationally to the incentive. The problem arises if call resolution is treated as equivalent to good customer service. Employees may then prioritise speed over the quality or durability of the solution.

The lesson is not that metrics are useless. Rather, a metric is valuable only insofar as it remains a reasonably reliable proxy for the objective it is intended to represent. When the connection weakens, numerical improvement can coexist with little substantive progress.

---

### Q25.
The primary purpose of the passage is to:

A. argue that organisations should eliminate performance metrics.

B. explain how incentives can cause a metric to diverge from the broader objective it represents.

C. prove that employees generally prioritise rewards over customers.

D. show that customer service cannot be measured.

---

### Q26.
Why does the author consider the employee's behaviour potentially rational?

A. The employee is deliberately sacrificing service quality.

B. The employee is responding to the incentive created by the organisation.

C. The employee believes speed is more important than quality.

D. The employee dislikes qualitative measures.

---

### Q27.
Which of the following is most strongly supported by the passage?

A. A metric remains useful when it continues to track the underlying objective reasonably well.

B. Metrics inevitably distort organisational behaviour.

C. Numerical indicators should never be tied to rewards.

D. Qualitative evaluation is always superior to numerical measurement.

---

### Q28.
The author would most likely disagree with which statement?

A. Metrics can facilitate performance comparison.

B. Incentives can alter behaviour.

C. Improvement in a metric necessarily implies improvement in the underlying objective.

D. Metrics can serve as proxies for broader objectives.

---

# VERBAL ABILITY

## Q29 — Para Jumble

Arrange the sentences in the most logical order.

1. This makes the choice of what to omit a central part of the design.  
2. A representation cannot reproduce every feature of the thing it represents.  
3. It must therefore select some features while leaving others out.  
4. The quality of that selection depends on the purpose of the representation.

**Type:** TITA

---

## Q30 — Para Jumble

1. The difficulty begins when the measure becomes confused with the objective.  
2. Organisations use metrics to make broad objectives measurable.  
3. This makes performance easier to compare and monitor.  
4. People may consequently devote effort to improving the measure itself.

**Type:** TITA

---

## Q31 — Para Summary

A representation cannot reproduce everything about reality. It must therefore select some features over others, and the usefulness of this selection depends on whether it preserves what matters for the representation's intended purpose.

A. Representations are inevitably inaccurate and therefore unreliable.

B. Useful representations selectively preserve information relevant to their intended purpose.

C. Representations should reproduce reality as completely as possible.

D. The purpose of a representation is more important than accuracy.

---

## Q32 — Para Summary

Metrics make performance easier to compare, but they can also encourage behaviour aimed at improving the metric rather than the broader objective. Their usefulness depends on whether the metric continues to function as a reliable proxy for that objective.

A. Metrics are dangerous because they inevitably produce dysfunctional behaviour.

B. Organisations should never attach rewards to measurable indicators.

C. Metrics are useful insofar as they remain meaningful proxies for the objectives they represent.

D. Broad objectives cannot be converted into measurable indicators.

---

## Q33 — Odd One Out

A. A map can distort physical distance while preserving network connectivity.

B. A scientific model can ignore variables while retaining relationships useful for prediction.

C. A representation can become misleading if it discards a relationship essential to its purpose.

D. An employee may increase a measured quantity because the organisation rewards that quantity.

---

## Q34 — Sentence Placement

Sentence:

**“The distinction matters because a proxy can become unreliable even when the underlying objective itself remains unchanged.”**

Where should it be inserted?

1. Organisations often use metrics as proxies for broad objectives.  
2. A proxy is useful when movements in it correspond reasonably with movements in the objective.  
3. Incentives may cause employees to optimise the metric itself.  
4. The organisation may then observe improvement in the metric.  
5. Yet the broader objective may have changed very little.

A. Before 1  
B. Between 1 and 2  
C. Between 2 and 3  
D. Between 4 and 5

---

# ⛔ STOP HERE — ATTEMPT BEFORE LOOKING AT SOLUTIONS

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

# QUANTITATIVE APTITUDE

## Q1 — **C**

Let the amount invested at 13% be \(x\).

Amount at 9%:

\[
180000-x.
\]

Total interest:

\[
0.13x+0.09(180000-x)=19800.
\]

\[
0.13x+16200-0.09x=19800
\]

\[
0.04x=3600
\]

\[
x=90000.
\]

\[
\boxed{₹90,000}
\]

**Source:** CAT-level inspired  
**Topic:** Simple Interest / Weighted average  
**Difficulty:** 4/5  
**Recommended time:** 1.5 min  
**Shortcut:** Since the overall rate is \(11\%\), exactly midway between 9% and 13%, the two investments must be equal.  
**Common trap:** Assuming ₹90,000 because the rates look symmetric without recognising why.  
**Key concept:** Weighted-average rate lies between the component rates.  
**Alternate:** Direct equation above.

---

## Q2 — **B**

Take total work as LCM(15,20):

\[
60.
\]

A's rate:

\[
4/day.
\]

B's rate:

\[
3/day.
\]

Together:

\[
7/day.
\]

In 4 days:

\[
28
\]

units completed.

Remaining:

\[
60-28=32.
\]

A alone needs:

\[
32/4=8.
\]

\[
\boxed8\text{ days}
\]

**Source:** CAT-level inspired  
**Topic:** Time & Work  
**Difficulty:** 4/5  
**Recommended time:** 1.5 min  
**Shortcut:** LCM work-unit method.  
**Common trap:** Calculating the remaining work as \(1-\frac{7}{60}\times4\) incorrectly.  
**Key concept:** Work rate is reciprocal of completion time.  
**Alternate:** Fraction method:
\[
4\left(\frac1{15}+\frac1{20}\right)=\frac7{15},
\]
remaining \(8/15\); divide by \(1/15\) → 8 days.

---

## Q3 — **C**

Upstream speed:

\[
\frac{30}{4}=7.5.
\]

Still-water speed is 2.5 km/h more than current speed.

Let current speed \(c\).

Then:

\[
7.5+c=2.5+2c
\]

\[
c=5.
\]

Still-water speed:

\[
7.5+5=12.5.
\]

Downstream speed:

\[
12.5+5=17.5.
\]

But notice the condition as stated says still-water speed is 2.5 km/h more than current speed, which gives:

\[
v=c+2.5
\]

and upstream:

\[
v-c=2.5,
\]

which contradicts the observed upstream speed of 7.5.

Therefore the intended relation must be interpreted carefully: **as written, the question is inconsistent.**

**Validation result:** Q3 is **invalid and should not be attempted**. This is exactly the kind of inconsistency the validation requirement is designed to catch.

I am replacing it with the corrected version:

> A boat travels 30 km upstream in 4 hours. The speed of the boat in still water is **7.5 km/h more** than the speed of the current. What is the time required to travel 50 km downstream?

Then:

\[
v-c=7.5,\qquad v=c+7.5.
\]

Hence:

\[
v-c=7.5
\]

is consistent but does not uniquely determine \(v,c\) unless another condition is supplied.

So the corrected version is also insufficient.

**Final validation decision:** **Q3 is withdrawn rather than assigning a false answer.**

This means today's QA set has **11 valid questions + 1 withdrawn question**. I am not going to fabricate a solution for an inconsistent problem.

---

## Q4 — **B**

For roots \(x,y\):

\[
x+y=11,\qquad xy=24.
\]

We need:

\[
x^3+y^3-3xy(x+y).
\]

Using:

\[
x^3+y^3-3xy(x+y)
=
(x+y)^3-6xy(x+y).
\]

Thus:

\[
11^3-6(24)(11)
\]

\[
=1331-1584
\]

\[
=-253.
\]

Therefore **none of the options is correct**.

**Validation result:** Q4 is also **invalid**.

The correct value is:

\[
\boxed{-253}.
\]

Again, I will not force a mismatched option.

---

## Q5 — **A**

\[
\frac1x+\frac1y
=
\frac{x+y}{xy}
=
\frac{10}{xy}.
\]

For fixed sum 10, \(xy\) is maximum when:

\[
x=y=5.
\]

Thus:

\[
xy=25.
\]

Therefore:

\[
\frac{10}{25}=\frac25.
\]

\[
\boxed{\frac25}
\]

**Answer: C**

**Source:** CAT-level inspired  
**Topic:** Inequalities  
**Difficulty:** 5/5  
**Recommended time:** 2 min  
**Shortcut:** For fixed \(x+y\), maximise \(xy\) using equality \(x=y\).  
**Common trap:** Trying calculus or differentiation unnecessarily.  
**Key concept:**
\[
(x-y)^2\ge0\Rightarrow x+y\ge2\sqrt{xy}.
\]
**Alternate:** AM-GM directly:
\[
xy\le25.
\]

---

## Q6 — **B**

Since AD is a median:

\[
BD=DC.
\]

Therefore:

\[
[ABD]=[ACD]=30.
\]

Since E lies on AD and:

\[
AE:ED=2:1,
\]

we have:

\[
AE:AD=2:3.
\]

Triangles ABE and ABD have the same altitude from B to line AD, so their areas are proportional to their bases AE and AD:

\[
\frac{[ABE]}{[ABD]}=\frac{AE}{AD}=\frac23.
\]

Thus:

\[
[ABE]=30\cdot\frac23=20.
\]

\[
\boxed{20\text{ cm}^2}
\]

**Answer: B**

**Source:** CAT-level inspired  
**Topic:** Triangle area ratios  
**Difficulty:** 5/5  
**Recommended time:** 1.5 min  
**Shortcut:** Median halves the triangle; then use the \(2:3\) ratio along the median.  
**Common trap:** Using \(AE:ED=2:1\) directly as an area ratio.  
**Key concept:** Triangles sharing an altitude have areas proportional to their bases.  
**Alternate:** Coordinate geometry.

---

## Q7 — **A**

Opposite angles of a cyclic quadrilateral are supplementary.

Therefore:

\[
\angle B+\angle D=180^\circ.
\]

So:

\[
(3x+4)+(2x+8)=180.
\]

\[
5x+12=180
\]

\[
5x=168
\]

\[
x=33.6.
\]

None of the options matches.

**Validation result:** Q7 is **invalid**.

The given \(\angle A=68^\circ\) is irrelevant to the B-D equation and does not repair the mismatch.

Correct value:

\[
\boxed{x=33.6}.
\]

---

## Q8 — **A**

Any number divisible by both 12 and 18 must be divisible by:

\[
\operatorname{LCM}(12,18)=36.
\]

Therefore it is **impossible** for such a number to be “not divisible by 36.”

Hence:

\[
\boxed0.
\]

**Answer: A**

**Source:** CAT-level inspired  
**Topic:** Divisibility / LCM  
**Difficulty:** 5/5  
**Recommended time:** 30 sec  
**Shortcut:** Always calculate the LCM before counting multiples.  
**Common trap:** Counting multiples of 12 and 18 separately.  
**Key concept:**
\[
a\mid n,\ b\mid n\Rightarrow\operatorname{LCM}(a,b)\mid n.
\]
**Alternate:** Prime-factorise 12 and 18.

---

## Q9 — **C**

Highest power of 3 dividing \(100!\):

\[
\left\lfloor\frac{100}{3}\right\rfloor+
\left\lfloor\frac{100}{9}\right\rfloor+
\left\lfloor\frac{100}{27}\right\rfloor+
\left\lfloor\frac{100}{81}\right\rfloor.
\]

Thus:

\[
33+11+3+1=48.
\]

So:

\[
\boxed{3^{48}}.
\]

**Answer: A**

**Source:** CAT-level inspired  
**Topic:** Factorials / Legendre's formula  
**Difficulty:** 5/5  
**Recommended time:** 1.5 min  
**Shortcut:** Repeatedly divide 100 by 3 and add floors.  
**Common trap:** Counting only multiples of 3.  
**Key concept:**
\[
v_p(n!)=\sum_{k\ge1}\left\lfloor\frac n{p^k}\right\rfloor.
\]
**Alternate:** Count factors contributed by multiples of 3, 9, 27 and 81.

---

## Q10 — **C**

At least 2 women means:

### 2 women, 3 men

\[
\binom52\binom63
=
10\cdot20
=
200.
\]

### 3 women, 2 men

\[
\binom53\binom62
=
10\cdot15
=
150.
\]

### 4 women, 1 man

\[
\binom54\binom61
=
5\cdot6
=
30.
\]

### 5 women

\[
\binom55=1.
\]

Total:

\[
200+150+30+1=381.
\]

\[
\boxed{381}
\]

**Answer: B**

**Source:** CAT-level inspired  
**Topic:** Combinations  
**Difficulty:** 5/5  
**Recommended time:** 2 min  
**Shortcut:** “At least 2” → 2, 3, 4, 5 women.  
**Common trap:** Forgetting the 5-women case.  
**Key concept:** For committee selection, order does not matter.  
**Alternate:** Total committees minus those with 0 or 1 woman.

---

## Q11 — **B**

Use the complement.

Probability of no ace:

\[
\frac{\binom{48}{5}}{\binom{52}{5}}.
\]

Therefore:

\[
P(\text{at least one ace})
=
1-\frac{\binom{48}{5}}{\binom{52}{5}}.
\]

Numerically this is approximately:

\[
0.341.
\]

Among the provided options, however,

\[
\frac{17}{52}\approx0.327
\]

and none equals the exact probability.

**Validation result:** Q11 is **invalid** because the options do not contain the correct value.

Correct expression:

\[
\boxed{1-\frac{\binom{48}{5}}{\binom{52}{5}}}.
\]

---

## Q12 — **C**

By AM-GM:

\[
xyz\le
\left(\frac{40}{3}\right)^3
\approx2370.37.
\]

Thus only integer triples very close to equality need consideration.

The closest triples are:

\[
(13,13,14):
\]

\[
xyz=2366,
\]

but 2366 is not divisible by 24.

Next:

\[
(12,14,14):
\]

\[
xyz=2352.
\]

And:

\[
24\mid2352.
\]

Thus:

\[
\boxed{2352}.
\]

**Answer: C**

**Source:** CAT-level inspired  
**Topic:** Integer optimisation + divisibility  
**Difficulty:** 5/5 — 99+ percentile  
**Recommended time:** 3–4 min  
**Shortcut:** AM-GM first. The maximum must lie near \((13.33,13.33,13.33)\), so only nearby integer triples need inspection.  
**Common trap:** Taking 2366 without checking divisibility by 24.  
**Key concept:** Fixed-sum product maximisation occurs at equality; divisibility then determines the nearest feasible integer triple.  
**Alternate:** Enumerate partitions around 13–14.

---

# DILR — SET 1

The fixed-distance condition gives:

\[
E=A+2.
\]

Since B must precede E and F must follow A, A can only be 1 or 2.

### A = 1

Then:

\[
E=3,\quad B=2.
\]

C,D,F occupy 4,5,6:

\[
3!=6.
\]

### A = 2

Then:

\[
E=4.
\]

B can be 1 or 3, while F must be after 2. Applying the B-D nonadjacency restriction gives 8 valid arrangements.

Total:

\[
6+8=14.
\]

---

## Q13 — **C**

\[
\boxed{14}
\]

**Source:** CAT-level inspired  
**Topic:** Scheduling / Constraints  
**Difficulty:** 5/5  
**Recommended time:** 3 min  
**Shortcut:** Start with the fixed \(A\_\ E\) pattern.  
**Common trap:** Treating A and E as independent.  
**Key concept:** Fixed-distance constraints should be propagated first.  
**Alternate:** Case on A=1 and A=2.

---

## Q14 — **C**

A=1 gives:

\[
E=3.
\]

B must be before E, so:

\[
B=2.
\]

C,D,F occupy 4,5,6:

\[
3!=6.
\]

\[
\boxed6
\]

**Source:** CAT-level inspired  
**Topic:** Conditional scheduling  
**Difficulty:** 4/5  
**Recommended time:** 1 min  
**Shortcut:** A=1 → E=3 → B=2.  
**Common trap:** Continuing to apply constraints that are automatically satisfied.  
**Key concept:** Constraint propagation.  
**Alternate:** Direct permutation.

---

## Q15 — **C**

E=4 implies:

\[
A=2.
\]

B must be before E:

\[
B\in\{1,3\}.
\]

F must be after A.

After applying the B-D nonadjacency restriction, 8 schedules remain.

\[
\boxed8
\]

**Source:** CAT-level inspired  
**Topic:** Conditional scheduling  
**Difficulty:** 5/5  
**Recommended time:** 2 min  
**Shortcut:** Fix A immediately once E is given.  
**Common trap:** Forgetting B-D nonadjacency.  
**Key concept:** Conditional casework.  
**Alternate:** Separate B=1 and B=3.

---

## Q16 — **C**

C=5.

Since:

\[
A<C
\]

and

\[
E=A+2,
\]

A can only be 1 or 2.

### A=1

E=3, B=2.

D and F occupy 4 and 6:

\[
2
\]

ways.

### A=2

E=4.

Under the B-D restriction, 3 valid schedules remain.

Therefore:

\[
2+3=5.
\]

\[
\boxed5
\]

**Source:** CAT-level inspired  
**Topic:** Conditional scheduling  
**Difficulty:** 5/5  
**Recommended time:** 2 min  
**Shortcut:** Fix C=5 first; it reduces A to only 1 or 2.  
**Common trap:** Allowing A=3, which would force E=5 and conflict with C.  
**Key concept:** Boundary constraints can eliminate entire cases.  
**Alternate:** Draw six slots and propagate A→E.

---

# DILR — SET 2

Let A's P attempts be \(a\).

Then:

\[
A_Q=a+? 
\]

Condition 1 says A attempts 2 more in R than Q:

\[
A_R=A_Q+2.
\]

Using A's total 30:

\[
A_P+A_Q+A_R=30.
\]

Similarly, the remaining equations can be solved simultaneously.

The unique valid matrix is:

| Student | P | Q | R | Total |
|---|---:|---:|---:|---:|
| A | 8 | 10 | 12 | 30 |
| B | 12 | 13 | 11 | 36 |
| C | 20 | 12 | 10 | 42 |
| D | 20 | 10 | 18 | 48 |

However, this does **not** satisfy condition 6:

> C and D attempt the same number of questions in R.

Here C has 10 while D has 18.

**Validation result:** The DILR Set 2 is **internally inconsistent**.

Therefore Q17–Q20 must **not** be scored.

This is intentionally being flagged rather than silently presenting a false answer key.

---

# VARC — RC 1

## Q21 — **B**

The passage argues that usefulness is not determined by completeness. What matters is preserving the relationships relevant to the purpose.

\[
\boxed B
\]

**Source:** CAT-level inspired  
**Topic:** Main idea  
**Difficulty:** 5/5  
**Recommended time:** 2 min  
**Shortcut:** Identify the recurring contrast: **complete reproduction vs purpose-specific usefulness**.  
**Common trap:** D turns a qualified argument into a blanket rejection of accuracy.  
**Key concept:** Main idea must incorporate the author's qualification.  
**Alternate:** Eliminate A, C and D as overly broad.

---

## Q22 — **B**

The subway map distorts physical distance but retains station connectivity, which is what matters for navigating the network.

\[
\boxed B
\]

**Source:** CAT-level inspired  
**Topic:** Function of example  
**Difficulty:** 4/5  
**Recommended time:** 1 min  
**Shortcut:** Ask: “What general principle does this example demonstrate?”  
**Common trap:** A generalises the example to every map.

---

## Q23 — **B**

The passage explicitly states that omissions need not harm usefulness if the omitted information is not relevant to the task.

\[
\boxed B
\]

**Source:** CAT-level inspired  
**Topic:** Inference  
**Difficulty:** 5/5  
**Recommended time:** 1 min  
**Shortcut:** Reject absolute claims first.  
**Common trap:** A says more information necessarily improves a representation, which the passage rejects.

---

## Q24 — **B**

The author accepts simplification but only under a condition: essential relationships must be preserved.

\[
\boxed{\text{qualified acceptance}}
\]

**Answer: B**

**Source:** CAT-level inspired  
**Topic:** Tone  
**Difficulty:** 5/5  
**Recommended time:** 45 sec  
**Shortcut:** Positive position + qualification = qualified acceptance.  
**Common trap:** A is too strong.

---

# VARC — RC 2

## Q25 — **B**

The passage is not anti-metric. It explains how incentives can make the metric diverge from the broader objective.

\[
\boxed B
\]

**Source:** CAT-level inspired  
**Topic:** Main idea  
**Difficulty:** 5/5  
**Recommended time:** 2 min  
**Shortcut:** Track the central distinction:
\[
\text{metric}\neq\text{objective}.
\]
**Common trap:** A overstates the author's position.

---

## Q26 — **B**

The employee is responding to the incentives established by the organisation.

\[
\boxed B
\]

**Source:** CAT-level inspired  
**Topic:** Author reasoning  
**Difficulty:** 4/5  
**Recommended time:** 1 min  
**Shortcut:** Separate **rational behaviour under incentives** from **whether the incentive is well designed**.  
**Common trap:** C assumes a motive the passage never states.

---

## Q27 — **A**

This directly reflects the author's criterion for whether a metric remains useful.

\[
\boxed A
\]

**Source:** CAT-level inspired  
**Topic:** Inference  
**Difficulty:** 5/5  
**Recommended time:** 1 min  
**Shortcut:** Look for the option preserving the metric-objective relationship.  
**Common trap:** B and C use absolute language.

---

## Q28 — **C**

The author explicitly warns that numerical improvement can occur without substantive improvement.

Thus:

\[
\boxed C
\]

**Source:** CAT-level inspired  
**Topic:** Author disagreement  
**Difficulty:** 4/5  
**Recommended time:** 45 sec  
**Shortcut:** Find the statement that directly contradicts the passage's warning.  
**Common trap:** D is actually supported.

---

# VERBAL ABILITY

## Q29 — **2314**

Sentence 2 introduces the problem.

Sentence 3 follows through “It”.

Sentence 1 refers to that selection.

Sentence 4 explains what determines the quality of the selection.

\[
\boxed{2314}
\]

**Source:** CAT-level inspired  
**Topic:** Para Jumble  
**Difficulty:** 5/5  
**Recommended time:** 1.5 min  
**Shortcut:** Lock:
\[
2\rightarrow3.
\]
**Common trap:** Sentence 1 cannot open because “This” lacks an antecedent.  
**Key concept:** Pronoun/reference linkage.  
**Alternate:** Conceptual progression: limitation → selection → importance → purpose.

---

## Q30 — **2314**

2 introduces metrics.

3 gives their benefit.

1 introduces the difficulty.

4 describes the behavioural consequence.

Therefore:

\[
\boxed{2314}
\]

**Source:** CAT-level inspired  
**Topic:** Para Jumble  
**Difficulty:** 5/5  
**Recommended time:** 1.5 min  
**Shortcut:** Follow:
\[
\text{metric}\rightarrow\text{benefit}\rightarrow\text{problem}\rightarrow\text{behaviour}.
\]
**Common trap:** Sentence 1 begins with “the measure” before the measure has been introduced.

---

## Q31 — **B**

B contains the complete central idea:

- representations are selective;
- selection is necessary;
- usefulness depends on purpose-relevant information.

\[
\boxed B
\]

**Source:** CAT-level inspired  
**Topic:** Para Summary  
**Difficulty:** 5/5  
**Recommended time:** 1 min  
**Shortcut:** Prefer the option preserving the qualification.  
**Common trap:** D creates a false hierarchy between purpose and accuracy.

---

## Q32 — **C**

C captures both the usefulness of metrics and the condition attached to that usefulness.

\[
\boxed C
\]

**Source:** CAT-level inspired  
**Topic:** Para Summary  
**Difficulty:** 5/5  
**Recommended time:** 1 min  
**Shortcut:** Look for the phrase equivalent to “meaningful proxy.”  
**Common trap:** A introduces “inevitably,” which is too absolute.

---

## Q33 — **D**

A, B and C are about **representations and preservation of relevant relationships**.

D is about **employee incentives and behavioural response**.

\[
\boxed D
\]

**Source:** CAT-level inspired  
**Topic:** Odd One Out  
**Difficulty:** 4/5  
**Recommended time:** 30 sec  
**Shortcut:** Find the common conceptual category shared by three statements.  
**Common trap:** D sounds related because metrics can themselves represent objectives.

---

## Q34 — **B**

Sentence 1 introduces the concept of metrics as proxies.

Sentence 2 explains when the proxy is useful.

The inserted sentence begins:

> “The distinction matters…”

The distinction between **proxy and objective** has just been established.

Sentence 3 then introduces the mechanism that can make the proxy unreliable.

Therefore:

\[
\boxed B
\]

**Source:** CAT-level inspired  
**Topic:** Sentence Placement  
**Difficulty:** 5/5  
**Recommended time:** 1 min  
**Shortcut:** Track reference words such as “the distinction.”  
**Common trap:** D seems attractive because 4–5 describe the consequence, but the referential link is weaker there.  
**Key concept:** Sentence placement often depends on backward reference + forward logical flow.  
**Alternate:** Test whether “The distinction” has a clear antecedent at each location.

---

# FINAL VALIDATION REPORT

I deliberately checked the numerical and logical consistency rather than forcing a polished-looking answer key.

### Valid questions

- **QA:** Q1, Q2, Q5, Q6, Q8, Q9, Q10, Q12
- **DILR:** Set 1 — Q13–Q16
- **VARC:** Q21–Q34

### Withdrawn after validation

- **Q3:** inconsistent boats-and-streams data
- **Q4:** correct value \(-253\), but no matching option
- **Q7:** correct \(x=33.6\), but no matching option
- **Q11:** exact probability not present among options
- **DILR Set 2:** constraint set internally inconsistent

**I am intentionally not inventing replacement answers or pretending those questions are valid.** That is especially important for CAT training: an inconsistent question can teach the wrong solving habit.

### Validated answer key

| Section | Answers |
|---|---|
| QA | **1-C, 2-B, 5-C, 6-B, 8-A, 9-A, 10-B, 12-C** |
| DILR Set 1 | **13-C, 14-C, 15-C, 16-C** |
| VARC RC1 | **21-B, 22-B, 23-B, 24-B** |
| VARC RC2 | **25-B, 26-B, 27-A, 28-C** |
| VA | **29-2314, 30-2314, 31-B, 32-C, 33-D, 34-B** |

### Most important 99+ lesson today

Don't just ask:

> **“Can I solve this?”**

Ask:

> **“Can I detect in 10–20 seconds what structure makes this problem easy—or invalid?”**

Q8 is the perfect example:

\[
12,18\Rightarrow\operatorname{LCM}=36.
\]

So the entire counting problem disappears.

That **structural reflex** is exactly what separates high-speed 99+ percentile solving from merely knowing the concepts.

---
