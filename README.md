<!-- 🌐 Language Switch -->
<p align="right">
  <a href="./README.md">English</a> | <a href="./README_CN.md">简体中文</a>
</p>

<!-- ═══════════════════════════════════════════════════ -->
<!-- HERO -->
<!-- ═══════════════════════════════════════════════════ -->

<div align="center">

<img src="./assets/hero-card-en.svg" width="900" alt="Nook: third-year undergraduate focused on backend, rendering, and solution architecture" />

<br>

<!-- Quick Links -->
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Nook001)
&nbsp;
[![Outlook](https://img.shields.io/badge/Email-0078D4?style=for-the-badge&logo=microsoftoutlook&logoColor=white)](mailto:nook_lyz@outlook.com)

</div>


<!-- ═══════════════════════════════════════════════════ -->
<!-- Education Cards -->
<!-- ═══════════════════════════════════════════════════ -->

## 🎓 Education

<table width="100%">
  <tr>
    <td valign="top" width="50%">
      <strong>University of Warwick</strong><br>
      <sub>BSc Computer Science · Sep 2023–Jun 2027</sub>
      <ul>
        <li>Current classification: 2:1</li>
        <li>Functional programming, computer security, AI</li>
      </ul>
    </td>
    <td valign="top" width="50%">
      <strong>Hong Kong University of Science and Technology</strong><br>
      <sub>Computer Engineering Exchange · Sep 2025–Jun 2026</sub>
      <ul>
        <li>Deep learning, cloud computing, distributed systems</li>
        <li>Large-scale ML systems and programming languages</li>
      </ul>
    </td>
  </tr>
</table>


<!-- ═══════════════════════════════════════════════════ -->
<!-- Tech Stack -->
<!-- ═══════════════════════════════════════════════════ -->

## 🛠️ Tech Stack

<div align="center">

**Production**

<a href="https://skillicons.dev">
  <img src="https://skillicons.dev/icons?i=java,kotlin,spring,mysql,redis,rabbitmq&theme=dark" />
</a>

**Projects & Research**

<a href="https://skillicons.dev">
  <img src="https://skillicons.dev/icons?i=go,cs,flutter,unity,godot,pytorch,haskell&theme=dark" />
</a>

</div>

> Also: `HLSL` `JavaFX` `TypeScript / Bun` `LangGraph` `MCP`


<!-- ═══════════════════════════════════════════════════ -->
<!-- About -->
<!-- ═══════════════════════════════════════════════════ -->

## 👋 About Me

Computer Science undergraduate with experience across backend systems, solution architecture, and real-time rendering. Currently focused on production agent tooling, distributed and asynchronous workflows, and GPU rendering optimisation; personal projects centre on Stardew Valley modding and graphics pipeline development.


<!-- ═══════════════════════════════════════════════════ -->
<!-- Work Experience -->
<!-- ═══════════════════════════════════════════════════ -->

## 💼 Work Experience

<table width="100%">
  <tr>
    <td valign="top" width="50%">
      <strong><img src="assets/tencent.png" height="18" alt="Tencent" /> — CSIG</strong><br>
      <sub>Solution Architect · Shenzhen · Apr 2026–Present</sub>
      <ul>
        <li>Built an MPS POC Agent with CLI-based MPS/COS tools, parameter validation, risk controls, state management, and observability.</li>
        <li>Developed an internal media workbench with TypeScript/Bun for asynchronous jobs, state tracking, and result publishing.</li>
      </ul>
    </td>
    <td valign="top" width="50%">
      <strong><img src="assets/cas.png" height="24" alt="ISCAS" /></strong><br>
      <sub>Distributed Systems Developer · Remote · Jan–Apr 2026</sub>
      <ul>
        <li>Contributed to <strong>rk8s</strong>, a K8s-compatible container orchestration system.</li>
        <li>Implemented OCI image import, export, metadata inspection, and tag management for rkforge.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td valign="top" width="50%">
      <strong><img src="assets/shopee.png" height="30" alt="Shopee" /> Shopee — Digital Bank</strong><br>
      <sub>Backend Developer · Shenzhen · Dec 2025–Apr 2026</sub>
      <ul>
        <li>Developed core loan-accounting flows for product conversion, transaction generation, daily accounting, and cross-system reconciliation.</li>
        <li>Built paginated concurrent checks and layered validation, reconciling tens of thousands of records in about five minutes.</li>
      </ul>
    </td>
    <td valign="top" width="50%">
      <strong><img src="assets/oppo.png" height="20" alt="OPPO" /></strong><br>
      <sub>Device SDK Developer · Shenzhen · Jun–Sep 2025</sub>
      <ul>
        <li>Reworked SDK detection around Intent-Filter scanning, covering 50+ major apps and system applications.</li>
        <li>Fixed concurrent request queuing in Push Demo and simplified debugging interfaces.</li>
      </ul>
    </td>
  </tr>
</table>

<details>
  <summary><strong>Earlier: Jinji Smart Equipment · Industrial Software Developer</strong></summary>
  <br>
  Built a JavaFX and Apache POI drawing workflow that reduced processing time by 80%; contributed to a Java → Kotlin migration and developed a C++ SolidWorks drawing inspection plugin.
</details>



<!-- ═══════════════════════════════════════════════════ -->
<!-- Featured Projects -->
<!-- ═══════════════════════════════════════════════════ -->

## 🚀 Mod Projects

<table>
<tr>
<td width="50%" valign="top">

### Dynamic Shader

> A custom HLSL shader bringing **HD2D-style** rendering to Stardew Valley.

![Downloads](https://img.shields.io/badge/Downloads-155,800+-6366F1?style=for-the-badge)
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
<!-- GitHub Activity -->
<!-- ═══════════════════════════════════════════════════ -->

<h2 align="center">📈 GitHub Activity</h2>

<div align="center">

![Streak](https://streak-stats.demolab.com?user=Nook001&theme=tokyonight&hide_border=true&background=0D1117&ring=6366F1&fire=818CF8&currStreakLabel=C9D1D9)

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