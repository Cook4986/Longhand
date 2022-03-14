# **Longhand** #
Longhand is a python notebook and associated Blender python (bpy) scripts that, combined, takes images of handwritten text and returns an immersive visualization. Longhand allows non-technical end users to explore unwieldy text corpora during early in the research lifecycle. 

![throughput diagram](https://images.squarespace-cdn.com/content/v1/532b70b6e4b0dca092974dbe/1627401430752-R7H10DTUUOSB4GKDDKD1/Longhand+Throughput_Cook2021.png?format=2500w)

### Usage
...

### Innovations
* Supports “raw” input data, at scale (HTR)
* Leverages large 3D asset collections (Sketchfab)
* Exposes humanities to the benefits of XR
  * Depth of field
  * Embodied interactivity
  * Sense of scale

### Limitations
* Best for nouns (i.e. things) in the corpus
* Proprietary HTR (Amazon, Google, Microsoft)
* Model placement in scene is unsolved 

### Next Steps
* Automate model distribution in Blender 
* Automate GLB file hosting for Hubs
* Hack hubs to recognize and change scene using GLBs

### Core Technologies
 * [HandPrint](https://github.com/caltechlibrary/handprint)(version: 1.5.1)
 * [SpaCy](https://github.com/explosion/spaCy)(3.2.1)
 * [Sketchfab data API, V3](https://docs.sketchfab.com/data-api/v3/index.html)
 * [Blender](https://www.blender.org/)(3.0.1)
 * [Blender 3.0.1 Python API](https://docs.blender.org/api/current/index.html)
 * [Mozilla Hubs](https://github.com/mozilla/hubs)

Matt Cook (mncook.net)- 2022
