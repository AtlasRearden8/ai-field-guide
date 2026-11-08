# 4.3 n8n, click by click
<!-- original: ch. 47 -->

In the next 30 minutes, you will build a real AI app. It is a small web form. You type any note into it. Claude reads the note, writes a one-line summary, and tells you if it is urgent. Every step below shows what to click and what you should see. No code is needed.

Here is what you are building. A person opens a page with a form. They type a note, like "The printer on the third floor is smoking and the meeting starts in ten minutes." They press submit. The form sends the note to n8n. n8n sends the note to Claude. Claude answers with a short summary and a yes or no for urgent. Then n8n shows that answer on the screen.

You need two things before you start. First, n8n itself. Second, an Anthropic API key, which is the secret password that lets n8n talk to Claude. You can get one from the Anthropic website, in the API section of your account settings. Keep it secret, like any password.

> NOTE: Buttons move between versions. This chapter was written with n8n 2.x, the current stable line as of November 2026. If a button has moved, look for the same label nearby. The ideas have not changed, only the furniture.

## Step 1: Get n8n running

You have three ways to run n8n. Pick the one that fits you best.

The easiest way is **n8n Cloud**. Go to the n8n website and sign up for a free trial. They run n8n for you. There is nothing to install. This is the best choice if you just want to learn.

The second way is to run it on your own computer with one command. You need Node.js installed first. Then open your terminal and type `npx n8n`. Press Enter. Wait for it to say it is ready. Then open your browser and go to the address it shows you, usually `http://localhost:5678`. This way is free, and your data stays on your own machine.

The third way is **Docker**, which is a tool that runs programs in neat little boxes. If you already use Docker, you know what to do. If you do not, skip this way for now.

Whichever way you choose, the first screen asks you to create an owner account. That is just your name, email, and a password for n8n itself. Fill it in. You will land on a blank canvas. That empty canvas is your workshop. Every workflow you build starts here.

> TRY IT: Before you build anything, click around the blank canvas for two minutes. Find the button to add a node. Find the list of workflows on the left. Find the settings menu. Knowing where things live will save you clicks later.

## Step 2: Add a form trigger

A **trigger** is the box that starts your workflow. Here, the trigger is a form. When someone fills in the form, the workflow runs.

Click the plus button on the canvas. A panel opens with a search box. Type "Form Trigger". Click it. A new box appears on your canvas, with a settings panel on the right.

The settings ask you what the form should look like. Give the form a title, like "Note summariser". Add one field. Set the field type to text, or to a long text box if you want room for longer notes. Name the field "note". That name matters, because the next steps will look for a field called "note".

There is also a setting for what happens after someone submits. Leave it as it is for now. We will come back to it in Step 6.

Click the "Test step" button, or the button that lets you listen for a test event. n8n will now wait for someone to fill in the form. A test address will appear. Copy it.

## Step 3: Test the form and look at the data

Open the test address in a new browser tab. You should see your form, with its title and one text box. Type a test note. Try this one: "The printer on the third floor is smoking and the meeting starts in ten minutes." Press submit.

Go back to n8n. The trigger box should now show the data it received. Click on it. You will see JSON, the labelled-facts format from Chapter 4.2. It will look something like this:

```
{
  "note": "The printer on the third floor is smoking and the meeting starts in ten minutes."
}
```

That is your data. Everything after this step will read from that "note" field. If you do not see the data, check two things. First, did you use the test address, not the live one? Second, did you click the listen or test button before you submitted the form? Fix that, and try again.

This habit matters more than any other skill in n8n. Test one box. Look at its data. Then build the next box. Never build five boxes and test them all at once.

## Step 4: Add the AI step

Now add the brain. Click the plus button on the right side of your form box. Search for "AI Agent". Click it. A new box appears, joined to the form by a line.

The AI Agent box has settings of its own. The most important is the **prompt**, which is the instruction you give the AI. A prompt is just a message that tells the AI what to do. Write something like this:

"Read the note below. Write a one-line summary. Then say if it is urgent. Answer with two lines, like this: Summary: ... Urgent: yes or no. Note: "

But how does the note get into the prompt? That is where **expressions** come in. An expression is a little snippet that pulls data from an earlier box. In n8n, you type `=` to start an expression, and then you drag the field you want into the prompt. Drag the "note" field from the form box into your prompt, right after "Note: ". The prompt will now include whatever the person typed.

Save the box. Do not worry about the other settings yet. The defaults are fine for a first build.

> NOTE: An expression is just a way of saying "put the value from that box here." You will use them everywhere in n8n. If a value looks wrong, click the expression and check which box and field it points to.

## Step 5: Connect Claude

The AI Agent box needs a model to think with. A **model** is the AI itself, like Claude. The box has a small connection point for a chat model. Click it, and choose "Anthropic Chat Model" from the list.

A new box appears. It asks for your Anthropic API key. Paste the key you got earlier. If you have not got one yet, go to the Anthropic website, open your account settings, find the API section, and create a key. Then paste it here.

