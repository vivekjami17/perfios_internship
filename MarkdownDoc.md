[](#headings)Headings
---------------------

To create a heading, add one to six # symbols before your heading text. The number of # you use will determine the size of the heading.

# The largest heading
## The second largest heading
###### The smallest heading
    

[//]: # (![H1, H2, and H6 headings]&#40;https://docs.github.com/assets/cb-8119/mw-1000/images/help/writing/headings-rendered.webp&#41;)

When you use two or more headings, GitHub automatically generates a table of contents which you can access by clicking within the file header. Each heading title is listed in the table of contents and you can click a title to navigate to the selected section.

![Screenshot highlighting the table of contents](https://docs.github.com/assets/cb-47415/mw-1000/images/help/repository/headings_toc.webp)

[](#styling-text)Styling text
-----------------------------

You can indicate emphasis with bold, italic, strikethrough, subscript, or superscript text in comment fields and `.md` files.

| Style                  | Syntax              | Keyboard shortcut                         | Example                              | Output                    |
|------------------------|---------------------|-------------------------------------------|--------------------------------------|---------------------------|
| Bold                   | `** **` or `__ __`  | Command+B (Mac) or Ctrl+B (Windows/Linux) | `**This is bold text**`              | **This is bold text**     |
| Italic                 | `* *` or `_ _`      | Command+I (Mac) or Ctrl+I (Windows/Linux) | `*This text is italicized*`          | _This text is italicized_ |
| Strikethrough          | `~~ ~~`             | `~~This was mistaken text~~`              | `~~This was mistaken text~~`         |~~This was mistaken text~~     |
| Bold and nested italic | `** **` and `_ _`   | `**This text is _extremely_ important**`  | `**This text is _extremely_ important**` |**This text is _extremely_ important**|
| All bold and italic    | `*** ***`           | `***All this text is important***`        | `**_All this text is important_**`     |**_All this text is important_**  |
| Subscript              | `<sub> </sub>`      | `<sub>This is a subscript text</sub>`     | `<sub>This is a subscript text</sub>`  |<sub>This is a subscript text</sub>| 
| Superscript            | `<sup> </sup>`      | `<sup>This is a superscript text</sup>`   | `<sup> This is a superscript text</sup>` |<sup> This is a superscript text</sup>| 

[](#quoting-text)Quoting text
-----------------------------

You can quote text with a \>.

    Text that is not a quote
    
    > Text that is a quote
    

![quoted text](https://docs.github.com/assets/cb-12181/mw-1000/images/help/writing/quoted-text-rendered.webp)

**Tip:** When viewing a conversation, you can automatically quote text in a comment by highlighting the text, then typing R. You can quote an entire comment by clicking , then **Quote reply**. For more information about keyboard shortcuts, see "[Keyboard shortcuts](https://docs.github.com/en/get-started/using-github/keyboard-shortcuts)."

[](#quoting-code)Quoting code
-----------------------------

You can call out code or a command within a sentence with single backticks. The text within the backticks will not be formatted. You can also press the Command+E (Mac) or Ctrl+E (Windows/Linux) keyboard shortcut to insert the backticks for a code block within a line of Markdown.

    Use `git status` to list all new or modified files that haven't yet been committed.
    

![nline code block](https://docs.github.com/assets/cb-4680/mw-1000/images/help/writing/inline-code-rendered.webp)

To format code or text into its own distinct block, use triple backticks.


>Some basic Git commands are:<br>
>\`\`\`<br>
>git status<br>
>git add<br>
>git commit<br>
>\`\`\`

![code block](https://docs.github.com/assets/cb-4274/mw-1000/images/help/writing/code-block-rendered.webp)

For more information, see "[Creating and highlighting code blocks](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-and-highlighting-code-blocks)."

If you are frequently editing code snippets and tables, you may benefit from enabling a fixed-width font in all comment fields on GitHub. For more information, see "[About writing and formatting on GitHub](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/about-writing-and-formatting-on-github#enabling-fixed-width-fonts-in-the-editor)."

[](#supported-color-models)Supported color models
-------------------------------------------------

In issues, pull requests, and discussions, you can call out colors within a sentence by using backticks. A supported color model within backticks will display a visualization of the color.

    The background color should be `#ffffff` for light mode and `#0d1117` for dark mode.
    
The background color should be `#ffffff` for light mode and `#0d1117` for dark mode.

![supported color model](https://docs.github.com/assets/cb-13280/mw-1000/images/help/writing/supported-color-models-rendered.webp)

Here are the currently supported color models.

|Color|Syntax|Example|Output|
|-----|------|-------|------|
|HEX|`` `#RRGGBB` ``|`` `#0969DA` ``|![Rendered supported color model in HEX format.](https://docs.github.com/assets/cb-1560/mw-1000/images/help/writing/supported-color-models-hex-rendered.webp)|
|RGB|`` `rgb(R,G,B)` ``|`` `rgb(9, 105, 218)` ``|![Rendered supported color model in RGB format.](https://docs.github.com/assets/cb-1962/mw-1000/images/help/writing/supported-color-models-rgb-rendered.webp)|
|HSL|`` `hsl(H,S,L)` ``|`` `hsl(212, 92%, 45%)` ``|![Rendered supported color model in HSL format.](https://docs.github.com/assets/cb-2068/mw-1000/images/help/writing/supported-color-models-hsl-rendered.webp)|



**Notes:**

*   A supported color model cannot have any leading or trailing spaces within the backticks.
*   The visualization of the color is only supported in issues, pull requests, and discussions.

[](#links)Links
---------------

You can create an inline link by wrapping link text in brackets `[ ]`, and then wrapping the URL in parentheses `( )`. You can also use the keyboard shortcut Command+K to create a link. When you have text selected, you can paste a URL from your clipboard to automatically create a link from the selection.

You can also create a Markdown hyperlink by highlighting the text and using the keyboard shortcut Command+V. If you'd like to replace the text with the link, use the keyboard shortcut Command+Shift+V.

`This site was built using [GitHub Pages](https://pages.github.com/).`

![link](https://docs.github.com/assets/cb-4329/mw-1000/images/help/writing/link-rendered.webp)

**Tip:** GitHub automatically creates links when valid URLs are written in a comment. For more information, see "[Autolinked references and URLs](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/autolinked-references-and-urls)."

[](#section-links)Section links
-------------------------------

You can link directly to a section in a rendered file by hovering over the section heading to expose the link:

![Section link within the README file for the github/scientist repository](https://docs.github.com/assets/cb-25655/mw-1000/images/help/repository/readme-links.webp)

[](#relative-links)Relative links
---------------------------------

You can define relative links and image paths in your rendered files to help readers navigate to other files in your repository.

A relative link is a link that is relative to the current file. For example, if you have a README file in root of your repository, and you have another file in _docs/CONTRIBUTING.md_, the relative link to _CONTRIBUTING.md_ in your README might look like this:

    [Contribution guidelines for this project](docs/CONTRIBUTING.md)
    

GitHub will automatically transform your relative link or image path based on whatever branch you're currently on, so that the link or path always works. The path of the link will be relative to the current file. Links starting with `/` will be relative to the repository root. You can use all relative link operands, such as `./` and `../`.

Relative links are easier for users who clone your repository. Absolute links may not work in clones of your repository - we recommend using relative links to refer to other files within your repository.

[](#images)Images
-----------------

You can display an image by adding ! and wrapping the alt text in `[ ]`. Then wrap the link for the image in parentheses `()`.

![This is an image](https://myoctocat.com/assets/images/base-octocat.svg)

[//]: # (![Github Image]&#40;https://docs.github.com/assets/cb-49261/mw-1000/images/help/writing/image-rendered.webp&#41;)

GitHub supports embedding images into your issues, pull requests, discussions, comments and `.md` files. You can display an image from your repository, add a link to an online image, or upload an image. For more information, see "[Uploading assets](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#uploading-assets)."

**Tip:** When you want to display an image which is in your repository, you should use relative links instead of absolute links.

Here are some examples for using relative links to display an image.

|Context|Relative Link|
|-------|-------------|
|In a `.md` file on the same branch|`/assets/images/electrocat.png`|
|In a `.md` file on another branch|`/../main/assets/images/electrocat.png`|
|In issues, pull requests and comments of the repository|`../blob/main/assets/images/electrocat.png?raw=true`|
|In a `.md` file in another repository|`/../../../../github/docs/blob/main/assets/images/electrocat.png`|
|In issues, pull requests and comments of another repository|`../../../github/docs/blob/main/assets/images/electrocat.png?raw=true`|

**Note**: The last two relative links in the table above will work for images in a private repository only if the viewer has at least read access to the private repository which contains these images.

For more information, see "[Relative Links](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#relative-links)."

### [](#specifying-the-theme-an-image-is-shown-to)Specifying the theme an image is shown to

You can specify the theme an image is displayed for in Markdown by using the HTML `<picture>` element in combination with the `prefers-color-scheme` media feature. We distinguish between light and dark color modes, so there are two options available. You can use these options to display images optimized for dark or light backgrounds. This is particularly helpful for transparent PNG images.

For example, the following code displays a sun image for light themes and a moon for dark themes:

    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://user-images.githubusercontent.com/25423296/163456776-7f95b81a-f1ed-45f7-b7ab-8fa810d529fa.png">
      <source media="(prefers-color-scheme: light)" srcset="https://user-images.githubusercontent.com/25423296/163456779-a8556205-d0a5-45e2-ac17-42d089e3c3f8.png">
      <img alt="Shows an illustrated sun in light mode and a moon with stars in dark mode." src="https://user-images.githubusercontent.com/25423296/163456779-a8556205-d0a5-45e2-ac17-42d089e3c3f8.png">
    </picture>
    

The old method of specifying images based on the theme, by using a fragment appended to the URL (`#gh-dark-mode-only` or `#gh-light-mode-only`), is deprecated and will be removed in favor of the new method described above.

[](#lists)Lists
---------------

You can make an unordered list by preceding one or more lines of text with \-, \*, or +.

    - George Washington
    * John Adams
    + Thomas Jefferson
    

![Rendered unordered list](https://docs.github.com/assets/cb-3302/mw-1000/images/help/writing/unordered-list-rendered.webp  )

To order your list, precede each line with a number.

    1. James Madison
    2. James Monroe
    3. John Quincy Adams
    

![Rendered ordered list](https://docs.github.com/assets/cb-3403/mw-1000/images/help/writing/ordered-list-rendered.webp)

### [](#nested-lists)Nested Lists

You can create a nested list by indenting one or more list items below another item.

To create a nested list using the web editor on GitHub or a text editor that uses a monospaced font, like [Visual Studio Code](https://code.visualstudio.com/), you can align your list visually. Type space characters in front of your nested list item, until the list marker character (\- or \*) lies directly below the first character of the text in the item above it.

1. First list item
   - First nested list item
     - Second nested list item


![Nested list with alignment highlighted](https://docs.github.com/assets/cb-5185/mw-1000/images/help/writing/nested-list-alignment.webp)
**Note**: In the web-based editor, you can indent or dedent one or more lines of text by first highlighting the desired lines and then using Tab or Shift+Tab respectively.

[//]: # (![List with two levels of nested items]&#40;https://docs.github.com/assets/cb-3697/mw-1000/images/help/writing/nested-list-example-1.webp&#41;)


To create a nested list in the comment editor on GitHub, which doesn't use a monospaced font, you can look at the list item immediately above the nested list and count the number of characters that appear before the content of the item. Then type that number of space characters in front of the nested list item.

In this example, you could add a nested list item under the list item `100. First list item` by indenting the nested list item a minimum of five spaces, since there are five characters (`100.` ) before `First list item`.

100. First list item
     - First nested list item
    

![List with a nested list item](https://docs.github.com/assets/cb-2411/mw-1000/images/help/writing/nested-list-example-3.webp)

You can create multiple levels of nested lists using the same method. For example, because the first nested list item has seven characters (`␣␣␣␣␣-␣`) before the nested list content `First nested list item`, you would need to indent the second nested list item by seven spaces.

100. First list item
     - First nested list item
       - Second nested list item
    

![List with two levels of nested items](https://docs.github.com/assets/cb-3655/mw-1000/images/help/writing/nested-list-example-2.webp)

For more examples, see the [GitHub Flavored Markdown Spec](https://github.github.com/gfm/#example-265).

[](#task-lists)Task lists
-------------------------

To create a task list, preface list items with a hyphen and space followed by `[ ]`. To mark a task as complete, use `[x]`.

- [ ] #739
- [ ] https://github.com/octo-org/octo-repo/issues/740
- [ ] Add delight to the experience when all tasks are complete :tada:
    

[//]: # (![task list]&#40;https://docs.github.com/assets/cb-64629/mw-1000/images/help/writing/task-list-rendered-simple.webp&#41;)

If a task list item description begins with a parenthesis, you'll need to escape it with \\:

- [ ] \(Optional) Open a followup issue
  `- [ ] \(Optional) Open a followup issue`

For more information, see "[About task lists](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/about-task-lists)."

[](#mentioning-people-and-teams)Mentioning people and teams
-----------------------------------------------------------

You can mention a person or [team](https://docs.github.com/en/organizations/organizing-members-into-teams) on GitHub by typing @ plus their username or team name. This will trigger a notification and bring their attention to the conversation. People will also receive a notification if you edit a comment to mention their username or team name. For more information about notifications, see "[About notifications](/en/account-and-profile/managing-subscriptions-and-notifications-on-github/setting-up-notifications/about-notifications)."

**Note:** A person will only be notified about a mention if the person has read access to the repository and, if the repository is owned by an organization, the person is a member of the organization.

`@github/support What do you think about these updates?`

![Rendered @mention](https://docs.github.com/assets/cb-3746/mw-1000/images/help/writing/mention-rendered.webp)

When you mention a parent team, members of its child teams also receive notifications, simplifying communication with multiple groups of people. For more information, see "[About teams](https://docs.github.com/en/organizations/organizing-members-into-teams/about-teams)."

Typing an @ symbol will bring up a list of people or teams on a project. The list filters as you type, so once you find the name of the person or team you are looking for, you can use the arrow keys to select it and press either tab or enter to complete the name. For teams, enter the @organization/team-name and all members of that team will get subscribed to the conversation.

The autocomplete results are restricted to repository collaborators and any other participants on the thread.

[](#referencing-issues-and-pull-requests)Referencing issues and pull requests
-----------------------------------------------------------------------------

You can bring up a list of suggested issues and pull requests within the repository by typing #. Type the issue or pull request number or title to filter the list, and then press either tab or enter to complete the highlighted result.

For more information, see "[Autolinked references and URLs](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/autolinked-references-and-urls)."

[](#referencing-external-resources)Referencing external resources
-----------------------------------------------------------------

If custom autolink references are configured for a repository, then references to external resources, like a JIRA issue or Zendesk ticket, convert into shortened links. To know which autolinks are available in your repository, contact someone with admin permissions to the repository. For more information, see "[Configuring autolinks to reference external resources](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/configuring-autolinks-to-reference-external-resources)."

[](#uploading-assets)Uploading assets
-------------------------------------

You can upload assets like images by dragging and dropping, selecting from a file browser, or pasting. You can upload assets to issues, pull requests, comments, and `.md` files in your repository.

[](#using-emoji)Using emoji
---------------------------

You can add emoji to your writing by typing `:EMOJICODE:`.

`@octocat :+1: This PR looks great - it's ready to merge! :shipit:`

![Rendered emoji](https://docs.github.com/assets/cb-7184/mw-1000/images/help/writing/emoji-rendered.webp)

Typing : will bring up a list of suggested emoji. The list will filter as you type, so once you find the emoji you're looking for, press **Tab** or **Enter** to complete the highlighted result.

For a full list of available emoji and codes, check out [the Emoji-Cheat-Sheet](https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md).

[](#paragraphs)Paragraphs
-------------------------

You can create a new paragraph by leaving a blank line between lines of text.

[](#footnotes)Footnotes
-----------------------

You can add footnotes to your content by using this bracket syntax:

    Here is a simple footnote[^1].
    
    A footnote can also have multiple lines[^2].
    
    You can also use words, to fit your writing style more closely[^note].
    
    [^1]: My reference.
    [^2]: Every new line should be prefixed with 2 spaces.
      This allows you to have a footnote with multiple lines.
    [^note]:
        Named footnotes will still render with numbers instead of the text but allow easier identification and linking.
        This footnote also has been made with a different syntax using 4 spaces for new lines.
    

The footnote will render like this:

![Rendered footnote](https://docs.github.com/assets/cb-6343/mw-1000/images/site/rendered-footnote.webp)

**Note**: The position of a footnote in your Markdown does not influence where the footnote will be rendered. You can write a footnote right after your reference to the footnote, and the footnote will still render at the bottom of the Markdown.

Footnotes are not supported in wikis.

[](#hiding-content-with-comments)Hiding content with comments
-------------------------------------------------------------

You can tell GitHub to hide content from the rendered Markdown by placing the content in an HTML comment.

<!-- This content will not appear in the rendered Markdown -->

[](#ignoring-markdown-formatting)Ignoring Markdown formatting
-------------------------------------------------------------

You can tell GitHub to ignore (or escape) Markdown formatting by using \\ before the Markdown character.

`Let's rename \*our-new-project\* to \*our-old-project\*`

![Rendered escaped character](https://docs.github.com/assets/cb-2978/mw-1000/images/help/writing/escaped-character-rendered.webp)

For more information, see Daring Fireball's "[Markdown Syntax](https://daringfireball.net/projects/markdown/syntax#backslash)."

[](#disabling-markdown-rendering)Disabling Markdown rendering
-------------------------------------------------------------

When viewing a Markdown file, you can click at the top of the file to disable Markdown rendering and view the file's source instead.

![Display Markdown as source](https://docs.github.com/assets/cb-17772/mw-1000/images/help/writing/display-markdown-as-source.webp)

Disabling Markdown rendering enables you to use source view features, such as line linking, which is not possible when viewing rendered Markdown files.