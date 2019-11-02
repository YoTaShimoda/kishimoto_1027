import glob

def numfour_return_file_path():
    numfour = glob.glob('/Users/yota/kishimoto_1027/result/result4/*')
    numfour = sorted(numfour)
    return numfour

def numfive_return_file_path():
    numfive = glob.glob('/Users/yota/kishimoto_1027/result/result5/*')
    numfive = sorted(numfive)
    return numfive
