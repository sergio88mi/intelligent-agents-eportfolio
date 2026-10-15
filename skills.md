---
layout: default
title: Skills matrix
---

[Home](index.html)

# Professional skills matrix and development plan

The eleven skills are the ones the module lists for the e-portfolio. The self-assessment uses the same kind of scale as my last module: strong growth, improved, adequate, weak. The evidence column points to things in this portfolio.

| Skill | Self-assessment | Evidence this module | Action |
|---|---|---|---|
| Time management | Weak | Team report on time; individual build on time; forum posts for all three discussions on one day in October, after two had closed | Post in the discussions in the week they open. The next module's e-portfolio is the test |
| Commercial awareness | Improved | Model choice justified from price, quota and benchmarks; free-tier data use flagged as a reason for a paid key on confidential questions | Cost every run before choosing a model, not after |
| Critical thinking and analysis | Strong growth | Every departure from the proposal listed with a reason; "agreement is not accuracy" stated where a better-looking number was available | Keep the "what is not measured" section in every README |
| Communication and literacy | Improved | Twelve forum posts with verified references; a README that a stranger can run from; a ten-slide narrated presentation | Shorter posts |
| IT and digital | Strong growth | A working multi-agent system in plain Python, 113 unit tests, sixteen functional tests, Crossref verification, a disk cache, two API clients with failover | Learn one agent framework well enough to say why I did not use one |
| Resilience | Improved | A retired model, three kinds of rate limit, a quota that killed runs at night; every one logged, fixed and written into the evidence | Build the retry and stop rules before the first live run next time |
| Interpersonal | Adequate | Replied to six posts by three classmates; three others replied to mine; no calls with the team | One call at the start of the next team project and one before the deadline |
| Problem-solving | Strong growth | Twenty-one remediation entries, each with cause, change and verification; the second-model check built when hand judging proved too slow | Keep the remediation log from day one |
| Ethical awareness | Improved | DOI verification against fabricated references; EU AI Act Article 50(2) read in the source; the responsibility question in Discussion 3 and the Unit 10 post | Add the checkable quote to every model reason before using the agent for real work |
| Teamwork and leadership | Adequate | Class diagram delivered early and used by the whole team; asynchronous work that produced a complete report; no meetings | Propose the first meeting myself |
| Critical reflection | Improved | Three case studies and a reflective piece that say what did not work, including the timing of my forum posts | Write the reflection during the module, not at the end |

## Development plan

1. **Forum posts in week one.** At the end of the last module I wrote that I would post in the discussions. I did, but late. This time the plan has a date: the initial post for the first discussion of the next module goes up in its first week, and this portfolio will be checked against that.
2. **No measure without a dataset.** Before claiming precision or recall for any screening step, build the gold set first, even a small one, and report agreement with people rather than between models.
3. **Checkable reasons.** Make the model quote the abstract for every paper it keeps and have the code verify the quote, so that every explanation carries something a program can test.
4. **Two calls per team project.** One at the start to agree the split, one before the internal deadline to catch what is late. Keep the chat and the shared folder, which worked.
5. **Retry and stop rules first.** Write the transient-error retry, the quota stop and the logging before the first call to any paid or rate-limited service, so that the first failure is recorded rather than lost.

## AI acknowledgement

Generative AI (Claude) helped me draft and edit this page. The full statement is on the [home page](index.html#ai-acknowledgement).
