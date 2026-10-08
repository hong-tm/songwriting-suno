# Multilingual songwriting craft — timing, tone, rhyme, register (and Suno)

How lyric writing differs by language: what you count (stress, syllable, mora, tone), tone–melody interaction, rhyme conventions, structure/register expectations, and how to prompt Suno. Confidence flags: `HIGH` = peer-reviewed/primary, cross-checked; `MED` = reputable secondary; `LOW` = single practitioner/community source or inference.

## Summary table — how the writing differs by language

| Language | Timing/counting unit | Tone–melody? | Rhyme convention | Structure/register notes |
|---|---|---|---|---|
| English | Stress-timed; stressed syllables → strong beats | None (lexical stress) | Perfect/family/assonance; end-rhyme normative | Short stressed hooks; contracts |
| Mandarin | Syllable-counted + tonal (4 tones) | **Weak**: melody dominates; ~1/3 match `HIGH` | 押韵 / 十三辙 (13 rhyme classes) | Mandopop V–C; heavy EN code-switch |
| Cantonese | Syllable + tonal (6 tones/9 contours) | **Strict 協音**: tone mirrors melodic direction; 拗音 = "fake" | 押韻 secondary to tone fit | 填詞 = specialist craft; dense; EN loans |
| Japanese | **Mora-timed** (拍/haku): long vowel=2, ん=1, っ=1 | None (pitch accent) | Weak end-rhyme; mora count + vowel colour | Pre-chorus mandatory; katakana EN loans; kigo |
| Korean | Syllable-timed; **no word stress** | None | Loose end-rhyme; syllable count + hook | 반말 in intimacy songs; EN intra-sentential switching |
| Malay/Indonesian | Syllable-timed; not tonal | None | **Pantun a-b-a-b** (sampiran→isi) | Dangdut repetition; aku/saya split |
| Spanish | Syllable-timed; **sinalefa** merges vowels | None; lines end weak (llano) | **consonante vs asonante**; romance = octosílabo, even-line assonance | Gender agreement forced; reggaeton/Latin |
| French | Syllable-timed; e muet rules; caesura ≥9 syllables | None; group-final prominence | Masc./fem. endings alternate; plates/croisées/embrassées | Alexandrine 6+6; chanson |
| Portuguese (BR) | Syllable + speech accent ("métrica derramada") | None | Vowel-ending rhymes (‑ar/‑er/‑ir) cheap | MPB/bossa; EP vs BP vowel reduction |
| Hindi/Urdu | Stress-light, syllable-counted | None | तुकांत (tukant); ghazal qāfiya + radīf | **Mukhda + antara**; filmi register |
| Arabic | Stress-timed; quantitative feet (ʿarūḍ, 16 buḥūr) | None | **qāfiyah** + radīf; bayt = 2 hemistichs | Song = dialect (Egyptian/Levantine); tarab |
| Russian | Stress-timed; **free lexical stress**; count ictuses | None | Inflectional rhyme "too cheap"; exact + fuzzy/slant | Dolnik → accentual verse; rock-poetry register |
| Thai | 5 tones; tonal | Avoid contrary; modern match declining | Loose end-rhyme | — |
| Vietnamese | 6 tones; tonal | Avoid contrary; ~77% similar motion `HIGH` | End-rhyme | — |
| Afrobeats | Tonal substrates (Yoruba/Igbo) | Short speech↔song distance | Pidgin "freedom of rhyme" | 4-language code-switch per song |

Bedrock: stress-timed languages put stressed syllables on strong beats, unstressed never do; syllable-timed ones need near-exact line length; tonal languages follow "avoid contrary settings" — similar > oblique > contrary [Ladd & Kirby, `HIGH`].

## Per-language blocks

### English — stress-timed, stress-to-beat
- (a) Stress-timed; match stressed syllables to strong beats, keep unstressed off them `HIGH`.
- (b) Tone–melody: none (lexical stress instead).
- (c) Rhyme: perfect / family / assonance; assonance signals "unstable" meaning (Berklee/Pattison) `HIGH`.
- (d) Verse–chorus; English contracts, hooks can be brutally short `MED`.
- (e) Example: "Happy Birthday" name slot — trochee *Sú-san* fits; iamb *Su-zánne* lands unstressed -zanne on the downbeat and is judged wrong (repair: upbeat + melisma). Mis-setting: Handel's "and the dead shall be raised incorruptible."
- (f) Ladd & Kirby; Wikipedia *Lyric setting*; Berklee; Language Log.

