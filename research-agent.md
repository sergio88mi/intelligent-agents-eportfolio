---
layout: default
title: Research agent
---

[Home](index.html)

# Individual project: the research agent

Code, README, tests and evidence: [github.com/sergio88mi/research-agent](https://github.com/sergio88mi/research-agent). The ten-slide presentation and its transcript are in the repository's `presentation/` folder.

## What it does

You give it a research question. It breaks the question into three to five sub-questions, searches OpenAlex and Semantic Scholar for each one, de-duplicates the records, checks every DOI against Crossref, scores each paper's relevance from its abstract, and writes an evidence brief: one note per paper, the themes across them, the gaps, and a reference list built from the records rather than written by the model. It stops twice to ask the researcher: once to approve the plan, once to approve the evidence.

## How it was built

Python, no agent framework, with the model (Gemini) used only for the judgement tasks: decomposing, scoring, summarising. Everything with an exact answer is ordinary code. Every model reply is checked against a schema and repaired once if it fails; if that fails too, the run stops. The build ran in eight stages between 9 September and 2 October 2026, with roughly one commit per stage. The tests grew from 5 to 68 over the stages and to 113 after a read-through on 1 October.

Evidence in the repository:

- `evidence/functional_tests.md`: sixteen live tests with steps, expected and observed results, and a section on the second-model check of one run's screening.
- `evidence/remediation_log.md`: twenty-one problems met during development, their causes, the changes made and how each fix was verified.
- `evidence/pytest_113_passed.txt` and `evidence/replay_offline.log`: the unit tests and an offline replay of the 30 September run after the corrections of 1 October.
- `evidence/judge_relevance.py` and `evidence/judge_with_model.py`: the two programs that check the relevance screening, by a person and by a second model.

## What went wrong

Most problems came from outside the code. The first call to Gemini returned a 404 because the model the build was configured for had been retired. Then came 503 errors, a read timeout, and a free quota of twenty requests a day that the retries burned through. On 23 September OpenAlex started refusing requests without a key. On 2 October Semantic Scholar's public pool refused all sixteen live searches. None of these needed a rewrite. The settings sit in one module and each service behind one small client, so each fix was a change of setting or a new retry policy.

<a id="evaluation"></a>
## Critical evaluation: the design in week 7 against the build in week 11

**What held.** The three agents, the orchestrator, both review points, both autonomy caps and the Crossref check are all in the build and match the proposal. The decision to keep the model away from anything with an exact answer paid off in a way I did not expect. In the live runs of 2 October, 18 of the 56 first replies from the model failed the schema check and were repaired. Without the check, almost a third of the model's replies would have passed broken data to the next stage.

**What changed.** The proposal put Semantic Scholar first with OpenAlex as a fallback. I built on OpenAlex alone until the last stage, because it needed no key, and only added Semantic Scholar after the tutor's feedback, as an equal source with failover. The proposal planned a varied set of test questions used throughout. I used one question for nearly all of the development and ran three others once each on the last day. Checking and scoring run one sub-question at a time, with a second retry trigger after scoring that the proposal did not have.

**What was not measured.** The feedback asked for clear targets for precision, recall, citation accuracy and de-duplication, and the dataset for each. The README states them, and states that the first three have not been measured because the datasets do not exist. I started judging the papers of one run by hand and stopped after four. A second Gemini model then judged all 65 papers of that run without seeing the agent's scores. Of the 35 kept papers it gave a clear answer on, it would keep 27 (0.77), with Cohen's kappa 0.65 over its clear answers, and every disagreement sat either side of the cut-off, at a score of 2 or 3. That is agreement between two models, not precision. De-duplication misses its target: a paper that appears under two DOIs is not merged, and this happened four times in 77 approved papers on 30 September and again on 2 October.

**What I think of it.** Against Wooldridge and Jennings (1995), the Retrieval Agent is a well-structured function with a goal check. It pursues a target and reacts to what a search returns, but its social ability is handing results to the orchestrator. What made it worth separating was the failover across two sources, not autonomy. The system is honest about what it cannot do, which is the quality I most wanted it to have, and it is not yet evaluated against people, which is the gap I most want to close.

Reference: Wooldridge, M. and Jennings, N.R. (1995) 'Intelligent agents: theory and practice', *The Knowledge Engineering Review*, 10(2), pp. 115–152. Available at: https://doi.org/10.1017/S0269888900008122
