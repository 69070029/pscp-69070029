"""ijudge"""
def main():
    """input"""
    link = input()
    number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    if link[-1:] == '/': #44
        if link[:-5] != "https://ijudge.it.kmitl.ac.th/problems/":
            star = 9
        else:
            if link[-2] in number and link[-3] in number and link[-4] in number:
                star = link[-5]
            else:
                star = 9
    else: #43
        if link[:-4] != "https://ijudge.it.kmitl.ac.th/problems/":
            star = 9
        else:
            if link[-1] in number and link[-3] in number and link[-2] in number:
                star = link[-4]
            else:
                star = 9

    if star in ['0', '1', '2', '3']:
        print(f"{star} STAR")
    else:
        print("INVALID")

main()
