# 20 · Tools & Projects Ecosystem

Open-source projects around Suno, songwriting, and AI music. Stars and last-push dates are from a GitHub survey on 2026-10-07; "stale" means no commits for a year or more.

## 1. Suno API clients, CLIs & MCP servers

All unofficial. They wrap paid relay endpoints (sunoapi.org and similar) or reverse-engineered cookies, break when Suno changes, and carry ToS risk. High stars do not mean maintained.

| Tool | What it does | URL |
|---|---|---|
| gcui-art/suno-api (TS, 3251★) | The reference unofficial Suno API: OpenAI-compatible endpoints for GPTs and agents, hosted demo. Push 2026-03. | https://github.com/gcui-art/suno-api |
| gochendong/suno-api (Python, 88) | Actively updated Python API client (2026-05). | https://github.com/gochendong/suno-api |
| paperfoot/suno-cli (Rust, 55) | Terminal client for v5.5/v6: style tags, exclude tags, vocal control, resume, download (2026-09). | https://github.com/paperfoot/suno-cli |
| slauger/suno-cli (Python, 15) | Batch generation with ID3 tagging and cover art (2026-09). | https://github.com/slauger/suno-cli |
| worthable/suno-sdk (TS, 13) | npm client, package `suno-api` v0.9.3: generate, extend, concat, lyrics. | https://github.com/worthable/suno-sdk |
| AceDataCloud/SunoMCP (62) | MCP for generation, lyrics, covers; PyPI `mcp-suno`. Most active Suno MCP (2026-10). Smaller: CodeKeanu/suno-mcp (14★, https://github.com/CodeKeanu/suno-mcp). | https://github.com/AceDataCloud/SunoMCP |
| apinetwork/piapi-mcp-server (75) | Aggregator MCP covering Suno plus other media via PiAPI (2026-09). | https://github.com/apinetwork/piapi-mcp-server |
| joeseesun/qiaomu-suno-master (Python, 71) | Agent-oriented: song idea to Suno-ready lyrics and style tags (2026-06). | https://github.com/joeseesun/qiaomu-suno-master |
| Stale but famous (all at github.com/, abandoned 2024-03 to 2025-04) | SunoAI-API/Suno-API (Python, 1810★), yihong0618/SunoSongsCreator (365★), wlhtea/Suno2openai (275★), disingn/sunotoapi (Go, 186★), Suno-API/Suno-API (Go, 157★), Malith-Rukshan/Suno-API (PyPI `SunoAI`, 128★). | (owner/repo) |
| Backup tooling | danny-englander/suno-ai-downloader (40★) fetches your songs with metadata: https://github.com/danny-englander/suno-ai-downloader | (inline) |

For Udio: flowese/UdioWrapper (Python, 181★), the main wrapper, stale since 2024-07 (https://github.com/flowese/UdioWrapper).

## 2. Prompt, lyric & agent-skill tooling

### Prompt libraries, references, generators

| Tool | What it does | URL |
|---|---|---|
| naqashmunir21/awesome-suno-prompts (97) | 1000+ style prompts by genre, updated for v6 (2026-10). | https://github.com/naqashmunir21/awesome-suno-prompts |
| stayen/suno-reference (71) | Formal meta-tag taxonomy, templates, DDEX provenance. Closest to a canonical tag reference (2025-12). | https://github.com/stayen/suno-reference |
| eas4ai/suno_ai_meta_tags_guide (70) | "Complete Meta Tags Guide" by @stonedoubt: genre, mood, instrument, structure tags (2025-12). | https://github.com/eas4ai/suno_ai_meta_tags_guide |
| mttkllr/suno-field-guide (23) | Explanatory guide: prompt processing, meta-tag syntax, structure, mastering (2026-06). | https://github.com/mttkllr/suno-field-guide |
| daveshap/suno (140) | Early Suno prompts for chatbots like Claude. Predates v4/v5 syntax, stale 2024-11. | https://github.com/daveshap/suno |
| ddv1982/suno-prompting (21) | Desktop app (Bun/Tauri): plain-English idea to v5-ready prompt (2026-04). | https://github.com/ddv1982/suno-prompting |
| sanic732/SunoForge (15) | 12-file prompt pack for chat assistants; targets Suno v5.5, Lyria 3, Flow Music, ElevenMusic (2026-09). | https://github.com/sanic732/SunoForge |

### Agent skills (Claude Code / agentskills.io style)

| Tool | What it does | URL |
|---|---|---|
| bitwize-music-studio/claude-ai-music-skills (536, CC0) | Most complete Suno skill ecosystem: concept, research, lyrics, Suno prompt, QC, mastering, promo. Ships `suno-engineer`, `lyric-writer`, `genre-creator` skills plus a genre/artist knowledge base (2026-09). | https://github.com/bitwize-music-studio/claude-ai-music-skills |
| jtydhr88/lyric-writing-skills (98) | 18 skills from 29 songwriting books plus Sondheim analysis; LYR-SPEC spec output. Multi-language (2026-09). | https://github.com/jtydhr88/lyric-writing-skills |
| NousResearch/hermes-agent skill `songwriting-and-ai-music` (repo 251.7k, MIT) | Songwriting craft plus Suno prompt patterns; triggers on "suno prompt" and "parody". | https://github.com/NousResearch/hermes-agent/blob/main/skills/creative/songwriting-and-ai-music/SKILL.md |
| joeseesun/music-genre-finder (182) | 5947 RateYourMusic genres in 49 categories as a Claude Code skill (2026-01). | https://github.com/joeseesun/music-genre-finder |
| AgriciDaniel/claude-music (66) | Claude Code driving ACE-Step 1.5 as a local studio, about 15 s per song (2026-08). | https://github.com/AgriciDaniel/claude-music |
| nwp/suno-song-creator-plugin (43, MIT) | Claude Code plugin: research-driven systematic Suno prompt creation with sub-agents (2026-01). | https://github.com/nwp/suno-song-creator-plugin |
| NuNaught/suno-songwriting-skill (28, Apache-2.0) | Suno-ready lyrics, style prompts, vocal direction, translation (2026-05). | https://github.com/NuNaught/suno-songwriting-skill |

Prompt-format references: lobehub/lobe-chat-agents encodes Suno section tags and the 120-char style limit in agent `systemRole` JSON (https://github.com/lobehub/lobe-chat-agents); nexu-io/open-design has a `plugin.v1.json` schema routing music to Suno V5, Udio, or Lyria (https://github.com/nexu-io/open-design/blob/main/plugins/_official/examples/audio-jingle/open-design.json); vllm-omni documents the MiniMax Music 3 contract: section-tagged lyrics plus style instruction (https://github.com/vllm-project/vllm-omni/blob/main/recipes/MiniMaxAI/MiniMax-Music3.md). No standard Suno prompt schema exists yet. Vendor skills: MiniMax-AI/skills (`minimax-music-guide.md`, repo 13.7k★) and ace-step/ACE-Step-1.5 (`.claude/skills/acestep`).

## 3. MIR, audio, theory & composition libraries

| Tool | What it does | URL |
|---|---|---|
| kennethreitz/pytheory (Python, 1653) | "Music theory for humans": tones, scales, chords, progressions (2026-10). | https://github.com/kennethreitz/pytheory |
| gciruelos/musthe (Python, 361) | Theory primitives: notes, intervals, scales, chords. Slow since 2024-07. | https://github.com/gciruelos/musthe |
| emo-eth/Phyme (Python, 69) | Rhyming dictionary: perfect and multisyllabic rhymes (2026-05). | https://github.com/emo-eth/Phyme |
| hlorenzi/theorytracker (141) | Browser songwriting app (WebAudio) with multitrack editing and chord analysis (2026-01). | https://github.com/hlorenzi/theorytracker |
| JuzzyDee/audio-analyzer-rs (Rust, 63) | Audio-analysis MCP: spectral, harmonic, rhythm. Lets an agent "listen" for QA loops (2026-03). | https://github.com/JuzzyDee/audio-analyzer-rs |
| tubone24/midi-mcp-server (54) | MCP generating MIDI from JSON, piano-roll preview (2026-04). | https://github.com/tubone24/midi-mcp-server |
| ghchen99/mcp-musescore (107) | MCP control of MuseScore: compose, edit, add lyrics (2026-10). | https://github.com/ghchen99/mcp-musescore |
| TwelveTake-Studios/reaper-mcp (73) | MCP for the REAPER DAW, 179 tools: mixing, MIDI (2026-09). | https://github.com/TwelveTake-Studios/reaper-mcp |
| williamzujkowski/live-coding-music-mcp (242) | MCP for live coding in Strudel.cc; best-maintained music MCP (2026-09). | https://github.com/williamzujkowski/live-coding-music-mcp |
| Agentic composition | to-the-sun/amanuensis (50★, automated songwriting/recording, https://github.com/to-the-sun/amanuensis). | (inline) |

## 4. Datasets

| Dataset | What it gives you | URL |
|---|---|---|
| Chordonomicon (168) | 666,000+ chord progressions tagged with structure, genre, date (2026-05). | https://github.com/spyroskantarelis/chordonomicon |
| ChoCo (113) | Unified chord corpus with knowledge-graph workflow (Nature Sci Data 2023) (2025-05). | https://github.com/smashub/choco |
| McGill Billboard | Canonical Billboard chord annotations. Mirror: boomerr1/The-McGill-Billboard-Project (9★). | https://github.com/boomerr1/The-McGill-Billboard-Project |
| Hooktheory dump (10) | Key, mode, relative chords and notes; 2017 snapshot. | https://github.com/owencm/hooktheory-data |
| Lakh MIDI (craffel/midi-dataset, 177) | Canonical 176,581 MIDI with matching code; data still standard. HF chords extract: ohollo/lmd_chords. | https://github.com/craffel/midi-dataset |
| GigaMIDI (94) | 2.1M+ MIDI files with loop detection (2026-02). | https://github.com/Metacreation-Lab/GigaMIDI-Dataset |
| Aria-MIDI (101) | 1.18M solo-piano MIDI transcriptions (2025-06). | https://github.com/loubbrad/aria-midi |
| MidiCaps (86) | Caption-annotated MIDI: text-to-MIDI training pairs (2024-07). | https://github.com/AMAAI-Lab/MidiCaps |
| DALI (382) | Aligned audio, lyrics, vocal notes; ISMIR 2018 (2020). | https://github.com/gabolsgabs/DALI |
| Lyrics corpora | musiXmatch: MSD lyrics bag-of-words (http://millionsongdataset.com/musixmatch/); Genius Song Lyrics HF: 2.76M rows with language tags (https://huggingface.co/datasets/sebastiandizon/genius-song-lyrics). | (inline) |
| Song Describer (178) | ~1.1k audio captions over 706 tracks: caption-audio pairs (2023-12). | https://github.com/mulab-mir/song-describer-dataset |
| ccmusic song_structure (HF) | 300 pop songs with structural section labels; one of the few direct structure datasets. | https://huggingface.co/datasets/ccmusic-database/song_structure |

## 5. Other AI music generators (Suno alternatives)

| Tool | What it does | URL |
|---|---|---|
| ace-step/ACE-Step-1.5 (13,143) | Leading open music model: caption plus lyrics, BPM and duration control, first-party agent skill (2026-10). | https://github.com/ace-step/ACE-Step-1.5 |
| multimodal-art-projection/YuE (10.9k) | Open lyrics-to-song model (YuE2), active. | https://github.com/multimodal-art-projection/YuE |
| gabotechs/MusicGPT (1459) | Local text-to-music in Rust; stale 2025-02. | https://github.com/gabotechs/MusicGPT |

## 6. Awesome lists & learning resources

| Resource | What it covers | URL |
|---|---|---|
| Curated-Awesome-Lists/awesome-ai-music-generation (499) | Broad AI-music resource list (2026-09). | https://github.com/Curated-Awesome-Lists/awesome-ai-music-generation |
| Zizwar/Awesome-Suno (73) | Suno projects by language: Python, TS, Go, C++, C#, PHP, Dart (2026-09). | https://github.com/Zizwar/Awesome-Suno |
| zoejane/awesome-music-programming (155) | Music-programming languages and libraries (2026-09). | https://github.com/zoejane/awesome-music-programming |
| suno-ai-farm/awesome-ai-music-tools (9) | Directory: generation, lyrics, stems, mastering (2026-07). | https://github.com/suno-ai-farm/awesome-ai-music-tools |
| yzfly/awesome-music-prompts (51) | Prompts for music generation across models (2026-09). | https://github.com/yzfly/awesome-music-prompts |
| theelderemo/ai-audio-tools (24) | AI audio tool directory (2026-10). | https://github.com/theelderemo/ai-audio-tools |

Non-repo guides: Blake Crosley's Suno tags/meta-tags guide (https://blakecrosley.com/guides/suno); SunoArt meta tags encyclopedia (https://docs.sunoai.art/professional-techniques/prompt-engineering/meta-tags-encyclopedia); Stability AI's Stable Audio 3 prompting guide (https://github.com/Stability-AI/stable-audio-3/blob/main/docs/guides/prompting.md); Google's Lyria 3 prompting guide (https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-lyria-3-pro).

## Recommendations

1. **Prompting knowledge:** stayen/suno-reference and mttkllr/suno-field-guide for the mental model and tag syntax, then naqashmunir21/awesome-suno-prompts for genre styles.
2. **Skill design:** bitwize-music-studio/claude-ai-music-skills is the best working reference for a full Suno pipeline (CC0, reusable); jtydhr88/lyric-writing-skills is the deepest lyric-craft library; the hermes skill shows a minimal validated version.
3. **Programmatic generation:** AceDataCloud/SunoMCP for MCP agents, gcui-art/suno-api for HTTP. Avoid the 1000+ star repos (SunoAI-API, yihong0618, Malith-Rukshan): abandoned, Suno changed since.
4. **Data grounding:** Chordonomicon for progressions with structure labels, ccmusic song_structure for section layouts, Song Describer for caption examples.
5. **Self-hosted generation:** ACE-Step-1.5, driven through AgriciDaniel/claude-music, avoids reverse-engineered APIs entirely.

## Sources

GitHub REST search plus README fetches (2026-10-07), plus 30 SERPER/EXA web queries. Key URLs, deduped and grouped; every catalog row above also carries its URL inline.

- API/CLI/MCP: https://github.com/gcui-art/suno-api, https://github.com/AceDataCloud/SunoMCP
- Prompts: https://github.com/naqashmunir21/awesome-suno-prompts, https://github.com/stayen/suno-reference, https://github.com/mttkllr/suno-field-guide
- Skills: https://github.com/bitwize-music-studio/claude-ai-music-skills, https://github.com/jtydhr88/lyric-writing-skills, https://github.com/NousResearch/hermes-agent/blob/main/skills/creative/songwriting-and-ai-music/SKILL.md
- Formats: https://github.com/lobehub/lobe-chat-agents, https://github.com/vllm-project/vllm-omni/blob/main/recipes/MiniMaxAI/MiniMax-Music3.md
- Datasets: https://github.com/spyroskantarelis/chordonomicon, https://github.com/craffel/midi-dataset, https://huggingface.co/datasets/ccmusic-database/song_structure
- Alternatives: https://github.com/ace-step/ACE-Step-1.5, https://github.com/multimodal-art-projection/YuE
- Guides: https://blakecrosley.com/guides/suno, https://docs.sunoai.art/professional-techniques/prompt-engineering/meta-tags-encyclopedia, https://github.com/Stability-AI/stable-audio-3/blob/main/docs/guides/prompting.md, https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-lyria-3-pro
