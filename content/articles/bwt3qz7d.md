---
title: Augmented Reality
slug: bwt3qz7d
date: '2025-07-07'
doi: 10.21428/e2759450.60de8266
authors:
- Neil McDonnell
section_editors:
- Adrian Alsmith
---

Augmented reality (AR) is a technology that provides perceptual experiences that blend the user’s real-world context with computer-generated virtual elements to form a unified scene. AR experiences situate the virtual in relation to the real world and then dynamically track changes in perspective to sustain the illusion that the virtual elements are “out there” in the world. AR is primarily a visual technology, but like the related technology of virtual reality (VR), spatial audio and haptic elements can be incorporated. The impact of AR experiences on users, especially on cognitive load and education, is a growing area of study in cognitive science.

# History

The origins of AR overlap with that of VR: in the lab of Ivan Sutherland in Utah in 1968 (Lanier, 2017). The first prototypes overlaid computer graphics selectively on top of the user’s field of view to create a jointly real and virtual visual experience. The major challenge of AR is matching the virtual elements to the real-world context in such a way that it looks like they belong together, and it takes some element of computer vision (Hoff et al., 1996)—via a camera attached to a computing device—to retain that match as the world changes around the user or as the user changes their perspective on the world. The advent of smartphones in the late 2000s created the opportunity for widespread, consumer-facing AR.

# Core concepts

There exists a wide disparity in the function and efficacy of different technologies that are labeled as AR and inconsistencies in the terminology used to refer to different variants. In general, it matters most how the device senses its relation to the world (tracking), how it represents the virtual elements (rendering), and what kind of display technology is used.

## *Tracking*

Consumer AR deployments in the early 2010s used a detection *trigger* image—initially a QR code, later any image with distinctive contrast—to *track* the relative position of the real-world *target* area or object to the camera. Later, SLAM (*simultaneous localization and mapping*) technologies dispensed with the need for trigger images and instead tracked general context features such as the horizontal surfaces of tables or the ground. The Pokémon Go smartphone game became a worldwide phenomenon in 2016 using this technology, and since then, both Apple and Google have embedded AR engines (called *AR Kit* and *AR Core*, respectively) into their iOS and Android operating systems to make development and distribution of AR experiences easier.

## *Rendering*

Tracking information, from a trigger or from SLAM, is used to *render* the appropriate point of view of a three-dimensional model and overlay this on the camera feed that the user sees. These calculations are undertaken by the graphics processor within the device and crucially require *games/physics* *engine* software (e.g., Unity) to generate 30 to 60 frames of animation per second to sustain the AR illusion whilst the camera or target are in motion.

## *Display: Augmented versus mixed reality*

Most AR deployments mediate all of the user’s AR experience—the virtual and the real—via a screen. This is also the approach taken by recent Meta Quest headsets (Quest Pro and Quest 3 are especially capable versions) and the Apple Vision Pro device. In the current nomenclature, this is usually referred to as *mixed reality*. Apple refer to theirs as *spatial computing*.

In contrast, the approach taken by Microsoft with its HoloLens (2016) and by the rival Magic Leap One (2018) was to use transparent lenses that allowed the user to see the real world naturally and only project the virtual elements. This relatively unmediated version of the technology was initially branded mixed reality by Microsoft but has since become more commonly referred to as (true) AR.

