---
layout: default
title: Collaborative discussions
---

[Home](index.html)

# Collaborative discussions: my twelve posts

The module had three collaborative discussions. For each one I wrote an initial post, two peer responses and a summary post. All twelve are reproduced here as posted, with links to the threads on the module site. I posted the first nine on 3 October, after Discussions 1 and 2 had formally closed, and the three summaries on 12 October after classmates had replied. The [reflective piece](reflection.html) says what I make of that.

What I argued, in one line each: in Discussion 1, that the benefit of agents for organisations is delegation with clear limits rather than autonomy itself, and that our own Retrieval Agent is closer to a structured function than to an agent; in Discussion 2, that the choice is not an agent communication language against method calls but how much of a contract each boundary needs; in Discussion 3, that the most serious ethical issue with generative models is fluent fabrication, and that most harms can only be reduced by making them measurable.

<a id="cd1"></a>
## Collaborative Discussion 1: Agent Based Systems

Units 1 to 3. Topic: what has led to the rise of agent-based systems, and the benefits this approach can offer organisations. Forum: [https://www.my-course.co.uk/mod/forum/view.php?id=1381232](https://www.my-course.co.uk/mod/forum/view.php?id=1381232)

<details markdown="1">
<summary><strong>Initial Post</strong> — posted 3 October 2026 · <a href="https://www.my-course.co.uk/mod/forum/discuss.php?d=392004">thread</a></summary>

Initial Post

I am posting this later than planned. The advantage is that the research agent our team designed has now been built and tested, so I can write about what actually happened and not only about the design.

Agent-based systems became popular because computing itself changed. Work is now spread across networks, services and organisations, and one program cannot see or control all of it. Wooldridge and Jennings (1995) describe an agent as autonomous, reactive, pro-active and social, and this definition is still useful today. Jennings (2000) argues that breaking a complex system into interacting agents is a natural way to build it, because each agent can take responsibility for one part of the problem. More recently, large language models have given agents a general way to plan, read and write. Wang et al. (2024) describe LLM-based agents in terms of profile, memory, planning and action modules.

For organisations, I think the main benefit is not autonomy itself but delegation with clear limits. Coming from logistics, I see this as similar to delegating to a warehouse team. Routine decisions are handed over, but there are checkpoints where a person signs off. Parasuraman, Sheridan and Wickens (2000) make the same point in a more formal way. Automation is not all or nothing, and its level can be set separately for gathering information, analysing it, deciding and acting.

Additional Task

STORM breaks a topic into perspectives and questions before it searches and builds an outline (Shao et al., 2024). PaSa separates a Crawler that searches from a Selector that judges each paper against the request (He et al., 2025). In both cases the model does not simply answer from memory. This is important, because a model answering from memory can invent sources. Walters and Wilder (2023) found that 55% of the citations produced by GPT-3.5 and 18% of those produced by GPT-4 were fabricated.

The design decision our team made, and I then built, was a deterministic orchestrator with three agents. A Planning Agent (language model) breaks the question into sub-questions, a Retrieval Agent with no language model searches for papers, and an Evaluation and Synthesis Agent (language model) scores and summarises them. A researcher approves the plan before any search and the evidence before any writing, and every DOI is checked against Crossref. After our tutor's feedback, I changed the Retrieval Agent to search both OpenAlex and Semantic Scholar for every sub-question instead of using one as a fallback. This proved useful in the live runs. On 2 October Semantic Scholar refused every live search, and each run continued with OpenAlex and recorded the gap in its output instead of hiding it.

References

He, Y. et al. (2025) 'PaSa: an LLM agent for comprehensive academic paper search', Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers). Vienna: Association for Computational Linguistics, pp. 11663–11679. Available at: https://doi.org/10.18653/v1/2025.acl-long.572

Jennings, N.R. (2000) 'On agent-based software engineering', Artificial Intelligence, 117(2), pp. 277–296. Available at: https://doi.org/10.1016/S0004-3702(99)00107-1