### Mandarin Chinese (华语/Mandopop)
- (a) Syllable-counted; 4 tones + neutral.
- (b) Tone–melody: weak — "the tendency is to allow the overall melody to dominate"; only ~1/3 of syllables match tone; tone is a weak bias `MED/HIGH`.
- (c) 押韵; toolkit is 十三辙 (13 rhyme "ruts" — 中东辙, 人辰辙, 言前辙…) grouping finals by sound `MED`.
- (d) Mandopop verse–chorus; English hooks standard; bilingual singers mix EN/ZH intra-sententially `MED`.
- (e) Example: Frozen "Let it go" — literal 放手 fàng shǒu fails the rising melody; singable version is 随他吧 suí tā ba. Tone mismatch causes mishearing: 似在眼前 sì zài yǎn qián ("as if before my eyes") heard as 死在眼前 sǐ zài yǎn qián ("die before my eyes") `HIGH`.
- (f) GagaST (ACL 2022); Language Log; Kirby 2023; 十三辙 (zh.wikipedia/Baidu); Du 2023 HPU.
### Cantonese (Cantopop) — 協音 is the identity
- (a) Syllable-counted; 6 tones / 9 contours.
- (b) **Strict 協音 (ngam yam, "tone-fit")**: tone direction must mirror melodic direction; mismatch is 拗音 and instantly sounds "fake" to natives. Only ~1 in 4 characters fits any given note (fully 協音 7-word line ≈ odds 1/16384, mrpinyin) `HIGH`.
- (c) 押韻/轍 exists but tone-fit dominates.
- (d) 填詞 (lyric-fitting) is a specialist profession; literary register mixes with colloquial particles.
- (e) Example: 帝女花《香夭》first line — 簡譜 `3656536` = 落花滿天蔽月光 (數字歌 `2343423`); "You Raise Me Up"《仍然是祢》— `5-5-13` = `0043` = 誰人瞭解. Kirby: 眼中 ngaan23-zung55 (low→high) on a rising melody; 車內 ce55-noi22 (high→low) on a falling one. UBC corpus (105 award-winning songs, 2000–2020): >80% of tone/melody bigrams match, contrary near zero; Wong & Diehl >90%. "Fake Cantonese": cover of 花僮《笑纳》sings 西 sai as *si*, 瘦 sau as *sou*; native covers rewrite rather than re-pronounce.
- (f) note.com Hiepyam; mrpinyin; Lee 2023; Kirby 2023; ToneCraft.

### Japanese — mora-timed
- (a) Count **morae** (拍/haku), not syllables: long vowel = 2, ん = 1, っ = 1 `HIGH`.
- (b) Tone–melody: none (pitch-accent, not lexically tonal).
- (c) End-rhyme weak/unusual; craft leans on **mora count and vowel colour** — what a Japanese ear hears as a line's shape `LOW` (flagged gap).
- (d) J-pop line ≈ 8–12 morae; pre-chorus not optional (intro 4 / verse 8 / preC 4 / chorus 8); "Royal Road" IV–V–iii–vi; seasonal kigo and mono no aware; EN title sung, katakana loans `LOW/MED`.
- (e) Example: きょう kyō = 2 morae (きょ・う); がっこう gakkō = 4 (が・っ・こ・う); コーヒー = 4; haiku 5-7-5 counts morae. Cut a vowel if the bar spills.
- (f) sljfaq; Raito Studio; phrasebend; BMI (J-pop/K-pop markets).

### Korean (K-pop)
- (a) Syllable-timed; shape lines by **syllable count and phrase breaks**, not stressed beats; no word stress `MED`.
- (b) Tone–melody: none.
- (c) Loose end-rhyme; hook and syllable prosody carry the line.
- (d) Speech levels — 존댓말 (합니다체 formal, 해요체 polite) vs 반말 (해체 intimate, 한다체 plain); register encodes relationship, not politeness (elon.io). Love/intimacy lyrics use 반말 (어디 가?, not 어디 가요?). Market craft: Western structures, explosive choruses; ~80% written by US/EU writers; adaptation lyricist earns 15–50% credit (BMI).
- (e) Example: English embedded intra-sententially and phonologically adapted — "crazy 사랑", "make it rain"; BTS "Dope" keeps English stress on *party* (~200 ms extra); "Yet to Come" evens *dreams come true* to ~140 ms/syllable (UCLA) `MED`.
- (f) sunomarket; elon.io Korean honorifics; LingoDeer; UCLA; BMI.

