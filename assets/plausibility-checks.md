# Plausibility Checks — pre-ship lyric reality audit

Run before shipping a lyric. Each line: trap — why it's wrong — check/fix.
Goal: no implausible, anachronistic, or culturally wrong detail. Concrete imagery from
`imagery-lexicon.json` is safe unless it collides with era, hemisphere, geography, or POV.

## Hemisphere and seasons
- "December snow" in a southern or tropical setting — December is winter only north of the equator; in Australia it is high summer, in most of Malaysia just regular rain — fix: pick month by hemisphere or make climate explicit (a coldsnap verse can name the south wind or mountain altitude).
- Bare deciduous trees in a tropical verse — tropics have no leaf-drop season; durian season or monsoon is the local marker — check: what tree did you name, does it shed? Mango, coconut, banana don't shed.
- Autumn leaves + "summer sun through the blinds" in adjacent stanzas — seasons drifted — fix: commit to one season per scene; time can move between sections but not inside one.
- "First snow" data without geography — snow lines depend on latitude and elevation (Cameron Highlands gets cold air, not snow) — fix: either name a plausible place or keep the detail (breath fogging, frost on glass) that holds anywhere cold.

## Light, sky, sun, moon
- Sunset over the sea when the narrator faces inland — the sun sets in the west regardless, so ocean-over-shoulder only works on a west-facing coast — fix: name a west coast, or shift to sunrise in the east.
- "The sun rose behind me as I walked toward the sea" on an east beach — that works westward; verify bearings once and keep them consistent.
- Moon phase vs tide: a full moon and a spring tide go together; a thin crescent moon with a violent high tide contradicts — fix: pick either moon-only or tide-only, or match the phase.
- Day/night logic: person "makes coffee at dawn" right after "midnight radio" with no time skip — dawn is not 45 minutes after midnight (midnight ends the day; dawn starts the next) — fix: interpolate a wake-up beat or sleep line.
- Light source: a lit phone screen in a 1950s verse, car headlight cone in a horse-cart verse — light sources date the scene hard — check: list every light in the song and match its era.

## Weather logic
- Rain "stops" then muddy ground one line later with sun high — ground doesn't flash-dry; puddles and damp hems survive — keep at least one wet-trace detail.
- Thunder heard before the lightning flash — sound loses to light — fix: flash first, then rumble.
- Snow falling while people lounge in short sleeves indoors-wide scene — temperature is one system — fix: keep bodies dressed for the weather.
- Monsoon imagery without rain words (Malay verse: storm cloud, flooded lot, zinc roof drumming) — Southeast Asian rain comes with specific props: atap zink, genangan, kaki lima shelter — use regional props when in a regional scene.

## Technology anachronisms vs stated era
- Payphones appear until ~2000s, smartphones after 2007, streaming after ~2015 — a 1995 verse with a stream link kills the scene — check: pick the verse's decade first, then pick its device (cassette, pager, burner, spin dial, dial-up tone).
- Cassette + airpods, needle on vinyl + Spotify queue on the bedside — mixed-era audio — fix: one listening format per song, or frame the old one as inherited (dad's tapes).
- Auto-reply and "leave a message" language belong to answerphones; read receipts belong to messengers — match the message medium to the decade.
- Currency of detail: "top up" implies prepaid phone; "coin slot" implies machine — small verbs date the tech too.

## Geography and city detail
- A real city named with a nonexistent river/mountain/subway line — named places invite checking — fix: verify the landmark, or swap in a generic (river, overpass, old town) that can't be wrong.
- Streets that cross impossible things: a subway under a village lane, a beach where the map says lake — check the one named feature; leave the rest vague.
- Distance and transport: "ten-minute drive" between named districts only if they are neighbors; a train between islands must be a ferry — fix: keep numbers vague unless verified.
- Dialect and regional vocabulary: lift vs elevator, sidewalk vs pavement, hawker vs vendor — one region per song; mixing registers reads as fake.

## Units, currency, measures
- Metric in a US street voice (liters, kilometers, kilos) and imperial in a Malay voice (pounds, gallons) — units are accent — fix: match units to the singer's region (US/UK idiom, metric for Malaysia/China).
- Currency plausible for the place and year: dollars not euros in a small-town American bar; ringgit and sen in a Malaysian verse — a wrong note feels instantly fake.
- Body-scale numbers: an 8-hour bus for a 40 km hop, a cup of coffee priced like a car — round, human numbers only ("two years", "ten blocks").
- Speed/time: walking-speed claims — nobody walks 100 km/ph faster than a train — check any measurable claim against one real number.

## Bodies and physical actions
- Arms reach, chairs bear weight, doors open where doors are — no slipping through the keyhole, no lifting a house with one hand — fix: scale the action to a real person.
- Anatomy order: thumbs on guitar necks, feet on the brake, breath against glass — the move should be physically locatable — check: can you mime it?
- Sound emitted by the stated source: distant church bells need a church, ubat gigi taste needs a brush — each sensory claim needs its object nearby.
- Injury/age coherence: an 80-year-old narrator tracks a teenager in the corridor — age sets stamina, eyesight, and habits.

## Timeline and POV consistency
- One narrator per section; "you" defined once and held — if "you" is the departed in verse 1 it can't be the mother in the chorus without a setup — check: list who "I" and "you" are on one line.
- Tense drift: past-tense verse, present-tense chorus, then past again mid-chorus without a time jump — fix: fix tense per section; changes must mark time shift.
- Age of narrator vs era detail: a father born in the 70s cannot recall streaming as a kid — cross-check narrator birth-year vs named tech.
- Distance clockwise: "three days road" but the reply is the next day's — travel time must add up end to end.

## Cultural and etiquette fit (zh / ms contexts)
- Chinese wedding register: 双喜, 请柬, 敬酒, 红盖头 belong to han weddings; avoid mixing mosque or church terms into the same scene — one ceremony tradition per song.
- Chinese family address: 妈, 老爸, 哥, 阿姨 — honorific order goes elder-before-younger; calling an elder by name is a flag — check the address words once.
- Malay context: weddings (bernikah, bersanding, pelamin, bunga telur, kompang), funerals (pintas, takziah), forms of respect (encik, puan, cik, ustaz) — a bar, beer, casino, or pork detail in a Muslim-character scene is a cultural off-key — verify the character's community before any such item.
- Malay kin terms: abang, kakak, adik, ibu, bapa, nenek — naming your father "Mr" reads odd; full-out English honorifics in a Malay verse need a reason.
- Mourning color: white (zh) vs black (ms/en) as the funeral color — swap by culture, not habit.
- Religious reference shape: prayer at dawn, 跪拜, berdoa, azan — generic devotion is safe; named rituals require the right faith — if unsure, go generic.

## When to go online to verify
Verify when the detail is: a real named place or landmark, a brand or product tied to a year,
a public event or news hook, a statistic or number quoted, a slang word claimed as regional,
or a ritual/custom detail beyond generic. Everything else can stay universal.

## Final rule
Prefer universal imagery unless a verified specific is needed. If a real-world claim is
load-bearing and unverified, either verify it or cut it.