Parasuraman, R., Sheridan, T.B. and Wickens, C.D. (2000) 'A model for types and levels of human interaction with automation', IEEE Transactions on Systems, Man, and Cybernetics – Part A: Systems and Humans, 30(3), pp. 286–297. Available at: https://doi.org/10.1109/3468.844354

Shao, Y. et al. (2024) 'Assisting in writing Wikipedia-like articles from scratch with large language models', Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers). Mexico City: Association for Computational Linguistics, pp. 6252–6278. Available at: https://doi.org/10.18653/v1/2024.naacl-long.347

Walters, W.H. and Wilder, E.I. (2023) 'Fabrication and errors in the bibliographic citations generated by ChatGPT', Scientific Reports, 13, article 14045. Available at: https://doi.org/10.1038/s41598-023-41032-5

Wang, L. et al. (2024) 'A survey on large language model based autonomous agents', Frontiers of Computer Science, 18(6), article 186345. Available at: https://doi.org/10.1007/s11704-024-40231-1

Wooldridge, M. and Jennings, N.R. (1995) 'Intelligent agents: theory and practice', The Knowledge Engineering Review, 10(2), pp. 115–152. Available at: https://doi.org/10.1017/S0269888900008122

</details>

<details markdown="1">
<summary><strong>Peer Response 1 (reply to Lana)</strong> — posted 3 October 2026 · <a href="https://www.my-course.co.uk/mod/forum/discuss.php?d=379503">thread</a></summary>

Peer Response

Hi Lana,

Your post gives a clear explanation of why splitting work across specialised agents makes a system harder to bring down. I would like to add some evidence from the research agent I built from our team's design, because it tested this point in practice.

The Retrieval Agent searches two sources for every sub-question and continues if one of them fails. On 2 October, Semantic Scholar refused all sixteen of my live searches. Every run still finished, and the three runs on new questions used OpenAlex as their only source. So the resilience was real. However, those runs were narrower ones, because half of the planned sources were missing, and nothing in the final list of papers showed it. Without a line in the output saying so, a reader would never have known.

For this reason, I think decentralised failure handling only helps an organisation if the degraded operation is visible. The brief now states how many searches each source answered and warns that coverage may be narrower. Jennings (2000) treats the relationships between agents as part of the design, and I would add a reporting line from every agent to whoever relies on its result.

I am less sure about "less manual oversight" as a benefit. Parasuraman, Sheridan and Wickens (2000) argue that the level of automation should be chosen separately for each stage, from gathering information to acting on a decision. In our design the searching is fully automated, but a person approves the plan and the evidence. The aim was not less oversight, but oversight placed where mistakes are expensive.

Your analysis would be even stronger if it showed where the human checkpoints should sit in the supply-chain examples you mention. Where would you put them?

References

Jennings, N.R. (2000) 'On agent-based software engineering', Artificial Intelligence, 117(2), pp. 277–296. Available at: https://doi.org/10.1016/S0004-3702(99)00107-1

Parasuraman, R., Sheridan, T.B. and Wickens, C.D. (2000) 'A model for types and levels of human interaction with automation', IEEE Transactions on Systems, Man, and Cybernetics – Part A: Systems and Humans, 30(3), pp. 286–297. Available at: https://doi.org/10.1109/3468.844354

</details>

<details markdown="1">
<summary><strong>Peer Response 2 (reply to Dragos)</strong> — posted 3 October 2026 · <a href="https://www.my-course.co.uk/mod/forum/discuss.php?d=384275">thread</a></summary>

Peer Response

Hi Dragos,

Your post describes our team's design very well. Reading it again now that the system is built, most of it held up. One part held up even better than I expected.

You argued that deterministic code should check the messages between agents. In the live runs of 2 October, 18 of the 56 first replies from the language model failed the schema check and needed the single repair the system allows. None needed a second. Without that check, almost a third of the model's replies would have passed broken data to the next stage. For me, this is the strongest evidence I have that bounded autonomy is a practical necessity with a cheaper model and not just a preference.

