Process and Parts of Article Writer
1. Scrape
    a. Take in a keyword that is a question
    b. Gets the top article search result
        - Needs to make sure it does not pull an ad link result, else pull next result, goes until top 3 are used
        - Needs to make sure it does not pull a link that has already been used before
            - Need this list to be saved everytime I use it
            - Can be a dictionary? Or using Database?
    c. Get h2 keywords from either the "People Also Ask" or "Related Searches"
    e. Uses h2 keywords and repeats step (b)
    d. Add Sports Quiz Link as dictionary keys with keywords as values
    f. Scrape content from the article links

2. Summarize

3. Spin

6/21/21
- Working on building an article scraper that takes in a url and formats the text and headers properly
- Tested Quillbot, using all three features (summarize, spin, grammar check)
    - Summary tool was questionable

6/22/21
- Working on article summarizer and spinner, testing out nlpcloud
    - Testing plagerism on 1text.com
        - Only using summary tool (nlpcoud), 0.4% unique
        - Only using spinner (Quillbot), 17.25% unique
        - Using both, 100% unique
    - Spinners Test:
        1. Quillbot
        2. WordAI
        3. Spin Rewriter
        4. Clever Spinner

6/22-6/23/21
- Working on automating Quillbot with selenium

7/1/21
- Converting functions/files into classes to be used on Google Colab and their GPU