### Malay / Indonesian
- (a) Syllable-timed-ish; not tonal `MED`.
- (b) Tone–melody: none.
- (c) Core oral unit is the **pantun**: 4 lines, strict **a-b-a-b**; first couplet (*sampiran*, nature imagery) sets up the second (*isi*, the message); UNESCO: "clear a-b-a-b rhyme scheme… used to express love, family, community, nature" `HIGH`; sampiran/isi split lightly sourced `MED`.
- (d) Dangdut: repetitive, direct; studies document vulgar lexicon and gender stereotyping; kroncong/langgam Jawa lineages. Pronouns (anda/kamu, saya/aku) form a register axis.
- (e) Example: the pantun form itself (sampiran→isi, a-b-a-b); dangdut conventions per JSSER/Smithsonian (lyrics not quoted there).
- (f) UNESCO Pantun; JSSER dangdut study; Smithsonian Folkways.

### Spanish
- (a) Syllable-timed; near-exact line length; most words are **llano** (penultimate stress) so lines end weak; **sinalefa** merges a word-final vowel with the next vowel, shortening the count; hiato/diéresis adjust it `HIGH`.
- (b) Tone–melody: none.
- (c) **Rima consonante** (vowels AND consonants identical from the stress: alguno/ninguno, morir/salir) vs **rima asonante** (vowels only from the stressed vowel to the end); the **romance** = octosílabo, assonance on even lines only; copla, redondilla `HIGH`.
- (d) Gender agreement forces addressee marking English avoids; reggaeton hooks.
- (e) Example: Zorrilla enfático/catedrático (perfect rhyme from the antepenult); assonance evento/presto ("e-o"); EN hook "Call me when you mean it" = 13 syllables → literal Spanish 22 → native 16.
- (f) medina502; Glossa 2025; Wikipedia *Copla*; Conlen 2016; sunomarket.

### French
- (a) Syllabic metre; count pure vowels/diphthongs; **e muet** counted mid-line but not at line end, elided before a vowel; caesura ≥9 syllables; alexandrine = 12 (6+6), décasyllabe = 10 (4+6) `HIGH`.
- (b) Tone–melody: none; no fixed word stress — prominence falls at the group end, so lines end strong by default and rhyme words are automatically accented `MED`.
- (c) Masculine (no final e muet) vs feminine endings **alternate strictly**; rimes plates (aabb), croisées (abab), embrassées (abba) `HIGH`.
- (d) Chanson/art song register.
- (e) Example: Habanera (Carmen) — "L'un parle bien, l'autre se tait;" (8; e muets of parle/autre counted) / "Rien n'y fait, menace ou prière." (8; e muet of menace **elides** into ou; prière sounds but is not counted).
- (f) MTO 21.3 (Pau, French chanson); sunomarket.

### Portuguese (BR)
- (a) Speech-driven accentuation: **métrica derramada** ("fluid meter"); syncopation is melody-vs-accompaniment interplay, not a grid `HIGH`.
- (b) Tone–melody: none; word stress and vowel "tensity" transfigure the melody (Elis Regina) `MED`.
- (c) Open-vowel endings stress the penult; ‑ar/‑er/‑ir rhymes are grammatically free, so rhyme must be earned by word choice, not endings `MED`.
- (d) MPB/bossa; **EP vs BP**: European Portuguese crushes unstressed vowels so lines run shorter in the mouth — a line scanning in São Paulo can compress in Lisbon.
- (f) MTO 30 (Ulhôa/Stover); sunomarket.

### Hindi/Urdu & Bollywood
- (a) Stress-light, syllable-counted; "writing to a tune": the composer hums a laa-laa dummy, the lyricist fits exact-sounding syllables per note — count is essential `MED`.
- (b) Tone–melody: none.
- (c) तुकांत (tukant) end-rhyme; in ghazal: **qāfiya** (rhyme word) + **radīf** (repeated phrase after it), rhyme on both lines of the opening **matla**.
- (d) Classic film song = **mukhda** (opening refrain / sthāyī) + 2–3 **antara** (verses, new melody, climbing higher), each ending with a **connector line** back into the mukhda. Rāga colouring: Bilawal≈happy, Kafi≈romantic, Bhairavi≈devotional `LOW`.
- (e) Example: *Awara hun* (Shankar-Jaikishan): antara "Ghar-baar nahin, sansar nahin…" → connector "Sunsan nagar anjaan dagar ka pyara hun… Awara hun." *Mere man ki Ganga* (S.D. Burman): connector "…Bol Radha bol…". Ghazal *Unko ye shikayat hai…* (Madan Mohan): radīf "kuchh nahin kahte" repeats, qāfiya on the preceding word.
- (f) Songs of Yore; BeatRootRaga; Megabronze; Produsso.

