---
summary: test page.
authors:
    - Waylan Limberg
    - Tom Christie
date: 2018-07-10
some_url: https://example.com
status: new
draft: true

---

# test page

## admonition

??? example "Examples"
    ### admonitions
    !!! note

        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
        nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
        massa, nec semper lorem quam in massa.

    !!! abstract "abstract-icon"

        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
        nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
        massa, nec semper lorem quam in massa.

    ??? info "info-collasaple"

        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
        nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
        massa, nec semper lorem quam in massa.

    !!! tip inline

        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
        nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
        massa, nec semper lorem quam in massa.

    !!! success inline end

        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
        nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
        massa, nec semper lorem quam in massa.

    !!! question

        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
        nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
        massa, nec semper lorem quam in massa.

    ???+ warning

        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
        nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
        massa, nec semper lorem quam in massa.

        ??? failure

            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
            nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
            massa, nec semper lorem quam in massa.

    !!! danger

        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
        nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
        massa, nec semper lorem quam in massa.

    !!! bug

        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
        nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
        massa, nec semper lorem quam in massa.

    !!! example

        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
        nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
        massa, nec semper lorem quam in massa.

    !!! quote

        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
        nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
        massa, nec semper lorem quam in massa.

## annotation

??? example "Examples"
    ??? tip
        Indentation is important Here

    - Lorem ipsum dolor sit amet, (1) consectetur adipiscing elit.
        { .annotate }
    
        1.  :man_raising_hand: I'm an annotation! (1)
            { .annotate }

            1.  :woman_raising_hand: I'm an annotation as well! :fontawesome-regular-face-laugh-wink:

    -   some text , (1) text.
        { .annotate }

        1.  :smile: some text

            ```py
            # some code
            print()
            
            ...
            ```
    
    ???+ example annotate "another example (1)"
        `can also host annotations by adding the annotate modifier after the type qualifier, which is similar to how inline blocks work`.
        !!! example
            -   Lorem ipsum dolor sit amet, (2) some.

    1.  :man_raising_hand: I'm an annotation!
    2.  :woman_raising_hand: I'm an annotation as well!

    ???+ example "markdown in html"
        <div class="annotate" markdown>

        > Lorem ipsum dolor sit amet, (1) consectetur adipiscing elit.

        </div>

        1.  :man_raising_hand: I'm an annotation!
    

## tasklist & defination list

??? example "Examples"
    ### DEF LIST

    `Lorem ipsum dolor sit amet`

    :   Sed sagittis eleifend rutrum. Donec vitae suscipit est. Nullam tempus
        tellus non sem sollicitudin, quis rutrum leo facilisis.

    `Cras arcu libero`

    :   Aliquam metus eros, pretium sed nulla venenatis, faucibus auctor ex. Proin
        ut eros sed sapien ullamcorper consequat. Nunc ligula ante.

        Duis mollis est eget nibh volutpat, fermentum aliquet dui mollis.
        Nam vulputate tincidunt fringilla.
        Nullam dignissim ultrices urna non auctor.

    ### TASK LIST

    - [x] Lorem ipsum dolor sit amet, consectetur adipiscing elit
    - [ ] Vestibulum convallis sit amet nisi a tincidunt
        * [x] In hac habitasse platea dictumst
        * [x] In scelerisque nibh non dolor mollis congue sed et metus
        * [ ] Praesent sed risus massa
    - [ ] Aenean pretium efficitur erat, donec pharetra, ligula non scelerisque

## content tabs and annotation

??? example "Examples"
    ### CONTENT TABS

    === "tab 1"
        
        ```py
        # some code
        print()
        ...
        ```
        
        tab one (1)
        { .annotate }

        1. :man_raising_hand: I'm an annotation!

    === "tab 2"
        tab two (1)
        { .annotate }

        1. :woman_raising_hand: I'm an annotation too!

## code block annotation

??? example "Examples"
    ### code block with annotation.

    ```txt
    # syntex: # (1)!
    # usage
    ... some code # (1)!
    ```

    ```py title="Example"
    # or use { .yaml .annotate }
    theme:
    features:
        - content.code.annotate # (1)!
    ```
    
    1.  :man_raising_hand: I'm a code annotation! I can contain `code`, __formatted
        text__, images, ... basically anything that can be written in Markdown.
    
    ???+ tip "Marker Syntax"
        In case if you are wondering! How?
        Here's how to use code annotation markers:
        
        -   Code block with marker
        -   Followed by content list
        -   `#!python hello()`
        
        ````markdown title="Markdown-usage-example"
        ```py
        def hello(): # (1)!
            print("Hello")
        ```

        1.  :man_raising_hand: Say's hello!!
        ````

        Here's the result:

        ```py title="Result" linenums="1" hl_lines="1-2"
        def hello(): # (1)!
            print("Hello")
        ```

        1.  :man_raising_hand: Say's hello!!

## code block with exteranal files/code snippets

