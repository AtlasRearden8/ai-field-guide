# 6.6 Build-along: a web app with logins and AI
<!-- original: ch. 115 -->

This weekend you will ship a real web app to the internet: Recipe Box. People sign in, save their own recipes, private to them, and tap Remix to have Claude invent a new dish from whatever is in their fridge.

You will build it with Claude Code as your pair programmer. You will store data in Supabase with proper row-level security. You will keep your AI key safely on the server. You will deploy on Vercel with a link you can send to friends.

Time: a weekend. Level: intermediate, no prior coding needed if you use Claude Code.

## What you will build

Recipe Box has four parts.

- **Sign up and log in.** Each user has an account. Each user sees only their own recipes.
- **Save recipes.** Title, ingredients, steps, and a photo if you like.
- **Remix with AI.** Tap Remix, list what is in your fridge, and Claude invents a new dish.
- **A live link.** Anyone with the link can visit the app. Only signed-in users can save recipes.

## Before you start

You need five things.

- **Claude Code or Cursor**, your pair programmer.
- **Node.js 24 or newer.** Node 18 and 20 no longer get security fixes as of November 5, 2026.
- **A free Supabase account.** Supabase gives you a database and logins.
- **A free Vercel account.** Vercel puts your app on the internet.
- **An Anthropic API key**, with a spending cap set.
- **A place to keep your code**, such as any Git host like GitLab or Codeberg, or the Vercel command-line tool. No GitHub account is needed.

## Step 1: write the spec, 20 minutes

A **spec** is a short document that says what the app must do. Write it before you write code. It keeps Claude on track.

Write a file called `SPEC.md` with these sections.

- **What it is.** Recipe Box: a personal recipe app with AI Remix.
- **Users.** People sign up with email and password. Each user sees only their own recipes.
- **Pages.** A home page, a login page, a recipe list, a recipe detail page, and an add-recipe form.
- **Features.** Add, edit, and delete recipes. Search by ingredient. Remix: given fridge ingredients, invent a new dish.
- **Rules.** Never show one user's recipes to another user. Never put the Anthropic key in the browser. The key lives on the server only.

Keep the spec to one page. A short spec is a clear spec.

## Step 2: scaffold with Claude Code, 30 minutes

**Scaffolding** means building the basic frame of the app: the folders, the config, and a page that loads.

Open a terminal in an empty folder. Start Claude Code. Paste your spec and say: "Scaffold this app with Next.js and Supabase. Set up the project, the database connection, and the login pages. Stop after the scaffold and show me what you built."

Claude creates the project. It installs the pieces. It writes the first pages. Read what it made. Run the app locally with `npm run dev`. Open it in your browser. You should see a home page and a login page.

If it fails to start, read the error message. Paste it back to Claude. "It fails with this error. Fix it." This loop is normal. Every build has it.

## Step 3: set up Supabase, 30 minutes

Open Supabase. Create a new project. Create a table called `recipes` with these columns: `id`, `user_id`, `title`, `ingredients`, `steps`, and `created_at`.

Turn on **row-level security**. Row-level security is a set of rules that keep each user's data private. Add a rule: a user can only read, write, and delete rows where `user_id` matches their own ID. This one rule is the heart of your app's privacy. Test it by creating two test users and checking that neither can see the other's recipes.

Copy the Supabase URL and the public key into your app's environment file. An **environment file** is a file called `.env.local` that holds secrets for your app. Never commit it to version control. Never share it.

## Step 4: build the recipe features, 60 minutes

Ask Claude to build the recipe list, the detail page, and the add-recipe form. One feature at a time.

- "Build the recipe list page. Show each recipe's title and a short ingredient summary. Add a search box that filters by ingredient."
- "Build the recipe detail page. Show the full ingredients and steps. Add edit and delete buttons."
- "Build the add-recipe form. Title, ingredients as a list, steps as a list. Save to Supabase with the current user's ID."

Test each feature as you go. Add a recipe. Search for it. Edit it. Delete it. Log in as a second user and check that the first user's recipes are invisible.

## Step 5: the Remix feature, 60 minutes

Remix is the AI feature. It needs a server route, because your Anthropic key must never reach the browser.

