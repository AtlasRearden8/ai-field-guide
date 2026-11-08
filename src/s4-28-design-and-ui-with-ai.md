# 4.28 Design and UI with AI
<!-- original: ch. 90 -->

Good design used to need years of training. Now AI can give you a head start on everything: moodboards, colour palettes, logos, layouts, full app screens, slide decks, and code that matches the design.

This chapter covers the tools, a start-to-finish workflow, how to get taste out of AI, design-to-code with Figma and MCP, accessibility, and quick wins for presentations and everyday graphics.

## The AI design toolbox

Different jobs need different tools. Here is the map.

**Graphics, social posts, and flyers.** Canva with Magic Studio, and Adobe Express. Templates plus AI generation plus brand kits. A **brand kit** is a saved set of your colours, fonts, and logo, so everything you make looks like it came from you.

**App and web UI design.** Figma with Figma Make and its AI features, Google Stitch, and Uizard. They turn a prompt into screens you can refine by hand. **UI** means user interface, the screens and buttons people see and touch.

**UI straight to code.** v0, Lovable, Bolt, and Claude Artifacts. They turn a description or a screenshot into working code. You get a real page, not just a picture of one.

**Websites.** Framer AI, Relume, Webflow AI, and Wix or Squarespace AI. They build sitemaps, wireframes, and full sites. A **wireframe** is a simple sketch of a page: boxes and labels, no colours or pictures.

**Logos and type.** Ideogram, Recraft, and brand tools such as Looka. Explore directions fast. Finish the winner by hand.

**Palettes and inspiration.** Claude, Coolors, and Khroma. They suggest palettes from a mood or a photo.

**Presentations.** Gamma, Canva, PowerPoint Copilot, Google Slides with Gemini, and Claude. They build decks from an outline or a document.

**Design to code bridge.** The Figma MCP server and the Canva MCP server. **MCP** is a standard plug that lets AI use your tools. Coding agents can read your real designs through it.

Your favourite assistant is a design partner too. ChatGPT and Gemini generate and edit mockups. Claude builds interactive prototypes as Artifacts. Mix and match.

> NOTE: AI gives you a fast first draft. It does not replace your taste. Look at what it made. Ask what is wrong with it. Fix the worst thing first. Taste is a skill, and this chapter teaches you how to practise it.

## A start-to-finish design workflow

Good design follows a path. Brief, moodboard, style, wireframe, high-fidelity, critique, code. Each step is small. Each step saves time later.

**Brief.** Ask AI to interview you. "Interview me with eight questions about this project's audience, goals, and vibe." The result is a one-paragraph design brief. A **brief** is a short statement of who the design is for and what it must do.

**Moodboard.** Ask for images that set the direction. "Generate six moodboard images for 'cosy, modern, plant shop, morning light.'" A **moodboard** is a collage of pictures that shows a feeling before any real design exists.

**Style.** Ask AI to turn the moodboard into a style guide. "From this moodboard, propose a palette with hex codes, two fonts, and a shape language." A **hex code** is a six-character code that names an exact colour. A style guide is a mini rulebook for your design.

**Wireframe.** Ask for layout without distraction. "Wireframe the homepage: sections, hierarchy, calls to action. Boxes and labels only." **Hierarchy** means making the important thing biggest and first. A **call to action** is the button you want people to press.

**High-fidelity.** Build real-looking screens in Figma Make, v0, or Claude. "Design this wireframe with our style guide." **High-fidelity** means close to the final look: real colours, real fonts, real pictures.

**Critique.** Ask AI to review the result. "Critique this like a senior product designer: top five fixes." You get a punch list. Fix the worst first.

**Code or export.** Turn the design into a working page, or export the files you need.

Six design rules AI can teach you in five minutes: hierarchy, contrast, alignment, whitespace, consistency, and one primary action per screen. **Whitespace** is empty space. It is not wasted. It helps the eye rest and find what matters. Ask: "Explain these design principles using my screenshot as the example."

## Colour, type, and layout with AI

**Colour.** Start with a mood, not a colour. "Calm, morning, plant shop" gives better palettes than "green." Ask for five palettes. Pick one. Ask for light and dark versions of it. Two themes in one go.

Keep palettes small. One main colour, one supporting colour, one accent, plus black, white, and grey. Small palettes look confident. Big palettes look messy.

**Type.** Pick two fonts at most. One for headings. One for body text. A **font** is a typeface, the style of the letters. Ask AI to suggest pairs that work together. "Suggest a heading font and a body font for a friendly café menu. Both must be free and easy to read."

**Layout.** Start with the wireframe. Put the most important thing first and biggest. Put one primary action on each screen. If everything shouts, nothing is heard.

Ask AI to explain a layout you like. Screenshot a site you admire. Ask: "What makes this layout work? Name the three strongest choices." You learn taste by studying good work.

## Getting taste out of AI: critique

AI critique is one of the most underrated design tools. Screenshot your work. Ask for a review.

Try these prompts.

