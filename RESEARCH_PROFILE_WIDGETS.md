# GitHub Profile README — Visual Widget & Tool Research

> Comprehensive catalog of the most popular tools, services, and widgets for creating rich GitHub profile READMEs with cards, charts, graphs, streak counters, activity graphs, skill icons, and other visual elements.

---

## Table of Contents

1. [Stats Cards](#1-stats-cards)
2. [Streak Stats](#2-streak-stats)
3. [Top Languages Card (with Ring/Donut/Pie Charts)](#3-top-languages-card)
4. [GitHub Profile Trophy](#4-github-profile-trophy)
5. [Activity Graph](#5-activity-graph)
6. [Snake Animation](#6-snake-animation)
7. [Skill / Tech Icons](#7-skill--tech-icons)
8. [Shields.io Badges](#8-shieldsio-badges)
9. [Typing SVG Animation](#9-typing-svg-animation)
10. [Capsule Render (Header/Footer Banners)](#10-capsule-render)
11. [Profile Views Counter](#11-profile-views-counter)
12. [Spotify / Music Widgets](#12-spotify--music-widgets)
13. [WakaTime Coding Stats](#13-wakatime-coding-stats)
14. [Summary Cards](#14-summary-cards)
15. [Metrics (lowlighter/metrics)](#15-metrics)
16. [Social / Connect Badges](#16-social--connect-badges)
17. [Misc / Other Widgets](#17-misc--other-widgets)

---

## 1. Stats Cards

### GitHub Readme Stats
| Field | Details |
|-------|---------|
| **What it does** | Dynamically generated GitHub stats card showing stars, commits, PRs, issues, contributions, and a rank circle/ring chart. Also provides repo pin cards, gist cards, and WakaTime cards. |
| **Stars** | ⭐ 78.6k |
| **Repo** | https://github.com/anuraghazra/github-readme-stats |
| **Service URL** | https://github-readme-stats.vercel.app |
| **Key Features** | Rank ring chart, 40+ themes, gradient backgrounds, locale support, responsive dark/light mode, donut/pie/compact layouts for languages |

#### Embed Code — Stats Card
```md
[![Anurag's GitHub stats](https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=radical)](https://github.com/anuraghazra/github-readme-stats)
```

#### Embed Code — Top Languages (default bar layout)
```md
[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=compact)](https://github.com/anuraghazra/github-readme-stats)
```

#### Embed Code — Repo Pin Card
```md
[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=YOUR_USERNAME&repo=REPO_NAME)](https://github.com/YOUR_USERNAME/REPO_NAME)
```

#### Key Parameters
| Param | Description |
|-------|-------------|
| `username` | GitHub username (required) |
| `show_icons` | Show icons (true/false) |
| `theme` | Theme name (radical, tokyonight, dark, dracula, etc.) |
| `hide` | Hide specific stats: `stars,commits,prs,issues,contribs` |
| `show` | Show additional stats: `reviews,discussions_started,prs_merged,prs_merged_percentage` |
| `rank_icon` | `github`, `percentile`, or `default` |
| `include_all_commits` | Count all commits, not just current year |
| `ring_color` | Custom hex color for rank circle |

---

## 2. Streak Stats

### GitHub Readme Streak Stats
| Field | Details |
|-------|---------|
| **What it does** | Displays total contributions, current streak, and longest streak with a fire ring animation. |
| **Stars** | ⭐ 6.6k |
| **Repo** | https://github.com/DenverCoder1/github-readme-streak-stats |
| **Service URL** | https://streak-stats.demolab.com |
| **Demo Site** | https://streak-stats.demolab.com/demo/ |
| **Key Features** | 50+ themes, 60+ locales, daily/weekly modes, exclude specific days, customizable colors for ring/fire/numbers/labels |

#### Embed Code
```md
[![GitHub Streak](https://streak-stats.demolab.com/?user=YOUR_USERNAME&theme=dark)](https://git.io/streak-stats)
```

#### Key Parameters
| Param | Description |
|-------|-------------|
| `user` | GitHub username (required) |
| `theme` | Theme name (dark, radical, highcontrast, etc.) |
| `hide_border` | true/false |
| `ring` | Ring color (hex without #) |
| `fire` | Fire color (hex without #) |
| `mode` | `daily` or `weekly` |
| `exclude_days` | e.g. `Sun,Sat` |
| `date_format` | PHP date format like `M j[, Y]` |
| `locale` | ISO code e.g. `zh_Hans`, `ja`, `ko` |
| `card_width` | Width in px (default 495) |
| `hide_total_contributions` | true/false |
| `hide_current_streak` | true/false |
| `hide_longest_streak` | true/false |

---

## 3. Top Languages Card

### GitHub Readme Stats — Top Languages (with Ring/Donut/Pie Charts)
| Field | Details |
|-------|---------|
| **What it does** | Shows most-used programming languages in circular donut chart, pie chart, compact bar, or vertical donut layout. |
| **Repo** | (Same as Stats Cards above) https://github.com/anuraghazra/github-readme-stats |

#### Layout Options
| Layout | Description |
|--------|-------------|
| `normal` | Default progress bars |
| `compact` | Compact horizontal bars |
| `donut` | **Circular ring/donut chart** |
| `donut-vertical` | Vertical donut chart |
| `pie` | **Pie chart** |

#### Embed Code — Donut Chart
```md
[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=donut&theme=radical)](https://github.com/anuraghazra/github-readme-stats)
```

#### Embed Code — Pie Chart
```md
[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=pie&theme=radical)](https://github.com/anuraghazra/github-readme-stats)
```

#### Key Parameters
| Param | Description |
|-------|-------------|
| `layout` | `normal`, `compact`, `donut`, `donut-vertical`, `pie` |
| `langs_count` | Number of languages (1-20) |
| `hide` | Hide specific languages: `html,css` |
| `exclude_repo` | Exclude repos: `repo1,repo2` |
| `size_weight` / `count_weight` | Weight algorithm (recommended: 0.5/0.5) |
| `hide_progress` | Hide bars and percentages |

---

## 4. GitHub Profile Trophy

### github-profile-trophy
| Field | Details |
|-------|---------|
| **What it does** | Dynamically generated trophy cards for GitHub stats (Stars, Commits, PRs, Issues, Followers, Repos, etc.) with ranks SSS → C. |
| **Stars** | ⭐ 6.4k |
| **Repo** | https://github.com/ryo-ma/github-profile-trophy |
| **Service URL** | https://github-profile-trophy.vercel.app |
| **Key Features** | 24 themes, rank filtering, row/column layout control, transparent backgrounds, margin controls |

#### Embed Code
```md
[![trophy](https://github-profile-trophy.vercel.app/?username=YOUR_USERNAME&theme=onedark&column=7)](https://github.com/ryo-ma/github-profile-trophy)
```

#### Key Parameters
| Param | Description |
|-------|-------------|
| `username` | GitHub username (required) |
| `theme` | `flat`, `onedark`, `dracula`, `gruvbox`, `tokyonight`, `nord`, `radical`, `discord`, `matrix`, etc. |
| `column` | Max columns (default 6, use -1 for adaptive) |
| `row` | Max rows (default 3) |
| `rank` | Filter by rank: `S,AAA,AA,A` or exclude: `-C,-B` |
| `title` | Filter trophies: `Stars,Followers` or exclude: `-Stars` |
| `margin-w` / `margin-h` | Margin between trophies |
| `no-bg` | Transparent background (true/false) |
| `no-frame` | Hide frames (true/false) |

---

## 5. Activity Graph

### GitHub Readme Activity Graph
| Field | Details |
|-------|---------|
| **What it does** | Dynamically generated contribution activity graph (line chart) showing the last 31 days of GitHub activity. |
| **Stars** | ⭐ 2.2k |
| **Repo** | https://github.com/Ashutosh00710/github-readme-activity-graph |
| **Service URL** | https://github-readme-activity-graph.vercel.app |
| **Key Features** | 11+ themes, customizable colors for line/points/area, adjustable height, selectable date range (1-90 days), area fill, grid control |

#### Embed Code
```md
[![Activity Graph](https://github-readme-activity-graph.vercel.app/graph?username=YOUR_USERNAME&theme=tokyo-night)](https://github.com/ashutosh00710/github-readme-activity-graph)
```

#### Key Parameters
| Param | Description |
|-------|-------------|
| `username` | GitHub username (required) |
| `theme` | `react-dark`, `tokyo-night`, `github-compact`, `dracula`, etc. |
| `bg_color` | Background color (hex without #) |
| `color` | Text color |
| `line` | Line color |
| `point` | Point color |
| `area` | Show area fill (true/false) |
| `area_color` | Area fill color |
| `hide_border` | true/false |
| `hide_title` | true/false |
| `custom_title` | Custom title (use %20 for spaces) |
| `height` | Graph height (200-600) |
| `days` | Days to show (1-90, recommended <40) |
| `radius` | Border radius (0-16) |

---

## 6. Snake Animation

### Platane/snk (Contribution Snake)
| Field | Details |
|-------|---------|
| **What it does** | Generates a snake game animation from your GitHub contribution graph. The snake "eats" contribution cells in an orderly fashion. Outputs SVG or GIF. |
| **Stars** | ⭐ 5.6k |
| **Repo** | https://github.com/Platane/snk |
| **Marketplace** | https://github.com/marketplace/actions/generate-snake-game-from-github-contribution-grid |
| **Key Features** | SVG and GIF output, customizable colors, dark mode support, GitHub Actions integration, multiple color palettes |

#### Setup (GitHub Action)
Create `.github/workflows/snake.yml`:
```yaml
name: Generate Snake

on:
  schedule:
    - cron: "0 0 * * *"
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: Platane/snk@v3
        with:
          github_user_name: ${{ github.repository_owner }}
          outputs: |
            dist/github-snake.svg
            dist/github-snake-dark.svg?palette=github-dark

      - uses: crazy-max/ghaction-github-pages@v3.1.0
        with:
          target_branch: output
          build_dir: dist
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

#### Embed Code (in README after action runs)
```md
![Snake animation](https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_USERNAME/output/github-snake-dark.svg)
```

#### Dark Mode Support
```html
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_USERNAME/output/github-snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_USERNAME/output/github-snake.svg" />
  <img alt="github-snake" src="https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_USERNAME/output/github-snake.svg" />
</picture>
```

---

## 7. Skill / Tech Icons

### Skill Icons (tandpfun/skill-icons)
| Field | Details |
|-------|---------|
| **What it does** | Beautiful, consistent skill/tech stack icons. Much prettier than shields.io badges. 200+ icons available including languages, frameworks, tools, platforms, and services. |
| **Stars** | ⭐ 11.7k |
| **Repo** | https://github.com/tandpfun/skill-icons |
| **Service URL** | https://skillicons.dev |
| **Key Features** | Dark/light themes, configurable icons per line, auto-resizing SVG, Cloudflare Workers powered |

#### Embed Code
```md
[![My Skills](https://skillicons.dev/icons?i=java,kotlin,spring,py,go,rust,docker,kubernetes,aws,git&theme=dark)](https://skillicons.dev)
```

#### With Custom Per-Line Count
```md
[![My Skills](https://skillicons.dev/icons?i=java,kotlin,spring,py,go,rust,docker,kubernetes,aws,git&perline=5)](https://skillicons.dev)
```

#### Centered
```html
<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=git,kubernetes,docker,cpp,java,py" />
  </a>
</p>
```

#### Key Parameters
| Param | Description |
|-------|-------------|
| `i` | Comma-separated list of icon IDs (required). See full list at repo. |
| `theme` | `dark` (default) or `light` |
| `perline` | Icons per line (1-50, default 15) |

#### Popular Icon IDs
`js`, `ts`, `py`, `java`, `cpp`, `c`, `cs`, `go`, `rust`, `kotlin`, `swift`, `dart`, `ruby`, `php`, `html`, `css`, `react`, `vue`, `angular`, `svelte`, `nextjs`, `nodejs`, `spring`, `django`, `flask`, `fastapi`, `express`, `docker`, `kubernetes`, `aws`, `gcp`, `azure`, `git`, `github`, `gitlab`, `vscode`, `linux`, `mongodb`, `postgres`, `mysql`, `redis`, `firebase`, `tensorflow`, `pytorch`, `figma`, `blender`, `unity`, `unreal`, `godot`, `tailwind`, `bootstrap`, `sass`, `webpack`, `vite`

---

## 8. Shields.io Badges

### Shields.io
| Field | Details |
|-------|---------|
| **What it does** | The original badge service. Concise, consistent SVG badges for any metric — CI status, version, downloads, coverage, social, custom text, etc. |
| **Stars** | ⭐ 26.2k |
| **Repo** | https://github.com/badges/shields |
| **Service URL** | https://shields.io |
| **Key Features** | Thousands of integrations (npm, PyPI, Docker Hub, etc.), static and dynamic badges, multiple styles (flat, flat-square, plastic, for-the-badge, social) |

#### Embed Code — Static Badge
```md
![Badge](https://img.shields.io/badge/Label-Message-color?style=for-the-badge&logo=logoname&logoColor=white)
```

#### Embed Code — Social Style
```md
![GitHub followers](https://img.shields.io/github/followers/YOUR_USERNAME?style=social)
![GitHub stars](https://img.shields.io/github/stars/YOUR_USERNAME/REPO?style=social)
```

#### Common Badge Examples
```md
<!-- Tech stack -->
![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Go](https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazonwebservices&logoColor=white)
```

#### Styles Available
| Style | Appearance |
|-------|------------|
| `flat` | Default, clean look |
| `flat-square` | Square corners |
| `plastic` | 3D gradient look |
| `for-the-badge` | Larger, bolder, uppercase |
| `social` | GitHub-social style |

---

## 9. Typing SVG Animation

### Readme Typing SVG
| Field | Details |
|-------|---------|
| **What it does** | Dynamically generated SVG that shows a typing/deleting text animation. Perfect for profile headlines. |
| **Stars** | ⭐ 8.4k |
| **Repo** | https://github.com/DenverCoder1/readme-typing-svg |
| **Service URL** | https://readme-typing-svg.demolab.com |
| **Demo/Generator** | https://readme-typing-svg.demolab.com/demo/ |
| **Key Features** | Multiple lines, custom fonts (Google Fonts), configurable speed, colors, sizes, center alignment, multiline mode |

#### Embed Code
```md
[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1000&color=6366F1&center=true&vCenter=true&width=520&lines=First+line+of+text;Second+line;Third+line)](https://git.io/typing-svg)
```

#### Key Parameters
| Param | Description |
|-------|-------------|
| `lines` | Text lines separated by `;`, spaces as `+` or `%20` |
| `font` | Google Font name (default: monospace) |
| `size` | Font size in px (default: 20) |
| `color` | Hex color without # (default: 36BCF7) |
| `center` | Center text (true/false) |
| `vCenter` | Vertically center (true/false) |
| `width` | SVG width (default: 400) |
| `height` | SVG height (default: 50) |
| `duration` | Typing duration in ms (default: 5000) |
| `pause` | Pause between lines in ms (default: 0) |
| `repeat` | Loop (true/false, default: true) |
| `multiline` | Wrap lines instead of delete/retype (true/false) |

---

## 10. Capsule Render

### capsule-render (Header/Footer Banners)
| Field | Details |
|-------|---------|
| **What it does** | Dynamic, colorful header/footer SVG banners for your README. Supports wave, egg, shark, slice, venom, speech bubble, blur, and more shape types with text overlays and animations. |
| **Stars** | ⭐ 1.6k |
| **Repo** | https://github.com/kyechan99/capsule-render |
| **Service URL** | https://capsule-render.vercel.app |
| **Generator** | https://capsule-render.vercel.app (interactive) |
| **Key Features** | 13 shape types, auto/random/gradient colors, text animations (fadeIn, scaleIn, blink, twinkling), header/footer sections, stroke effects, theme support |

#### Embed Code — Header
```md
![header](https://capsule-render.vercel.app/api?type=waving&color=gradient&height=250&section=header&text=Your%20Name&fontSize=50&fontColor=fff&animation=fadeIn&fontAlignY=35&desc=Your%20Tagline&descSize=20&descAlignY=55)
```

#### Embed Code — Footer
```md
![footer](https://capsule-render.vercel.app/api?type=waving&color=gradient&height=120&section=footer)
```

#### Shape Types
`wave` (default), `egg`, `shark`, `slice`, `rect`, `soft`, `rounded`, `cylinder`, `waving`, `venom`, `speech`, `blur`, `transparent`

#### Key Parameters
| Param | Description |
|-------|-------------|
| `type` | Shape type (see above) |
| `color` | `auto`, `gradient`, `timeAuto`, `timeGradient`, `random`, or hex without # |
| `section` | `header` (default) or `footer` |
| `height` | Image height (default: 120) |
| `text` | Overlay text (use %20 for spaces, -nl- for newlines) |
| `fontSize` | Font size (default: 70) |
| `fontColor` | Text color hex without # |
| `animation` | `fadeIn`, `scaleIn`, `blink`, `blinking`, `twinkling` |
| `fontAlignY` | Vertical text position (0-100) |
| `desc` | Description text |
| `descSize` | Description font size |
| `reversal` | Flip image (true/false) |
| `theme` | Theme name (from github-readme-stats themes) |
| `stroke` | Text stroke color |
| `strokeWidth` | Stroke width |

---

## 11. Profile Views Counter

### GitHub Profile Views Counter
| Field | Details |
|-------|---------|
| **What it does** | Counts and displays how many times your GitHub profile has been viewed. Simple badge counter. |
| **Stars** | ⭐ 4.8k |
| **Repo** | https://github.com/antonkomarev/github-profile-views-counter |
| **Service URL** | https://komarev.com |
| **Key Features** | Multiple styles (flat, flat-square, plastic, for-the-badge, pixel/invisible), custom colors, custom labels, abbreviation mode |

#### Embed Code
```md
![Profile Views](https://komarev.com/ghpvc/?username=YOUR_USERNAME&color=blueviolet&style=flat-square)
```

#### Key Parameters
| Param | Description |
|-------|-------------|
| `username` | GitHub username (required) |
| `color` | Named color or hex without # (default: blue) |
| `style` | `flat`, `flat-square`, `plastic`, `for-the-badge`, `pixel` |
| `label` | Custom label text (use + for spaces) |
| `base` | Base number to add (for migration) |
| `abbreviated` | Abbreviate (12.3K instead of 12345) |

#### Named Colors
`brightgreen`, `green`, `yellow`, `yellowgreen`, `orange`, `red`, `blue`, `grey`, `lightgrey`, `blueviolet`

---

## 12. Spotify / Music Widgets

### A. spotify-github-profile (kittinan)
| Field | Details |
|-------|---------|
| **What it does** | Shows your currently playing Spotify track on your GitHub profile with album art, song name, and artist. |
| **Stars** | ⭐ 2.1k |
| **Repo** | https://github.com/kittinan/spotify-github-profile |
| **Service URL** | https://spotify-github-profile.kittinanx.com |
| **Key Features** | 6 themes (default, compact, natemoo-re, novatorem, karaoke, spotify-embed), explicit content filter |

#### Setup
1. Visit https://spotify-github-profile.kittinanx.com/api/login
2. Connect your Spotify account
3. Copy the generated markdown

#### Embed Code
```md
[![spotify-github-profile](https://spotify-github-profile.kittinanx.com/api/view?uid=YOUR_SPOTIFY_ID&cover_image=true&theme=default&show_offline=false&background_color=121212&interchange=false)](https://spotify-github-profile.kittinanx.com/api/view?uid=YOUR_SPOTIFY_ID&redirect=true)
```

### B. novatorem (Spotify Now Playing)
| Field | Details |
|-------|---------|
| **What it does** | Dynamic real-time Spotify "now playing" card with animated progress bar, album art, and Last.FM support. |
| **Stars** | ⭐ 728 |
| **Repo** | https://github.com/novatorem/novatorem |
| **Key Features** | Animated progress bar, marquee text, compact mode, Last.FM support, Vercel/Heroku/Docker deployment |

### C. spotify-recently-played-readme
| Field | Details |
|-------|---------|
| **What it does** | Shows your recently played Spotify tracks as a list. |
| **Repo** | https://github.com/JeffreyCA/spotify-recently-played-readme |

---

## 13. WakaTime Coding Stats

### GitHub Readme Stats — WakaTime Card
| Field | Details |
|-------|---------|
| **What it does** | Displays your WakaTime weekly coding stats (languages, time spent) as a card. |
| **Repo** | (Part of github-readme-stats) https://github.com/anuraghazra/github-readme-stats |
| **Requires** | Public WakaTime profile with public stats enabled |

#### Embed Code
```md
[![WakaTime stats](https://github-readme-stats.vercel.app/api/wakatime?username=YOUR_WAKATIME_USERNAME&layout=compact&theme=radical)](https://github.com/anuraghazra/github-readme-stats)
```

#### Key Parameters
| Param | Description |
|-------|-------------|
| `username` | WakaTime username (required) |
| `layout` | `default` or `compact` |
| `hide` | Hide languages |
| `langs_count` | Limit number of languages |
| `api_domain` | Use with Hakatime/Wakapi: `wakapi.dev` |
| `display_format` | `time` or `percent` |

---

## 14. Summary Cards

### github-profile-summary-cards
| Field | Details |
|-------|---------|
| **What it does** | Generates multiple summary cards: profile details, repos per language (pie chart), commit time distribution, productive time, and stats. Uses GitHub Actions. |
| **Stars** | ⭐ 2.5k+ |
| **Repo** | https://github.com/vn7n24fzkq/github-profile-summary-cards |
| **Key Features** | Multiple card types in one action, pie charts for languages, commit time heatmap, 15+ themes |

#### Setup (GitHub Action)
```yaml
- uses: vn7n24fzkq/github-profile-summary-cards@release
  env:
    GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
  with:
    USERNAME: ${{ github.repository_owner }}
    THEME: radical
```

#### Embed Code (after action runs)
```md
![](https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_USERNAME/master/profile-summary-card-output/radical/0-profile-details.svg)
![](https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_USERNAME/master/profile-summary-card-output/radical/1-repos-per-language.svg)
![](https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_USERNAME/master/profile-summary-card-output/radical/2-most-commit-language.svg)
![](https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_USERNAME/master/profile-summary-card-output/radical/3-stats.svg)
![](https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_USERNAME/master/profile-summary-card-output/radical/4-productive-time.svg)
```

---

## 15. Metrics (lowlighter/metrics)

### GitHub Metrics
| Field | Details |
|-------|---------|
| **What it does** | The most comprehensive and feature-rich profile infographic generator. 30+ plugins: languages, achievements, stars, habits, contributions calendar, isometric view, music, tweets, LeetCode, WakaTime, StackOverflow, and much more. |
| **Stars** | ⭐ 14k+ |
| **Repo** | https://github.com/lowlighter/metrics |
| **Service URL** | https://metrics.lecoq.io |
| **Key Features** | 30+ plugins, SVG/PNG/JSON output, GitHub Actions, highly customizable, supports third-party integrations |

#### Embed Code (via GitHub Actions)
```yaml
- uses: lowlighter/metrics@latest
  with:
    token: ${{ secrets.METRICS_TOKEN }}
    user: YOUR_USERNAME
    template: classic
    plugin_languages: yes
    plugin_languages_details: percentage
    plugin_isocalendar: yes
    plugin_achievements: yes
    plugin_habits: yes
```

#### Quick Embed (public instance)
```md
![Metrics](https://metrics.lecoq.io/YOUR_USERNAME?template=classic&languages=1&isocalendar=1)
```

#### Notable Plugins
- `plugin_languages` — Language usage with pie/donut charts
- `plugin_isocalendar` — Isometric contribution calendar
- `plugin_achievements` — GitHub achievements
- `plugin_habits` — Coding habits (active hours, languages)
- `plugin_stars` — Star history
- `plugin_music` — Spotify/Last.fm/Apple Music now playing
- `plugin_wakatime` — WakaTime integration
- `plugin_leetcode` — LeetCode stats
- `plugin_stackoverflow` — Stack Overflow stats
- `plugin_notable` — Contributions to notable repos

---

## 16. Social / Connect Badges

Using Shields.io badges with logos to create social link buttons:

```md
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/YOUR_USERNAME)
[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/YOUR_USERNAME)
[![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://youtube.com/c/YOUR_CHANNEL)
[![Discord](https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/YOUR_INVITE)
[![Dev.to](https://img.shields.io/badge/Dev.to-0A0A0A?style=for-the-badge&logo=devdotto&logoColor=white)](https://dev.to/YOUR_USERNAME)
[![Medium](https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@YOUR_USERNAME)
[![Stack Overflow](https://img.shields.io/badge/Stack_Overflow-FE7A16?style=for-the-badge&logo=stack-overflow&logoColor=white)](https://stackoverflow.com/users/YOUR_ID)
[![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/YOUR_USERNAME)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:your@email.com)
```

---

## 17. Misc / Other Widgets

### A. GitHub Readme Quotes
| Field | Details |
|-------|---------|
| **Repo** | https://github.com/PiyushSuthar/github-readme-quotes |
| **What** | Random dev/motivational quotes |

```md
[![Readme Quotes](https://quotes-github-readme.vercel.app/api?type=horizontal&theme=radical)](https://github.com/piyushsuthar/github-readme-quotes)
```

### B. GitHub Readme Jokes
| Field | Details |
|-------|---------|
| **Repo** | https://github.com/ABSphreak/readme-jokes |
| **What** | Random programming jokes |

```md
![Jokes Card](https://readme-jokes.vercel.app/api?theme=radical)
```

### C. GitHub Widgetbox
| Field | Details |
|-------|---------|
| **Repo** | https://github.com/Jurredr/github-widgetbox |
| **What** | Beautiful widget cards for skills, GitHub stats, and profile info |

```md
![](https://github-widgetbox.vercel.app/api/skills?names=java,python,go,docker,kubernetes&includeNames=true)
```

### D. GitHub Stats Terminal Style
| Field | Details |
|-------|---------|
| **Repo** | https://github.com/yogeshwaran01/github-stats-terminal-style |
| **What** | Terminal/console-style GitHub stats card |

### E. Socialify (repo social cards)
| Field | Details |
|-------|---------|
| **Repo** | https://github.com/wei/socialify |
| **Service** | https://socialify.git.ci |
| **What** | Generate beautiful social preview images for repos |

```md
![Socialify](https://socialify.git.ci/YOUR_USERNAME/REPO_NAME/image?description=1&font=Inter&language=1&pattern=Plus&theme=Dark)
```

### F. Markdown Badges Collection
| Field | Details |
|-------|---------|
| **Repo** | https://github.com/Ileriayo/markdown-badges |
| **What** | Comprehensive collection of copy-paste shields.io badges organized by category (languages, frameworks, tools, social, etc.) |
| **Stars** | ⭐ 14k+ |

---

## Quick Reference: Side-by-Side Layout

To display cards side by side on GitHub, use this pattern:

```html
<a href="https://github.com/anuraghazra/github-readme-stats">
  <img height=200 align="center" src="https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=radical" />
</a>
<a href="https://github.com/anuraghazra/github-readme-stats">
  <img height=200 align="center" src="https://github-readme-stats.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=donut&theme=radical&langs_count=8" />
</a>
```

---

## Quick Reference: Dark/Light Mode Support

### Method 1: GitHub `<picture>` element
```html
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&theme=dark" />
  <source media="(prefers-color-scheme: light)" srcset="https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&theme=default" />
  <img src="https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME" />
</picture>
```

### Method 2: GitHub theme context tags
```md
![Stats Dark](https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&theme=dark#gh-dark-mode-only)
![Stats Light](https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&theme=default#gh-light-mode-only)
```

---

## Summary Table

| # | Tool | Category | Stars | Repo |
|---|------|----------|-------|------|
| 1 | GitHub Readme Stats | Stats cards, lang charts, pins | 78.6k | [anuraghazra/github-readme-stats](https://github.com/anuraghazra/github-readme-stats) |
| 2 | GitHub Readme Streak Stats | Streak counter | 6.6k | [DenverCoder1/github-readme-streak-stats](https://github.com/DenverCoder1/github-readme-streak-stats) |
| 3 | GitHub Profile Trophy | Trophy cards | 6.4k | [ryo-ma/github-profile-trophy](https://github.com/ryo-ma/github-profile-trophy) |
| 4 | GitHub Readme Activity Graph | Contribution line graph | 2.2k | [Ashutosh00710/github-readme-activity-graph](https://github.com/Ashutosh00710/github-readme-activity-graph) |
| 5 | Contribution Snake (snk) | Snake animation | 5.6k | [Platane/snk](https://github.com/Platane/snk) |
| 6 | Skill Icons | Tech stack icons | 11.7k | [tandpfun/skill-icons](https://github.com/tandpfun/skill-icons) |
| 7 | Shields.io | Any badge/badge builder | 26.2k | [badges/shields](https://github.com/badges/shields) |
| 8 | Readme Typing SVG | Typing animation | 8.4k | [DenverCoder1/readme-typing-svg](https://github.com/DenverCoder1/readme-typing-svg) |
| 9 | Capsule Render | Header/footer banners | 1.6k | [kyechan99/capsule-render](https://github.com/kyechan99/capsule-render) |
| 10 | Profile Views Counter | View counter badge | 4.8k | [antonkomarev/github-profile-views-counter](https://github.com/antonkomarev/github-profile-views-counter) |
| 11 | Spotify GitHub Profile | Now playing card | 2.1k | [kittinan/spotify-github-profile](https://github.com/kittinan/spotify-github-profile) |
| 12 | Novatorem | Spotify now playing | 728 | [novatorem/novatorem](https://github.com/novatorem/novatorem) |
| 13 | GitHub Metrics | All-in-one infographics | 14k+ | [lowlighter/metrics](https://github.com/lowlighter/metrics) |
| 14 | Profile Summary Cards | Multi-card summary | 2.5k+ | [vn7n24fzkq/github-profile-summary-cards](https://github.com/vn7n24fzkq/github-profile-summary-cards) |
| 15 | Markdown Badges | Badge collection | 14k+ | [Ileriayo/markdown-badges](https://github.com/Ileriayo/markdown-badges) |
| 16 | GitHub Widgetbox | Skill/stats widgets | — | [Jurredr/github-widgetbox](https://github.com/Jurredr/github-widgetbox) |
| 17 | Socialify | Repo social cards | — | [wei/socialify](https://github.com/wei/socialify) |
