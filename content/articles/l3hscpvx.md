---
title: Motor Learning
slug: l3hscpvx
date: '2025-12-04'
doi: 10.21428/e2759450.0b8879c0
authors:
- Jonathan Tsay
section_editors:
- Michael C. Frank
---

Humans possess a remarkable ability to acquire, adapt, and retain movements—a capacity known as *motor learning* (literally “learning to move,” from the Latin *movere*, “to move”). Through motor learning, we continuously compare expected movement outcomes with actual movement outcomes, using errors, rewards, cognitive strategies, and repeated practice to refine performance as the body (e.g., muscle fatigue), environment (e.g., uneven terrain), and goals (e.g., performing a wheelie or winning a race) dynamically evolve. Motor learning engages multiple learning processes, each supported by specialized brain networks and tuned to distinct forms of feedback and contextual factors. Situated at the intersection of multiple disciplines, motor learning research has uncovered fundamental principles of learning and memory while catalyzing transformative advances in neurorehabilitation and neurotechnology.

# **History **

From a baby’s first steps to a pianist’s flawless recital, humans exhibit an extraordinary ability for motor learning—the ability to acquire, adapt, and retain skilled movement. Motor learning may be one of the nervous system’s most fundamental functions. Consider the sea squirt: after a brief period of movement to find a home, it anchors to a surface and digests its own nervous system. From this observation, evolutionary biologists have suggested that the ability to move, and to learn from movement, may be the very reason nervous systems evolved in the first place.

Understanding motor learning has long fascinated scientists across fields. Its scientific roots trace back to the early days of experimental psychology. In 1896, George Stratton conducted a classic self-experiment, wearing mirror-inverting glasses for eight days (Stratton, 1896). Stratton describes how, at first, “all images . . . appeared to be inverted; the room and all in it seemed upside down,” and his movements were “awkward, uncertain, and full of surprises.” Yet, through repeated trial and error, he gradually regained coordination: “The mistake was then seen . . . and the desired movement was at last brought about.” This landmark study offered an early glimpse into the brain’s ability to rapidly recalibrate movement in response to feedback and practice.

The cognitive revolution marked a breakthrough in motor learning, sparked by Brenda Milner’s seminal work with patient H.M. After surgeons removed both medial temporal lobes, including the hippocampus, to treat his severe epilepsy, H.M. was left unable to form new long-term memories (Milner, 1962). Yet, in a mirror-tracing task, in which H.M. was asked to trace a star as quickly as possible while viewing his hand only through a mirror, he showed normal learning, with steady improvements in both speed and accuracy over three days, despite having no memory of ever performing the task before. This striking dissociation revealed that motor learning constitutes a distinct form of memory—separate from episodic memory for past events or semantic memory for words and concepts—one that can operate implicitly, without conscious awareness [see [Memory](/articles/s41l0yu6)].

These foundational studies paved the way for the cognitive neuroscience era, which sought to uncover the neural and computational principles supporting motor learning. The motor system came to be modeled as a *controller*—similar to a thermostat that adjusts its output based on the mismatch between the desired and actual temperature. In this *control-theoretic framework*, motor learning arises from comparisons between the predicted movement outcome (e.g., reaching for a cup of milk) and the actual movement outcome (e.g., spilling milk all over the floor). Errors in turn drive corrective adjustments that keep the motor system calibrated amid changes in the body or environment (Shadmehr et al., 2010).

# **Core concepts**

Consider the challenge of learning to ride a bike. Staying upright requires the brain to estimate the body’s current state—how fast you’re moving, how far you’re leaning—by integrating sensory inputs such as vision and proprioception. Based on this *state estimate*, the system generates motor commands to steer, balance, and pedal. However, sensory feedback alone is way too slow to support fast, seamless control. Imagine riding a bike over uneven terrain but only being able to adjust your balance 50 ms after hitting a rock (the typical delay in proprioception) or 100 ms later (the typical delay in vision). By the time you feel the wobble, you’ve already fallen!

