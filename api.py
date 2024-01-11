import paralleldots
paralleldots.set_api_key("UvrNAo166XJ5IlEBV3IP87Y4ySeGaHKsHRRqPfMNVfs")

def ner(txt):
    ner=paralleldots.ner(txt)
    return ner
    