Tugba asked you when separate agents become unnecessary complexity, and I think the question applies to us as well. Our Retrieval Agent has no language model at all. It counts usable records and asks for a new query when there are too few, and in practice it never had to. Is that really an agent? Wooldridge and Jennings (1995) ask for autonomy, reactivity, pro-activeness and social ability. It pursues a target on its own and reacts to what a search returns, but its social ability is limited to handing results to the orchestrator. To be honest, it is closer to a well-structured function with a goal check. What made it worth separating was the failover across two sources, not autonomy.

Your point about predictable cost was also confirmed. Three fresh runs on new questions made 18, 28 and 22 model requests. This came from the fixed sequence and the one-retry cap rather than from the agents themselves.

Would you now separate an agent from a component by what it decides, or by whether it can refuse a request?

References

Wooldridge, M. and Jennings, N.R. (1995) 'Intelligent agents: theory and practice', The Knowledge Engineering Review, 10(2), pp. 115–152. Available at: https://doi.org/10.1017/S0269888900008122

</details>

<details markdown="1">
<summary><strong>Summary Post</strong> — posted 12 October 2026 · <a href="https://www.my-course.co.uk/mod/forum/discuss.php?d=393164">thread</a></summary>

Summary Post

In my initial post I argued that agent-based systems grew because computing became distributed and, more recently, because language models gave agents a general way to plan and communicate (Wooldridge and Jennings, 1995; Wang et al., 2024). I also argued that the main organisational benefit is delegation with clear limits rather than autonomy itself.

Essa replied to my post and suggested a separate critic agent. In our design one model scores the papers and later summarises the approved ones, and nothing independent checks its judgements apart from the researcher. I agree with the risk. Before his reply I had already run a small version of this idea. A second Gemini model judged the 65 papers of one run without seeing the agent's scores, and every disagreement was next to the cut-off. It was a check after the run, not a critic in the pipeline, but it showed where one would help most. Ali's reply to Lana also changed my view. He argued that decentralisation moves complexity into the relationships between agents instead of removing it. My runs gave a small example, because a failed search source was only visible where I had written it into the output.

Unit 1 traced the rise of agents to trends in computing, and Unit 2's first-order logic showed that organisations often need exact rules rather than judgement. In Unit 3, a deliberative agent plans well but can react slowly, while a reactive agent responds quickly but cannot pursue long-term goals (Wooldridge, 2009). My system ended up as a hybrid, with a fixed sequence of steps, the model used only for judgement, and two human review points, which fits the different levels of automation for different stages in Parasuraman, Sheridan and Wickens (2000).

Overall, my conclusion is narrower than at the start. Agent-based systems benefit organisations when the work is distributed and uncertain, and when each agent's autonomy is bounded, logged and checked by something other than the agent itself.

References

Parasuraman, R., Sheridan, T.B. and Wickens, C.D. (2000) 'A model for types and levels of human interaction with automation', IEEE Transactions on Systems, Man, and Cybernetics – Part A: Systems and Humans, 30(3), pp. 286–297. Available at: https://doi.org/10.1109/3468.844354

Wang, L. et al. (2024) 'A survey on large language model based autonomous agents', Frontiers of Computer Science, 18(6), article 186345. Available at: https://doi.org/10.1007/s11704-024-40231-1

Wooldridge, M. (2009) An introduction to multiagent systems. 2nd edn. Chichester: John Wiley & Sons.

Wooldridge, M. and Jennings, N.R. (1995) 'Intelligent agents: theory and practice', The Knowledge Engineering Review, 10(2), pp. 115–152. Available at: https://doi.org/10.1017/S0269888900008122

</details>

<a id="cd2"></a>
## Collaborative Discussion 2: Agent Communication Languages