To overcome sensory delays, the motor system relies on forward and inverse models working in concert. The *forward model* uses an* efference copy*—an internal duplicate of the motor command—to predict the sensory consequences of movement, whereas the *inverse model* translates desired sensory outcomes into the motor commands needed to achieve them. For example, when you turn the handlebars on uneven ground, your brain predicts how your balance will shift (forward model) and instantly generates the corrective motor commands to stabilize your posture (inverse model)—all before any sensory feedback reaches the brain.

Yet, these forward and inverse models, collectively known as *internal models*, are not always perfectly calibrated. Motor learning occurs when predicted and actual movement outcomes diverge, generating a *sensory prediction error* that recalibrates these internal models. Consequently, the next time a cyclist encounters similar uneven terrain, they draw on these refined models to anticipate and correct their movements more effectively.

Internal models are rapidly established in childhood (Hill et al., 2025). Because these models are still developing, children often appear clumsy, making countless motor errors as they gradually learn the sensory consequences of their actions and how to interact effectively with the world around them. This process also continues throughout the lifespan—whether in athletes refining their swing or musicians mastering a difficult passage—each repetition fine-tuning the brain’s internal models to achieve smoother, more precise, and more predictive motor control.

Motor learning engages almost the entire brain—a complex network in which each component of the control loop crudely maps onto distinct neural substrates (Figure 1; Shadmehr & Krakauer, 2008). Goals are encoded in the prefrontal and parietal cortices. The cerebellum generates sensory predictions through a forward model and translates desired sensory outcomes into motor commands via an inverse model. Peripheral sensors in the muscles, joints, and eyes send signals to sensory cortices, allowing the brain to estimate the body’s current state. The basal ganglia maintain an internal model that predicts a movement’s utility—balancing costs (e.g., effort) against benefits (e.g., reward)—and use reward prediction errors, arising when actual and expected utility diverge, to keep this model calibrated. The primary motor cortex issues the motor command to activate muscles downstream. Altogether, this distributed organization highlights that motor learning is not localized to a single brain region but emerges from the integration of neural systems supporting perception, decision-making, and action.

![](images/articles/l3hscpvx/figure_1.png)

**Figure 1.** The motor system uses a motor goal (e.g., drinking) to generate a motor command (e.g., reaching toward a cup). A forward model in the cerebellum predicts the sensory consequences of this command (e.g., feeling the fingers contact the cup handle) while an inverse model rapidly computes the next movement in the sequence (e.g., bringing the cup to one’s mouth)—well before sensory feedback arrives from the muscles, joints, and eyes. When the delayed sensory outcome becomes available, it is compared with the predicted outcome to compute a sensory prediction error, updating the cerebellar internal models. In parallel, the basal ganglia compute reward prediction errors—the mismatch between expected utility (e.g., the anticipated pleasure of drinking) and actual utility (e.g., whether the beverage tastes good or bad)—allowing its internal model to remain calibrated. This control theoretic framework continues to evolve, with modern formulations incorporating multiple, interacting control loops that operate across different timescales, feedback modalities, and behavioral contexts.

# **Questions, controversies, and new developments**

Motor learning is supported by multiple interacting systems that can be distinguished along several dimensions. One key distinction lies in their temporal dynamics; fast processes respond rapidly to sensory prediction errors but decay quickly, whereas slow processes adapt more gradually and retain their effects over extended timescales (Hadjiosif et al., 2023; Smith et al., 2006). Different systems also differ in the types of feedback they use. E*rror-based learning* relies on sensory prediction errors (Tseng et al., 2007). In contrast, *reward-based motor learning* is driven by *reward prediction errors*—the discrepancy between expected and actual rewards (Nikooyan & Ahmed, 2015; Therrien et al., 2016) [see [Reinforcement Learning](/articles/k2ek981x)]. *Strategy-based learning* depends on explicit instructions, such as verbal cues (“aim farther to the right”) or imagery-based strategies (“imagine your body as a stable tripod”), prompting deliberate, reasoning-based adjustments rather than purely sensory-driven ones (Taylor et al., 2014). Finally, some forms of motor learning arise with minimal feedback, emerging through repetition alone to enhance movement accuracy* *(use-dependent learning;* *Verstynen & Sabes, 2011)* *and/or movement precision* (motor acuity*;* *Shmuelof et al., 2012).

