---
layout: default
title: Unit 6 activity
---

[Home](index.html)

# Unit 6 – Creating Agent Dialogues

Activity: create an agent dialogue, using KQML and KIF, between two agents named Alice and Bob. Alice procures stock and Bob controls the stock levels of a warehouse. Alice asks Bob about the available stock of 50-inch televisions and about the number of HDMI slots the televisions have.

## Shared vocabulary

Before Alice can ask anything, both agents have to use the same content language and the same ontology. Here the content language is KIF and the ontology is called `warehouse-stock`. It defines four terms.

| Term | Kind | Meaning |
|---|---|---|
| `tv-50in` | object constant | the product line of 50-inch televisions held in the warehouse |
| `available-stock` | relation | `(available-stock ?product ?n)` is true when ?n units of ?product are in stock and not reserved for another order |
| `hdmi-slots` | relation | `(hdmi-slots ?product ?n)` is true when each unit of ?product has ?n HDMI slots |
| `next-delivery` | relation | `(next-delivery ?product ?date)` is true when the next delivery of ?product is due on ?date |

In KIF a word that starts with `?` is a variable (Genesereth and Fikes, 1992). In a question, the variable marks the value Alice wants Bob to fill in.

## The dialogue

**1. Alice asks how many 50-inch televisions are available**

```
(ask-one
   :sender      Alice
   :receiver    Bob
   :reply-with  q1
   :language    KIF
   :ontology    warehouse-stock
   :content     (available-stock tv-50in ?n))
```

**2. Bob replies**

```
(reply
   :sender      Bob
   :receiver    Alice
   :in-reply-to q1
   :language    KIF
   :ontology    warehouse-stock
   :content     (available-stock tv-50in 40))
```

**3. Alice asks how many HDMI slots the televisions have**

```
(ask-one
   :sender      Alice
   :receiver    Bob
   :reply-with  q2
   :language    KIF
   :ontology    warehouse-stock
   :content     (hdmi-slots tv-50in ?n))
```

**4. Bob replies**

```
(reply
   :sender      Bob
   :receiver    Alice
   :in-reply-to q2
   :language    KIF
   :ontology    warehouse-stock
   :content     (hdmi-slots tv-50in 3))
```

**5. Alice asks when more televisions will arrive**

```
(ask-one
   :sender      Alice
   :receiver    Bob
   :reply-with  q3
   :language    KIF
   :ontology    warehouse-stock
   :content     (next-delivery tv-50in ?date))
```

**6. Bob understands the question but has no answer**

```
(sorry
   :sender      Bob
   :receiver    Alice
   :in-reply-to q3)
```

The numbers (40 televisions, 3 HDMI slots) are example values for the exercise.

## How it works

- The first word of each message is the performative (Finin et al., 1994). It says what kind of act the message is. `ask-one` is a question that wants one answer, and `reply` is the answer. The module's seminar showed the same ask-one and reply pattern.
- `:content` holds the question or the answer, written in KIF. Bob's reply is the same sentence as Alice's question, with the variable replaced by a value.
- `:reply-with` and `:in-reply-to` link each answer to its question. This lets Alice match a reply to its question without reading the content, which matters when many questions are open at the same time.
- `:language` and `:ontology` tell Bob how to read the content.
- `sorry` means the agent that sends it understood the question but cannot give a response (External Interfaces Working Group, 1993). Bob knows the term `next-delivery` from the shared ontology, but he controls stock levels, not deliveries, so he has no date to give.

## What I noticed

Even this short exchange depends on a lot of agreement made in advance. Alice and Bob must share the performatives, the content language and every ontology term. The ontology also has to settle questions that look obvious, for example whether "available" stock includes televisions already reserved for other orders. If the two agents read that term differently, Bob's answer is correct for him and wrong for Alice, and nothing in the message would show it. Labrou, Finin and Peng (1999) describe semantics as the main unresolved issue for agent communication languages, and this small example shows why.

It also made me compare with my research agent. There the orchestrator calls each agent through an ordinary Python method, and the nearest thing to an agreed content language is the JSON schema that every model reply is checked against. Writing this dialogue showed me what the schema does not cover. It fixes the shape of an answer, but not what its words mean, which is the job of an ontology.

## AI acknowledgement

Generative AI (Claude) helped me draft and edit this page. The full statement is on the [home page](index.html#ai-acknowledgement).

## References

External Interfaces Working Group (1993) *Specification of the KQML agent-communication language plus example agent policies and architectures*. Draft, 15 June. DARPA Knowledge Sharing Initiative. Available at: https://research.cs.umbc.edu/kqml/papers/kqmlspec.pdf (Accessed: 12 October 2026).

Finin, T., Fritzson, R., McKay, D. and McEntire, R. (1994) 'KQML as an agent communication language', *Proceedings of the Third International Conference on Information and Knowledge Management (CIKM '94)*. New York: ACM, pp. 456–463. Available at: https://doi.org/10.1145/191246.191322

Genesereth, M.R. and Fikes, R.E. (1992) *Knowledge Interchange Format, version 3.0 reference manual*. Technical Report Logic-92-1. Stanford, CA: Computer Science Department, Stanford University.

Labrou, Y., Finin, T. and Peng, Y. (1999) 'Agent communication languages: the current landscape', *IEEE Intelligent Systems*, 14(2), pp. 45–52. Available at: https://doi.org/10.1109/5254.757631
