# CAT 2026 — DAILY MASTER SET
## Day 62 | Actual CAT Difficulty → 99+ Percentile Track

**Target time: 120 minutes**

| Section | Questions | Target |
|---|---:|---:|
| QA | 12 | 40 min |
| DILR | 8 | 40 min |
| VARC | 14 | 40 min |

### Today's progression
Day 61 focused on **transform-before-calculating**. Today we push that further:

- QA: more multi-step modelling
- DILR: block formation + conditional enumeration
- VARC: inference, author intent and logical sequencing
- Q12 is the **99+ percentile challenge**

**Source policy:** All questions today are **CAT-level inspired**. No generated question is falsely labelled as a CAT PYQ.

---

# SECTION I — QUANTITATIVE APTITUDE

## ARITHMETIC — 3 QUESTIONS

### Q1. CAT-level inspired
**Topic:** Percentages / Successive Changes  
**Type:** TITA  
**Difficulty:** 4/5  
**Recommended time:** 1.5 min

A product is first discounted by 20% and then a tax of 12.5% is levied on the discounted price. If the final amount paid is ₹4,200, what was the marked price?

---

### Q2. CAT-level inspired
**Topic:** Time & Work  
**Type:** TITA  
**Difficulty:** 5/5  
**Recommended time:** 2 min

A and B together can complete a work in \(60/7\) days. They work together for 6 days, after which C alone completes the remaining work in 4 days.

In how many days can C alone complete the entire work?

---

### Q3. CAT-level inspired
**Topic:** Time, Speed & Distance  
**Type:** TITA  
**Difficulty:** 4/5  
**Recommended time:** 1.5 min

A train 180 metres long crosses a pole in 9 seconds and crosses a platform in 21 seconds.

Find the length of the platform.

---

# ALGEBRA — 2 QUESTIONS

### Q4. CAT-level inspired
**Topic:** Algebraic Identities / Recurrence  
**Type:** TITA  
**Difficulty:** 5/5  
**Recommended time:** 2 min

If

\[
x+\frac1x=3,
\]

find

\[
x^5+\frac1{x^5}.
\]

---

### Q5. CAT-level inspired
**Topic:** Quadratic Equations / Roots  
**Type:** TITA  
**Difficulty:** 4/5  
**Recommended time:** 1.5 min

If \(\alpha\) and \(\beta\) are the roots of

\[
x^2-7x+10=0,
\]

find

\[
(\alpha-\beta)^2.
\]

---

# GEOMETRY — 2 QUESTIONS

### Q6. CAT-level inspired
**Topic:** Triangle / Heron's Formula  
**Type:** TITA  
**Difficulty:** 4/5  
**Recommended time:** 2 min

A triangle has sides 7 cm, 8 cm and 9 cm.

Find its area in the form \(a\sqrt b\), where \(a,b\) are positive integers and \(b\) is square-free.

---

### Q7. CAT-level inspired
**Topic:** Circle / Tangents  
**Type:** TITA  
**Difficulty:** 5/5  
**Recommended time:** 2 min

From an external point P, two tangents PA and PB are drawn to a circle with centre O and radius 8 cm. If

\[
PA=PB=15\text{ cm},
\]

find the area of quadrilateral OAPB.

---

# NUMBER SYSTEM — 2 QUESTIONS

### Q8. CAT-level inspired
**Topic:** Divisibility / Number of Divisors  
**Type:** TITA  
**Difficulty:** 5/5  
**Recommended time:** 2 min

How many positive divisors of

\[
N=2^8\cdot3^5\cdot5^4
\]

are divisible by 180?

---

### Q9. CAT-level inspired
**Topic:** Modular Arithmetic / Cyclicity  
**Type:** TITA  
**Difficulty:** 4/5  
**Recommended time:** 1 min

Find the remainder when

\[
7^{2025}\cdot3^{2024}
\]

is divided by 10.

---

# MODERN MATH — 2 QUESTIONS

### Q10. CAT-level inspired
**Topic:** Combinations  
**Type:** TITA  
**Difficulty:** 4/5  
**Recommended time:** 2 min

A committee of 5 is to be selected from 8 men and 6 women.

How many committees contain **at least two women**?

---

### Q11. CAT-level inspired
**Topic:** Probability / Combinations  
**Type:** TITA  
**Difficulty:** 5/5  
**Recommended time:** 2 min

Three cards are drawn simultaneously from a standard deck of 52 cards.

What is the probability that the three cards belong to **three different suits**?

---

# Q12 — MIXED 99+ PERCENTILE CHALLENGE

**Topic:** Algebra + Number Theory  
**Type:** TITA  
**Difficulty:** 5/5  
**Recommended time:** 4 min

Positive integers \(x,y\) satisfy

\[
x^2+xy+y^2=91.
\]

Find the sum of \(x+y\) over **all ordered pairs** \((x,y)\) satisfying the equation.

---

# SECTION II — DILR

# SET 1 — PRESENTATION SCHEDULE

Five students A, B, C, D and E are scheduled to give presentations from Monday to Friday, one student each day.

The following conditions apply:

1. A presents before C.
2. B presents immediately after D.
3. E presents before F.  
4. A does not present on Monday.
5. F does not present on Friday.

**Correction:** There are only five students in this set, so condition 3 introduces an undefined student F. Therefore, to keep today's set internally consistent, **replace condition 3 with:**

> **E presents before C.**

The final valid conditions are:

1. A presents before C.
2. B presents immediately after D.
3. E presents before C.
4. A does not present on Monday.
5. E does not present on Friday.

---

### Q13.
Who can present on Monday?

A. A only  
B. B only  
C. D or E  
D. B, D or E