Ask Claude: "Add a server route called `/api/remix`. It takes a list of ingredients, calls Claude with a prompt to invent a new dish from them, and returns the recipe as JSON. The Anthropic key comes from the server environment only. Add a Remix button on the recipe page that asks for fridge ingredients and shows the result."

Test it with real ingredients. "Eggs, spinach, feta, stale bread." Claude should invent a dish, such as a spinach and feta strata. If the result is thin, improve the prompt. "Invent a dish using only these ingredients, plus salt, oil, and pepper. Give it a name, a cooking time, and clear steps for a beginner."

Add a spending cap. Remix calls cost money. Limit each user to a reasonable number of remixes per day. A simple counter in the database works.

## Step 6: make it beautiful, 45 minutes

A working app is good. A beautiful app is better. Ask Claude to improve the design.

- "Make the home page warm and friendly, with a clear headline and a big Add Recipe button."
- "Style the recipe cards with a photo area, a title, and tags for cooking time."
- "Make the app work well on a phone. Big buttons, readable text, no sideways scrolling."

Check the design on your phone. Fix anything that looks broken. Ask Claude to screenshot and critique the design if you have Playwright set up. Small polish makes a big difference.

## Step 7: deploy to Vercel, 30 minutes

Deploying puts your app on the internet.

Connect your code to Vercel. Add the same environment variables in Vercel's settings: your Supabase URL, your Supabase key, and your Anthropic key. Deploy. Vercel gives you a link, such as `recipe-box.vercel.app`.

Open the link. Sign up as a new user. Add a recipe. Tap Remix. If it works live, you have shipped.

Share the link with one friend. Ask them to sign up and add a recipe. Watch for errors. Fix them. Then share it more widely.

## Step 8: the pre-launch safety check

Before you share the link widely, run this check.

- [ ] Each user sees only their own recipes.
- [ ] The Anthropic key is not in any browser code. Search the code for the key.
- [ ] The `.env.local` file is not in version control.
- [ ] Row-level security is on, and you tested it with two users.
- [ ] Remix has a per-user daily limit.
- [ ] Passwords are handled by Supabase, not stored by you.
- [ ] The app works on a phone.

> NOTE: Your Anthropic key is the most valuable secret in this build. It lives on the server only, in environment variables. If it ever leaks into browser code or a public file, revoke it and make a new one. A leaked key can be used by anyone to spend your money.

## Level-ups

- **Photos.** Let users upload a photo per recipe, stored in Supabase Storage.
- **Sharing.** Let a user share one recipe with a public link, while the rest stay private.
- **Meal plan.** A weekly plan page that picks seven recipes and builds a shopping list.
- **Ratings.** Let users rate recipes and sort by their favourites.

## Troubleshooting

- **Login fails.** Check the Supabase URL and key in your environment file. Check that email logins are enabled in Supabase.
- **Recipes are visible to everyone.** Row-level security is off or the rule is wrong. Turn it on and test with two users.
- **Remix fails.** Check the server route logs in Vercel. Check the Anthropic key and the spending cap.
- **Deploy fails.** Read the Vercel build log. The error is usually a missing environment variable.

> TRY IT: Write your one-page spec today, even before you start building. A spec you can read in one minute is a spec Claude can follow. Then scaffold the app and get the login page working. That first working page is the hardest step, and the most satisfying.

## Check yourself

1. Why must the Anthropic key live on the server only?
**Answer:** Because anything in the browser is visible to users, and a leaked key lets anyone spend your money.

2. What does row-level security do?
**Answer:** It is a set of database rules that keep each user's data private, so a user can only see their own rows.

3. What should you test with two users?
**Answer:** That neither user can see the other's recipes.

4. Why write a spec before you write code?
**Answer:** Because a short, clear spec keeps Claude on track and stops the build from drifting.

## In short

- Write a one-page spec before you build anything.
- Scaffold with Claude Code, then set up Supabase with row-level security.
- Build recipes, search, and editing one feature at a time.
- Add Remix as a server route so the AI key never reaches the browser.
- Deploy on Vercel, run the safety check, then share the link.
- Keep the key secret, cap the spending, and test with two users.
