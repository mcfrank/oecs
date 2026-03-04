---
title: Levels of Analysis
slug: ztivn7hx
date: '2025-12-16'
doi: 10.21428/e2759450.f61797a0
authors:
- Richard P. Cooper
- David Peebles
section_editors:
- Michael C. Frank
---

Complex information-processing systems can be understood or analyzed in terms of their function (what the system does and why), the processes and operations that achieve that function (how it does it), or the physical hardware that performs those processes and operations (how those processes and operations are implemented). These different perspectives are considered to be distinct levels of analysis and can be applied to the mind/brain or their subsystems. For example, choosing which breakfast cereal to buy can be understood from an abstract information-processing perspective as selecting from a set of options subject to perceived costs and benefits. The same choice can also be described in terms of processes that generate and evaluate options to produce a decision. In turn, those processes can be described in terms of the patterns of activity within neural circuits that transform sensory input into a specific response. Although all three perspectives capture the target phenomenon (in this case, choosing a cereal), they do so using distinct units of analysis and characteristic “languages”: at the functional level, abstract mathematical descriptions of goals and constraints; at the process and operational level, descriptions of information-processing operations and representational formats; and at the physical hardware level, descriptions couched in terms of neural and other physical mechanisms. This multilevel approach is useful because different levels are appropriate for answering different types of questions and because analyses at individual levels can often proceed, at least initially, without a fully worked-out account at the other levels.

# **History**

That systems may be understood at different levels has long been accepted in the sciences. A chemical reaction, for example, can be understood both at the level of chemistry and the level of subatomic physics. However, Marr and Poggio (1976) were amongst the first to argue that neural systems might be analyzed at multiple levels and that doing so was vital to fully understanding them. David Marr (1982) refined this idea during his investigation of the function of vision and the algorithms that might transform retinal input into a mental representation of a scene. Crucially, Marr generalized the approach beyond human vision to apply to any information-processing system. He further argued that it was impossible to understand processing at the neural level without knowing both what the system was achieving and how it was achieving it. Marr’s proposal was a direct counter to contemporary, purely bottom-up, neural attempts to understand visual processing.

Although Marr’s account is the most well known, other level-based accounts of analysis have also been influential. Drawing analogies from computer science, Allen Newell (1982, 1990) proposed a unified framework with several tightly integrated levels distinguished by their timescale, functional role, and mode of operation. Another account is John Anderson's (1990) rational analysis, which begins by identifying the cognitive system’s goals and the structure of its environment to explain why cognition takes the form it does [see [Rational Analysis](/articles/lurik5dk)]. In doing so, rational analysis seeks to show how cognitive behavior can be understood as an optimal response to environmental demands under resource constraints.

# **Core concepts**

The standard approach to analyzing complex information-processing systems involves three levels (Marr, 1982). Level one, the *computational theory* level, is the most abstract and specifies the system’s goal or function—what is being computed and why. Level two, the *algorithmic and representational* level, specifies how the level one function is achieved in terms of the representations employed and the algorithm that operates over those representations. Level three, the *implementational* level, specifies how level two algorithms are implemented in physical hardware such as neurons and brain tissue.

A critical element of this approach is *multiple realizability*: a theory at a more abstract level can be realized in more than one way at the level immediately below [see [Multiple Realizability](/articles/c1pqmxoq)]. For example, the same level-one function—*choosing the option with the highest expected value*—could be achieved by different level-two algorithms, such as (1) explicitly computing and comparing expected values, (2) using a simple heuristic (e.g., “pick the option with the best payoff on the most likely outcome”), or (3) approximating the computation by sampling a few possible outcomes and averaging them. Likewise, any one of these algorithms could be implemented in multiple physical ways (e.g., in circuits made of neurons or silicon).

# **Questions, controversies, and new developments**

The relationship between each of Marr’s levels remains an active area of investigation, and bridging them has become a central goal within cognitive science. Attempts have proceeded from two directions. One *top-down* approach starts from normative principles—theories about what an ideal system should do given the information available [see [Bayesian Models of Cognition](/articles/lwxmte1p)]. It then asks how people might approximate that ideal when time, memory, and attention are limited (Lieder & Griffiths, 2020), for example, by relying on simple stochastic procedures that sample a few possible outcomes rather than performing exhaustive calculations (Griffiths et al., 2024).

In the opposite direction, *bottom-up* approaches begin with biologically plausible neural mechanisms to build upward toward cognitive and computational functions. This approach is exemplified by the *Spaun* cognitive architecture that implements basic cognitive functions using spiking neurons (neurons that communicate via binary, all-or-nothing signals) and is capable of a diverse range of cognitive tasks (Eliasmith, 2013).