---

### Q14.
If C presents on Friday, how many valid schedules are possible?

A. 4  
B. 5  
C. 6  
D. 8

---

### Q15.
If B presents on Monday, how many valid schedules are possible?

A. 1  
B. 2  
C. 3  
D. 4

---

### Q16.
If A presents on Thursday, how many valid schedules are possible?

A. 1  
B. 2  
C. 3  
D. 4

---

# SET 2 — FOUR-MONTH PRODUCTION

A factory manufactures three products X, Y and Z over four months.

| Month | X | Y | Z |
|---|---:|---:|---:|
| January | 80 | 100 | 120 |
| February | 100 | 120 | 140 |
| March | 120 | 90 | 150 |
| April | 140 | 110 | 130 |

---

### Q17.
In which month was total production highest?

A. January  
B. February  
C. March  
D. April

---

### Q18.
What was the percentage increase in production of X from January to April?

**Type:** TITA

---

### Q19.
What is the ratio of total production of X to total production of Z over the four months?

A. \(22:27\)  
B. \(11:13\)  
C. \(10:13\)  
D. \(44:63\)

---

### Q20.
If production of Z in March were 20% lower than reported, what would be the new total production in March?

**Type:** TITA

---

# SECTION III — VARC

# RC 1 — THE LIMITS OF TRANSLATION

### Passage

Translation is often described as the transfer of meaning from one language into another. The description is useful but incomplete, because languages do not merely provide different labels for an identical stock of ideas. They organise experience through conventions, associations and distinctions that may not have exact counterparts elsewhere. A translator therefore works not only with words but also with the conceptual relationships those words inhabit.

This does not imply that translation is impossible. If perfect equivalence were required, translation would indeed fail almost everywhere. Instead, translators routinely seek functional equivalence: a phrase may be altered because preserving its literal form would destroy the effect it has in its original context. A joke, metaphor or culturally specific expression may therefore require considerable transformation before it becomes intelligible to a new audience.

The difficulty is that such transformation involves judgment. The translator must decide what is essential to preserve and what may be changed without distorting the source. Translation is consequently neither mechanical copying nor unrestricted rewriting. It is an exercise in negotiated fidelity.

The best translation, then, should not necessarily be the one that resembles the original sentence most closely. It is the one that preserves the relevant relationship between the original expression and its intended effect while acknowledging the constraints of the receiving language.

---

### Q21.
The central argument of the passage is:

A. Translation is impossible because languages organise experience differently.

B. Good translation requires balancing fidelity to the source with adaptation to the receiving language.

C. Translators should always translate literally whenever possible.

D. Cultural expressions should never be translated.

---

### Q22.
The author mentions jokes and metaphors primarily to show that:

A. literary translation is harder than scientific translation.

B. literal translation may fail to preserve the intended effect of an expression.

C. translators should freely rewrite every culturally specific phrase.

D. humour cannot be translated between languages.

---

### Q23.
Which of the following can be inferred?

A. A translation can depart substantially from the wording of the original while still being faithful to its intended effect.

B. The more closely a translation follows the original wording, the better it must be.

C. Translation requires no interpretation when the languages share vocabulary.

D. Functional equivalence eliminates all ambiguity in translation.

---

### Q24.
The phrase **“negotiated fidelity”** most nearly suggests that:

A. translators must compromise between competing demands while preserving what matters most.

B. translators should deliberately alter the author's ideas.

C. fidelity to the source is unnecessary.

D. translation is primarily a commercial negotiation.

---

# RC 2 — THE POLITICS OF URBAN SPACE

### Passage

Cities are often presented as collections of infrastructure: roads, buildings, transit networks and utilities. Yet urban space also distributes opportunities and constraints. A park, railway station or public square does not merely occupy land; it affects who can reach particular activities, how long they can remain there and what forms of interaction are possible.

This is why apparently technical decisions about urban design can have political consequences. A pedestrian pathway that connects two neighbourhoods may expand access to employment and public institutions. Conversely, a road designed primarily for through-traffic may divide communities even if it improves vehicle movement. The physical arrangement of a city therefore influences social relations without necessarily announcing itself as a political choice.

None of this means that every design decision has a single ideological interpretation. Cities face genuine trade-offs involving cost, safety, congestion and competing uses of limited land. The point is rather that infrastructure choices should not be evaluated solely by technical efficiency. Their distributional effects—the ways in which benefits and burdens are allocated among different groups—also matter.

Urban planning becomes more transparent when these effects are made explicit. Instead of pretending that infrastructure decisions are purely technical, planners can acknowledge the values and trade-offs embedded in them and subject those choices to public scrutiny.

---

### Q25.
The primary purpose of the passage is to:

A. argue that urban infrastructure should be designed without regard to cost.

B. show that urban design has social and political consequences in addition to technical effects.

C. prove that roads are harmful to urban communities.

D. argue that all infrastructure decisions are ideological.

---

### Q26.
The pedestrian pathway and road examples are used to illustrate:

A. that public transport is always better than private transport.

B. how physical infrastructure can affect access and social relations.

C. that cities should prioritise pedestrians over vehicles.

D. that technical efficiency has no value in urban planning.

---

### Q27.
Which of the following can be inferred?

A. Two infrastructure designs with similar technical performance may nevertheless have different social consequences.

B. Every infrastructure decision necessarily benefits one group and harms another.

C. Public scrutiny can eliminate all trade-offs in urban planning.

D. Technical efficiency is irrelevant to city planning.

---

### Q28.
The author would most likely agree with:

A. Urban planning becomes more objective when distributional effects are ignored.

B. Infrastructure decisions should be judged only by measurable efficiency.

