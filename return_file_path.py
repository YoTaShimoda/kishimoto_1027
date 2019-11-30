import glob

def numfour_heart():
  numfour = glob.glob('no4_heart/*')
  numfour = sorted(numfour)
  return numfour

def numfive_heart():
  numfive = glob.glob('no5_heart/*')
  numfive = sorted(numfive)
  return numfive

def numfour_active():
  numfour = glob.glob('no4_active/*')
  numfour = sorted(numfour)
  return numfour

def numfive_active():
  numfive = glob.glob('no5_active/*')
  numfive = sorted(numfive)
  return numfive