??? example "Examples"
    ### Code snippets
    --8<-- "docs/tags.md:3"
    ---
    ```markdown title="tags.md" linenums="1" hl_lines="1"
    --8<-- "docs/tags.md"
    ```
    ---
    :octicons-file-code-24:{ .filename }
    ```markdown
    # tags.md
    <!-- this commment won't be shown -->
    >>>
    --8<-- "docs/tags.md:tagsdemo:5"
    <<<
    ```

## tooltips

??? example "Examples"
    ### Tooltips
    The HTML specification is maintained by the W3C.
    ---
    [Hover Me](https://www.example.com "this is tool tip")
    ---
    [Hover me][example]
    [example]: https://example.com "I'm a tooltip!"
    ---
    :material-information-outline:{ title="Important information" }

## button

- [Admonition]

  [Admonition]: ./test.md#admonitions

??? example "Examples"
    [Annotation Section :fontawesome-solid-paper-plane:](#annotation){ .md-button }
    ---

## footnotes

??? example "Examples"
    Lorem ipsum[^1] dolor sit amet, consectetur adipiscing elit.[^2]

    [^1]: Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    [^2]:
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
        nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
        massa, nec semper lorem quam in massa.

## links

??? example "Examples"
    see [footnotes](#footnotes) and [admonitions](#admonitions) section

## grid

??? example "Examples"
    <div class="grid cards" markdown>

    - :fontawesome-brands-html5: __HTML__ for content and structure
    - :fontawesome-brands-js: __JavaScript__ for interactivity
    - :fontawesome-brands-css3: __CSS__ for text running out of boxes
    - :fontawesome-brands-internet-explorer: __Internet Explorer__ ... huh?
    
    </div>
    
    ---
    
    <div class="grid cards" markdown>
    
    - :material-clock-fast:{ .lg .middle } __Set up in 5 minutes__
    
        ---
    
        Install [`mkdocs-material`](#) with [`pip`](#) and get up
        and running in minutes
    
        [:octicons-arrow-right-24: Getting started](#)
    
    - :fontawesome-brands-markdown:{ .lg .middle } __It's just Markdown__
    
        ---
    
        Focus on your content and generate a responsive and searchable static site
    
        [:octicons-arrow-right-24: Reference](#)
    
    - :material-format-font:{ .lg .middle } __Made to measure__
    
        ---
    
        Change the colors, fonts, language, icons, logo and more with a few lines
    
        [:octicons-arrow-right-24: Customization](#)
    
    - :material-scale-balance:{ .lg .middle } __Open Source, MIT__
    
        ---
    
        Material for MkDocs is licensed under MIT and available on [GitHub]
    
        [:octicons-arrow-right-24: License](#)
    
    </div>

    ---
    
    <div class="grid" markdown>

    :fontawesome-brands-html5: __HTML__ for content and structure
    { .card }

    :fontawesome-brands-js: __JavaScript__ for interactivity
    { .card }

    :fontawesome-brands-css3: __CSS__ for text running out of boxes
    { .card }

    > :fontawesome-brands-internet-explorer: __Internet Explorer__ ... huh?

    </div>
    
    ---
    
    <div class="grid" markdown>

    === "Unordered list"

        * Sed sagittis eleifend rutrum
        * Donec vitae suscipit est
        * Nulla tempor lobortis orci

    === "Ordered list"

        1. Sed sagittis eleifend rutrum
        2. Donec vitae suscipit est
        3. Nulla tempor lobortis orci

    ``` title="Content tabs"
    === "Unordered list"

        * Sed sagittis eleifend rutrum
        * Donec vitae suscipit est
        * Nulla tempor lobortis orci

    === "Ordered list"

        1. Sed sagittis eleifend rutrum
        2. Donec vitae suscipit est
        3. Nulla tempor lobortis orci
    ```

    </div>

## grid with image

??? example "Examples"
    <div class="grid cards" markdown>
    ![Image title](https://dummyimage.com/600x400/){ width="400" }
    ![Image title](https://dummyimage.com/600x400/){ width="400" }
    ![Image title](https://dummyimage.com/600x400/){ width="100" }
    <figure markdown="span">
        ![Image title](https://dummyimage.com/600x400/){ width="500" }
        <figcaption>Tulum, Mexico. Credit: Blueswen</figcaption>
    </figure>
    ![Image title](https://dummyimage.com/600x400/){ width="500" data-title="Cabo da Roca, Portugal. Credit: Blueswen" data-description=".custom-desc1" data-caption-position="right"}
    <div class="glightbox-desc custom-desc1">
        <p>Saint George's Castle is a historic castle in the Portuguese capital of Lisbon, located in the freguesia of Santa Maria Maior.</p>
        <p>Human occupation of the castle hill dates to at least the 8th century BC while the first fortifications built date from the 1st century BC.</p>
    </div>
    </div>
    ---
    ![Image title](https://dummyimage.com/600x400/){ width="300" }
    /// caption
    Image caption
    ///

## test

??? example "Examples"
    demo
