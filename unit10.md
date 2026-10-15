---
layout: default
title: Unit 10 activity
---

[Home](index.html)

# Unit 10 – Deep Learning in Action

Activity: research an application of deep learning that will have an impact on society, and make a post on the discussion forum that covers what the technology does, how it works, and its ethical, privacy, social and other socio-technical impacts. This is the post.

## Deep learning for weather forecasting: GraphCast

### What it does

GraphCast is a weather forecasting model from Google DeepMind. It takes the current state of the global atmosphere and predicts the next ten days, at a resolution of 0.25 degrees, in under one minute on a single TPU chip (Lam et al., 2023). In the published evaluation it was more accurate than the leading conventional forecast system on 90% of 1,380 test targets, and its forecasts gave earlier warning of severe events such as tropical cyclone tracks and extreme temperatures (Lam et al., 2023).

I chose this example because forecasts are not an abstract product. In logistics, a forecast decides whether a shipment leaves today or tomorrow, which route a vessel takes, and how much stock a warehouse holds before a storm. If forecasts become cheaper and better, those decisions change for everyone who depends on them.

### How it works

A conventional forecast works by solving the physical equations of the atmosphere step by step on a supercomputer. GraphCast does not solve any equations. It was trained on 39 years of historical weather data, the ERA5 reanalysis from 1979 to 2017, and it learned the statistical relationship between the weather now and the weather six hours later (Lam et al., 2023).

The model is a graph neural network. The globe is represented as a mesh of points, built by dividing an icosahedron six times, so that nearby points on the earth are connected (Lam et al., 2023). The network has three parts. An encoder maps the weather grid onto the mesh, a processor passes information between mesh points sixteen times, and a decoder maps the result back onto the grid. The model takes the two most recent weather states as input and produces the state six hours ahead. To forecast ten days, it feeds its own output back in, forty times in a row. Training took about three weeks on 32 TPU chips (Lam et al., 2023). Once trained, running it costs almost nothing compared with a conventional system, which runs on a cluster of thousands of cores for about an hour per forecast.

### Impacts

**Social good.** The clearest benefit is access. A forecast that needs a supercomputer belongs to a few national centres. A forecast that runs on one chip in a minute can be run by a university, a company or a smaller national weather service. Better warnings for cyclones and heatwaves save lives, and many of the places most exposed to them do not have a supercomputer of their own.

**Dependence and ownership.** The model learned from ERA5, which is itself produced by the conventional system it now competes with. It also needs an analysis of the current weather as its starting point, and that comes from the same centres. So the new models do not replace the old infrastructure. They sit on top of it (Ben Bouallègue et al., 2024). If funding for the physical models falls because the learned ones look cheaper, the training data for the next generation of learned models disappears too.

**Safety and trust.** The published evaluations found that the learned forecasts become too smooth at longer lead times and do poorly on the intensity of tropical cyclones (Ben Bouallègue et al., 2024). A smooth forecast looks confident and misses the extremes, which are the cases that matter most. The model was trained on the past. A climate that drifts away from the training period is a risk that nobody can measure yet. In the same way as the language model in my research agent, the network gives an answer with no sign of how far it is from anything it has seen before, so the people who use it need to know where it is weak.

**Who is accountable.** When a physical model gets a storm wrong, meteorologists can trace the error to an equation or an input. A learned model offers no such explanation. If a port closes, or does not close, on the strength of a forecast that no one can inspect, the question of responsibility is open. I think the answer is the same as for the agent I built this term: keep the conventional system running alongside, compare them, and keep a person in the decision for anything that is expensive to get wrong.

### AI acknowledgement

This declaration applies to the whole Intelligent Agents e-portfolio, including this page and all artefact pages it links to. I used generative AI tools (Grammarly and Claude) to proofread, improve wording and help with formatting. The analysis, interpretation, conclusions and recommendations throughout are my own.
### References

Ben Bouallègue, Z. et al. (2024) 'The rise of data-driven weather forecasting: a first statistical assessment of machine learning–based weather forecasts in an operational-like context', *Bulletin of the American Meteorological Society*, 105(6), pp. E864–E883. Available at: https://doi.org/10.1175/BAMS-D-23-0162.1

Lam, R. et al. (2023) 'Learning skillful medium-range global weather forecasting', *Science*, 382(6677), pp. 1416–1421. Available at: https://doi.org/10.1126/science.adi2336
