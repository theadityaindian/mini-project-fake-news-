import random
subject = {
    "sharukh khan ",
    "virat kohli",
    "Nirmala sitharaman",
    "aditya birla",
    "sundar pichai",
    "elon musk",
    "a lesbin group",
"a gay with lay ",
"housefull made them famous"
}
actions = {
    "riiding a donkey ",

"gst free goods",
"war with china",
"night out"
}
destination = {"goa ",
"london",   
    "paris",
    "nallasupara",
            "dubai", 
            "shamshan gali",
            "anderi gali"}

where= random.choice    (list(destination))
who= random.choice(list(subject))       
what= random.choice(list(actions))
headline=F"BREAKING NEWS : {who} is  {what}  in {where} "
print(headline)

user_input=input("Press enter to generate news headline?yes/no").strip
if user_input.lower()=="yes":
    where= random.choice    (list(destination))
    who= random.choice(list(subject))       
    what= random.choice(list(actions))
    headline=F"BREAKING NEWS : {who} is  {what}  in {where} "
    print(headline)