A central challenge is understanding whether these learning systems operate independently (Taylor et al., 2014), compete for shared resources (Albert et al., 2022), or interact in complementary ways (Miyamoto et al., 2020). These processes are now being examined with increasing granularity, revealing that each comprises multiple subprocesses that differ in their degree of conscious awareness, the speed with which they respond to feedback, the computational resources they require, and the neural substrates they engage. Understanding these interactions is crucial for explaining how the brain flexibly combines distinct learning mechanisms to support adaptive, efficient motor behavior.

Motor learning is undergoing a cognitive revolution, highlighting the often-overlooked influence of higher-order decision-making, attentional, memory, and motivational processes that shape how we learn to move (Song, 2019; Vassiliadis et al., 2021). Recent work has moved beyond examining how people execute movements to explore how they decide when to move, stop, or change course (Wadsley & Greenhouse, 2024). As researchers increasingly recognize the limitations of the traditional control theoretic framework, which fails to accurately capture the richness and diversity of individual motor learning strategies, the field is borrowing computational approaches grounded in cognitive science that enable a deeper understanding of how people plan, select, and optimize complex, ecological movements (Tsay et al., 2024).

Motor learning does not occur in a vacuum—context matters (Heald et al., 2023). Growing evidence shows that factors such as the spatial arrangement of movement targets, the timing and structure of feedback during practice, and the overall demands of the learning environment all shape how we acquire and refine motor skills (Ogasa et al., 2024). Understanding how context modulates these processes is crucial for predicting when learning will generalize to new situations or, conversely, when conflicting contextual cues will lead to interference. These insights have direct implications for optimizing training and rehabilitation, in which tailoring the learning context to the individual can determine whether recovery is accelerated or hindered.

# **Broader connections**

Motor learning can be harnessed to develop more effective rehabilitation strategies. When one learning system is compromised, therapy can leverage intact learning systems to promote recovery (Roemmich & Bastian, 2018). These mechanisms can also augment human performance—from lifting heavier loads to refining finger dexterity for musical skill (Kieliba et al., 2021)—and reveal principles that generalize beyond the motor domain, informing cognitive science, robotic learning, and the design of prosthetic control in amputees (Schone et al., 2024).

Motor learning plays a central role in the design of brain–computer interfaces, guiding training protocols that enable users to interact more effectively with technology and the world around them (Collinger et al., 2013; Orsborn et al., 2014). Brain–computer interfaces also offer longitudinal access to neural dynamics during human–computer interaction, making them a powerful tool for uncovering the neural mechanisms of motor learning (Sadtler et al., 2014). More broadly, advances in motor control and learning can inform the design of neurotechnologies that leverage these principles to restore and enhance movement (see, e.g., de Freitas et al., 2025; Pimenta Silva et al., 2025; Spix et al., 2021).

Digital games, virtual reality, and crowdsourced platforms enable large-scale investigation of naturalistic motor behavior (Russell et al., 2016; Tsay et al., 2024) [see [Virtual Reality](/articles/2vci5sg1)]. This shift allows researchers to track skill development not just over minutes or hours but across months or even years (Listman et al., 2021). Recent technological advances also make it possible to capture motor behavior with high precision at scale, offering a richer and more ecological view of how skills are acquired, adapted, and retained in the real world (Fooken et al., 2023). Indeed, we are moving toward a future in which insights from motor learning drive training programs for everyday skills that are not only effective and accessible but also precisely tailored to the individual.

