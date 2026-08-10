<!-- 🌐 语言切换 -->
<p align="right">
  <a href="./README.md">English</a> | <a href="./README_CN.md">简体中文</a>
</p>

<!-- ═══════════════════════════════════════════════════ -->
<!-- HERO -->
<!-- ═══════════════════════════════════════════════════ -->

<div align="center">

<img src="./assets/hero-card-zh.svg" width="900" alt="Nook：本科三年级，方向为后端、渲染与解决方案架构" />

<br>

<!-- 快捷链接 -->
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Nook001)
&nbsp;
[![Outlook](https://img.shields.io/badge/邮箱-0078D4?style=for-the-badge&logo=microsoftoutlook&logoColor=white)](mailto:nook_lyz@outlook.com)

</div>


<!-- ═══════════════════════════════════════════════════ -->
<!-- 学历卡片 -->
<!-- ═══════════════════════════════════════════════════ -->

## 🎓 教育经历

<table width="100%">
  <tr>
    <td valign="top" width="50%">
      <strong>英国华威大学</strong><br>
      <sub>计算机科学 本科 · 2023.09–2027.06</sub>
      <ul>
        <li>成绩：2:1</li>
        <li>方向：函数式编程、计算机安全、人工智能</li>
      </ul>
    </td>
    <td valign="top" width="50%">
      <strong>香港科技大学</strong><br>
      <sub>计算机工程 本科联培 · 2025.09–2026.06</sub>
      <ul>
        <li>深度学习、云计算、分布式系统</li>
        <li>大规模机器学习系统、程序设计语言原理</li>
      </ul>
    </td>
  </tr>
</table>


<!-- ═══════════════════════════════════════════════════ -->
<!-- 技术栈 -->
<!-- ═══════════════════════════════════════════════════ -->

## 🛠️ 技术栈

<div align="center">

**生产开发**

<a href="https://skillicons.dev">
  <img src="https://skillicons.dev/icons?i=java,kotlin,spring,mysql,redis,rabbitmq&theme=dark" />
</a>

**项目与研究**

<a href="https://skillicons.dev">
  <img src="https://skillicons.dev/icons?i=go,cs,flutter,unity,godot,pytorch,haskell&theme=dark" />
</a>

</div>

> 核心能力：`状态机与事务边界` `异步任务队列` `跨系统一致性` `Agent Tooling` `OCI / K8s` `GPU Profiling` `Shader Pipeline`


<!-- ═══════════════════════════════════════════════════ -->
<!-- 自我介绍 -->
<!-- ═══════════════════════════════════════════════════ -->

## 👋 关于我

计算机科学专业本科生，经历覆盖 后端、分布式系统、解决方案架构和实时渲染。目前主要专注于生产级Agent工具、分布式和异步工作流以及GPU渲染优化。



<!-- ═══════════════════════════════════════════════════ -->
<!-- 实习经验 -->
<!-- ═══════════════════════════════════════════════════ -->

## 💼 实习经验

<table width="100%">
  <tr>
    <td valign="top" width="50%">
      <strong><img src="assets/tencent.png" height="18" alt="腾讯" /> 腾讯 </strong><br>
      <sub>解决方案架构师 · 2026.04–至今</sub>
      <ul>
        <li>设计面向 LLM 的自描述 CLI 协议，将参数校验、互斥约束、密钥脱敏与风险操作参数哈希下沉工具层；通过 <code>next_action</code> 强状态返回驱动 Agent 按固定生命周期执行。GLM 5.1 多轮测试中输出速度由 30–45 提升至 95–120 token/s，深度思考降至约 1/3，目录探索和重复/错误调用清零。</li>
        <li>基于 TypeScript/Bun/Express/SQLite WAL 开发全栈智能媒体工作台；以 <code>BEGIN IMMEDIATE</code> 原子化配额检查与任务入队，通过 QUEUED→SUBMITTING→PROCESSING→DONE 状态机、原子领取、限流、重试和并发 Worker 实现宕机后可恢复的异步任务链路。</li>
      </ul>
    </td>
    <td valign="top" width="50%">
      <strong><img src="assets/cas.png" height="24" alt="中国科学院软件研究所" /> 中科院 </strong><br>
      <sub>分布式系统开发 · 线上 · 2026.01–2026.04</sub>
      <ul>
        <li>参与基于 Rust 重实现的 K8s 兼容容器编排系统 <strong>rk8s</strong> 的功能开发与维护。</li>
        <li>为 rkforge 构建本地镜像管理子命令：合并输出 manifest/config 元数据，从 OCI Image Layout tar 导入/导出镜像，并维护镜像标签引用。</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td valign="top" width="50%">
      <strong><img src="assets/shopee.png" height="30" alt="Shopee" /> Shopee </strong><br>
      <sub>后端开发 · 深圳 · 2025.12–2026.04</sub>
      <ul>
        <li>负责贷款核算核心链路：消费 Loan Core 交易事件，完成贷款产品转换、转入/转出流水发生额生成、Park 类资金边界处理和日终核算。</li>
        <li>设计分页并发核对任务，先过滤近期活跃借据再关联 LA/LC 多表数据；分层执行表内自洽、跨表期次/交易和跨系统金额校验，约 5 分钟完成万级记录核对，并将异常自动落库、告警。</li>
      </ul>
    </td>
    <td valign="top" width="50%">
      <strong><img src="assets/oppo.png" height="20" alt="OPPO" /> OPPO </strong><br>
      <sub>终端 SDK 开发 · 深圳 · 2025.06–2025.09</sub>
      <ul>
        <li>以 Intent-Filter 扫描替代组件名匹配，解决第三方二次开发导致的 SDK 组件识别失效，覆盖 50+ 头部 App 和系统应用。</li>
        <li>定位并修复 Push Demo 多线程管理不当造成的网络请求堆积，同时封装调试接口以缩短第三方接入链路。</li>
      </ul>
    </td>
  </tr>
</table>

<details>
  <summary><strong>更早经历：金机智能装备 · 工业软件开发</strong></summary>
  <br>
  基于 JavaFX 与 Apache POI 开发图纸自动分类、打包和检索工具，将流程耗时缩减 80%；参与 Java → Kotlin 迁移，并使用 C++ 开发 SolidWorks 图纸检测插件。
</details>



<!-- ═══════════════════════════════════════════════════ -->
<!-- 精选项目 -->
<!-- ═══════════════════════════════════════════════════ -->

## 🚀 Mod项目

<table>
<tr>
<td width="50%" valign="top">

### Dynamic Shader

> 基于 HLSL 开发的自定义 Shader，为《星露谷物语》实现 **HD2D 风格** 渲染。

![Downloads](https://img.shields.io/badge/下载量-155,800+-6366F1?style=for-the-badge)
![Endorsements](https://img.shields.io/badge/推荐数-500+-818CF8?style=for-the-badge)


- 通过 **Harmony** 重排游戏渲染管线并注入顶点/像素着色器，实现 3D 投影模拟、接触硬化阴影、环境光色相偏移与移轴效果
- 构建 GPU 加速的双缓冲阴影收集与 RenderTarget 预渲染链路；使用 LUT、分离卷积、Dual Kawase 与降采样降低约 **87%** 模糊计算复杂度，缓存有效像素轮廓减少约 **80%** Alpha Clip 采样耗时
- 基于 **Intel GPA** 帧分析重排渲染顺序、复用 RenderTarget 并按纹理分类批处理，降低约 **72% XVE Stall** 和 **82% Draw Call**；使用等值数学计算替代 Shader 分支以提高 GPU 并行度

`HLSL` `GPU Batching` `Harmony` `Shader`

</td>
<td width="50%" valign="top">

### BetterBuildingUpgrades

> 使用 Harmony + SMAPI 框架扩展《星露谷物语》核心方法的游戏模组。

![Downloads](https://img.shields.io/badge/下载量-12,700+-6366F1?style=for-the-badge)
![Endorsements](https://img.shields.io/badge/推荐数-190+-818CF8?style=for-the-badge)

- 使用 **Harmony Patch + 反射注入**扩展游戏核心方法，将建筑升级规则与原版流程解耦
- 处理多人模式下的状态同步与数据一致性边界，避免客户端间升级结果分叉
- 收敛大范围自动化逻辑中的重复扫描与计算，保持复杂存档下的帧率稳定

`C#` `SMAPI` `Harmony`

</td>
</tr>
</table>

<br>

<!-- ═══════════════════════════════════════════════════ -->
<!-- FOOTER -->
<!-- ═══════════════════════════════════════════════════ -->

<!-- ═══════════════════════════════════════════════════ -->
<!-- GITHUB 活跃度 -->
<!-- ═══════════════════════════════════════════════════ -->

<h2 align="center">📈 GitHub 活跃度</h2>

<div align="center">

![Streak](https://streak-stats.demolab.com?user=Nook001&theme=tokyonight&hide_border=true&background=0D1117&ring=6366F1&fire=818CF8&currStreakLabel=C9D1D9)

</div>

<!-- 活动图 -->
<div align="center">

![Activity Graph](https://github-readme-activity-graph.vercel.app/graph?username=Nook001&theme=tokyo-night&hide_border=true&bg_color=0D1117&color=6366F1&line=818CF8&point=C9D1D9&area=true&area_color=6366F1)

</div>

<br>

<!-- 访问量 -->
<div align="center">

![Profile Views](https://komarev.com/ghpvc/?username=Nook001&color=6366F1&style=flat-square&label=访问量)

</div>

![footer](https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,12,20&height=120&section=footer)