### Arabic
- (a) Stress-timed [Conlen, `MED`]; classical **al-ʿarūḍ** scans by vowel/consonant pattern (ḥarakah vs sukūn) across 16 meters (*buḥūr*); a *bayt* = two hemistichs (ṣadr + ʿajuz) `MED`.
- (b) Tone–melody: none.
- (c) **Qāfiyah**: the final vowel of each half-line is lengthened into a shared rhyme carrier, often followed by a repeated **radīf**.
- (d) Sung Arabic is largely **dialect** (Egyptian/Levantine); MSA for classical/religious material; delivery is tarab — improvisatory, repeat/paraphrase lines, melisma, audience-driven, floating fixed/free rhythm.
- (e) Example: ṭawīl = فَعُولُنْ مَفَاعِيلُنْ فَعُولُنْ مَفَاعِلُنْ (as-Samawʾal, Fluent Arabic); canonical song: Umm Kulthum's *Al Atlal* (1966), *Inta Omri* (1964) — tarab repeat-and-vary.
- (f) Fluent Arabic; furious.com (Umm Kulthum); Conlen 2016.

### Russian
- (a) Stress-timed; **free lexical stress** — one main stress per word regardless of length (Одиночество = 5 syllables, one stress) `MED`.
- (b) Tone–melody: none.
- (c) Inflection hands out rhymes cheaply (‑ла feminine past: мечтала/устала/знала; ‑ать/‑ить; ‑ом instrumental) — "you can rhyme an entire song without choosing a single word for its meaning." Fix: **rhyme across parts of speech** (устала ↔ вокзала). Exact vs fuzzy/slant rhyme in rock.
- (d) Verse system: syllabo-tonic (iamb/trochee) → **dolnik** (counted in ictuses, 1–2 variable syllables between stresses) → accentual/tonic verse. Case endings license near-free word order (inversion for rhyme), archaic forms (брег/глас/град), vocatives (Боже), folk diminutives that add syllables for the metre.
- (e) Example: Akhmatova dolnik "Я зажгла заветные свечи…"; Blok "Его встречали повсюду / На улицах в сонные дни…"; Lermontov "Белеет парус одинокой…" (inversion for rhyme).
- (f) sunomarket; ru.wikipedia Дольник; Pilshchikov 2022; elon.io; cyberleninka.

### Thai & Vietnamese (tonal cross-reference)
- (a) Thai 5 tones, Vietnamese 6, both syllable-timed.
- (b) **Avoid contrary settings**; similar favoured, oblique allowed. Vietnamese best model = 77% similar motion. Thai: traditional ~90% similar, contemporary 60–70%, modern top-10 pop 52.2% (falling/rising treated "as high"). Tone tokens: khāː/khàː/khâː/kháː/khǎː — one syllable, five meanings `HIGH`.
- (f) Kirby & Ladd 2016 (ISCA/TAL, Vietnamese); ICPhS 2023 (Thai); Ladd & Kirby.

### Afrobeats (Yoruba/Igbo/Pidgin/English) — bonus
Four resources inside one song: English (hooks/global readability), Nigerian Pidgin (base narrative, "freedom of rhyme"), Yoruba (praise-poetry oríkì, call-and-response), Igbo (Highlife sentiment). Yoruba/Igbo are tonal, so meaning lands the moment words sit on melody; code-switch texture acts like changing instruments; opacity drives engagement. Vocabulary: omo, orí, àṣẹ, gbedu, shakara, japa, wahala, sabi; Pidgin markers **na / dey / don / no be / wetin / abi** `LOW-MED` (note.com AFRICANIST).

## Common pitfalls

