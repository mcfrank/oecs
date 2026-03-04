---
title: Scene Perception
slug: mhjvjq8o
date: '2026-01-24'
authors:
- Melissa Lê-Hoa Võ
section_editors:
- Timothy F. Brady
---

As soon as you open your eyes, you perform something that is referred to as *scene perception*, a cognitive process by which the brain interprets and understands its visual environment. It involves recognizing, organizing, and extracting meaningful information from complex scenes, enabling humans to identify objects, their relationships, spatial layout, and relevant features within a given environment. This cognitive process is key to navigating and interacting effectively with our surroundings. A hallmark of scene perception is that it takes only a brief glimpse to extract rich meaning from complex visual input (see Figure 1). The remarkable speed and ease with which we process scenes is the product of swiftly integrating bottom-up visual information with top-down scene knowledge. It is this fascinating cognitive feat that will be covered here.

![]()

# History

While formal research on "scene perception" as a defined concept emerged in the 20th century, earlier philosophical and observational writings already touched on related ideas about visual perception and the human ability to interpret environments. Helmholtz's theory of unconscious inference (1876), for instance, suggests that perception is an active process where the brain makes implicit assumptions or inferences to interpret sensory information, particularly in complex or ambiguous scenes. This idea posits that our perception of scenes is not a direct reflection of the sensory input but results from the brain's unconscious guessing and hypothesis testing based on prior knowledge and context. In the early 1910s, Max Wertheimer and his colleagues Wolfgang Köhler and Kurt Koffka famously founded the Gestalt School ("Gestaltschule") in Germany, which significantly contributed to understanding perceptual organization and gestalt principles (e.g. that “the whole is perceived as more than just the sum of its parts”). But it wasn’t until the 1970s and 80s that researchers like David Marr, Molly Potter and Irv Biederman significantly shaped the way how research is done on scene perception to this day. Their seminal works provided some core insights on scene perception, for example that visual perception involves transforming retinal input into a series of increasingly abstract, computational representations that enable scene understanding (Marr, 1982, see also Groen et al., 2022); that the briefest of glances of a complex scene is enough to process its meaning (Potter, 1975, see also Greene, 2009); and that *scene semantics* and *syntax* play a key role in the processing of objects therein (Biederman, 1976, see also Võ, 2021).

# Core concepts

## The Scene Grammar Framework

The Scene Grammar Framework (see Fig. 2, Võ et al., 2019; Võ, 2021) proposes that objects within scenes are hierarchically organised and constrained by a *scene grammar* - internalized rules that predict what objects tend to be where within a scene, how objects are positioned relative to one another and how they relate to the global scene context. Within a scene, so-called *anchor objects* (e.g., the shower or bathtub) guide the placement, identification, and use of associated objects (e.g., the shampoo inside the shower, the towels next to it), forming meaningful and functionally optimized clusters or *phrases*. This highly structured composition of objects in scenes helps the brain efficiently process complex visual environments, boosting efficient object recognition and search as well as scene understanding, all of which enable us to efficiently adapt and function in a diverse range of settings (Biederman, 1977; Draschkow & Võ, 2017; Henderson & Ferreira, 2004; Võ & Henderson, 2009; Võ & Wolfe, 2013).

![]()

## What guides attention in real-world scenes?

A red poppy along a lush green hiking path might grab your attention, or a ball that your kid is launching your way. The view that attentional guidance by low-level features like color contrast or movements was prominently featured in Itti and Koch’s saliency model (2001), but later accounts favoured a greater role for top-down guidance of attention. Keeping visual saliency controlled, Võ and Henderson (2009) for instance showed that objects violating scene grammar (e.g. a fire hydrant in a kitchen) keep attracting eye movements once fixated (it has been debated whether semantic or syntactic violations actually attract attention parafoveally (i.e. from the corner of your eye) or not, see Henderson & Võ, 2009). Using *meaning maps* Henderson and Hayes (2017) later demonstrated that meaning plays the dominant role in guiding attention through scenes. And more recently, deep neural networks like DeepGaze III (Kümmerer, Bethge, & Wallis, 2022) - which combines image information with the history of previous fixations – have been shown to predict where observers might look next while freely viewing a scene. Most of the time, however, we do not just passively view scenes, but instead search for objects and interact with them for the purpose of goal-directed actions. Try searching for the shampoo in Figure 3.

![]()

Most likely, scene grammar allowed you to ignore the left 2/3 of the scene (i.e. the toilet and sink phrases) and to limit your search to the shower phrase, likely to contain the target. And before deciding that the detergent is absent from this scene, you would likely open the cupboard and find it inside.

# Questions, controversies, and new developments

As in many other disciplines, the rise of deep neural networks (DNNs) has opened up new possibilities for answering long-standing questions. A particular type of DNN - so-called Generative Adversarial Networks or GANs (Goodfellow et al., 2014) - for instance, are becoming increasingly good at “hallucinating” images of scenes that do not actually exist. What exactly is the scene grammar that GANs have learned? Lesioning GANs could serve as a useful testbed to investigate what actually makes a scene.

Lately the classic notion of object affordances à la Gibson has been reintroduced to scene perception [see [Affordances](/articles/984ungzu)]. How do functions affect scene categorization (Greene et al., 2016) and which parts of a scene drive function understanding (Müller Karoza et al., 2025)? Making use of more interactable 3D virtual environments will likely provide new answers to some old questions.

While often merely used as an analogy, processing objects in scenes and words in sentences might actually share common, domain-general cognitive mechanisms. Do, for example, children with developmental language delay (DLD) also show impediments in the processing of pictorial information (Bahn et al., 2025; Lindfors et al., 2025)? Investigating the commonalities and differences between scene perception and language processing has the potential to improve the understanding of both of these core cognitive abilities (for some initial thoughts on this matter see also Henderson & Ferreira, 2004)