Next, pick a model. The list will show the Claude models available to you. For this build, any recent Claude model works. Pick the one marked as the standard choice, not the fastest or the most powerful. You can change it later.

Click save, and then test this box. If the key is right, the box will connect. If you see an error about authentication, the key is wrong or was copied with a missing character. Paste it again, carefully.

## Step 6: Show the answer on screen

The AI now writes its answer, but nobody sees it. The form needs a way to show it. That job belongs to a **Respond to Webhook** node, or to the form's own completion screen, depending on your n8n version.

The simple path: open your Form Trigger box again. Find the setting for what happens after submit. Choose the option that shows a message, often called "Show completion screen" or "Respond with text". In that message box, use an expression to pull in the AI's answer. Drag the AI Agent's output field into the message. Add a little text around it, like "Here is your summary:" and then the answer.

If your version uses a separate Respond node instead, add that node after the AI Agent box. Set its message to the same thing: your text plus the AI's output field.

Either way, the idea is the same. Take what the AI wrote. Show it to the person who filled in the form.

## Step 7: Run it end to end

Now test the whole thing. Go back to the form's test address. Type a different note. Try: "Reminder: buy milk, bread, and birthday candles before Friday."

Submit it. Wait a few seconds. You should see a screen with a one-line summary and "Urgent: no". If you see that, you built a working AI app. Well done.

If you see an error instead, do not panic. Read the error out loud. Then check the boxes in order, from left to right. Did the form receive the note? Did the AI box get the note? Did the model connect? Most errors are in one box, not in the whole workflow. Fix that box, and test again.

## Step 8: Publish it

So far, you have been using test addresses. They only work while you are listening. To make the form work any time, you need to **activate** the workflow. Look for the "Active" switch, usually at the top right of the screen. Turn it on.

When the workflow is active, n8n gives you a live address for the form. That is the real one. Share it with a friend. They can use your AI app without ever seeing n8n.

Congratulations. You have built, tested, and published a real AI workflow. It is small. It is also the same shape as every workflow in this book: trigger, gather, AI, act.

## If something goes wrong

Here are the four most common problems, and their fixes.

The form shows nothing. You are using the live address while the workflow is not active, or the test address after you stopped listening. Use the test address while testing, and the live address after you activate.

The AI says nothing, or the box shows an error about the model. Your API key is wrong, or you have run out of credit on your Anthropic account. Check the key, and check your balance on the Anthropic website.

The AI's answer is empty in the final message. Your expression points to the wrong field. Open the final box, click the expression, and drag the AI's output field in again.

The workflow runs, but slowly. AI takes a few seconds to think. That is normal. If it takes more than a minute, something is stuck. Stop the test, and run it again.

## Reference: the nodes you will use every day

You do not need to memorise this list. Just know it exists, and come back to it.

- **Form Trigger**: starts a workflow when someone fills in a form.
- **Webhook**: starts a workflow when another app sends it a message.
- **Schedule Trigger**: starts a workflow at a set time.
- **AI Agent**: lets an AI decide what to do, using tools you give it.
- **Chat Model**: connects the AI Agent to Claude, or another model.
- **HTTP Request**: talks to any API, as you learned in Chapter 4.2.
- **Set**: renames or reshapes data between boxes.
- **IF**: sends data down one path or another, based on a condition.
- **Code**: runs a small piece of JavaScript when the boxes are not enough.

## Ten n8n builds to try next

1. A daily news summary, sent to you every morning.
2. A form that turns ideas into tidy rows in a spreadsheet.
3. An email sorter that labels urgent mail.
4. A price watcher that tells you when something gets cheaper.
5. A meeting-notes summariser.
6. A Telegram bot that answers your questions.
7. A social media post scheduler.
8. A job-post watcher for a role you want.
9. A backup that saves your files to a second place.
10. A birthday reminder that messages you a week ahead.

> TRY IT: Pick one build from the list above. Do not build it yet. Write its five steps on paper: trigger, gather, AI, route, act. Then build only the trigger, and test it. Small steps, tested one at a time, are how every good workflow gets built.

## Check yourself

1. What is a trigger in n8n?
**Answer:** A trigger is the first box in a workflow. It starts the workflow when something happens, such as a form being filled in.

2. Why should you test one box at a time?
**Answer:** So you can see exactly which box has a problem, instead of guessing across five boxes at once.

3. What is an expression?
**Answer:** An expression is a snippet that pulls a value from an earlier box into a later one, such as putting the form's note into the AI's prompt.

4. What does activating a workflow do?
**Answer:** It turns the workflow on, so its live address works any time, not only while you are testing.

5. What do you need to connect Claude in n8n?
**Answer:** An Anthropic API key, pasted into the chat model box.

## In short

- You built a real AI app: a form, an AI step, and an answer on screen.
- The workflow shape is trigger, gather, AI, act.
- Test one box at a time, and look at the data it produces.
- Expressions pull values from earlier boxes into later ones.
- Activate the workflow to make its live address work any time.
- Start your next build the same way: one box, one test, then the next box.