A second question concerns how closely levels must align: Should a level-two algorithm reproduce the level-one function exactly, or—consistent with the distinction between competence and performance (Chomsky, 1965)—do resource limits and performance considerations mean that algorithms only approximate the ideal competence function (e.g., by imposing real-time constraints on processing)? Analogous considerations apply to the relation between algorithms and their neural implementation, with physical constraints (e.g., on the precision of representations) limiting the neural implementation.

Strict distinctions between levels of analysis have been criticized by mechanistic philosophers of science for not taking a sufficient account of the integrated nature of explanation in neuroscience [see [Mechanistic Explanation](/articles/vgigt1aq)]. Mechanists regard levels not as independent layers of explanation but as different kinds of abstractions providing useful simplifying descriptions within a single, integrated mechanistic model (Boone & Piccinini, 2016; Craver, 2007). Mechanists advocate explanations that reveal how organized parts and processes give rise to cognitive functions simultaneously across multiple levels (Kaplan & Craver, 2011; Piccinini & Craver, 2011), with levels being seen as interacting dimensions of a framework for constructing integrated, multilevel models of cognitive systems (Bechtel & Shagrir, 2015; Shagrir, 2010).

# **Broader connections**

Although bridging levels offers valuable insights, it also makes clear why intermediate, algorithmic-level descriptions are indispensable. The links between abstract goals and neural implementations are rarely transparent or one-to-one. At the computational level, specifying what is being achieved (and why) typically underdetermines how it is achieved, as many different representations and procedures could realize the same function. Conversely, neural descriptions of where and when activity occurs cannot be interpreted at the computational level without a theory of what information is being represented and how it is being manipulated. As a result, algorithmic-level accounts provide a critical common conceptual framework for integration with a set of concrete representations, operations, and processing constraints that can simultaneously be (1) shaped by—and evaluated against—higher-level functional principles and (2) mapped onto candidate biological mechanisms. The ACT-R cognitive architecture (Anderson, 2007) exemplifies this function in its concrete specification of cognitive operations, memory structures, and processing constraints and its linking of detailed algorithmic accounts with goal-level rational analyses above (e.g., Anderson & Schooler, 1991) and biological mechanisms below (e.g., Borst & Anderson, 2024).

Multilevel analysis is an active topic in the context of modern machine learning, especially deep learning. For instance, Marr’s levels have been employed to analyze deep reinforcement learning agents and convolutional neural networks (Hamrick & Mohamed, 2020). At the computational level, the system is characterized in terms of its task or objective function (e.g., maximizing cumulative reward); at the algorithmic and representational level, the network architecture and learning procedure is specified (e.g., temporal difference learning with a particular convolutional architecture); and at the implementation level, the concrete realization in software and hardware is considered (e.g., graphics processing units [GPUs], neuromorphic devices, and distributed training configurations). Similar Marr-inspired frameworks have been proposed for neuromorphic computing hardware (Guo et al., 2021) and for updating Marr’s hierarchy for contemporary neural network models (Collins & Shenhav, 2022; Poggio, 2012). This suggests that rather than being made obsolete by contemporary developments in cognitive science, levels of analysis continue to provide a useful way of organizing explanations of both biological and artificial information-processing systems.

# **Further reading **

