vote = input("Voting...\nEnter 'con' for Conservative and 'lab' for Labour")

con = "con"
lab = "lab"

if vote.lower() == con:
    print("Vote registered for Conservative")
elif vote.lower() == lab:
    print("Vote registered for Labour")
else:
    print("Sorry voting party unrecognised")