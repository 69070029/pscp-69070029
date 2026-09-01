"""3d"""
def main():
    """input"""
    xyz1 = (input()).split()
    xyz2 = (input()).split()

    distance = ((int(xyz1[0]) - int(xyz2[0]))**2
                + (int(xyz1[1]) - int(xyz2[1]))**2
                + (int(xyz1[2]) - int(xyz2[2]))**2)**0.5

    print(f"{distance:.2f}")

main()