- Colombo, M., & Knauff, M. (2020). Editors’ review and introduction: Levels of explanation in cognitive science: From molecules to culture. *Topics in Cognitive Science*, *12*(4), 1224-1240. [https://doi.org/10.1111/tops.12503](https://doi.org/10.1111/tops.12503)
- Griffiths, T. L., Chater, N., Kemp, C., Perfors, A., & Tenenbaum, J. B. (2010). Probabilistic models of cognition: Exploring representations and inductive biases. *Trends in Cognitive Sciences*, *14*(8), 357-364. [https://doi.org/10.1016/j.tics.2010.05.004](https://doi.org/10.1016/j.tics.2010.05.004)
- McClelland, J. L., Botvinick, M. M., Noelle, D. C., Plaut, D. C., Rogers, T. T., Seidenberg, M. S., & Smith, L. B. (2010). Letting structure emerge: Connectionist and dynamical systems approaches to cognition. *Trends in Cognitive Sciences*, *14*(8), 348-356. [https://doi.org/10.1016/j.tics.2010.06.002](https://doi.org/10.1016/j.tics.2010.06.002)
- Peebles, D., & Cooper, R. P. (2015). Thirty years after Marr’s vision: Levels of analysis in cognitive science. *Topics in Cognitive Science*, *7*(2), 187-190. [https://doi.org/10.1111/tops.12137](https://doi.org/10.1111/tops.12137)

# References

Marr, D., & Poggio, T. (1976). From understanding computation to understanding neural circuitry. AI Memo 357. Massachusetts Institute of Technology Artificial Intelligence Laboratory.

Marr, D. (1982). *Vision: A computational investigation into the human representation and processing of visual information*. MIT Press.

Newell, A. (1982). The knowledge level. *Artificial Intelligence*, *18*(1), 87-127. <https://doi.org/10.1016/0004-3702(82)90012-1>

Newell, A. (1990). *Unified theories of cognition*. Harvard University Press.

Anderson, J. R. (1990). *The adaptive character of thought.* Psychology Press.

Marr, D. (1982). *Vision: A computational investigation into the human representation and processing of visual information*. MIT Press.

Lieder, F., & Griffiths, T. L. (2020) Resource-rational analysis: Understanding human cognition as the optimal use of limited computational resources. *Behavioral and Brain Sciences*, *43*, e1. <https://doi.org/10.1017/S0140525X1900061X>

Grifﬁths, T. L., Vul, E., Sanborn, A. N., & Chater, N. (2024) Sampling as a bridge across levels of analysis. In T. L. Griffiths, N. Chater, & J. B. Tenenbaum (Eds.), *Bayesian models of cognition: Reverse engineering the mind* (pp. 285-297). MIT Press.

Eliasmith, C. (2013). *How to build a brain: A neural architecture for biological cognition.* Oxford University Press.

Chomsky, N. (1965). *Aspects of the theory of syntax*. MIT Press.

Boone, W., & Piccinini, G. (2016). Mechanistic abstraction. *Philosophy of Science*, *83*(5), 686–697. <https://doi.org/10.1086/687855>

Craver, C. F. (2007). *Explaining the brain: Mechanisms and the mosaic unity of neuroscience*. Oxford University Press.

Kaplan, D. M., & Craver, C. F. (2011). The explanatory force of dynamical and mathematical models in neuroscience: A mechanistic perspective. *Philosophy of Science*, *78*(4), 601-627. <https://doi.org/10.1086/661755>

Piccinini, G., & Craver, C. F. (2011). Integrating psychology and neuroscience: Functional analyses as mechanism sketches. *Synthese*, 183(3), 283-311. <https://doi.org/10.1007/s11229-011-9898-4>

Bechtel, W., & Shagrir, O. (2015). The non‐redundant contributions of Marr’s three levels of analysis for explaining information‐processing mechanisms. *Topics in Cognitive Science*, *7*(2), 312–322. <https://doi.org/10.1111/tops.12141>

Shagrir, O. (2010). Marr on computational‐level theories. *Philosophy of Science*, *77*(4), 477–500. <https://doi.org/10.1086/656005>

Anderson, J. R. (2007). *How can the human mind occur in the physical universe?* Oxford University Press.

Anderson, J. R., & Schooler, L. J. (1991). Reflections of the environment in memory. *Psychological Science*, *2*(6), 396-408.<https://doi.org/10.1111/j.1467-9280.1991.tb00174.x>

Borst, J. P., & Anderson, J. R. (2024). Discovering cognitive stages in M/EEG data to inform cognitive models. In B. U. Forstmann & B. M. Turner (Eds.), *An introduction to model-based cognitive neuroscience* (2nd ed., pp. 101-117). Springer, Cham. <https://doi.org/10.1007/978-3-031-45271-0_5>

Hamrick, J., & Mohamed, S. (2020). Levels of analysis for machine learning. *arXiv*. <https://doi.org/10.48550/arXiv.2004.05107>

Guo, Y., Zou, X., Hu, Y., Yang, Y., Wang, X., He, Y., Kong, R., Guo, Y., Li, G., Zhang, W., Wu, S., & Li, H. (2021). A Marr’s three‐level analytical framework for neuromorphic electronic systems. *Advanced Intelligent Systems*, *3*(11), 2100054. <https://doi.org/10.1002/aisy.202100054>

Collins, A. G. E., & Shenhav, A. (2022). Advances in modeling learning and decision-making in neuroscience. *Neuropsychopharmacology*, *47*, 104–118. <https://doi.org/10.1038/s41386-021-01126-y>

Poggio, T. (2012). The Levels of Understanding framework, revised. *Perception*, *41*(9), 1017-1023. <https://doi.org/10.1068/p7299>