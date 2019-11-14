import glob

def numfour_return_file_path():
    numfour = glob.glob('result/result4/*')
    numfour = sorted(numfour)
    return numfour

def numfive_return_file_path():
    numfive = glob.glob('result/result5/*')
    numfive = sorted(numfive)
    return numfive

def numfour_before_and_after_file():
  numfour_file_paths = glob.glob('before_and_after_merge_file/no4/*')
  numfour_file_paths = sorted(numfour_file_paths)
  return numfour_file_paths

def numfive_before_ane_after_file():
  numfive = glob.glob('before_and_after_merge_file/no5/*')
  numfive = sorted(numfive)
  return numfive