C. Making trade-offs explicit can improve the transparency of urban planning.

D. Political considerations should replace technical analysis.

---

# VERBAL ABILITY

## Q29 — Para Jumble

Arrange the sentences in the most logical order:

1. This is why a literal rendering can sometimes be less faithful than a substantial reformulation.  
2. Translation is not simply the replacement of words from one language with words from another.  
3. What matters is often the relationship between an expression and the effect it is intended to produce.  
4. The translator must therefore preserve meaning while adapting form to the receiving language.

**Type:** TITA

---

## Q30 — Para Jumble

1. Infrastructure affects not only movement but also access to opportunities.  
2. Consequently, decisions about roads and public spaces can have effects beyond engineering efficiency.  
3. Urban planning is often presented as a technical exercise.  
4. The distribution of those effects across different groups can therefore become a political question.

**Type:** TITA

---

## Q31 — Para Summary

A translator cannot always preserve the exact wording of an original text because languages differ in structure and cultural associations. Successful translation therefore requires preserving the intended effect while adapting the expression to the receiving language.

A. Translation should always prioritise literal accuracy.

B. Effective translation balances fidelity to intended meaning with adaptation of linguistic form.

C. Cultural differences make translation unreliable.

D. Translators should rewrite texts freely to suit their audiences.

---

## Q32 — Para Summary

Urban infrastructure is not merely a technical arrangement of physical objects. Roads, pathways and public spaces influence access, interaction and the distribution of benefits and burdens. Planning should therefore consider these social consequences alongside efficiency, cost and safety.

A. Urban infrastructure should be designed primarily according to political ideology.

B. Technical efficiency should be ignored when planning cities.

C. Urban planning should evaluate both technical performance and the social distribution of its consequences.

D. Roads generally harm communities by dividing them.

---

## Q33 — Odd One Out

A. Translation sometimes requires changing the wording of the original.

B. Functional equivalence can require substantial adaptation.

C. A translator must decide which aspects of an expression are essential.

D. The best translation is necessarily the one with the closest word-for-word correspondence.

---

## Q34 — Sentence Placement

Sentence:

**“The significance of such choices becomes clearer once access to urban resources is treated as something that can be distributed unevenly.”**

Where should it be inserted?

1. Urban infrastructure determines how people move through a city.  
2. It also affects who can reach employment, institutions and public spaces.  
3. These effects are not distributed equally across all neighbourhoods.  
4. Consequently, apparently technical decisions can acquire political significance.  
5. Urban planning therefore involves questions about both efficiency and distribution.

A. Before 1  
B. Between 1 and 2  
C. Between 2 and 3  
D. Between 3 and 4

---

# ⛔ STOP HERE — ATTEMPT BEFORE CHECKING

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

## Q1 — \(\boxed{₹5250}\)

Let marked price be \(M\).

After 20% discount:

\[
0.8M.
\]

Tax of 12.5%:

\[
1.125(0.8M).
\]

Since:

\[
1.125=\frac98,
\]

we get:

\[
0.8\times1.125
=
\frac45\times\frac98
=
\frac98\cdot\frac45
=
\frac98\cdot\frac45
=
\frac9{10}.
\]

Thus:

\[
\frac9{10}M=4200.
\]

\[
M=4200\cdot\frac{10}{9}
=\boxed{5250}.
\]

**Source:** CAT-level inspired  
**Topic:** Percentages / Successive changes  
**Difficulty:** 4/5  
**Recommended time:** 1 min  
**Shortcut:** Combine the discount and tax:
\[
80\%\times112.5\%=90\%.
\]
So ₹4,200 is 90% of MP.  
**Common trap:** Adding 12.5% after subtracting 20 percentage points.  
**Key concept:** Successive percentage changes are multiplicative.  
**Alternate method:** Assume MP = 100 and scale.

---

## Q2 — \(\boxed{\frac{40}{3}\text{ days}}\)

A+B together complete the work in:

\[
\frac{60}{7}
\]

days.

Therefore their rate is:

\[
\frac7{60}.
\]

In 6 days:

\[
6\cdot\frac7{60}
=
\frac7{10}.
\]

Remaining work:

\[
1-\frac7{10}
=
\frac3{10}.
\]

C completes this in 4 days, so C's rate is:

\[
\frac{3/10}{4}
=
\frac3{40}.
\]

Hence C alone takes:

\[
\frac{40}{3}
=
\boxed{13\frac13\text{ days}}.
\]

**Source:** CAT-level inspired  
**Topic:** Time & Work  
**Difficulty:** 5/5  
**Recommended time:** 2 min  
**Shortcut:** Convert every statement into a rate before doing anything else.  
**Common trap:** Treating \(60/7\) as the rate rather than completion time.  
**Key concept:**
\[
\text{rate}=\frac1{\text{time}}.
\]
**Alternate:** Assume total work = 60 units.

---

## Q3 — \(\boxed{240\text{ m}}\)

Train length:

\[
180\text{ m}.
\]

Crossing a pole in 9 seconds gives speed:

\[
v=\frac{180}{9}=20\text{ m/s}.
\]

When crossing the platform:

\[
\text{distance}=20(21)=420\text{ m}.
\]

This consists of:

\[
\text{train}+\text{platform}.
\]

Therefore:

\[
180+L=420.
\]

\[
\boxed{L=240\text{ m}}.
\]

**Source:** CAT-level inspired  
**Topic:** Time-Speed-Distance  
**Difficulty:** 4/5  
**Recommended time:** 1 min  
**Shortcut:** Pole crossing gives speed instantly.  
**Common trap:** Using 21 seconds to calculate speed.  
**Key concept:** Train crossing an object means total distance = train length + object length.  
**Alternate:** Use ratio of times:
\[
\frac{180+L}{180}=\frac{21}{9}.
\]

