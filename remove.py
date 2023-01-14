import os

if __name__ == '__main__':
    for file in os.listdir("video"):
        if file.endswith("tc.ass"):
            os.remove("video/{}".format(file))
        print(file)
