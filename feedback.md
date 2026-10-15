---
layout: default
title: Feedback
---

[Home](index.html)

# Feedback from the tutor and from peers

## Tutor feedback on the team design proposal (64%, Merit)

Received on the module site; read on 29 September 2026. The three points under "Guidance for Improvement" are quoted in full, because each one changed the build.

> 1. Your team mentions using a general-purpose LLM, but there is not enough evidence to explain why that model was chosen. Include relevant benchmarks, context limits, function-calling performance and pricing or quota information to support your choice.
>
> 2. You mention testing with pytest, but the targets for measuring retrieval and synthesis quality are still quite broad. Set clear targets for things such as recall, precision, citation accuracy and deduplication, and explain what dataset you will use to test them.
>
> 3. The main retrieval process depends heavily on the Semantic Scholar API, with OpenAlex only used as a fallback. Consider using several sources as part of the normal retrieval process, with automatic failover, to improve search coverage and reduce the impact of downtime or rate limits.

What I did with each: the README has a section, *Why this model*, with the provider's own figures for context limits, structured output, quota, price and benchmarks (point 1). It states the targets and the dataset each one needs, and says plainly that the first three are not measured (point 2). Both sources are now searched for every sub-question with automatic failover, which kept every run alive when Semantic Scholar refused all sixteen live searches on 2 October (point 3).

The positive comments singled out the diagrams, the deterministic orchestrator and the human review points. The class diagram was my part of the report.

## Peer feedback in the collaborative discussions

Three classmates replied to my initial posts, all after I had built the system, so their comments are about something that exists.

- **Essa** (Discussions 1 and 2, 12 October) suggested a separate critic agent, so that the model does not validate its own interpretation, and a capped number of repairs with a defined failure state and escalation to a person. The first is the next change I would make; the second is close to what the system already does.
- **Yasmin** (Discussion 3, 6 October) suggested mandatory verification, showing the researcher why each source was chosen, and evaluation against people's judgements. The system does the first two. The third has not been done.
- **Fedi** (Discussion 3, 10 October) asked how I know the model's reason is right when the model wrote it, described his own design (a quote from the abstract checked word for word by code), and half-agreed with me on responsibility, putting the company before the user. His question is the one I keep coming back to, and his design is in my action plan.

My summary posts answer each of them; they are on the [discussions](forums.html) page.

## Feedback within the team

Lara reviewed my class diagram and pointed out the missing boundary class for the researcher. I added it. That was the one piece of direct feedback on my work inside the team, and it was right.