*Note: If you want to experience motor learning tasks firsthand, you can see a number of demonstrations here: *[https://www.tsaylab.com/play](https://www.tsaylab.com/play)*.*

# **Further reading **

- Bastian, A. J. (2006). Learning to predict the future: the cerebellum adapts feedforward movement control. Current Opinion in Neurobiology, 16(6), 645–649. [https://doi.org/10.1016/j.conb.2006.08.016](https://doi.org/10.1016/j.conb.2006.08.016)
- Krakauer, J., Hadjiosif, A. M., Xu, J., Wong, A. L., & Haith, A. M. (2019). Motor learning. *Comprehensive Physiology*,* 9*(2), 613-663. [https://doi.org/10.1002/cphy.c170043](https://doi.org/10.1002/cphy.c170043)
- Shadmehr, R., & Krakauer, J. W. (2008). A computational neuroanatomy for motor control. *Experimental Brain Research*, *185*(3), 359-381. [https://doi.org/10.1007/s00221-008-1280-5](https://doi.org/10.1007/s00221-008-1280-5)
- Tsay, J. S., Kim, H. E., McDougle, S. D., Taylor, J. A., Haith, A., Avraham, G., Krakauer, J. W., Collins, A. G. E., & Ivry, R. B. (2024). Fundamental processes in sensorimotor learning: Reasoning, refinement, and retrieval. *eLife*, *13*, e91839. [https://doi.org/10.7554/eLife.91839](https://doi.org/10.7554/eLife.91839)

# References

Stratton, G. M. (1896). Some preliminary experiments on vision without inversion of the retinal image. *Psychological Review*, *3*(6), 611–617. <https://doi.org/10.1037/h0072918>

Milner, B. (1962). Les troubles de la memoire accompagnant des lesions hippocampiques bilaterales. In P. Passouant (Ed.), *Physiologie de l’Hippocampe* (pp. 257–272). Centre National de la Recherche Scientifique.

Shadmehr, R., Smith, M. A., & Krakauer, J. (2010). Error correction, sensory prediction, and adaptation in motor control. *Annual Review of Neuroscience*, *33*, 89–108. <https://doi.org/10.1146/annurev-neuro-060909-153135>

Hill, N. M., Tripp, H. M., Wolpert, D. M., Malone, L. A., & Bastian, A. J. (2025). Age-dependent predictors of effective reinforcement motor learning across childhood. *eLife*, *13*, RP101036. <https://doi.org/10.7554/eLife.101036>

Shadmehr, R., & Krakauer, J. W. (2008). A computational neuroanatomy for motor control. *Experimental Brain Research*, *185*(3), 359–381. <https://doi.org/10.1007/s00221-008-1280-5>

Hadjiosif, A. M., Morehead, J. R., & Smith, M. A. (2023). A double dissociation between savings and long-term memory in motor learning. *PLoS Biology*, *21*(4), e3001799. <https://doi.org/10.1371/journal.pbio.3001799>

Smith, M. A., Ghazizadeh, A., & Shadmehr, R. (2006). Interacting adaptive processes with different timescales underlie short-term motor learning. *PLoS Biology*, *4*(6), e179. <https://doi.org/10.1371/journal.pbio.0040179>

Tseng, Y. W., Diedrichsen, J., Krakauer, J. W., Shadmehr, R., & Bastian, A. J. (2007). Sensory prediction errors drive cerebellum-dependent adaptation of reaching. *Journal of Neurophysiology*, *98*(1), 54–62. <https://doi.org/10.1152/jn.00266.2007>

Nikooyan, A. A., & Ahmed, A. A. (2015). Reward feedback accelerates motor learning. *Journal of Neurophysiology*, *113*(2), 633–646. <https://doi.org/10.1152/jn.00032.2014>

Therrien, A. S., Wolpert, D. M., & Bastian, A. J. (2016). Effective reinforcement learning following cerebellar damage requires a balance between exploration and motor noise. *Brain: A Journal of Neurology*, *139*(Pt 1), 101–114. <https://doi.org/10.1093/brain/awv329>

Taylor, J. A., Krakauer, J. W., & Ivry, R. B. (2014). Explicit and implicit contributions to learning in a sensorimotor adaptation task. *Journal of Neuroscience*, *34*(8), 3023–3032. <https://doi.org/10.1523/JNEUROSCI.3619-13.2014>

Verstynen, T., & Sabes, P. N. (2011). How each movement changes the next: An experimental and theoretical study of fast adaptive priors in reaching. *Journal of Neuroscience*, *31*(27), 10050–10059. <https://doi.org/10.1523/JNEUROSCI.6525-10.2011>

Shmuelof, L., Krakauer, J. W., & Mazzoni, P. (2012). How is a motor skill learned? Change and invariance at the levels of task success and trajectory control. *Journal of Neurophysiology*, *108*(2), 578–594. <https://doi.org/10.1152/jn.00856.2011>

Albert, S. T., Jang, J., Modchalingam, S., ’t Hart, M., Henriques, D., Lerner, G., Della-Maggiore, V., Haith, A. M., Krakauer, J. W., & Shadmehr, R. (2022). Competition between parallel sensorimotor learning systems. *eLife*, *11,* e65361. <https://doi.org/10.7554/eLife.65361>

Miyamoto, Y. R., Wang, S., & Smith, M. A. (2020). Implicit adaptation compensates for erratic explicit strategy in human motor learning. *Nature Neuroscience*, *23*(3), 443–455. <https://doi.org/10.1038/s41593-020-0600-3>

Song, J. H. (2019). The role of attention in motor control and learning. *Current Opinion in Psychology*, *29*, 261–265. <https://doi.org/10.1016/j.copsyc.2019.08.002>

Vassiliadis, P., Derosiere, G., Dubuc, C., Lete, A., Crevecoeur, F., Hummel, F. C., & Duque, J. (2021). Reward boosts reinforcement-based motor learning. *iScience*, *24*(7), 102821. <https://doi.org/10.1016/j.isci.2021.102821>

Wadsley, C. G., & Greenhouse, I. (2024). Failures to launch preclude response inhibition. *Trends in Cognitive Sciences*, *28*(5), 400–403. <https://doi.org/10.1016/j.tics.2024.03.001>

Tsay, J. S., Kim, H. E., McDougle, S. D., Taylor, J. A., Haith, A., Avraham, G., Krakauer, J. W., Collins, A. G. E., & Ivry, R. B. (2024). Fundamental processes in sensorimotor learning: Reasoning, refinement, and retrieval. *eLife*, *13*, e91839. <https://doi.org/10.7554/eLife.91839>

Heald, J. B., Lengyel, M., & Wolpert, D. M. (2023). Contextual inference in learning and memory. *Trends in Cognitive Sciences*, *27*(1), 43–64. <https://doi.org/10.1016/j.tics.2022.10.004>

Ogasa, K., Yokoi, A., Okazawa, G., Nishigaki, M., Hirashima, M., & Hagura, N. (2024). Decision uncertainty as a context for motor memory. *Nature Human Behaviour*, *8*(9), 1738–1751. <https://doi.org/10.1038/s41562-024-01911-x>

Roemmich, R. T., & Bastian, A. J. (2018). Closing the loop: From motor neuroscience to neurorehabilitation. *Annual Review of Neuroscience*, *41*, 415–429. <https://doi.org/10.1146/annurev-neuro-080317-062245>

Kieliba, P., Clode, D., Maimon-Mor, R. O., & Makin, T. R. (2021). Robotic hand augmentation drives changes in neural body representation. *Science Robotics*, *6*(54), eabd7935. <https://doi.org/10.1126/scirobotics.abd7935>

Schone, H. R., Udeozor, M., Moninghoff, M., Rispoli, B., Vandersea, J., Lock, B., Hargrove, L., Makin, T. R., & Baker, C. I. (2024). Biomimetic versus arbitrary motor control strategies for bionic hand skill learning. *Nature Human Behaviour*, *8*(6), 1108–1123. <https://doi.org/10.1038/s41562-023-01811-6>

Collinger, J. L., Wodlinger, B., Downey, J. E., Wang, W., Tyler-Kabara, E. C., Weber, D. J., McMorland, A. J. C., Velliste, M., Boninger, M. L., & Schwartz, A. B. (2013). High-performance neuroprosthetic control by an individual with tetraplegia. *Lancet*, *381*(9866), 557–564. <https://doi.org/10.1016/S0140-6736(12)61816-9>

Orsborn, A. L., Moorman, H. G., Overduin, S. A., Shanechi, M. M., Dimitrov, D. F., & Carmena, J. M. (2014). Closed-loop decoder adaptation shapes neural plasticity for skillful neuroprosthetic control. *Neuron*, *82*(6), 1380–1393. <https://doi.org/10.1016/j.neuron.2014.04.048>

Sadtler, P. T., Quick, K. M., Golub, M. D., Chase, S. M., Ryu, S. I., Tyler-Kabara, E. C., Yu, B. M., & Batista, A. P. (2014). Neural constraints on learning. *Nature*, *512*(7515), 423–426. <https://doi.org/10.1038/nature13665>

de Freitas, R. M., Bhatia, S., Sorensen, E., Verma, N., Carranza, E., Ensel, S., Borda, L., Boos, A., Goldsmith, J., Fisher, L. E., Fields, D. P., Powell, M. P., Gordon, S., Balzer, J., Friedlander, R. M., Wittenberg, G. F., Gerszten, P., Krakauer, J. W., Pirondini, E., … Capogrosso, M. (2025). Spinal cord stimulation improves motor function and spasticity in chronic post-stroke upper limb hemiparesis. *medRxiv*. <https://doi.org/10.1101/2025.08.01.25332445>

Pimenta Silva, D., Bouça-Machado, R., Pona-Ferreira, F., Lobo, T., Cacho, R., Anker, R., Krakauer, J. W., & Ferreira, J. J. (2025). Combining immersive exergaming with physiotherapy in a specialized intensive Parkinson’s disease rehabilitation program: A randomized controlled trial. *Journal of Neuroengineering and Rehabilitation*, *22*(1), 131. <https://doi.org/10.1186/s12984-025-01640-w>

Spix, T. A., Nanivadekar, S., Toong, N., Kaplow, I. M., Isett, B. R., Goksen, Y., Pfenning, A. R., & Gittis, A. H. (2021). Population-specific neuromodulation prolongs therapeutic benefits of deep brain stimulation. *Science*, *374*(6564), 201–206. <https://doi.org/10.1126/science.abi7852>

Russell, H. E. B., Harbott, L. K., Nisky, I., Pan, S., Okamura, A. M., & Gerdes, J. C. (2016). Motor learning affects car-to-driver handover in automated vehicles. *Science Robotics*, *1*(1), eaah5682. <https://doi.org/10.1126/scirobotics.aah5682>

Tsay, J. S., Asmerian, H., Germine, L. T., Wilmer, J., Ivry, R. B., & Nakayama, K. (2024). Large-scale citizen science reveals predictors of sensorimotor adaptation. *Nature Human Behaviour*, *8*, 510-525. <https://doi.org/10.1038/s41562-023-01798-0>

Listman, J. B., Tsay, J. S., Kim, H. E., Mackey, W. E., & Heeger, D. J. (2021). Long-term motor learning in the “wild” with high volume video game data. *Frontiers in Human Neuroscience*, *15*, 777779. <https://doi.org/10.3389/fnhum.2021.777779>

Fooken, J., Baltaretu, B. R., Barany, D. A., Diaz, G., Semrau, J. A., Singh, T., & Crawford, J. D. (2023). Perceptual-cognitive integration for goal-directed action in naturalistic environments. *Journal of Neuroscience*, *43*(45), 7511–7522. <https://doi.org/10.1523/JNEUROSCI.1373-23.2023>