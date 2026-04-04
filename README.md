<!-- 🌐 Language Switch -->
<p align="right">
  <a href="./README.md">English</a> | <a href="./README_CN.md">简体中文</a>
</p>

<!-- ═══════════════════════════════════════════════════ -->
<!-- HERO -->
<!-- ═══════════════════════════════════════════════════ -->

<div align="center">

<h1>✦ Yuanzhi Liu ✦</h1>

<img src="./assets/hero-card-en.svg" width="900" alt="hero-card" />

<br>

<!-- Quick Links -->
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Nook001)
&nbsp;
[![Outlook](https://img.shields.io/badge/Email-0078D4?style=for-the-badge&logo=microsoftoutlook&logoColor=white)](mailto:nook_lyz@outlook.com)

</div>


<!-- ═══════════════════════════════════════════════════ -->
<!-- Education Cards -->
<!-- ═══════════════════════════════════════════════════ -->

<h2 align="center">🎓 Education</h2>

<div align="center">

<table>
  <tr>
    <td align="center" valign="top" width="50%">
      <img src="./assets/edu-card-warwick-en.svg" width="500" alt="warwick-card" />
    </td>
    <td align="center" valign="top" width="50%">
      <img src="./assets/edu-card-hkust-en.svg" width="500" alt="hkust-card" />
    </td>
  </tr>
</table>

</div>


<!-- ═══════════════════════════════════════════════════ -->
<!-- Work Experience -->
<!-- ═══════════════════════════════════════════════════ -->

## 💼 Work Experience

> <table>
>   <tr>
>     <td width="56" align="center" valign="middle">
>       <img src="assets/tencent.png" height="46" alt="tencent-logo" />
>     </td>
>     <td valign="top">
>       <b>Solutions Architect · Tencent CSIG · Shenzhen · 2026/04 – Present</b>
>       <ul>
>         <li>Designed cloud migration solutions for enterprise users of Tencent Cloud audio and video products, and provided architecture design support.</li>
>       </ul>
>     </td>
>   </tr>
> </table>

> <table>
>   <tr>
>     <td width="56" align="center" valign="middle">
>       <img src="assets/cas.png" height="" alt="cas-logo" />
>     </td>
>     <td valign="top">
>       <b>Distributed Systems Developer · Institute of Software, CAS · Remote · 2026/01 – 2026/04</b>
>       <ul>
>         <li>Contributed to the development and maintenance of <b>rk8s</b>, a K8S-compatible container orchestration system reimplemented in <b>Rust</b>.</li>
>         <li>Designed and implemented a full local image management command suite for <b>rkforge</b>, including exporting merged <b>manifest + config JSON</b> metadata, importing images from OCI image layout tar archives, exporting OCI image layout tarballs, and creating new image tag references.</li>
>       </ul>
>     </td>
>   </tr>
> </table>

> <table>
>   <tr>
>     <td width="56" align="center" valign="middle">
>       <img src="assets/shopee.png" height="46" alt="shopee-logo" />
>     </td>
>     <td valign="top">
>       <b>Backend Developer · Shopee Digital Banking · Shenzhen · 2025/12 – 2026/04</b>
>       <ul>
>         <li>Built backend features for Shopee Digital Banking loan productization, covering transaction processing, fund flow generation, and reconciliation across the loan accounting pipeline.</li>
>         <li>Extended transaction pipeline nodes for employee loan changes and corresponding fund flow generation, then completed full end-to-end validation through cross-system debugging and test data construction.</li>
>         <li>Designed and implemented scheduled balance and transaction reconciliation jobs that validate loan balances, statuses, and fund movements by trading day and business flow grouping, combining accounting rules, amount consistency checks, and special <b>Park</b> fund handling to surface accounting anomalies and help pinpoint core system bugs.</li>
>       </ul>
>     </td>
>   </tr>
> </table>

> <table>
>   <tr>
>     <td width="56" align="center" valign="middle">
>       <img src="assets/oppo.png" height="60" alt="oppo-logo" />
>     </td>
>     <td valign="top">
>       <b>Terminal SDK Developer · OPPO · Shenzhen · 2025/06 – 2025/09</b>
>       <ul>
>         <li>Refactored the SDK automated detection tool using <b>Intent-Filter scanning</b>, resolving component name matching failures caused by third-party redevelopment — covering <b>50+ top Apps</b> and system-level applications.</li>
>         <li>Fixed Push Demo multi-thread concurrent request queuing issues, simplified/encapsulated debugging interfaces to accelerate third-party developer onboarding.</li>
>       </ul>
>     </td>
>   </tr>
> </table>

> <table>
>   <tr>
>     <td width="56" align="center" valign="middle">🏭</td>
>     <td valign="top">
>       <b>Industrial Software Developer · Jinji Smart Equipment · Shenzhen · 2024/07 – 2024/09</b>
>       <ul>
>         <li>Integrated <b>Apache POI</b> with JavaFX to build an automated drawing file classification, packaging, and retrieval tool — reducing packaging workflow by <b>80%</b>.</li>
>         <li>Led Java → Kotlin migration (5k → 3.8k lines), improving null-safety handling for IO operations.</li>
>         <li>Developed a <b>C++ Solidworks plugin</b> for detecting hole-punching patterns in drawings.</li>
>       </ul>
>     </td>
>   </tr>
> </table>



<!-- ═══════════════════════════════════════════════════ -->
<!-- Featured Projects -->
<!-- ═══════════════════════════════════════════════════ -->

## 🚀 Mod Projects

<table>
<tr>
<td width="50%" valign="top">

### Dynamic Shader

> A custom HLSL shader bringing **HD2D-style** rendering to Stardew Valley.

![Downloads](https://img.shields.io/badge/Downloads-51,600+-6366F1?style=for-the-badge)
![Endorsements](https://img.shields.io/badge/Endorsements-500+-818CF8?style=for-the-badge)


- Intercepts game render pipeline via **Harmony** to inject custom shaders simulating a 3D lighting system
- **GPU-accelerated** shadow rendering + double-buffered shadow collection queues for low-overhead global shadows. LUT saves 15M math ops; separable convolution kernel optimises Gaussian blur; dual-dict texture classification cuts 90% draw calls
- **Custom vertex/pixel shaders**: 3D projection simulation, contact-hardening shadows, ambient hue shift, tilt-shift effect

`HLSL` `GPU Batching` `Harmony` `Shader`

</td>
<td width="50%" valign="top">

### BetterBuildingUpgrades

> A Stardew Valley mod extending core game methods using Harmony + SMAPI.

![Downloads](https://img.shields.io/badge/Downloads-12,700+-6366F1?style=for-the-badge)
![Endorsements](https://img.shields.io/badge/Endorsements-190+-818CF8?style=for-the-badge)

- Rewrites and extends core game methods via **reflection injection**
- Resolves **multiplayer data consistency** issues
- Optimises computation overhead for large-scale automation logic, ensuring stable frame rates

`C#` `SMAPI` `Harmony`

</td>
</tr>
</table>

<br>




<!-- ═══════════════════════════════════════════════════ -->
<!-- Tech Stack -->
<!-- ═══════════════════════════════════════════════════ -->

## 🛠️ Tech Stack

<div align="center">

**Work & Production**

<a href="https://skillicons.dev">
  <img src="https://skillicons.dev/icons?i=java,kotlin,spring,mysql,redis,git&theme=dark" />
</a>

**Personal Projects**

<a href="https://skillicons.dev">
  <img src="https://skillicons.dev/icons?i=go,python,cs,rabbitmq,flutter,unity,blender&theme=dark" />
</a>

**Exploring**

<a href="https://skillicons.dev">
  <img src="https://skillicons.dev/icons?i=pytorch,tauri,unreal,haskell&theme=dark" />
</a>

</div>

> Other skills: `HLSL` `JavaFX` `LangGraph` `MCP`

<br>

<!-- ═══════════════════════════════════════════════════ -->
<!-- Community & Activities -->
<!-- ═══════════════════════════════════════════════════ -->

## 📜 Other Activities

- 🎮 Tencent IEG "Opening Lesson" — Game Client (UE) Track Certificate
- 🌐 Contributed Chinese translations for indie games *Big Ambitions* and *Supermarket Simulator* via Localizor
- ✍️ Published mod development articles on Xiaoheihe with **61,900+** total reads
- 🌿 Volunteered at Warwick Nature Conservation for **30+ hours** of environmental work

<br>

<!-- ═══════════════════════════════════════════════════ -->
<!-- GitHub Stats -->
<!-- ═══════════════════════════════════════════════════ -->

<h2 align="center">📊 GitHub Stats</h2>

<div align="center">

![GitHub Stats](https://github-readme-stats.vercel.app/api?username=Nook001&show_icons=true&theme=tokyonight&hide_border=true&bg_color=0D1117&title_color=6366F1&icon_color=818CF8&text_color=C9D1D9&rank_icon=github)
&nbsp;
![Streak](https://streak-stats.demolab.com?user=Nook001&theme=tokyonight&hide_border=true&background=0D1117&ring=6366F1&fire=818CF8&currStreakLabel=C9D1D9)

</div>

<div align="center">

![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=Nook001&layout=donut&theme=tokyonight&hide_border=true&bg_color=0D1117&title_color=6366F1&text_color=C9D1D9)

</div>

<!-- Trophies -->
<div align="center">

![Trophy](https://github-profile-trophy.vercel.app/?username=Nook001&theme=discord&no-frame=true&no-bg=true&column=7)

</div>

<!-- Activity Graph -->
<div align="center">

![Activity Graph](https://github-readme-activity-graph.vercel.app/graph?username=Nook001&theme=tokyo-night&hide_border=true&bg_color=0D1117&color=6366F1&line=818CF8&point=C9D1D9&area=true&area_color=6366F1)

</div>

<br>

<!-- Profile Views -->
<div align="center">

![Profile Views](https://komarev.com/ghpvc/?username=Nook001&color=6366F1&style=flat-square&label=Profile+Views)

</div>

![footer](https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,12,20&height=120&section=footer)
