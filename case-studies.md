---
layout: default
title: Case studies
---

[Home](index.html)

# Three reflective case studies

Each case study follows the three questions of Rolfe, Freshwater and Jasper (2001): what happened, what it meant, and what I will do differently. All three come from the research agent I built from our team's design.

## 1. Explainable decisions: the one-sentence reason

**What.** For every paper the agent scores, the model has to give a one-sentence reason that points to what the abstract does or does not cover, and the researcher sees those reasons before approving the evidence. In the telemedicine run of 2 October, 9 of the 65 papers had no abstract in the index. Four of them were kept at the cut-off score, and their reasons said, in effect, that there was no abstract and the title looked relevant. A second model, asked the same question without seeing the scores, disagreed with the agent on eight kept papers, and all eight sat at the cut-off.

**So what.** The reasons did their job. They showed me a weakness I would otherwise have missed, which is that papers without abstracts are judged on their titles alone and still pass. But a classmate's question in the forum went further: the reason is written by the same model, so how do I know the reason itself is right? I cannot check it automatically. An explanation that cannot be checked is a story, and Maynez et al. (2020) show how easily a model's story drifts from its source.

**Now what.** The next version will make the model quote the abstract for every paper it keeps, and the code will check the quote word for word. A reason with a verified quote inside it is something a program can test. That cannot work for papers with no abstract, so those will be shown to the researcher as a flagged group instead of being judged on their titles inside a score.

## 2. AI safety constraints: bounded autonomy

**What.** The design caps the system's autonomy at every step: one automatic query rewrite per sub-question, one scope revision per run, one repair of a model reply that fails the schema, and a hard stop when the daily quota is reached. One of these caps fired in practice, and one gap showed up next to them. On 23 September the word "approv", a typo, was read as feedback at the first review and the system re-planned. On 2 October a run on the food-waste question had one sub-question that stayed below the relevance threshold after its single rewrite, and the system recorded the thin evidence instead of trying again.

**So what.** The typo incident is the one I think about most. Nothing was broken; the system did exactly what it was told. A person had typed something ambiguous and an autonomous component took it as an instruction. The fix was small, because short input that is not a known command is now re-asked, but the lesson is general. The risky moment in an agent system is not only when it fails. It is also when it obeys. Parasuraman, Sheridan and Wickens (2000) describe automation as levels that can be set separately for each stage, and the level I had set for the review step was higher than I had realised.

**Now what.** I will treat every point where human input enters an agent as a boundary that needs its own validation, in the same way as a model reply. I will also keep the caps where they are. The one-rewrite limit cost me evidence on one sub-question, but a system that knows when to stop is worth more than one that tries harder.

## 3. Bias in autonomous decision-making: the cut-off

**What.** The agent keeps a paper when the model scores it 3 or more out of 5. On the same research question, the Flash-Lite model kept 42 of 77 papers where the full Flash model kept 26 of 78, each on the plan it had written itself. On the telemedicine run, every disagreement between the second model and the agent sat next to the cut-off, at a score of 2 or 3. And the papers with no abstract were scored from much less information than the rest, which Mehrabi et al. (2021) would call a measurement bias.

**So what.** None of this involves people, gender or race, and it is still bias in the plain sense: the system systematically favours some papers over others for reasons that have nothing to do with the research question. A cut-off of three out of five reads as neutral and is a value judgement expressed as a number. Which model you can afford changes which papers you read. A missing abstract in the index changes a paper's chances. I had chosen the cut-off for convenience and not calibrated it at all.

**Now what.** Before the cut-off is used for real work, it needs to be set against people's judgements on a small gold set, separately for each model. Papers without abstracts should be shown to the researcher as a group, so that the decision about them is made once and openly, rather than paper by paper inside a score.

## References

Maynez, J., Narayan, S., Bohnet, B. and McDonald, R. (2020) 'On faithfulness and factuality in abstractive summarization', *Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics*. Online: Association for Computational Linguistics, pp. 1906–1919. Available at: https://doi.org/10.18653/v1/2020.acl-main.173

Mehrabi, N., Morstatter, F., Saxena, N., Lerman, K. and Galstyan, A. (2021) 'A survey on bias and fairness in machine learning', *ACM Computing Surveys*, 54(6), pp. 1–35. Available at: https://doi.org/10.1145/3457607

Parasuraman, R., Sheridan, T.B. and Wickens, C.D. (2000) 'A model for types and levels of human interaction with automation', *IEEE Transactions on Systems, Man, and Cybernetics – Part A: Systems and Humans*, 30(3), pp. 286–297. Available at: https://doi.org/10.1109/3468.844354

Rolfe, G., Freshwater, D. and Jasper, M. (2001) *Critical reflection in nursing and the helping professions: a user's guide*. Basingstoke: Palgrave Macmillan.