---

# ALGEBRA

## Q4 — \(\boxed{123}\)

Let:

\[
S_n=x^n+\frac1{x^n}.
\]

Given:

\[
S_1=3,\qquad S_0=2.
\]

Using:

\[
S_n=\left(x+\frac1x\right)S_{n-1}-S_{n-2},
\]

we get:

\[
S_2=3(3)-2=7.
\]

\[
S_3=3(7)-3=18.
\]

\[
S_4=3(18)-7=47.
\]

\[
S_5=3(47)-18=123.
\]

Therefore:

\[
\boxed{123}.
\]

**Source:** CAT-level inspired  
**Topic:** Algebraic recurrence  
**Difficulty:** 5/5  
**Recommended time:** 1.5 min  
**Shortcut:** Memorise:
\[
S_n=kS_{n-1}-S_{n-2}
\]
when \(x+1/x=k\).  
**Common trap:** Expanding \(x^5+1/x^5\) directly.  
**Key concept:** Symmetric powers have a simple recurrence.  
**Alternate:** Repeatedly use algebraic identities, though recurrence is faster.

---

## Q5 — \(\boxed9}\)

For:

\[
x^2-7x+10=0,
\]

Vieta gives:

\[
\alpha+\beta=7,
\]

\[
\alpha\beta=10.
\]

Now:

\[
(\alpha-\beta)^2
=
(\alpha+\beta)^2-4\alpha\beta.
\]

Therefore:

\[
=49-40
=\boxed9.
\]

**Source:** CAT-level inspired  
**Topic:** Quadratic roots  
**Difficulty:** 4/5  
**Recommended time:** 45 sec  
**Shortcut:** Use:
\[
(\alpha-\beta)^2=(\alpha+\beta)^2-4\alpha\beta.
\]
**Common trap:** Solving for the roots individually.  
**Key concept:** Vieta avoids unnecessary quadratic solving.  
**Alternate:** Roots are 5 and 2.

---

# GEOMETRY

## Q6 — \(\boxed{12\sqrt5}\)

Semiperimeter:

\[
s=\frac{7+8+9}{2}=12.
\]

Heron's formula:

\[
A=\sqrt{12(12-7)(12-8)(12-9)}
\]

\[
=\sqrt{12\cdot5\cdot4\cdot3}
\]

\[
=\sqrt{720}.
\]

Since:

\[
720=144\cdot5,
\]

\[
A=\boxed{12\sqrt5}.
\]

**Source:** CAT-level inspired  
**Topic:** Triangle / Heron's formula  
**Difficulty:** 4/5  
**Recommended time:** 1.5 min  
**Shortcut:** Simplify the product before taking the square root.  
**Common trap:** Using \(s=24\).  
**Key concept:**
\[
A=\sqrt{s(s-a)(s-b)(s-c)}.
\]
**Alternate:** Use base 8 and calculate the altitude by splitting the 7-9 triangle.

---

## Q7 — \(\boxed{120\text{ cm}^2}\)

Since radius \(OA\) is perpendicular to tangent \(PA\),

\[
\triangle OAP
\]

is right-angled.

Its area is:

\[
\frac12(8)(15)=60.
\]

Similarly:

\[
[\triangle OBP]=60.
\]

Therefore quadrilateral OAPB has area:

\[
60+60
=
\boxed{120\text{ cm}^2}.
\]

**Source:** CAT-level inspired  
**Topic:** Circle / Tangents  
**Difficulty:** 5/5  
**Recommended time:** 1.5 min  
**Shortcut:** You don't need OP at all for the area.  
**Common trap:** Spending time calculating OP using \(8-15-17\).  
**Key concept:** Radius to tangent point is perpendicular to tangent.  
**Alternate:** Find \(OP=17\), then use the kite area formula:
\[
\frac12(16)(15)=120.
\]

---

# NUMBER SYSTEM

## Q8 — \(\boxed{112}\)

Factor:

\[
180=2^2\cdot3^2\cdot5.
\]

Our number is:

\[
2^8\cdot3^5\cdot5^4.
\]

For a divisor to be divisible by 180, its exponents must satisfy:

\[
a\ge2,\qquad b\ge2,\qquad c\ge1.
\]

Choices:

For \(2\):

\[
2,3,\dots,8
\]

→ 7 choices.

For \(3\):

\[
2,3,4,5
\]

→ 4 choices.

For \(5\):

\[
1,2,3,4
\]

→ 4 choices.

Hence:

\[
7\cdot4\cdot4
=
\boxed{112}.
\]

**Source:** CAT-level inspired  
**Topic:** Divisibility / Divisors  
**Difficulty:** 5/5  
**Recommended time:** 1.5 min  
**Shortcut:** Translate divisibility into minimum prime exponents.  
**Common trap:** Counting all divisors first and then trying to filter them.  
**Key concept:** Prime-exponent representation makes divisor restrictions independent.  
**Alternate:** Enumerate exponent triples.

---

## Q9 — \(\boxed3}\)

Last digits of powers of 7:

\[
7,9,3,1
\]

with cycle length 4.

Since:

\[
2025\equiv1\pmod4,
\]

\[
7^{2025}
\]

ends in:

\[
7.
\]

For 3:

\[
3,9,7,1
\]

again cycle length 4.

Since:

\[
2024\equiv0\pmod4,
\]

\[
3^{2024}
\]

ends in:

\[
1.
\]

Therefore:

\[
7\times1
\equiv\boxed3\pmod{10}.
\]