- **Translating instead of rewriting.** Translation keeps the source skeleton (stress positions, line lengths, rhyme logic) and sounds dubbed; EN hook 13 syllables → literal Spanish 22 → native 16 [sunomarket, `MED`].
- **Syllable expansion/contraction.** English contracts; Spanish/Italian/Russian expand [sunomarket].
- **Forced rhyme where rhyme is cheap** (Russian, Italian). Grammar supplies rhyme free; the listener predicts the ending, and the last word carries no information. Earn rhyme across parts of speech [sunomarket].
- **Tone↔melody mismatch**: wrong word or unintelligible. 似/死 (Mandarin), 拗音 (Cantonese), Thai falling-tone mismatches [GagaST; note.com; ICPhS, `HIGH`].
- **Miscounting Japanese morae**: long vowels, ん, っ each add a unit; "8-syllable" lines are mora counts [sljfaq].
- **Romaji-only Japanese sheets**: long vowels hidden; kanji homophones (橋/箸) misfire [phrasebend, `LOW`].
- **Pinyin instead of 汉字** [HookGenius, `LOW-MED`]; **Korean register slip**: 반말 where deference is owed, or stiff 존댓말 to a lover [elon.io, `HIGH`]; **missing Spanish sinalefa/gender**: lines run long; sola/solo forces a choice English dodges [medina502; sunomarket]; **ignoring French e muet and caesura** breaks count and declamation [MTO Pau, `HIGH`].

## How Suno handles non-English

**Per-language quality tiers are community reports, not official — Suno publishes no ranking; treat that part as `LOW` confidence.**

- **Coverage**: "some level of support for ~50 languages," including Chinese and Russian-folk styles [FLTMAG, `MED-HIGH`].
- **Quality tiers (community, `LOW`)**: good reports for Hindi, Spanish, German, Japanese, Chinese, Italian; "absolutely terrible" with some languages; Italian struggles vs English/Spanish (r/SunoAI + Facebook titles/snippets).
- **Tonal-language tone accuracy**: Suno "sometimes gets tones wrong, making words unintelligible." Write lyrics in **Chinese characters (汉字), not pinyin**; break long phrases; `[Pronunciation: 难字 = nán zì]` metatags; tag "singing in Mandarin Chinese" `LOW-MED`. Cantonese: traditional characters + "Cantopop, Hong Kong pop"; Suno is **confused between Mandarin and Cantonese** (r/SunoAI, `LOW`). Inference: full 協音 is a hard constraint natives enforce, so Cantonese output may read "fake/拗音" even when pronunciation is fine `LOW`.
- **Accents/pronunciation workflow** (Jack Righteous, `MED`): one language per section block (`[Verse – Spanish]`); native script first; respell only the failing sound (AI → A-I); identical hook spellings; regenerate only the smallest affected section.
- **Code-switching**: possible within a block but "not always consistent"; one language per section is the safe default `LOW`.
- **Style prompt**: keep it **in English**; use specific genre tags (Mandopop, Cantopop, K-Pop) not generic "Chinese music" [HookGenius, `MED`]. Recipe: name language + genre (`Mandopop`, `Cantopop`, `J-Pop`, `K-Pop`, `dangdut`, `Bollywood`, `tarab`); lyrics in native script (汉字, 日本語, 한글, Arabic script, Devanagari); one language per labeled section; short lines, broken phrases, pronunciation metatags; for Cantonese, pre-check 協音 fit or expect tone violations. Tone↔pitch harmony is an explicitly modeled ML problem (ToneCraft; GagaST) — expect models to violate tone constraints more than native lyricists.

## Confidence & open questions

- **Cantonese match-rate range**: >90% (Wong & Diehl), >80% (Lee 2023 UBC), 92% (Ladd comment). Same ~80–90%+ range, different corpora. `HIGH`
- **Mandarin tone relevance**: sources range from "melody dominates" to "~37% match, better than random." Reconciled: melody dominates; tone is a weak bias, not a hard constraint. `MED`
- **Thai decline**: modern pop 52% vs earlier ~80%, contemporary 60–70% — unsettled debate. `MED`
- **"Stress- vs syllable-timed"** is a gradient; isochrony empirically weak. `HIGH` (methodological)
- **Suno quality by language**: no official ranking; all tiers community hearsay `LOW`.
- **Japanese rhyme**: mora/vowel-melody well attested; no rigorous citable statement on end-rhyme norms — flagged gap.

## Sources