Units 5 to 7. Topic: the advantages and disadvantages of agent communication languages such as KQML, and how they compare with method invocation in Python or Java. Forum: [https://www.my-course.co.uk/mod/forum/view.php?id=1381259](https://www.my-course.co.uk/mod/forum/view.php?id=1381259)

<details markdown="1">
<summary><strong>Initial Post</strong> — posted 3 October 2026 · <a href="https://www.my-course.co.uk/mod/forum/discuss.php?d=392006">thread</a></summary>

Initial Post

The main advantage of KQML is that a message states what kind of act it is. Based on speech act theory (Searle, 1969), a performative such as ask-if, tell or achieve separates the force of a message, meaning the act it performs, from its content, and the content language and ontology are named separately as well (Finin et al., 1994). As a result, two systems built by different organisations, in different programming languages, can exchange requests without sharing any code. A method call in Python or Java offers none of this. The caller and the callee share an interface, the call simply means "run this", and the callee has no choice.

However, the disadvantages are the other side of the same design. The meaning of the performatives was never defined precisely enough, and semantics became the main unresolved issue for agent communication languages (Labrou, Finin and Peng, 1999). Singh (1998) adds a deeper objection. If a performative is defined by the sender's beliefs and intentions, nobody else can check whether it was used correctly, because those mental states are private. He suggested defining communication by the public commitments it creates instead. There is also a practical overhead in parsing, routing and agreeing on ontologies, whereas a method call is checked by the language itself.

Building the research agent our team designed made this comparison concrete for me. In the design discussion, Dragos proposed a KQML-style request for the moment when the Retrieval Agent asks the Planning Agent for a new query. In the build, it became a normal Python method call carrying the sub-question and a written reason, routed through the orchestrator. Interestingly, something similar to an ACL appeared anyway, at the boundary with the language model. Every prompt describes the task in natural language together with the exact JSON format expected back, and every reply is validated against that schema before it is used. In this way the schema plays the role of the agreed content language. When a reply fails, which happened for 18 of 56 first replies on 2 October, the error is sent back to the model once for repair.

In summary, method invocation suits components under one design authority, while an ACL is worth its overhead when the receiver is truly independent and its replies cannot simply be trusted.

References

Finin, T., Fritzson, R., McKay, D. and McEntire, R. (1994) 'KQML as an agent communication language', Proceedings of the Third International Conference on Information and Knowledge Management (CIKM '94). New York: ACM, pp. 456–463. Available at: https://doi.org/10.1145/191246.191322

Labrou, Y., Finin, T. and Peng, Y. (1999) 'Agent communication languages: the current landscape', IEEE Intelligent Systems, 14(2), pp. 45–52. Available at: https://doi.org/10.1109/5254.757631

Searle, J.R. (1969) Speech acts: an essay in the philosophy of language. Cambridge: Cambridge University Press. Available at: https://doi.org/10.1017/CBO9781139173438

Singh, M.P. (1998) 'Agent communication languages: rethinking the principles', Computer, 31(12), pp. 40–47. Available at: https://doi.org/10.1109/2.735849

</details>

<details markdown="1">
<summary><strong>Peer Response 1 (reply to Dragos)</strong> — posted 3 October 2026 · <a href="https://www.my-course.co.uk/mod/forum/discuss.php?d=386499">thread</a></summary>

Peer Response

Hi Dragos,

Your post draws a clear and practical line between deterministic operations and requests that need interpretation. Now that the system is built, your boundary held, although not exactly in the form you proposed.

Deduplication went just as you described, as a plain function the orchestrator calls. The reformulation request did not become a KQML message either. It became a method call to the Planning Agent with the sub-question and a reason. The reason is a sentence the orchestrator writes after scoring, for example how many of the returned records were judged relevant against the minimum. So the "perform" you wanted is carried by the prompt's wording rather than a performative.

The Planning Agent can reinterpret, because it writes whatever query it thinks is best. However, it cannot refuse, negotiate or ask back, and only one reformulation per sub-question is allowed. By your own test in Lara's thread, this is method invocation with an agent's judgement inside, not agent communication.

Imoh's interaction contract is the part I wish I had read before building. I implemented part of it anyway. The brief keeps the original query next to the new one, and the log records why the rewrite was requested and that it used the one allowed attempt. The old query's results are also kept, which covers part of the fallback. I did not implement refusal or confidence. Singh (1998) argues that communication should be judged by the public commitments it creates rather than by private intentions, and the recorded before-and-after query is the closest thing we have to that, because anyone can check afterwards whether the rewrite still served the sub-question.

If you rebuilt it, would you give the Planning Agent the right to answer "this cannot be searched better" instead of always returning a new query?

References

Singh, M.P. (1998) 'Agent communication languages: rethinking the principles', Computer, 31(12), pp. 40–47. Available at: https://doi.org/10.1109/2.735849

</details>

<details markdown="1">
<summary><strong>Peer Response 2 (reply to Lana)</strong> — posted 3 October 2026 · <a href="https://www.my-course.co.uk/mod/forum/discuss.php?d=386375">thread</a></summary>

Peer Response

Hi Lana,

Your post explains the contrast between closed, trusted systems that suit method invocation and open systems that need an ACL very clearly. I would like to add a third situation that I did not expect before building our research agent, which is a component inside our own code whose replies we could not trust.

The Planning and Evaluation agents in the system I built are called through ordinary Python methods, so in your terms the coupling is tight. However, each call ends at a language model, whose reply may or may not match what was asked. So I treated that boundary as if it were open. Each prompt states the exact JSON format expected, and each reply is checked against a schema before it is used. On 2 October, 18 of 56 first replies failed this check. The failure was never about meaning. It was about form, because each time the model returned a plain list where an object was required. A single repair request, with the error attached, fixed every one.

This makes me think that the semantic problem Labrou, Finin and Peng (1999) placed at the centre of ACL research is only half of the problem in practice. Before two agents can disagree about what "tell" means, they need to agree on the shape of the message, and with language models even that cannot be assumed. Yasmin's suggestion of negotiating meanings would come after this step, not instead of it.

Your conclusion would be even stronger with one more measure: a typed contract at every boundary, checked at run time, with failures logged and counted. It is cheaper than a full ACL and catches the errors that actually occurred.

Would you count a schema-checked JSON message as a minimal ACL, or is it still method invocation?

References

Labrou, Y., Finin, T. and Peng, Y. (1999) 'Agent communication languages: the current landscape', IEEE Intelligent Systems, 14(2), pp. 45–52. Available at: https://doi.org/10.1109/5254.757631

</details>

<details markdown="1">
<summary><strong>Summary Post</strong> — posted 12 October 2026 · <a href="https://www.my-course.co.uk/mod/forum/discuss.php?d=393193">thread</a></summary>

Summary Post

In my initial post I argued that the strength of KQML is making the force of a message explicit, separately from its content and ontology (Searle, 1969; Finin et al., 1994), and that its weakness is semantics that were never agreed precisely enough to guarantee understanding (Labrou, Finin and Peng, 1999). Method invocation is the opposite: tightly coupled, checked by the language, and silent about intent.

Essa replied to my post. He suggested limiting the number of repairs, treating the exchange as a failure, or escalating to a person, so that a retry loop cannot run on. Our system does part of this. A reply that fails the schema check is repaired once, and if the repair fails the run stops with a message. No live reply needed a second repair, and there is no other escalation. In other threads, Imoh's reply to Dragos proposed an explicit contract for a reformulation request, and Dragos asked in Lara's thread whether a receiver that cannot reject a request is really an agent. For my build the answer is no, because our Planning Agent reinterprets but cannot refuse.

The speech act material in Unit 5 explained why a request is an act and not just data. The Unit 6 exercise made the semantic problem concrete. My KQML/KIF dialogue, in which Alice asks Bob about 50-inch televisions and their HDMI slots, needed agreement on every ontology term, even on whether "available" stock includes reserved units. Unit 7 showed that natural language is harder still, although the failures in my runs were simpler, with replies of the wrong shape rather than the wrong meaning.

Overall, I now think the choice is not ACL against method calls, but how much of a contract each boundary needs. Within one design authority, typed calls are enough. With an independent or untrusted receiver, the contract has to be explicit, checked at run time and logged.

References

Finin, T., Fritzson, R., McKay, D. and McEntire, R. (1994) 'KQML as an agent communication language', Proceedings of the Third International Conference on Information and Knowledge Management (CIKM '94). New York: ACM, pp. 456–463. Available at: https://doi.org/10.1145/191246.191322

Labrou, Y., Finin, T. and Peng, Y. (1999) 'Agent communication languages: the current landscape', IEEE Intelligent Systems, 14(2), pp. 45–52. Available at: https://doi.org/10.1109/5254.757631

Searle, J.R. (1969) Speech acts: an essay in the philosophy of language. Cambridge: Cambridge University Press. Available at: https://doi.org/10.1017/CBO9781139173438

</details>

<a id="cd3"></a>
## Collaborative Discussion 3: Deep Learning

Units 9 to 11. Topic: whether technologies that generate new content, such as DALL·E and ChatGPT, raise ethical issues that should be considered. Forum: [https://www.my-course.co.uk/mod/forum/view.php?id=1381288](https://www.my-course.co.uk/mod/forum/view.php?id=1381288)

<details markdown="1">
<summary><strong>Initial Post</strong> — posted 3 October 2026 · <a href="https://www.my-course.co.uk/mod/forum/discuss.php?d=392007">thread</a></summary>

Initial Post

Yes, these technologies raise ethical issues, and I would put one of them ahead of the others. These systems produce false statements with the same fluency as true ones. Ji et al. (2023) call this hallucination and show that it appears across summarisation, dialogue and question answering. Walters and Wilder (2023) measured one form of it directly. In short literature reviews written by ChatGPT, 55% of the citations from GPT-3.5 and 18% of those from GPT-4 pointed to papers that do not exist.

The ethical problem is not only the error itself but also who carries the responsibility. Weidinger et al. (2022) list misinformation among the main risk areas of language models, and Bender et al. (2021) argue that fluent text makes readers assume a meaning and intent that is not really there. Fluency also creates trust. Parasuraman and Manzey (2010) show that people monitor reliable automation less, especially when they are busy with other tasks, so the rare wrong answer gets through. If a student, clinician or journalist repeats a fabricated source, they carry the consequences, not the model.

Regulation only helps in part. The EU AI Act requires providers of systems that generate synthetic text, images, audio or video to mark the outputs in a machine-readable format so that they can be detected as artificially generated (European Union, 2024, Article 50(2)). This deals with deception about the origin of content, but a correctly marked paragraph can still be wrong.

Additional Task

For the research agent I built from our team's design, I chose the explainability of relevance decisions. For every paper it scores, the model is asked for a one-sentence reason pointing to what the abstract does or does not cover, and the researcher sees these reasons before approving the evidence. Every DOI is also checked against Crossref, and failures are flagged rather than hidden. These explanations showed me weaknesses I would otherwise have missed. In one run, four papers with no abstract were kept on the strength of their titles alone, and the reasons said so. On our main question, 28 of 77 approved papers could not be verified with Crossref, typically preprints registered elsewhere.

To address the remaining risk, I would keep the reasons and flags visible, make the human approval step mandatory, and measure the screening against people's judgements instead of assuming that it works.

References

Bender, E.M., Gebru, T., McMillan-Major, A. and Shmitchell, S. (2021) 'On the dangers of stochastic parrots: can language models be too big?', Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency (FAccT '21). New York: ACM, pp. 610–623. Available at: https://doi.org/10.1145/3442188.3445922

European Union (2024) Regulation (EU) 2024/1689 of the European Parliament and of the Council of 13 June 2024 laying down harmonised rules on artificial intelligence (Artificial Intelligence Act). Official Journal of the European Union, L series, 12 July. Available at: https://eur-lex.europa.eu/eli/reg/2024/1689/oj (Accessed: 2 October 2026).

Ji, Z. et al. (2023) 'Survey of hallucination in natural language generation', ACM Computing Surveys, 55(12), pp. 1–38. Available at: https://doi.org/10.1145/3571730

Parasuraman, R. and Manzey, D.H. (2010) 'Complacency and bias in human use of automation: an attentional integration', Human Factors, 52(3), pp. 381–410. Available at: https://doi.org/10.1177/0018720810376055

Walters, W.H. and Wilder, E.I. (2023) 'Fabrication and errors in the bibliographic citations generated by ChatGPT', Scientific Reports, 13, article 14045. Available at: https://doi.org/10.1038/s41598-023-41032-5

Weidinger, L. et al. (2022) 'Taxonomy of risks posed by language models', Proceedings of the 2022 ACM Conference on Fairness, Accountability, and Transparency (FAccT '22). New York: ACM, pp. 214–229. Available at: https://doi.org/10.1145/3531146.3533088

</details>

<details markdown="1">
<summary><strong>Peer Response 1 (reply to Lara)</strong> — posted 3 October 2026 · <a href="https://www.my-course.co.uk/mod/forum/discuss.php?d=391079">thread</a></summary>

Peer Response

Hi Lara,

Your post makes a strong case that fairness has to be built in throughout development and not corrected at the end. I would like to add an example from a much smaller system than DALL·E 2.

The research agent I built screens papers by asking a language model to score each title and abstract. Nothing about gender or occupation is involved, but there is still a pattern that the system keeps without anyone choosing it. Papers with no abstract in the index are judged on their titles alone. In my telemedicine test run, 9 of the 65 papers had no abstract, and whether they were kept depended on how their titles read. Mehrabi et al. (2021) would call this a measurement bias, because the same feature, relevance, is measured with much less information for one group of papers than for the rest.

The threshold is a second choice that is easy to miss. On the same research question, the cheaper Flash-Lite model kept 42 of 77 papers, while the full Flash model kept 26 of 78, each on its own plan. "Relevant" sounds neutral, but a cut-off of three out of five is a value judgement expressed as a number.

On your closing question, I would not try to decide in the abstract which patterns to keep. I would write the criterion down, show it to the people affected, and measure the outputs against their judgements. Gallegos et al. (2024), whom you cite, treat mitigation as a multi-stage problem. I would add that each stage needs its own explicit and testable criterion, otherwise decisions are made silently by default settings like ours.

Would you accept a model whose bias matches a documented reference, such as labour statistics, if that reference is itself what people want to change?

References

Gallegos, I.O. et al. (2024) 'Bias and fairness in large language models: a survey', Computational Linguistics, 50(3), pp. 1097–1179. Available at: https://doi.org/10.1162/coli_a_00524

Mehrabi, N., Morstatter, F., Saxena, N., Lerman, K. and Galstyan, A. (2021) 'A survey on bias and fairness in machine learning', ACM Computing Surveys, 54(6), pp. 1–35. Available at: https://doi.org/10.1145/3457607

</details>

<details markdown="1">
<summary><strong>Peer Response 2 (reply to Lana)</strong> — posted 3 October 2026 · <a href="https://www.my-course.co.uk/mod/forum/discuss.php?d=391135">thread</a></summary>

Peer Response

Hi Lana,

Your post gives a broad overview of the ethical issues. Your list covers deliberate misuse, but I would like to add the unintended version of the same harm, which is honest users repeating content that the model invented. In our project, this was the starting point. Walters and Wilder (2023) found that 55% of the citations GPT-3.5 produced in literature reviews were fabricated, so the research agent I built never lets the model supply a reference. Every paper comes from a scholarly index, and its DOI is checked against Crossref.

Anne asked how each harm can be linked to a specific, measurable control, and our case is one small answer. Fabricated references are linked to DOI verification, and the result can be counted. On my main test run, 78 of the 117 papers found had a DOI that Crossref confirmed with a matching title, and the rest were flagged rather than dropped. This is a control that someone can audit.

However, it also shows the limit of fixing harms one at a time, which supports your conclusion. The same pipeline asks the model to summarise each abstract, and a verified DOI says nothing about whether the summary is faithful. Maynez et al. (2020) found that abstractive summaries often contain content that the source does not support. I could not check this automatically, so the brief tells the reader to check the summaries against the full texts.

All things considered, I agree with your holistic approach, with one condition. Each harm still needs its own named control and a measure of how often it fails, otherwise "holistic" can hide the gaps. Which of your five issues do you think is the hardest to measure in this way?

References

Maynez, J., Narayan, S., Bohnet, B. and McDonald, R. (2020) 'On faithfulness and factuality in abstractive summarization', Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics. Online: Association for Computational Linguistics, pp. 1906–1919. Available at: https://doi.org/10.18653/v1/2020.acl-main.173

Walters, W.H. and Wilder, E.I. (2023) 'Fabrication and errors in the bibliographic citations generated by ChatGPT', Scientific Reports, 13, article 14045. Available at: https://doi.org/10.1038/s41598-023-41032-5

</details>

<details markdown="1">
<summary><strong>Summary Post</strong> — posted 12 October 2026 · <a href="https://www.my-course.co.uk/mod/forum/discuss.php?d=393194">thread</a></summary>

Summary Post

In my initial post I argued that the most serious ethical issue with generative models is fluent fabrication, and that the responsibility for it falls on the people who trust the output (Ji et al., 2023; Walters and Wilder, 2023). I also argued that marking AI-generated content, as Article 50(2) of the EU AI Act requires (European Union, 2024), deals with origin but not accuracy.

Yasmin replied and suggested making verification mandatory, showing users why each source was chosen, and evaluating the agent against people's judgements. My research agent does the first two. The third has not been done. I stopped judging papers by hand after four, and the second-model check I ran instead only measures agreement between two models. Fedi asked how I know the reason shown to the researcher is right, since the model writes it too. I cannot check it automatically. In his agent the model must quote the abstract and the code checks the quote word for word, so the reason has something checkable. He also noted that generated text can return in later training data and degrade future models (Shumailov et al., 2024). On responsibility he only half agreed with me, because users cannot see how often a model is wrong and the company can. That is a fair point.

Units 9 and 10 helped explain why grounding matters. A deep network learns statistical patterns, not facts it can cite, so there is no internal record to check an output against. In the Unit 11 examples from manufacturing and finance, a wrong output becomes an action, not just a sentence.

Overall, I think most of these harms can only be reduced by making them measurable. Each output should come with something a program can check, and both the provider and the user should stay accountable for what cannot be checked.

References

European Union (2024) Regulation (EU) 2024/1689 of the European Parliament and of the Council of 13 June 2024 laying down harmonised rules on artificial intelligence (Artificial Intelligence Act). Official Journal of the European Union, L series, 12 July. Available at: https://eur-lex.europa.eu/eli/reg/2024/1689/oj (Accessed: 2 October 2026).

Ji, Z. et al. (2023) 'Survey of hallucination in natural language generation', ACM Computing Surveys, 55(12), pp. 1–38. Available at: https://doi.org/10.1145/3571730

Shumailov, I., Shumaylov, Z., Zhao, Y., Papernot, N., Anderson, R. and Gal, Y. (2024) 'AI models collapse when trained on recursively generated data', Nature, 631(8022), pp. 755–759. Available at: https://doi.org/10.1038/s41586-024-07566-y

Walters, W.H. and Wilder, E.I. (2023) 'Fabrication and errors in the bibliographic citations generated by ChatGPT', Scientific Reports, 13, article 14045. Available at: https://doi.org/10.1038/s41598-023-41032-5

</details>
