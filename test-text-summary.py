import nlpcloud


client = nlpcloud.Client("bart-large-cnn", "f08cfeac6052670bfa75c7180548c43df23e2a19")
# Returns a json object.
print(
    client.summarization("""The BRRRR (Buy, Rehab, Rent, Refinance, Repeat) Method is a real estate investment strategy that involves flipping distressed property, renting it out, and then cash-out refinancing it in order to fund further rental property investment. One of the main differences between the BRRRR method and a conventional investment property strategy is the focus on investing in distressed properties and on refinancing the purchased property in order to buy another one. If you’re a real estate investor considering this type of strategy, read on to learn about how the BRRRR Method works, its pros and cons and if it’s the right method for your financial or real estate investing goals.""")
)