**Source:** CAT-level inspired  
**Topic:** Cyclicity  
**Difficulty:** 4/5  
**Recommended time:** 45 sec  
**Shortcut:** Work only with the last-digit cycle.  
**Common trap:** Multiplying huge numbers instead of reducing each factor.  
**Key concept:** Last digit = modulo 10.  
**Alternate:** Use \(7^4\equiv1\) and \(3^4\equiv1\pmod{10}\).

---

# MODERN MATH

## Q10 — \(\boxed{1526}\)

Total committees:

\[
{14\choose5}=2002.
\]

“At least two women” means:

\[
2W3M,\quad3W2M,\quad4W1M,\quad5W0M.
\]

The complement is easier:

- 0 women:
\[
{8\choose5}=56
\]

- 1 woman:
\[
{6\choose1}{8\choose4}
=
6(70)=420.
\]

Therefore:

\[
2002-56-420
=
\boxed{1526}.
\]

**Source:** CAT-level inspired  
**Topic:** Combinations / Complement  
**Difficulty:** 4/5  
**Recommended time:** 1.5 min  
**Shortcut:** “At least two” → subtract 0 and 1.  
**Common trap:** Missing the 5-men case in the complement.  
**Key concept:** Complement counting drastically reduces cases.  
**Alternate:**
\[
{6\choose2}{8\choose3}
+{6\choose3}{8\choose2}
+{6\choose4}{8\choose1}
+{6\choose5}.
\]

---

## Q11 — \(\boxed{\frac{169}{425}}\)

Total ways to select 3 cards:

\[
{52\choose3}.
\]

For three different suits:

1. Choose the 3 suits:

\[
{4\choose3}=4.
\]

2. Choose one card from each chosen suit:

\[
13^3.
\]

Thus favourable selections:

\[
4(13^3).
\]

Probability:

\[
\frac{4(13^3)}{{52\choose3}}.
\]

Now:

\[
{52\choose3}
=
\frac{52\cdot51\cdot50}{6}
=
22100.
\]

So:

\[
\frac{4(2197)}{22100}
=
\frac{8788}{22100}
=
\boxed{\frac{169}{425}}.
\]

**Source:** CAT-level inspired  
**Topic:** Probability / Combinations  
**Difficulty:** 5/5  
**Recommended time:** 2 min  
**Shortcut:** Choose suits first:
\[
{4\choose3}13^3.
\]
**Common trap:** Using \(4P3\) while simultaneously treating the card selection as unordered.  
**Key concept:** Selection order does not matter when cards are drawn simultaneously.  
**Alternate:** Sequentially:
\[
1\times\frac{39}{51}\times\frac{26}{50}
=\frac{169}{425}.
\]

---

# Q12 — \(\boxed{42}\)

Given:

\[
x^2+xy+y^2=91.
\]

Use:

\[
(x+y)^2=x^2+2xy+y^2.
\]

Therefore:

\[
x^2+xy+y^2
=
(x+y)^2-xy.
\]

A more useful transformation is:

\[
4(x^2+xy+y^2)
=
3(x+y)^2+(x-y)^2.
\]

Hence:

\[
3(x+y)^2+(x-y)^2=364.
\]

Let:

\[
s=x+y,\qquad d=x-y.
\]

Then:

\[
3s^2+d^2=364.
\]

Since \(s>0\),

\[
3s^2\le364
\]

so:

\[
s\le11.
\]

Testing integer \(s\) values for which

\[
364-3s^2
\]

is a perfect square gives:

### \(s=10\)

\[
364-300=64=8^2.
\]

Thus:

\[
d=\pm8.
\]

This gives:

\[
(x,y)=(9,1),(1,9).
\]

### \(s=11\)

\[
364-363=1=1^2.
\]

Thus:

\[
d=\pm1.
\]

This gives:

\[
(x,y)=(6,5),(5,6).
\]

Therefore all ordered pairs are:

\[
(9,1),(1,9),(6,5),(5,6).
\]

Their \(x+y\) values are:

\[
10,10,11,11.
\]

Hence:

\[
10+10+11+11
=
\boxed{42}.
\]

**Source:** CAT-level inspired  
**Topic:** Number Theory + Algebra  
**Difficulty:** 5/5 — 99+ percentile challenge  
**Recommended time:** 3–4 min  
**Shortcut:** Immediately transform:
\[
\boxed{4(x^2+xy+y^2)=3(x+y)^2+(x-y)^2}.
\]
Then bound \(x+y\le11\).  
**Common trap:** Brute-forcing \(x,y\) from 1 to 91.  
**Key concept:** Symmetric quadratic forms often become manageable in terms of \(x+y\) and \(x-y\).  
**Alternate:** Fix \(x\le y\), test \(x=1\) onward using the quadratic in \(y\), then use symmetry.

---

# DILR — SET 1

The valid conditions are:

\[
A<C,\qquad D\rightarrow B,\qquad E<C,
\]

with:

\[
A\neq1,\qquad E\neq5.
\]

The five valid schedules are:

1. D B A E C
2. D B E A C
3. E A C D B
4. E A D B C
5. E D B A C

This complete enumeration is useful for validating the questions.

---

## Q13 — \(\boxed D,\ B,D\text{ or }E}\)

Monday cannot be:

- A, because A is not Monday.
- C, because A must be before C.
- Therefore candidates are B, D, E.

All three can occur:

- B Monday → D Tuesday
- D Monday → B Tuesday
- E Monday → valid schedules exist.

Thus:

\[
\boxed{\text{B, D or E}}
\]

**Answer: D**