The trajectory of the technology is towards (true) AR, but the devices to date have not become commercially viable. The technical challenges are considerable, relating primarily to optics (field of view, brightness of image) and secondarily to the size, weight, heat output, and cost of devices. Mixed reality via a screen represents a more achievable interim step and is the most common form of AR today, with an estimated 1.4 billion AR devices of varying levels of sophistication in the world today ([Statista](https://www.statista.com/statistics/1098630/global-mobile-augmented-reality-ar-users/)).

# Questions, controversies, and new developments

The impact of AR on learning outcomes has been studied for almost three decades (Garzón, 2021) and remains a prominent and growing topic (Avila-Garzon et al., 2021). Areas of particular concern to cognitive scientists include spatial judgement (Shelton & Hedley, 2004), information retention (Huang et al., 2019), and in embodied approaches to learning (Abrahamson, 2014).

In both educational and industrial applications of AR, the topic of cognitive load (within cognitive load theory) is ubiquitous. Understanding the load experienced by users across different devices, tasks, and applications is vital to understanding the net impact of such adoption (Buchner et al., 2021). How load is measured and the different types of load (intrinsic, extrinsic, germane) remain challenges in the literature (Buchner et al., 2022)

Clinical applications of AR are also being studied (Vinci et al., 2020), in particular, the role of AR in exposure-based therapies (Riva et al., 2016).

As with the concept of VR before it (Savickaite et al., 2022), the lack of consensus regarding what counts as AR makes for inconsistent nomenclature across studies. This observation in turn makes literature reviews challenging and headline claims about AR ambiguous across significantly different technological approaches: mobile, wearable via screens, and wearable via transparent lenses.

# Broader connections

Within cognitive science, there are clear connections with the broader topics of cognitive load (Sweller et al., 2019), education and learning (Poupard et al., 2024; Quintero et al., 2019), exposure therapy (Wechsler et al., 2019), and vision (Scarfe & Glennerster, 2015). Virtual content is often characterized as illusory [see [Virtual Reality](/articles/2vci5sg1)]. However, it is a controversial matter within philosophy whether the virtual content in AR (and VR) experiences are genuinely real and thus whether or not we should think of such overall experiences as genuinely illusory (see Chalmers, 2017). This question has potential ramifications in the law, especially as it regards to the apparent theft of virtual objects (Wildman & McDonnell, 2020).

On a practical level, access to high-end AR technology is not ubiquitous, and the cost and other technical barriers limit the scope of work. There are specific considerations around access to AR technology in education, including the need for inclusive design to cater to learners with diverse abilities, such as those with sensory impairments or neurodivergence, and the imperative to address equality issues arising from affordability to prevent disparities in educational opportunities (McDonnell et al., 2024). Sophisticated AR devices and the exciting use cases that they promise require sophisticated camera arrays and sensors to understand their environment and, in the case of head-worn devices, to understand the user via eye tracking, retina sensing, and more. These technical issues raise significant privacy and data security questions around AR technology for researchers and policy makers (Colburn et al., 2024).

# Further reading

- Lanier, J. (2017). *Dawn of the new everything: Encounters with reality and virtual reality*. Henry Holt and Company.
- Queiroz, A., Bailenson, J., Blair, K., Schwartz, D., Thille, C., & Wagner, A. (2024). Extended realities and the future of knowledge work: Opportunities and challenges. *Proceedings of the 31st IEEE Conference on Virtual Reality and 3D User Interfaces Abstracts and Workshops*, 662-666. [https://doi.org/10.1109/VRW62533.2024.00130](https://doi.org/10.1109/VRW62533.2024.00130)
- Scoble, R., & Israel, S. (2016). *The fourth transformation: How augmented reality and artificial intelligence change everything*. Patrick Brewster Press.

# References

Lanier, J. (2017). *Dawn of the new everything: Encounters with reality and virtual reality.* Henry Holt and Company.

Hoff, W. A., Nguyen, K., & Lyon, T. (1996). Computer-vision-based registration techniques for augmented reality. Proceedings of SPIE 2904, *Intelligent Robots and Computer Vision XV: Algorithms, Techniques, Active Vision, and Materials Handling*. <https://doi.org/10.1117/12.256311>

Garzón, J. (2021). An overview of twenty-five years of augmented reality in education. *Multimodal Technologies and Interaction*, *5*(7), 37. <https://doi.org/10.3390/mti5070037>

Avila-Garzon, C., Bacca-Acosta, J., Kinshuk, Duarte, J., & Betancourt, J. (2021). Augmented reality in education: An overview of twenty-five years of research. *Contemporary Educational Technology*, *13*(3), ep302. <https://doi.org/10.30935/cedtech/10865>

Shelton, B. E., & Hedley, N. R. (2004). Exploring a cognitive basis for learning spatial relationships with augmented reality. *Technology, Instruction, Cognition and Learning*, *1*(4), 323.

Huang, K. T., Ball, C., Francis, J., Ratan, R., Boumis, J., & Fordham, J. (2019). Augmented versus virtual reality in education: An exploratory study examining science knowledge retention when using augmented reality/virtual reality mobile applications. *Cyberpsychology, Behavior, and Social Networking*, *22*(2), 105-110. <https://doi.org/10.1089/cyber.2018.0150>

Abrahamson, D. (2014). Building educational activities for understanding: An elaboration on the embodied-design framework and its epistemic grounds. *International Journal of Child-Computer Interaction*, *2*(1), 1–16. <https://doi.org/10.1016/j.ijcci.2014.07.002>

Buchner, J., Buntins, K., & Kerres, M. (2021). A systematic map of research characteristics in studies on augmented reality and cognitive load. *Computers and Education Open*, *2*, 100036. <https://doi.org/10.1016/j.caeo.2021.100036>

Buchner, J., Buntins, K., & Kerres, M. (2022). The impact of augmented reality on cognitive load and performance: A systematic review. *Journal of Computer Assisted Learning*, 38(1), 285–303. <https://doi.org/10.1111/jcal.12617>

Vinci, C., Brandon, K. O., Kleinjan, M., & Brandon, T. H. (2020). The clinical potential of augmented reality. *Clinical Psychology: Science and Practice*, *27*(3), e12357. <https://doi.org/10.1111/cpsp.12357>

Riva, G., Baños, R. M., Botella, C., Mantovani, F., & Gaggioli, A. (2016). Transforming experience: The potential of augmented reality and virtual reality for enhancing personal and clinical change. *Frontiers in Psychiatry*, *7*, 164. <https://doi.org/10.3389/fpsyt.2016.00164>

Savickaite, S., McDonnell, N., & Simmons, D. (2022). Defining virtual reality (VR). Scoping literature review on VR applications in autism research. *PsyArXiv Preprints*. <https://doi.org/10.31234/osf.io/p3nh6>

Sweller, J., van Merriënboer, J. J. G., & Paas, F. (2019). Cognitive architecture and instructional design: 20 years later. *Educational Psychology Review*, *31*, 261–292. <https://doi.org/10.1007/s10648-019-09465-5>

Poupard, M., Larrue, F., Sauzéon, H., & Tricot, A. (2024). A systematic review of immersive technologies for education: Learning performance, cognitive load and intrinsic motivation. *British Journal of Educational Technology*, *56*(1), 5–41. <https://doi.org/10.1111/bjet.13503>

Quintero J., Baldiris S., Rubira R., Cerón J., & Velez, G. (2019). Augmented reality in educational inclusion. A systematic review on the last decade. *Frontiers in Psychology*, *10*, 1835. <https://doi.org/10.3389/fpsyg.2019.01835>

Wechsler, T. F., Kümpers, F., & Mühlberger, A. (2019). Inferiority or even superiority of virtual reality exposure therapy in phobias? A systematic review and quantitative meta-analysis on randomized controlled trials specifically comparing the efficacy of virtual reality exposure to gold standard in vivo exposure in agoraphobia, specific phobia, and social phobia. *Frontiers in Psychology*, *10*, 1758. <https://doi.org/10.3389/fpsyg.2019.01758>

Scarfe, P., & Glennerster, A. (2015). Using high-fidelity virtual reality to study perception in freely moving observers. *Journal of Vision*, *15*(9), 3. <https://doi.org/10.1167/15.9.3>

Chalmers, D. J. (2017). The virtual and the real. *Disputatio*, *9*(46), 309-352. <https://doi.org/10.1515/disp-2017-0009>

Wildman, N., & McDonnell, N. (2020). The puzzle of virtual theft. *Analysis*, *80*(3), 493–499. <https://doi.org/10.1093/analys/anaa005>

McDonnell, N., Hirsu, L., Rodolico, G., Savickaite,S. Latkovskis, I., & Chaproniere, L. (2024). XRED: Preparing for immersive education. University of Glasgow. <https://www.gla.ac.uk/media/Media_1030423_smxx.pdf>

Colburn, B., Macpherson, F., Brown, D., Fearnley, L., & McDonnell, N. (2024). Policy and practice recommendations for augmented and mixed reality. University of Glasgow. <https://www.gla.ac.uk/media/Media_1074026_smxx.pdf>