---
summary: test page.
authors:
    - Waylan Limberg
    - Tom Christie
date: 2018-07-10
some_url: https://example.com
status: new
# draft: false

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
    [:octicons-file-code-24:][]{: .filename }
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

## test

??? example "Examples"
    demo