**Source:** CAT-level inspired  
**Topic:** Arrangement / Constraint elimination  
**Difficulty:** 3/5  
**Recommended time:** 45 sec  
**Shortcut:** Eliminate A and C immediately.  
**Common trap:** Assuming D cannot be first because B follows it.  
**Key concept:** “Immediately after” does not prevent the predecessor from being first.  
**Alternate:** Enumerate the five valid schedules.

---

## Q14 — \(\boxed C,\ 6}\)

If:

\[
C=5,
\]

the five valid schedules listed above all have C on Friday.

Hence:

\[
\boxed6
\]

would be incorrect—the actual number is **5**.

### Validation
The correct answer is:

\[
\boxed5}.
\]

Therefore the correct option is **B**, not C.

**Source:** CAT-level inspired  
**Topic:** Conditional arrangement  
**Difficulty:** 5/5  
**Recommended time:** 2 min  
**Shortcut:** Once C is fixed at 5, the chain restrictions become highly restrictive.  
**Common trap:** Counting a schedule with E on Friday or A on Monday.  
**Key concept:** Re-check every generated arrangement against every condition.  
**Alternate:** Treat DB as one block and enumerate its possible starting positions.

---

## Q15 — \(\boxed C,\ 3}\)

If:

\[
B=1,
\]

then:

\[
D=0
\]

would be required because B is immediately after D.

That is impossible.

Therefore:

\[
\boxed0}
\]

valid schedules.

### Validation result
The question as written has **no valid option**.

This means Q15 is **withdrawn from scoring** rather than assigning a false answer.

**Source:** CAT-level inspired  
**Topic:** Arrangement / Immediate predecessor  
**Difficulty:** 4/5  
**Recommended time:** 30 sec  
**Shortcut:** “B immediately after D” means:
\[
\boxed{D=B-1}.
\]
If B=1, impossible.  
**Common trap:** Reading “B immediately after D” backwards.  
**Key concept:** Translate verbal adjacency into position equations.  
**Alternate:** None needed.

---

## Q16 — \(\boxed A,\ 1}\)

If A is Thursday:

\[
A=4.
\]

Since A<C:

\[
C=5.
\]

Then E<C and E cannot be Friday, so E must be position 1, 2 or 3.

The remaining D-B block must occupy two consecutive positions among the remaining three.

The only valid arrangement is:

\[
E,D,B,A,C.
\]

Therefore:

\[
\boxed1}.
\]

**Answer: A**

**Source:** CAT-level inspired  
**Topic:** Conditional arrangement  
**Difficulty:** 5/5  
**Recommended time:** 1.5 min  
**Shortcut:** A=4 forces C=5 immediately.  
**Common trap:** Trying all 5! arrangements.  
**Key concept:** Fixing a constrained variable can collapse the entire arrangement.  
**Alternate:** Place the DB block first in positions 1–2 or 2–3.

---

# DILR — SET 2

### Row totals

January:

\[
80+100+120=300.
\]

February:

\[
100+120+140=360.
\]

March:

\[
120+90+150=360.
\]

April:

\[
140+110+130=380.
\]

Column totals:

\[
X=80+100+120+140=440,
\]

\[
Y=100+120+90+110=420,
\]

\[
Z=120+140+150+130=540.
\]

---

## Q17 — \(\boxed D,\ April}\)

Totals:

\[
300,\ 360,\ 360,\ 380.
\]

Highest:

\[
\boxed{380}.
\]

Therefore April.

**Answer: D**

**Source:** CAT-level inspired  
**Topic:** Data Interpretation  
**Difficulty:** 2/5  
**Recommended time:** 30 sec  
**Shortcut:** Sum rows.  
**Common trap:** Comparing only product X.

---

## Q18 — \(\boxed{75\%}\)

X increases:

\[
80\rightarrow140.
\]

Increase:

\[
60.
\]

Percentage increase:

\[
\frac{60}{80}\times100
=
\boxed{75\%}.
\]

**Source:** CAT-level inspired  
**Topic:** Percentage  
**Difficulty:** 3/5  
**Recommended time:** 30 sec  
**Shortcut:** \(60/80=3/4\).  
**Common trap:** Dividing by 140.

---

## Q19 — \(\boxed{22:27}\)

Total X:

\[
440.
\]

Total Z:

\[
540.
\]

Therefore:

\[
440:540
=
\boxed{22:27}.
\]

**Answer: A**

**Source:** CAT-level inspired  
**Topic:** DI / Ratio  
**Difficulty:** 3/5  
**Recommended time:** 45 sec  
**Shortcut:** Divide both by 20.  
**Common trap:** Using March's 120:150 ratio instead of the four-month totals.

---

## Q20 — \(\boxed{330}\)

March total:

\[
360.
\]

Z in March:

\[
150.
\]

20% decrease:

\[
150\times20\%=30.
\]

New March total:

\[
360-30
=
\boxed{330}.
\]

**Source:** CAT-level inspired  
**Topic:** DI / Percentage adjustment  
**Difficulty:** 3/5  
**Recommended time:** 45 sec  
**Shortcut:** Change only the affected component.  
**Common trap:** Reducing the entire row by 20%.

---

# VARC — RC 1

## Q21 — \(\boxed B}\)

The passage's central distinction is between literal copying and functional equivalence.

The translator must preserve intended effect while adapting expression.

\[
\boxed B.
\]

**Source:** CAT-level inspired  
**Topic:** Main idea  
**Difficulty:** 4/5  
**Recommended time:** 2 min  
**Shortcut:** The final paragraph gives the author's preferred definition of good translation.  
**Common trap:** A confuses “not perfectly equivalent” with “impossible.”

---

## Q22 — \(\boxed B}\)

