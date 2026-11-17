# HyperFrames production lane

## Purpose

HyperFrames is an optional, local-first HTML/CSS/JavaScript-to-video renderer. Use it for motion-design shots that are naturally built from web primitives: kinetic typography, animated labels, schematic process diagrams, data-led explainers, chart reveals and restrained transitions.

It complements the AMORDER production stack. Blender remains the primary tool for cinematic PBR environments, camera animation, object animation and true 3D hero shots. FFmpeg/ffprobe remain the finishing, compositing, encoding and validation tools. HyperFrames must not be used to disguise a still image as genuine moving footage or to bypass the existing delivery quality gate.

Official project: https://github.com/heygen-com/hyperframes
Official quickstart: https://hyperframes.heygen.com/quickstart
Official rendering guide: https://hyperframes.heygen.com/guides/rendering
Official HTML schema: https://hyperframes.heygen.com/reference/html-schema

## Good uses in AMORDER videos

- Animated explanations of data freshness, completeness, validity, consistency and provenance.
- Kinetic typography for a hook, chapter transition or key takeaway.
- Schematic data-flow diagrams and non-numeric process visualisations.
- Animated chart frames only when every plotted value comes from the approved claim ledger and has a visible source/date/unit context.
- Transparent overlays or compositing intermediates when the composition has been designed with a transparent background and its alpha has been verified.

Do not use it to create fabricated market dashboards, fake broker interfaces, simulated trades presented as real, unsupported statistics, or synthetic footage that implies a real event.

## Tool selection

| Shot requirement | Preferred tool |
| --- | --- |
| Photorealistic 3D scene, detailed materials, lighting, camera/object movement | Blender Eevee |
| Kinetic type, 2D diagrams, data labels, animated chart reveals | HyperFrames |
| Clip assembly, colour/audio finishing, frame interpolation, captions and final encode | FFmpeg / existing AMORDER renderer |
| Technical media inspection and release checks | ffprobe and existing AMORDER validators |

Use the tool that best serves each shot. A short may mix Blender scenes and HyperFrames inserts, but the finished master must still pass every applicable AMORDER quality gate. Do not count a static card or still-image zoom as motion coverage.

## Local setup

The local CLI path is the default for AMORDER. Do not require a HeyGen account, Studio sign-in, hosted render, API key or paid credit for routine rendering.

Requirements:
- Node.js 22 or newer.
- FFmpeg available on `PATH`.
- A supported local browser runtime; the HyperFrames engine uses Puppeteer/Chromium.

From the HyperFrames project folder, the AMORDER smoke-test workflow currently pins CLI version `0.9.58`:

```bash
npx --yes hyperframes@0.9.58 --help
npx --yes hyperframes@0.9.58 browser ensure
npx --yes hyperframes@0.9.58 lint
npx --yes hyperframes@0.9.58 check
npx --yes hyperframes@0.9.58 render --fps 30 --quality high --output render.mp4
```

The project root composition is normally `index.html`. Check the installed CLI's help before relying on a less-common flag; the installed version is authoritative. Keep the CLI version pinned for production and update the pin only after the starter composition passes the smoke test. Record that version in the render manifest.

To install the agent skills in a local working copy, use the official installer from that project's folder and select Core Skills:

```bash
npx skills add heygen-com/hyperframes
```

Restart the coding agent in that folder after installation. Do not run a skill installer against the public AMORDER repository if it would add third-party skill source or generated files that have not been reviewed. An agent may instead follow this integration guide and the official HyperFrames documentation directly.

## Starter composition

A small vertical starter composition is provided at:

`examples/hyperframes/vertical-data-reveal/index.html`

It uses the HyperFrames composition root attributes and a paused GSAP timeline so frames can be sought reproducibly. It contains no live market feed, external data or generated performance numbers. Copy the folder to a date-scoped working directory before adapting it to an approved story.

Example:

```bash
cd examples/hyperframes/vertical-data-reveal
npx hyperframes lint
npx hyperframes check
npx hyperframes render --fps 30 --quality high --output ../../../../work/vertical-data-reveal.mp4
```

Keep project-local source and temporary renders out of the public media library until the content has passed the normal review. Only reviewed, public-safe final exports and their approved evidence belong in this public repository.

The non-publishing CI smoke test lives at `.github/workflows/hyperframes-smoke-test.yml`. It pins HyperFrames `0.9.58`, installs Node.js 22 and FFmpeg, ensures the local browser, then runs lint, browser/layout/motion/contrast checks, a vertical render and ffprobe/full-decode validation. It has read-only repository permission and does not upload or publish anything.

## Joining HyperFrames shots to an AMORDER master

1. Build each HyperFrames shot against the approved timecoded shot list and visual bible.
2. Use 1080x1920 for vertical-first Shorts/Reels inserts. Keep the composition's dimensions and output FPS explicit.
3. Render each shot separately where practical. This makes timing, retries and editorial replacement easier than rendering the full film as one HTML composition.
4. Assemble the HyperFrames inserts with the Blender shots and narration/music using the existing AMORDER FFmpeg workflow.
5. Burn and export English captions through the existing workflow; retain the SRT sidecar.
6. Inspect the finished master, not just the individual HyperFrames scene. Run the existing full-file decode, stream, duration, audio, subtitle, privacy, rights, disclosure, motion-coverage and release checks.
7. Record HyperFrames as a visual engine in the manifest and capture the exact CLI version, project path/commit, composition dimensions, FPS, render command, output path and validation result.

A HyperFrames preview, lint pass or successful render does not mean the final AMORDER video is technically approved or publishable.

## Reproducibility, rights and safety

- Keep source HTML, CSS, JavaScript, media and render settings with the working project until the final output is verified.
- Pin third-party script versions (the starter references GSAP 3.14.2) and review each dependency's current licence and use terms before production.
- Record creator, source URL, licence/version, acquisition date and permitted use for all external images, video, audio, fonts, models and code.
- Avoid third-party media, remote fonts and remote data in release renders unless the exact asset is cleared and reproducibly available.
- Never place credentials, private broker data, trading-system source, private research or unpublished performance in a composition, project file, prompt, output or log.
- Label illustrative or simulated graphics where a viewer could mistake them for literal market evidence.
- Keep the complete required paper-trading disclosure on the final closing card. Do not assume a HyperFrames scene provides the required disclosure unless the final export proves it.
- Do not add HyperFrames' cloud rendering, Studio publishing or any separate social publisher to the AMORDER workflow. Publishing remains exclusively with the existing authorized AMORDER/Buffer path.