Primary:
- https://www.phonetik.uni-muenchen.de/~jkirby/docs/ladd2018tone.pdf
- https://www.phonetik.uni-muenchen.de/~jkirby/docs/kirby2023comparative.pdf
- https://en.wikipedia.org/wiki/Lyric_setting
- https://online.berklee.edu/takenote/prosody-in-music-and-songwriting/
- https://digitalcommons.wayne.edu/cgi/viewcontent.cgi?article=1025&context=honorstheses (Conlen 2016)
- https://www.glossa-journal.org/article/id/18411/
- https://www.mtosmt.org/issues/mto.15.21.3/mto.15.21.3.pau.html (Pau, French)
- https://research-repository.griffith.edu.au/server/api/core/bitstreams/e4ed69a0-35a0-454b-a749-1e207c45938c/content (Ulhôa/Stover)
- https://www.isca-archive.org/tal_2016/kirby16_tal.html
- https://www.internationalphoneticassociation.org/icphs-proceedings/ICPhS2023/full_papers/588.pdf
- https://aclanthology.org/2022.findings-acl.60.pdf (GagaST)
- https://aclanthology.org/2025.emnlp-main.18/ (ToneCraft)
- https://open.library.ubc.ca/media/stream/pdf/24/1.0431335/4 (Lee 2023)
- https://www.philology.nsc.ru/journals/kis/pdf/CS_2022_1/15.pdf (Pilshchikov)

Craft/practitioner:
- https://sunomarket.com/blog/writing-songs-in-another-language
- https://languagelog.ldc.upenn.edu/nll/?p=69330
- https://note.com/sasaleut/n/n6d90732b6f04?hl=en (Hiepyam)
- https://lyrics.mrpinyin.net/
- https://www.sljfaq.org/afaq/mora.html
- https://raito.studio/guides/japanese-lyrics-mora/
- https://www.phrasebend.com/how-to-write-jpop-lyrics-without-fluency-the-romaji-to-hook-framework/
- https://www.bmi.com/advice/how_to_write_and_pitch_songs_for_the_j_pop_and_k_pop_markets
- https://elon.io/grammar/korean/honorifics/jondaemal-vs-banmal
- https://blog.lingodeer.com/korean-speech-levels/
- https://languagedlife.ucla.edu/sociolinguistics/code-switching-and-bilingualism-in-k-pop-phonological-adaptation-and-audience-engagement-through-korean-english-lyrics/
- https://www.hpu.edu/research-publications/tesol-working-papers/2023/4_yuhui_du.pdf
- https://ich.unesco.org/en/RL/pantun-02274
- https://jsser.org/index.php/jsser/article/view/1085
- https://music.si.edu/album/music-indonesia-vol-2-indonesian-popular-music-kroncong-dangdut-and-langgam-jawa
- https://medina502.com/classes/reading/Spanish_versification.php
- https://en.wikipedia.org/wiki/Copla_(poetry)
- https://www.songsofyore.com/where-is-the-mukhada-gone-where-is-antara-gone/
- https://beatrootraga.com/learn/indian-music/mukhda-and-antara
- https://megabronze.com/how-to-write-hindi-lyrics.html
- https://produsso.com/blog/gaana-kaise-banaye-khud-ka-gaana-banane-ki-poori-prakriya
- https://fluentarabic.net/introduction-to-arabic-poetry/
- https://www.furious.com/perfect/oumkalthoum.html
- https://ru.wikipedia.org/wiki/%D0%94%D0%BE%D0%BB%D1%8C%D0%BD%D0%B8%D0%BA
- https://elon.io/grammar/russian/register/poetry-and-song-language
- https://cyberleninka.ru/article/n/russkiy-rok-v-kontekste-avtorskoy-pesennosti
- https://zh.wikipedia.org/zh-hans/%E5%8D%81%E4%B8%89%E8%BE%99
- https://baike.baidu.com/item/%E5%8D%81%E4%B8%89%E9%81%93%E5%A4%A7%E8%BE%99/9880377
- https://note.com/africanist/n/ne5d5f7185778?hl=en

Suno:
- https://fltmag.com/suno-ai/
- https://hookgenius.app/guide/multi-language
- https://hookgenius.app/learn/suno-chinese-prompts/
- https://jackrighteous.com/en-us/blogs/guides-using-suno-ai-music-creation/suno-v5-multilingual-english-pronunciation-guide
- https://www.reddit.com/r/SunoAI/comments/1i18y6o/suno_is_great_with_some_languages_absolutely/
- https://www.reddit.com/r/SunoAI/comments/1hx8aoh/suno_confused_between_mandarin_and_cantonese/
- https://www.reddit.com/r/SunoAI/comments/1kyl44e/languages_in_suno/
- https://www.facebook.com/groups/1673444546790462/posts/1957994415002139/