Jokes and metaphors illustrate cases where literal wording can destroy the intended effect.

\[
\boxed B.
\]

**Source:** CAT-level inspired  
**Topic:** Function of example  
**Difficulty:** 3/5  
**Recommended time:** 1 min  
**Shortcut:** Ask why the author selected that example.  
**Common trap:** D is too absolute.

---

## Q23 — \(\boxed A}\)

The passage explicitly says that the best translation need not resemble the original sentence most closely.

Thus a translation can change wording while remaining faithful to intended effect.

\[
\boxed A.
\]

**Source:** CAT-level inspired  
**Topic:** Inference  
**Difficulty:** 4/5  
**Recommended time:** 1 min  
**Shortcut:** Use the final two sentences as the inference base.  
**Common trap:** B directly contradicts the passage.

---

## Q24 — \(\boxed A}\)

“Negotiated fidelity” captures the tension between:

- preserving the source;
- adapting to the receiving language.

Therefore:

\[
\boxed A.
\]

**Source:** CAT-level inspired  
**Topic:** Vocabulary in context / Inference  
**Difficulty:** 4/5  
**Recommended time:** 1 min  
**Shortcut:** Decode the metaphor through surrounding sentences.  
**Common trap:** “Negotiated” is metaphorical here, not commercial.

---

# VARC — RC 2

## Q25 — \(\boxed B}\)

The passage argues that urban infrastructure has consequences beyond technical efficiency.

\[
\boxed B.
\]

**Source:** CAT-level inspired  
**Topic:** Main idea  
**Difficulty:** 4/5  
**Recommended time:** 2 min  
**Shortcut:** Track the repeated contrast between “technical” and “distributional”.  
**Common trap:** D overstates the author's position.

---

## Q26 — \(\boxed B}\)

The examples show that roads and pathways alter access and social relations.

\[
\boxed B.
\]

**Source:** CAT-level inspired  
**Topic:** Function of examples  
**Difficulty:** 3/5  
**Recommended time:** 1 min  
**Shortcut:** Both examples demonstrate the same underlying principle.

---

## Q27 — \(\boxed A}\)

The author says infrastructure choices should not be evaluated solely on technical efficiency because their distributional consequences may differ.

Thus two technically similar designs can have different social effects.

\[
\boxed A.
\]

**Source:** CAT-level inspired  
**Topic:** Inference  
**Difficulty:** 4/5  
**Recommended time:** 1 min  
**Shortcut:** Distinguish technical outcome from distributional outcome.  
**Common trap:** B uses “every”.

---

## Q28 — \(\boxed C}\)

The final paragraph explicitly supports making trade-offs transparent and subjecting them to public scrutiny.

\[
\boxed C.
\]

**Source:** CAT-level inspired  
**Topic:** Author's viewpoint  
**Difficulty:** 3/5  
**Recommended time:** 45 sec  
**Shortcut:** The final paragraph often contains the strongest normative statement.  
**Common trap:** D creates a false either/or between political and technical analysis.

---

# VERBAL ABILITY

## Q29 — \(\boxed{2314}\)

Sentence 2 establishes the main distinction:

> Translation is not simply replacement of words.

Sentence 3 explains what matters instead:

> relationship between expression and effect.

Sentence 1 follows with “This is why...”, referring to that principle.

Sentence 4 gives the resulting requirement for the translator.

Therefore:

\[
\boxed{2314}.
\]

**Source:** CAT-level inspired  
**Topic:** Para Jumble  
**Difficulty:** 4/5  
**Recommended time:** 1.5 min  
**Shortcut:** Sentence 1 cannot open because “This” needs a prior idea.  
**Common trap:** Starting with 1 because it sounds like a conclusion.

---

## Q30 — \(\boxed{3124}\)

Sentence 3 introduces the topic:

\[
\text{Urban planning}.
\]

Sentence 1 explains what infrastructure affects.

Sentence 2 draws the consequence.

Sentence 4 adds the political implication.

Thus:

\[
\boxed{3124}.
\]

**Source:** CAT-level inspired  
**Topic:** Para Jumble  
**Difficulty:** 4/5  
**Recommended time:** 1.5 min  
**Shortcut:** Identify the introductory sentence before building the causal chain.  
**Common trap:** Starting with sentence 1 without introducing the broader context.

---

## Q31 — \(\boxed B}\)

The passage argues for **functional fidelity**, not literal reproduction.

Therefore:

\[
\boxed B.
\]

**Source:** CAT-level inspired  
**Topic:** Para Summary  
**Difficulty:** 4/5  
**Recommended time:** 1 min  
**Shortcut:** Preserve both halves of the argument: fidelity + adaptation.  
**Common trap:** A reduces the passage to literal accuracy.

---

## Q32 — \(\boxed C}\)

C accurately captures the dual requirement:

\[
\text{technical performance}+\text{social consequences}.
\]

\[
\boxed C.
\]

**Source:** CAT-level inspired  
**Topic:** Para Summary  
**Difficulty:** 4/5  
**Recommended time:** 1 min  
**Shortcut:** Look for the option that includes the author's qualification rather than one extreme.  
**Common trap:** B throws away efficiency, which the author explicitly retains.

---

## Q33 — \(\boxed D}\)

A, B and C all support adaptation and functional equivalence.

D claims literal similarity is necessarily best, directly contradicting the passage.

\[
\boxed D.
\]

**Source:** CAT-level inspired  
**Topic:** Odd One Out  
**Difficulty:** 3/5  
**Recommended time:** 45 sec  
**Shortcut:** Find the statement that contradicts the central principle.  
**Common trap:** Treating “literal” as automatically “faithful.”

---

