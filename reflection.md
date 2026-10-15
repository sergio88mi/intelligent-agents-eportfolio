---
layout: default
title: Reflective piece
---

[Home](index.html)

# Reflective piece

Intelligent Agents, July to October 2026. 922 words, excluding headings and references.

Looking back over this module, I have used the same three questions as in my last reflection, from Rolfe, Freshwater and Jasper (2001): what happened, what it meant, and what I will do next.

## What?

Group D proposed a research agent that takes a research question, plans sub-questions, searches scholarly indexes, checks every DOI against Crossref and writes an evidence brief. Two of the three agents use a language model for the judgement work, and a deterministic orchestrator does everything with an exact answer. My part of the proposal was the class diagram, which fixed the names and responsibilities before anyone wrote code. We never held a meeting. We split the sections on WhatsApp, worked in a shared Google Drive, and Lara pulled the report together. It went in on 7 September and came back with 64% and three points of feedback: justify the model, set measurable targets, and use more than one source.

I then built the system on my own between 9 September and 2 October, in Python, with no agent framework. It ended with 113 unit tests, sixteen functional tests run against the live services, and a remediation log of twenty-one entries. The first call to Gemini returned a 404 because the model I had configured had been retired. Then came 503 errors, a read timeout, and a free quota of twenty requests a day that my retries burned through. After the feedback I added Semantic Scholar as a second source, searched alongside OpenAlex with failover. On 2 October Semantic Scholar refused all sixteen live searches, and every run still finished.

The collaborative discussions were a different story. I posted my initial posts and peer responses for all three discussions on 3 October, when two of them had already closed, and the summaries on 12 October after three classmates had replied.

## So what?

In my last reflection I wrote that posting in the discussions was the one thing I would do differently. I did post, all twelve, but the first nine went up on a single day in October. The honest reading is that I changed the outcome and not the habit. Time management came out as "adequate" in my last plan and it should have said "weak", because the pattern repeated. What surprised me was that the late posts still worked. Essa, Yasmin and Fedi replied, and Fedi asked the best question anyone has asked about my system: the reason the researcher reads is also written by the model, so how do I know it is right? I do not, and my summary post says so.

The build taught me something I did not expect. Most of the problems came from outside the code. A retired model, a rate limit, a quota and a policy change at OpenAlex each stopped a run, and none of them needed a rewrite, because the settings sat in one module and each service behind one small client. I had put them there for tidiness. They turned out to be the reason the project survived.

The tutor's second point, measurable targets, was the one I could not fully meet. I stated precision and recall targets in the README and the datasets each one needs, but no gold set exists, so no result is claimed. I started judging the papers of one run by hand and stopped after four. Instead, a second Gemini model judged all 65 papers without seeing the agent's scores. It agreed on most of them, with Cohen's kappa 0.65, and every disagreement sat at the cut-off. That is agreement between two models, not accuracy, and writing that sentence rather than a better-looking one was the most useful thing I did in the module. Wooldridge and Jennings (1995) ask for autonomy, reactivity, pro-activeness and social ability. Measured against that list my Retrieval Agent is a well-structured function with a goal check, and I said so in the forum. Parasuraman, Sheridan and Wickens (2000) gave me the vocabulary for what I actually built: full automation for searching, and a person at the two points where mistakes are expensive.

The feeling I associate with the build is frustration turning into a kind of stubbornness. Watching a run die at the daily quota at half past ten at night, after a day of refused attempts, made me want to stop. Writing the failure into the log and the brief, instead of hiding it, is what made the next run possible. On the team side the feeling was quieter. The work was good, but I never spoke to the people I wrote the report with, and I noticed it most when I had to answer their forum posts weeks later.

## Now what?

Three changes. First, forum posts in week one, not week ten. Last time I wrote that I would post, and I did, so the test this time is the week they go up, and the next e-portfolio will show it. Second, no measure without a dataset. Before I claim precision for any screening step I will build the gold set first, even a small one. Third, every reason a model gives should carry something the code can check. Fedi's design, a quote from the abstract verified word for word, is the first change I would make to the agent, and I will build it before I use the system for real work.

On teams, the change is small and concrete. A short call at the start and one before the internal deadline, alongside the chat. The report would have been the same. I would have known the people.

## References

Parasuraman, R., Sheridan, T.B. and Wickens, C.D. (2000) 'A model for types and levels of human interaction with automation', *IEEE Transactions on Systems, Man, and Cybernetics – Part A: Systems and Humans*, 30(3), pp. 286–297. Available at: https://doi.org/10.1109/3468.844354

Rolfe, G., Freshwater, D. and Jasper, M. (2001) *Critical reflection in nursing and the helping professions: a user's guide*. Basingstoke: Palgrave Macmillan.

Wooldridge, M. and Jennings, N.R. (1995) 'Intelligent agents: theory and practice', *The Knowledge Engineering Review*, 10(2), pp. 115–152. Available at: https://doi.org/10.1017/S0269888900008122