# Broader connections

The study of scene perception is inherently interdisciplinary. As briefly outlined above, knowing a scene’s grammar will strongly affect [Visual Search](about:blank) in naturalistic environments providing a highly efficient, top-down guidance of [Attention](about:blank) that allows detecting objects in scenes even if they are occluded or even hidden from view. Also, people interested in memory have been intrigued by what features of a scene make it more or less memorable has recently gained more traction in AI where deep Convolutional Neural Networks (CNNs) are trained on large datasets to predict memorability scores for new images (for a review see Rust & Mehrpour, 2020).

# Acknowledgments

“This work was supported by the Deutsche Forschungsgemeinschaft (German Research Foundation, DFG) under Germany’s Excellence Strategy (EXC 3066/1 “The Adaptive Mind”, Project No. 533717223) as well as by the DFG Research Unit FOR 5368.”

# Further reading

- Bartnik, C. G. & Groen, I. I. A. (2023). Visual perception in the human brain: How the brain perceives and understands real-world scenes. In *Oxford Research Encyclopedia of Neuroscience.*
- Hansen, B.C., Greene, M.R., Lewinsohn, H.A.S., Kris, A.E., Smyth, S., & Tang, B. (2025). [Brain-Guided Convolutional Neural Networks Reveal Task-Specific Representations in Scene Processing](https://www.biorxiv.org/content/10.1101/2025.01.02.631092v3.full.pdf). [Biorxiv](about:blank)

# References

Bahn, D., Deniz Türk, D., Tsenkova, N., Schwarzer, G., Võ, M. L.-H., & Kauschke, C. (2025). Processing of Scene-Grammar Inconsistencies in Children with Developmental Language Disorder—Insights from Implicit and Explicit Measures. Brain Sciences, 15(2), 139. [http://doi.org/10.3390/brainsci15020139](https://doi.org/10.3390/brainsci15020139)

Biederman. I. (1976). On processing information from a glance at a scene: some implications for a syntax and semantics of visual processing. UODICS’76. 75–88. [https://doi](https://doi).org/10.1145/1024273.1024283.

Goodfellow, I. et al. Generative Adversarial Nets. In Advances in Neural Information Processing Systems (eds. Ghahramani, Z., Welling, M., Cortes, C., Lawrence, N. & Weinberger, K. Q.) vol. 27, (Curran Associates, Inc., 2014).

Greene, M. R., & Oliva, A. (2009). The briefest of glances: the time course of natural scene understanding. *Psychological Science, 20*(4), 464–472.

Greene, M. R., Baldassano, C., Esteva, A., Beck, D. M. & Fei-Fei, L. (2016) Visual scenes are categorized by function. *J. Exp. Psychol. Gen.* **1**, 82–94. [https://doi](https://doi).org/10.1037/xge0000129.

Groen, I. I. A., Dekker T. A, Knapen, T., & Silson, E. H. (2022) Visuospatial coding as ubiquitous scaffolding for human cognition. *Trends in Cognitive Sciences,* *26*(1), 81-96

Helmholtz, H. von (1867). *Handbuch der Physiologischen Optik*. (translated as *Treatise on Physiological Optics* in 1920-1925, available [here](https://web.archive.org/web/20180320133752/http:/poseidon.sunyopt.edu/BackusLab/Helmholtz/)).

Henderson, J. M., & Ferreira, F. (Eds.) (2004). The interface of language, vision, and action: Eye movements and the visual world. New York: Psychology Press.

Henderson, J. M., & Hayes, T. R. (2017). Meaning-based guidance of attention in scenes as revealed by meaning maps. *Nature Human Behaviour*, 1, 743-747.

Kallmayer, A., & Võ, M. L.-H. (2024). Anchor objects drive realism while diagnostic objects drive categorization in GAN generated scenes.* Communications Psychology, 2*(1), 68. [https://doi.org/10.1038/s44271-024-00119-z](https://www.nature.com/articles/s44271-024-00119-z)

Lindfors, H., Hansson, K., Cohn, N., & Andersson, A. (2025). [Similarities in semantic processing across verbal and pictorial domains in school children with developmental language disorder.](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2025.1548289/full) *Frontiers in Psychology*, 16. [https://doi.org/10.3389/fpsyg.2025.1548289](https://doi.org/10.3389/fpsyg.2025.1548289)

Marr, D. (1982). *Vision: A Computational Investigation into the Human Representation and Processing of Visual Information*. New York: W. H. Freeman and Company.

Potter, M. C. (1975). Meaning in visual search. *Science*, *187*(4180), 965–966

Rust, N. C. & Mehrpour, V. (2020). Understanding Image Memorability, *Trends in Cognitive Sciences,* *24*(7), 557-568.

Võ, M. L.-H. (2021). The Meaning and Structure of Scenes.* Vision Research, 181*, 10-20. [https://doi.org/10.1016/j.visres.2020.11.003](https://doi.org/10.1016/j.visres.2020.11.003)

Võ, M. L.-H., & Henderson, J. M. (2009). Does gravity matter? Effects of semantic and syntactic inconsistencies on the allocation of attention during scene perception. *Journal of Vision, 9*(3), 24. [https://doi.org/10.1167/9.3.24](https://doi.org/10.1167/9.3.24)

Wiesmann, S. L., & Võ, M. L.-H. (in press). Flexible Usage of Object and Global Scene Information During Human Scene Categorization. *Journal of Experimental Psychology: Human Perception and Performance*.