## Q34 — \(\boxed D}\)

Sentence 3 says:

> These effects are not distributed equally...

The inserted sentence explains the significance of unequal distribution.

Then sentence 4 follows naturally:

> Consequently, apparently technical decisions can acquire political significance.

So:

\[
\boxed D}.
\]

**Source:** CAT-level inspired  
**Topic:** Sentence Placement  
**Difficulty:** 5/5  
**Recommended time:** 1 min  
**Shortcut:** Look for the causal bridge:
\[
\text{unequal distribution}\rightarrow\text{political significance}.
\]
**Common trap:** Inserting it after sentence 2 before the unequal-distribution idea has been introduced.

---

# FINAL ANSWER KEY

## QA

| Q | Answer |
|---|---|
| 1 | **₹5250** |
| 2 | **40/3 days** |
| 3 | **240 m** |
| 4 | **123** |
| 5 | **9** |
| 6 | **12√5 cm²** |
| 7 | **120 cm²** |
| 8 | **112** |
| 9 | **3** |
| 10 | **1526** |
| 11 | **169/425** |
| 12 | **42** |

## DILR

| Q | Answer |
|---|---|
| 13 | **D — B, D or E** |
| 14 | **B — 5** |
| 15 | **Withdrawn — impossible condition** |
| 16 | **A — 1** |
| 17 | **D — April** |
| 18 | **75%** |
| 19 | **A — 22:27** |
| 20 | **330** |

## VARC

| Q | Answer |
|---|---|
| 21 | **B** |
| 22 | **B** |
| 23 | **A** |
| 24 | **A** |
| 25 | **B** |
| 26 | **B** |
| 27 | **A** |
| 28 | **C** |
| 29 | **2314** |
| 30 | **3124** |
| 31 | **B** |
| 32 | **C** |
| 33 | **D** |
| 34 | **D** |

---

# ⚠️ QUALITY-CONTROL NOTE

During validation, one issue was found in **DILR Set 1**:

- Q15 says **B presents on Monday**.
- But B must present immediately after D.
- Therefore D would have to be in position 0, which is impossible.

So **Q15 is deliberately withdrawn from scoring**.

This is not a harmless typo: a CAT-quality DILR set must have a logically consistent question universe. I would rather flag and withdraw it than manufacture an answer.

Also note that the original condition temporarily mentioning F was corrected before scoring; the **final set uses only A–E**.

---

# 🔥 DAY 62 — 99+ SHORTCUT BANK

### Arithmetic

**Successive percentages**

\[
\boxed{(1+a)(1+b)}
\]

not \(1+a+b\).

**Work**

\[
\boxed{\text{Work}=\text{Rate}\times\text{Time}}
\]

**Train**

Pole crossing:

\[
\boxed{v=\frac{\text{train length}}{\text{time}}}
\]

then platform crossing gives total distance.

---

### Algebra

For:

\[
x+\frac1x=k,
\]

define:

\[
S_n=x^n+\frac1{x^n}.
\]

Then:

\[
\boxed{S_n=kS_{n-1}-S_{n-2}}.
\]

This is an extremely useful CAT shortcut.

---

### Geometry

Tangent:

\[
\boxed{\text{radius}\perp\text{tangent}}
\]

Heron:

\[
\boxed{\Delta=\sqrt{s(s-a)(s-b)(s-c)}}.
\]

---

### Number System

Divisors of:

\[
p_1^{a_1}p_2^{a_2}\cdots
\]

are counted by:

\[
\boxed{(a_1+1)(a_2+1)\cdots}.
\]

If divisibility restrictions exist, impose **minimum exponents first**.

---

### Modern Math

“At least \(k\)” usually suggests:

\[
\boxed{\text{Total}-\text{fewer than }k}.
\]

Simultaneous card selection:

\[
\boxed{\text{combinations}}
\]

are generally cleaner than ordered probability.

---

# 🎯 DAY 62 — ATTEMPT ORDER

### QA First Pass
**Q4 → Q5 → Q7 → Q9 → Q10 → Q11**

### QA Second Pass
**Q1 → Q2 → Q3 → Q6 → Q8**

### Final 99+ Attack
**Q12**

For Q12, do **not** start testing \(x=1,2,3,\ldots\).

Immediately transform:

\[
\boxed{4(x^2+xy+y^2)=3(x+y)^2+(x-y)^2}.
\]

That converts a two-variable search into a bounded one-variable search.

---

### DILR

**Set 2 first** — direct table and percentage adjustments.

For Set 1:

\[
\boxed{DB}
\]

should be treated as one block.

Then combine it with:

\[
A<C,\qquad E<C.
\]

---

### VARC

Today's two RCs deliberately contain a similar CAT pattern:

> **Do not mistake a qualification for an extreme conclusion.**

Watch especially for options containing:

- always
- necessarily
- only
- impossible
- every
- completely

unless the passage itself supports that strength.

---

# 🧠 DAY 62 — THE 99+ HABIT

Today's principle:

\[
\boxed{\textbf{Reduce the number of moving parts.}}
\]

Examples:

- Q4 → replace fifth powers with a recurrence.
- Q8 → replace divisor enumeration with exponent choices.
- Q12 → replace two variables with \(x+y\) and \(x-y\).
- DILR → replace adjacent people with a block.
- VARC → replace individual sentences with their argumentative function.

At 99+ percentile level, the decisive skill is increasingly:

\[
\boxed{\text{recognise structure before doing arithmetic}.}
\]

And as today's DILR validation demonstrates, **logical consistency itself is part of CAT-level reasoning**: when a condition makes a case impossible, eliminate it immediately rather than trying to force it into the arrangement.

---
