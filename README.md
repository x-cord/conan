# conan
A community effort to provide Detective Conan subtitles with consistent styling and translation.

## Structure
- `fonts/` Fonts required for all episodes.
- `subs/` Subtitles, `0001-0999` is the main directory where work is needed.
- `tools/` All sorts of tools for retiming, restyling and analysis.

## Contributing
If editing a subtitle file already in the repo:
- Open in Aegisub and load your video. When prompted, *do not* resample the file, simply discard the dialog box.
- Make desired edits.
- Open a terminal in `tools/` and run `style-fixup.py`. This will reapply any missing styling and remove Aegisub version information.

If importing brand new subtitles:
- Make a directory `og/` with relevant sub-dirs for the file to be imported, e.g. `og/0001-0999/`
- Place your subtitles according to the following: `og/0001-0999/0123 (TL Source here).ass`
- Open a terminal in `tools/` and run `restyle.py`, then `style-fixup.py`. This will restyle your subtitles to be in line with all others.
- Run `unknown-styles.py` and make sure to rename residual styles (if any).
- Delete the `og/` directory.
- If lines are out of order, run `sort-by-time.py`.
- If subs don't sync to DVD, look through `sushi-*.py` or manually sync them yourself.

When making pull requests:
- Clearly specify changes in the commit message.
- Keep initial retiming/restyling and manual edits as separate commits.
- A single PR for a single set of changes. e.g. Changing a character's name across episodes and adding subtitles for intro narration go into two separate PRs. Broader changes are allowed if targeting specific episodes.

## Current focus
- Translate all introduction, preview, hint and end joke segments.
- Properly time all subtitles to DVD (Reghost-Fabre\*), TV (usotsuki&WinxBloom1980) and WEB (Intervención&Erai-raws)
- Tag every line of dialogue that happens in a special context. (Thoughts, Over the phone, Narration, Flashback)

\* Reghost-Fabre suffers from heavy blending, making scene snaps impossible. While waiting for better encodes, count the start of a blend as the scene cut.

## Long-term goals
- Translation check of all episodes, completely new translations for those deemed unsalvageable.
- Consistent character names.
- Song translations & karaoke.
- Tag the "Actor" field.
- Sign typesetting.
- Movies, OVAs and other specials.

## Completed work
- OCR all ~400 remaining hardcoded subtitles.
- Restyle all episodes.
- Spellcheck and basic fixes.

## Acknowledgments
Most of these are not wholly original translations, but an attempt at providing a cohesive experience across existing translations produced over many years by many different people.  
Each subtitle file includes a "TL Source" line specifying the origin of the bulk of this file's translation.
