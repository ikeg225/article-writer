import spacy

# Use en_core_web_sm for efficiency and en_core_web_trf for accuracy

nlp = spacy.load("en_core_web_sm") 

def para_token(x):
    '''
    Takes in paragraph string and returns a list of tokenized string values.
    '''
    lis, doc = [], nlp(x)
    for token in doc:
        lis.append(token.text)
    return lis

def article_token(x):
    '''
    Takes in a list of paragraphs and tokenizes each.
    '''
    lis = []
    for i in x:
        lis.append(para_token(i))
    return lis


# Testing two functions above and counting tokens

article1 = ["LeBron James, in full LeBron Raymone James, byname King James, (born December 30, 1984, Akron, Ohio, U.S.), American professional basketball player who is widely considered one of the greatest all-around players of all time and who won National Basketball Association (NBA) championships with the Miami Heat (2012 and 2013), the Cleveland Cavaliers (2016), and the Los Angeles Lakers (2020).",
"A locally known basketball prodigy since elementary school, James was named Ohio’s Mr. Basketball (high-school player of the year) three times while leading Akron’s St. Vincent–St. Mary High School to three Ohio state championships in his four years on the team. He became a national media sensation in his junior year after appearing on the cover of Sports Illustrated, where he was billed by the magazine as “The Chosen One.” James was the consensus national high-school player of the year in his senior season, and he was selected by the Cleveland Cavaliers with the first overall selection of the 2003 NBA draft. Additionally, he signed an unprecedented $90 million endorsement contract with the Nike shoe company before he ever played a professional game.",
"Despite the pressures brought on by these singular circumstances, James led the Cavaliers in scoring, steals, and minutes played over the course of the 2003–04 season, winning the league’s Rookie of the Year award in the process. A 6-foot 8-inch (2.03-metre) “point forward” who was as adept at bringing the ball down the court as at playing near the basket, James presented a unique challenge for opposing teams; his unmatched athleticism and well-muscled body would not have been out of place in the National Football League.",
"His game progressed over the following years. He was voted one of the starting forwards on the Eastern Conference All-Star team during his second season, and in his third season he led the Cavaliers to their first playoff berth in nine years. These accomplishments were exceeded during the 2006–07 season, when James guided Cleveland to the franchise’s first berth in the NBA finals. After the Cavaliers upset the favoured Detroit Pistons in the Eastern Conference finals, the Cavaliers were swept by the San Antonio Spurs in the NBA finals, but James’s impressive postseason play led many observers to place him among the very best players in the league. He led the NBA in scoring during the 2007–08 season and earned first team All-NBA honours, but the Cavaliers lost to the eventual champion Boston Celtics in a dramatic seven-game series in the Eastern Conference semifinals. James piloted the Cavaliers to a team-record 66 wins during the 2008–09 season, which helped to earn him the league’s Most Valuable Player (MVP) award. The following season James averaged nearly 30 points per game as he was again named MVP.",
"At the end of the 2009–10 season, James became arguably the most sought-after free agent in NBA history when his contract with the Cavaliers expired, and he began a prolonged courtship process with a number of teams that had in some cases been planning for his free agency for over two years. In an unprecedented hour-long television special, criticized by many for its undue grandiosity, James announced that he was signing with the Heat. He helped Miami reach the NBA finals in his first year with the team, but the Heat lost the championship to the Dallas Mavericks. In the 2011–12 season James averaged 27.1 points per game and won his third MVP award while helping Miami advance to its second consecutive NBA finals appearance. Backed by his stellar play—James was named the finals MVP—the Heat defeated the Oklahoma City Thunder to win the championship.",
"He had arguably his greatest individual season in 2012–13, as he averaged 26.8 points, 7.3 assists, and a career-high 8.0 rebounds per game while posting a .565 field-goal percentage, a remarkable rate of made shots for someone who so frequently played away from the basket. James also helped Miami win 27 consecutive games that season (the second longest such streak in NBA history), and he was rewarded with his fourth league MVP award. In the following postseason, the Heat defeated the San Antonio Spurs in a seven-game series to win the NBA championship, and James was again named the finals MVP. He continued his stellar play in the following season, even increasing his shooting percentage by .002, and he again led the Heat to an appearance in the NBA finals. However, Miami lost that rematch with the Spurs in a five-game series.",
"After that finals loss, James opted out of his contract with the Heat, leaving an aging Miami roster, and—after a week of frenzied speculation among fans and media—he decided to return to Cleveland. Although his 25.3 points per game was James’s lowest scoring average since his rookie season, he nevertheless guided a young and inexperienced Cavaliers roster to the second best record in the Eastern Conference in 2014–15. In the following postseason he led an injury-laden Cleveland team to just two playoff losses en route to a berth in the NBA finals. There James had one of the greatest individual performances in finals history, averaging 35.8 points, 13.3 rebounds, and 8.8 assists per game while leading the undermanned Cavaliers to the franchise’s first two finals victories before ultimately losing a six-game series to the Golden State Warriors.",
"James had another strong regular season in 2015–16 but, once again, truly shined in the playoffs. He led the Cavaliers to a rematch against the Warriors, who had set a league record with 73 wins during the regular season, in the NBA finals. There the Cavaliers became the first team to come back from a 3–1 finals deficit to capture the first title in franchise history and end a 52-year title drought for Cleveland professional sports teams. James averaged 29.7 points, 11.3 rebounds, 8.9 assists, 2.6 steals, and 2.3 blocks per game in the finals—becoming the first person to lead all five statistical categories for players on both teams in the finals—and was unanimously named finals MVP.",
"In 2016–17 James had arguably his best regular season by setting career highs with averages of 8.7 assists and 8.6 rebounds per game while still scoring 26.4 points per game. He sustained his excellence in the Eastern Conference playoffs, scoring 32.5 points per game (which included his 5,988th career postseason point, breaking Michael Jordan’s all-time NBA playoff scoring record) while leading the Cavaliers to a third consecutive match-up against the Warriors in the NBA finals. There Cleveland could not overcome the team James referred to as a “juggernaut,” losing to the Warriors in five games despite James becoming the first player in NBA history to average a triple-double over the course of the finals (with 33.6 points, 12 rebounds, and 10 assists per game).",
"In 2017–18 he played a full 82-game regular season for the first time in his career and led the NBA in minutes played per game (36.9) while averaging 27.5 points, 8.6 rebounds, and a new career-high 9.1 assists per game. James again excelled in the following playoffs, scoring more than 40 points seven times in the team’s 18 Eastern Conference postseason games (which included two seven-game series) to lead the Cavaliers to their fourth straight NBA finals series against the Warriors. He continued his strong individual play in the finals, but it was not enough to overcome Golden State’s overwhelming talent advantage, and the Warriors swept the series.",
"In the following off-season, James, a free agent, joined the Los Angeles Lakers. He continued to play at a high level, averaging 27.4 points, 8.5 rebounds, and 8.3 assists per game, but he missed significant playing time because of an injury (a strained groin) for the first time in his career. The Lakers struggled in his absence and ultimately finished the 2018–19 season with a 37–45 record, ending James’s personal playoff streak at 13 seasons. The following season was disrupted by the COVID-19 pandemic, which caused a four-month suspension. Play resumed in July 2020 with a shortened schedule, and the Lakers ultimately defeated the Miami Heat to claim the franchise’s 17th NBA title. James’s dominating performance—he averaged 29.8 points, 11.8 rebounds, and 8.5 assists per game—earned him his fourth finals MVP award.",
"In addition to his achievements in the NBA, James was a member of the U.S. men’s Olympic basketball teams that won the bronze medal at the 2004 Games, the gold medal at the 2008 Games, and the gold at the 2012 Games. He also published a memoir, Shooting Stars (2009; cowritten with Buzz Bissinger), that chronicles his years as a high-school standout."]

def token_counter(x):
    '''
    Takes in a list of list that is tokenized and returns a list with the token count for each tokenized list. 
    '''
    lis = []
    for i in x:
        lis.append(len(i))
    return lis

lis1 = article_token(article1)
print(lis1)
lis2 = token_counter(lis1)
print(lis2)