- "Critique this like a senior product designer. Give me the top five fixes, in order."
- "Here are three versions. Which is strongest and why? What would you steal from the others?"
- "What is the first thing a visitor's eye goes to? Is that the thing I want them to see?"
- "List anything that looks broken, misaligned, or hard to read."
- "How would you make this look more expensive? More friendly? More fun?"

**Screenshot loops** make this automatic. When you build UI with Claude Code, connect Playwright MCP and say: "Screenshot the page at desktop and phone widths, critique it against our style guide, and fix the top three issues. Repeat twice." Playwright is a tool that controls a browser. The AI designs, looks, and improves on its own.

Do not accept every critique. AI can be wrong. It can suggest changes that break your brand. Your taste is the final judge. But always ask why. A critique you disagree with still teaches you something.

## Design-to-code with Figma and MCP

This is the bridge between design and code. It works in five steps.

1. **Design screens in Figma.** Or generate them with Figma Make.
2. **Connect the Figma MCP server** to Claude Code, Cursor, or VS Code.
3. **Select a frame and ask.** "Implement this frame as a responsive React component using our Tailwind config and existing components." **React** is a popular way to build web pages from pieces. **Tailwind** is a styling system. **Responsive** means the page works on phones and desktops.
4. **The agent reads real values.** It reads your actual colours, spacing, components, and variables. It does not guess from a screenshot.
5. **Screenshot the result.** Compare it with the design. Iterate.

Design systems make this sing. A **design system** is a shared set of named colours, fonts, and components used everywhere. Name your colours, fonts, and components consistently in Figma and in code. Then agents reuse them instead of inventing new ones.

Start small. One screen. One component. Get the loop working before you hand over a whole app.

## Accessibility: design for everyone

**Accessibility** means everyone can use what you make, including people with different needs. Good design is accessible design.

Follow these basics.

- **Contrast.** Text must stand out from its background. Dark text on a light background is safest. Check contrast with a free checker tool.
- **Size.** Body text should be big enough to read without zooming. Buttons should be big enough to tap on a phone.
- **Alt text.** Every meaningful picture needs a short description for screen readers. A **screen reader** is software that reads a page aloud for blind users. Write alt text like this: "A red fox asleep on books in a library."
- **Colour is not the only signal.** Do not use colour alone to show an error. Add words or an icon too.
- **Captions.** Add captions to videos. They help deaf viewers and everyone watching without sound.

Ask AI to check your work. "Check this screenshot for accessibility problems. List contrast issues, small text, and missing labels." Fix the list.

## Presentations and everyday graphics

Presentations have one rule: each slide says one thing. Ask AI: "For each slide, what is the one thing the audience should remember? If it is unclear, split or cut the slide."

Keep slides simple. Big words. One picture. Almost no text. If you need notes, put them in the speaker notes, not on the slide.

Everyday graphics follow the same rules. A flyer needs one headline, one picture, and one action. A social post needs one idea and one image. A menu needs clear sections and prices that are easy to find.

Here are twelve design projects to practise with.

1. A complete brand kit for an imaginary shop: logo, palette, fonts, and social templates.
2. Redesign an app you find frustrating, then critique your redesign.
3. A personal homepage, from moodboard to deployed site.
4. A poster series for your local library or club.
5. Turn a boring report into a beautiful one-page infographic.
6. Wedding or party invitations with a matching RSVP page.
7. Light and dark themes for a site you like.
8. A friendly redesign of a confusing form you had to fill in.
9. A menu for a friend's café.
10. A chore chart your kids will actually like.
11. A book cover for your story.
12. A personal design system in Figma, used by Claude Code to build a site.

> TRY IT: Pick a poster, a flyer, or a slide you made recently. Screenshot it. Ask Claude: "Critique this like a senior product designer. Give me the top five fixes, in order." Fix the top two. Compare the before and after. You have just practised taste.

## Check yourself

1. What is a moodboard, and when do you make one?
**Answer:** A collage of pictures that shows a feeling before any real design exists, made right after the brief.

2. Why should you keep a colour palette small?
**Answer:** Small palettes look confident, while big palettes look messy.

3. What is the best way to get taste out of AI?
**Answer:** Ask it to critique your work, with a screenshot, and fix the worst issues first.

4. How does the Figma MCP server help turn designs into code?
**Answer:** It lets a coding agent read your real colours, spacing, components, and variables instead of guessing from a screenshot.

5. What is one simple accessibility rule for text?
**Answer:** Text must stand out from its background, with strong contrast and a readable size.

## In short

- AI helps at every design step: brief, moodboard, style, wireframe, high-fidelity, critique, code.
- Keep palettes small, use two fonts at most, and one primary action per screen.
- Critique is how you build taste; screenshot your work and ask for the top five fixes.
- Figma MCP lets coding agents read real design values, not guesses.
- Accessibility is part of good design: contrast, size, alt text, captions.
- Each slide says one thing; if it is unclear, split or cut it.
